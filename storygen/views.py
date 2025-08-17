from django.shortcuts import render
from PIL import Image, ImageDraw, ImageFont
import os
import random
import textwrap

# This function generates a simple story and character description based on the user's prompt.
def generate_dynamic_text(user_prompt):
    """
    Generates a story and character description using a simple rule-based model.
    """
    # Create more detailed lists of story fragments and character archetypes.
    story_fragments = [
        "In a city of towering chrome spires, a lone hacker discovered a truth hidden in the digital shadows. The truth was not just a secret, but a living entity that threatened to consume the city's entire network. The hacker knew this would be a difficult battle, but they had a plan.",
        "Deep within a forgotten jungle, a team of explorers found a lost temple and a power they could not comprehend. The temple, built by a civilization long thought extinct, held the key to a source of infinite energy. The explorers had to decide whether to harness this power or leave it untouched.",
        "On a starship hurtling through a nebula of vibrant colors, a message from an ancient alien race was received. The message, a series of complex equations, pointed to a new world. The crew, intrigued by the discovery, decided to change course and investigate.",
        "In a quaint, rainy town, a quiet librarian found a magical book that had the power to change reality. With a simple turn of the page, the librarian could alter the past or glimpse into the future. They had to learn to control this power before it fell into the wrong hands.",
        "A detective in a bustling metropolis was assigned a case that led them to the city's corrupt foundation. The case, a seemingly simple missing person report, was just the tip of the iceberg. The detective soon discovered a conspiracy that went all the way to the top of the city's government.",
        "A young wizard's apprentice, exiled from their academy, discovered a powerful forbidden spell in a hidden library. The spell was a dangerous one, capable of bending time itself. The apprentice had to master the spell quickly to save their master from a terrible fate.",
        "At the edge of a frozen wasteland, a small village lived in fear of a mythical beast that hunted in the night. The village elder tasked a young hunter with a seemingly impossible quest: to track and slay the beast. The hunter, though young, was determined to protect their home.",
        "In a kingdom ravaged by a strange plague, a healer embarked on a quest to find a legendary herb. The herb, rumored to grow only at the highest peaks of the Dragon's Tooth mountains, was the only known cure for the illness. The healer had to brave treacherous terrain and ancient guardians to reach their destination.",
        "An archaeologist exploring the Great Pyramid of Giza uncovered a hidden chamber. Inside, they found a map that led to a forgotten civilization. The map, filled with strange symbols, promised untold riches and knowledge to those who could decipher it.",
        "A knight, disgraced and banished from their order, sought redemption by facing a fearsome dragon that terrorized the land. The dragon, a monstrous creature of fire and scale, was a formidable foe. The knight, armed with only a broken sword and an unyielding will, prepared for their final battle.",
        "In a cyberpunk city where technology and crime were intertwined, a retired mercenary was pulled back into the world they tried to leave behind. The job was simple: retrieve a stolen piece of technology from a rival gang. But the mercenary soon discovered that nothing in this city was ever simple.",
        "A team of intergalactic smugglers, known for their daring heists, took on a job that put them against the most powerful crime syndicate in the galaxy. The target was a priceless artifact, said to hold the key to a lost planet. The team had to rely on their wits and their aresnal of gadgets to succeed.",
        "On a planet consumed by a sentient fog, a group of scientists sought to find a way to communicate with the mysterious entity. The fog, capable of manifesting the deepest fears of those who entered it, was a difficult subject to study. The scientists risked their lives to uncover its secrets.",
        "A young woman, gifted with the ability to control wind and storms, was hunted by an ancient organization that sought to harness her power. She had to use her abilities to evade her pursuers and find a safe haven. Her only ally was a renegade warrior who promised to protect her.",
        "In a realm of magic and mythical creatures, a baker discovered they could infuse their pastries with magical properties. Their baked goods could grant flight, enhance strength, or even heal wounds. The baker's newfound power, however, attracted unwanted attention from powerful mages.",
        "An ancient god, forgotten and powerless, awoke in the modern world to a reality they no longer recognized. They had to navigate a world of technology and mortals, all while trying to regain their lost power. Their journey was filled with confusion, wonder, and a sense of profound loss.",
        "In a world where art could come to life, a young painter accidentally created a monster from a nightmare. The monster, a creature of shadow and ink, began to terrorize the city. The painter had to find a way to defeat their creation before it was too late.",
        "At the bottom of the ocean, a group of deep-sea divers discovered a sunken city from a forgotten era. The city, untouched for thousands of years, held a secret that could change the course of human history. The divers had to race against time to uncover the truth before the city was lost forever.",
        "In a land of perpetual winter, a prophecy foretold of a hero who would bring back the sun. The hero, a simple village girl with no special abilities, was tasked with a journey to the highest peak of the world. Her only guide was an old, wise wolf who communicated with her through telepathy.",
        "A group of friends, playing an old video game, discovered a glitch that transported them into the virtual world. Trapped in a world of pixels and code, they had to complete the game to return home. Their friendship and skills were put to the test as they faced the game's final boss."
    ]
    character_archetypes = [
        "a seasoned space captain, with a weary heart and a secret past. Their face, a roadmap of a hundred battles and countless star systems, is framed by a neatly trimmed beard. They wear a tattered but functional flight suit, its patches telling stories of daring escapes and lost friends.",
        "a brilliant young scientist, driven by a thirst for knowledge and a desire to save the world. With wide, intelligent eyes and a perpetually messy hair, they are often found hunched over a worktable, surrounded by bubbling beakers and complex equations.",
        "a rogue archaeologist, more comfortable with ancient puzzles than with people. Their rugged leather jacket and dusty boots suggest a life of adventure, but their gentle hands and keen eyes reveal a deep respect for the history they unearth.",
        "a powerful empath, who can feel the emotions of others and is burdened by their pain. They are often quiet and reserved, a reflection of the emotional turmoil they constantly navigate. Their simple, unassuming clothes hide a power that could bring even the strongest to their knees.",
        "a stoic warrior, whose unbreakable will is matched only by their incredible skill with a blade. Their face is a mask of calm determination, but their eyes hold the fire of a thousand battles. They are clad in a simple, practical set of armor, each dent and scratch a testament to their victories.",
        "a charismatic thief, known for their charm and a knack for getting into and out of trouble. With a mischievous grin and a twinkle in their eye, they can talk their way out of any situation. They wear a dark, stylish coat with many hidden pockets and a collection of lockpicks.",
        "a wise old wizard, whose beard is as long as their life. They are a keeper of ancient knowledge and have seen empires rise and fall. They wear a flowing robe of deep blue, embroidered with constellations, and carry a gnarled staff topped with a glowing crystal.",
        "a young hunter, whose determination is stronger than their fear. They have grown up in a harsh land, learning to survive on their own. Their clothes are made from animal hides, and they carry a hand-carved bow that has never missed its mark.",
        "a graceful dancer, whose movements are as fluid as water. They are a master of their art, capable of telling stories with their body. They wear a beautiful, shimmering costume that catches the light with every turn, and their feet are always bare, feeling the earth beneath them.",
        "a mysterious wanderer, whose past is shrouded in secrecy. They travel from town to town, never staying in one place for too long. Their face is always hidden by a hood, and their voice is a soft whisper. They carry a simple knapsack, but what it holds is a mystery.",
        "a cunning spy, with a mysterious past. Their face is a mask of calm determination, but their eyes hold the fire of a thousand battles. They are clad in a simple, practical set of armor, each dent and scratch a testament to their victories.",
        "a reclusive scholar, with a secret to hide and a thirst for knowledge. Their rugged leather jacket and dusty boots suggest a life of adventure, but their gentle hands and keen eyes reveal a deep respect for the history they unearth.",
        "a powerful sorceress, who controls the elements with a flick of her wrist. With a mischievous grin and a twinkle in her eye, she can talk her way out of any situation. She wears a dark, stylish coat with many hidden pockets and a collection of lockpicks.",
        "a determined inventor, whose mind is always a whirl of new ideas. They are a master of their craft, capable of building anything from a simple tool to a complex machine. They wear a leather apron covered in grease and soot, and their hands are often stained with ink and oil.",
        "a grizzled mercenary, whose face is a roadmap of a hundred battles and countless star systems. They are a veteran of countless wars and have a deep respect for the history they unearth. Their rugged leather jacket and dusty boots suggest a life of adventure.",
        "a charismatic bard, who can weave stories with their music. They are a master of their craft, capable of inspiring hope or inciting rebellion with a single tune. They wear a simple tunic and carry a lute that has seen better days.",
        "a mystical druid, whose connection to nature is deeper than any other. They can speak with animals and plants, and they draw their power from the earth itself. They wear a simple robe of woven leaves and carry a gnarled staff.",
        "a humble farmer, whose life is a testament to hard work and determination. They have a deep respect for the land they work on and a simple, honest heart. They wear a straw hat and work clothes that have seen better days.",
        "a lost princess, whose kingdom was taken from her. She is a beacon of hope for her people and a symbol of a forgotten era. She wears a simple dress and a silver locket that holds a picture of her parents.",
        "a wise alchemist, who can turn lead into gold and create potions that can heal any wound. They are a master of their craft, capable of creating anything from a simple potion to a complex elixir. They wear a simple robe and carry a gnarled staff."
    ]
    
    # Use a random choice to create a dynamic story and character.
    story_fragment = random.choice(story_fragments)
    character_archetype = random.choice(character_archetypes)

    story_text = (
        f"Based on your idea, '{user_prompt}', a new tale unfolds:\n\n{story_fragment} "
        f"Our protagonist, {character_archetype}, found their journey beginning with this single, pivotal event."
    )
    character_description_text = (
        f"The main character of this story is {character_archetype}. Their unique abilities and "
        f"mysterious background make them the perfect person to face the challenges presented by your prompt."
    )

    return story_text, character_description_text

# This is your main Django view function that handles all web requests.
def generate_story(request):
    if request.method == 'POST':
        user_prompt = request.POST.get('prompt')

        story_text, character_description_text = generate_dynamic_text(user_prompt)
        
        combined_image_path = None
        
        try:
            # Create two placeholder images
            background_img = Image.new('RGB', (800, 600), color='blue')
            character_img = Image.new('RGB', (300, 400), color='red')

            # Draw some text on the placeholder images for demonstration
            draw_character = ImageDraw.Draw(character_img)
            draw_background = ImageDraw.Draw(background_img)

            # Define a font for the text
            try:
                font = ImageFont.truetype("arial.ttf", 20)
            except IOError:
                font = ImageFont.load_default()

            # Add placeholder text to the images
            draw_character.text((10, 10), "Character", fill="white", font=font)
            draw_background.text((10, 10), "Background", fill="white", font=font)

            # Combine the images
            if character_img and background_img:
                # Resize the character image to prevent it from being too big
                character_img.thumbnail((background_img.width, background_img.height), Image.Resampling.LANCZOS)
                
                # Paste the character image onto the background
                background_img.paste(character_img, (50, 50)) # Position the character in the scene

                # Save the combined image
                combined_image_path = os.path.join('static', 'combined_image.png')
                background_img.save(combined_image_path)
            
        except Exception as e:
            print(f"An error occurred during image processing: {e}")
            
        context = {
            'user_prompt': user_prompt,
            'story_text': story_text,
            'character_description_text': character_description_text,
            'combined_image_path': combined_image_path,
        }
        return render(request, 'index.html', context)
    
    # This block of code runs for the initial page load (a GET request).
    return render(request, 'index.html')
