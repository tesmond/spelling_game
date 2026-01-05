"""
Dictionary Manager for Spelling Game
Handles loading and managing dictionary data.
"""

import gzip
import json
import os
import urllib.request


class DictionaryManager:
    """Manages the dictionary data for the spelling game."""

    DICT_URL = "https://github.com/wordset/wordset-dictionary/raw/refs/heads/master/allwords_wordset.json.gz"
    CACHE_FILE = "dictionary_cache.json"

    def __init__(self, use_downloaded=False):
        self.use_downloaded = use_downloaded
        self.dictionary = {}
        self.load_dictionary()

    def load_dictionary(self):
        """Load dictionary from cache or download it."""
        if not self.use_downloaded:
            self.dictionary = self._get_fallback_dictionary()
            print(f"Using fallback dictionary with {len(self.dictionary)} words.")
            return

        if os.path.exists(self.CACHE_FILE):
            try:
                with open(self.CACHE_FILE, "r", encoding="utf-8") as f:
                    self.dictionary = json.load(f)
                print(f"Loaded {len(self.dictionary)} words from cache.")
                return
            except Exception as e:
                print(f"Error loading cache: {e}")

        self.download_dictionary()

    def download_dictionary(self):
        """Download dictionary from GitHub."""
        print("Downloading dictionary...")
        try:
            with urllib.request.urlopen(self.DICT_URL, timeout=30) as response:
                content = gzip.decompress(response.read())
                data = content.decode("utf-8")
                self.dictionary = json.loads(data)
        except Exception as e:
            print(f"Error downloading: {e}")
            # Use a fallback mini dictionary
            self.dictionary = self._get_fallback_dictionary()
            return

        # Cache the dictionary
        try:
            with open(self.CACHE_FILE, "w", encoding="utf-8") as f:
                json.dump(self.dictionary, f)
            print(f"Downloaded and cached {len(self.dictionary)} words.")
        except Exception as e:
            print(f"Error caching: {e}")

    def _get_fallback_dictionary(self):
        """Return a fallback dictionary if download fails."""
        return {
            "abstract": {
                "meanings": [
                    {
                        "def": "existing in thought or as an idea but not having a physical or concrete existence."
                    }
                ]
            },
            "easel": {"meanings": [{"def": "a stand for holding a painter's canvas."}]},
            "kiln": {
                "meanings": [
                    {
                        "def": "a furnace or oven for burning, baking, or drying something, especially one for firing pottery."
                    }
                ]
            },
            "acrylic": {
                "meanings": [{"def": "a synthetic resin used in paints and plastics."}]
            },
            "exhibition": {
                "meanings": [
                    {"def": "a public display of works of art or items of interest."}
                ]
            },
            "landscape": {
                "meanings": [
                    {
                        "def": "all the visible features of an area of land, often considered in terms of their aesthetic appeal."
                    }
                ]
            },
            "charcoal": {
                "meanings": [
                    {
                        "def": "a porous black solid, consisting of an amorphous form of carbon, obtained as a residue when wood, bone, or other organic matter is heated in the absence of air."
                    }
                ]
            },
            "foreground": {
                "meanings": [
                    {"def": "the part of a view that is nearest to the observer."}
                ]
            },
            "palette": {
                "meanings": [
                    {
                        "def": "a thin board or slab on which an artist lays and mixes colors."
                    }
                ]
            },
            "collage": {
                "meanings": [
                    {
                        "def": "an artistic composition made of various materials (e.g., paper, cloth, or wood) glued on a surface."
                    }
                ]
            },
            "frieze": {
                "meanings": [
                    {
                        "def": "a broad horizontal band of sculpted or painted decoration, especially on a wall near the ceiling."
                    }
                ]
            },
            "pastel": {
                "meanings": [
                    {
                        "def": "a crayon made of powdered pigments bound with gum or resin."
                    }
                ]
            },
            "collection": {
                "meanings": [
                    {"def": "a group of objects of one type that have been collected."}
                ]
            },
            "gallery": {
                "meanings": [
                    {
                        "def": "a room or building for the display or sale of works of art."
                    }
                ]
            },
            "perspective": {
                "meanings": [
                    {
                        "def": "the art of representing three-dimensional objects on a two-dimensional surface so as to give the right impression of their height, width, depth, and position in relation to each other."
                    }
                ]
            },
            "colour": {
                "meanings": [
                    {
                        "def": "the property possessed by an object of producing different sensations on the eye as a result of the way it reflects or emits light."
                    }
                ]
            },
            "highlight": {
                "meanings": [
                    {"def": "an outstanding part of an event or period of time."}
                ]
            },
            "portrait": {
                "meanings": [
                    {
                        "def": "a painting, drawing, photograph, or engraving of a person, especially one depicting only the face or head and shoulders."
                    }
                ]
            },
            "crosshatch": {
                "meanings": [
                    {
                        "def": "shade (an area of a drawing or engraving) with intersecting sets of parallel lines."
                    }
                ]
            },
            "illusion": {
                "meanings": [
                    {
                        "def": "a thing that is or is likely to be wrongly perceived or interpreted by the senses."
                    }
                ]
            },
            "sketch": {
                "meanings": [
                    {
                        "def": "a rough or unfinished drawing or painting, often made to assist in making a more finished picture."
                    }
                ]
            },
            "dimension": {
                "meanings": [
                    {
                        "def": "a measurable extent of some kind, such as length, breadth, depth, or height."
                    }
                ]
            },
            "impasto": {
                "meanings": [
                    {
                        "def": "the technique of laying on paint thickly so that it stands out from a surface."
                    }
                ]
            },
            "spectrum": {
                "meanings": [
                    {
                        "def": "a band of colors, as seen in a rainbow, produced by separation of the components of light by their different degrees of refraction according to wavelength."
                    }
                ]
            },
            "display": {
                "meanings": [{"def": "an arrangement of something for public view."}]
            },
            "aesthetic": {
                "meanings": [
                    {"def": "concerned with beauty or the appreciation of beauty."}
                ]
            },
            "hygiene": {
                "meanings": [
                    {
                        "def": "conditions or practices conducive to maintaining health and preventing disease, especially through cleanliness."
                    }
                ]
            },
            "presentation": {
                "meanings": [
                    {
                        "def": "the manner or style in which something is given, offered, or displayed."
                    }
                ]
            },
            "brief": {"meanings": [{"def": "of short duration."}]},
            "ingredient": {
                "meanings": [
                    {
                        "def": "any of the foods or substances that are combined to make a particular dish."
                    }
                ]
            },
            "production": {
                "meanings": [
                    {
                        "def": "the action of making or manufacturing from components or raw materials, or the process of being so manufactured."
                    }
                ]
            },
            "carbohydrate": {
                "meanings": [
                    {
                        "def": "any of a large group of organic compounds occurring in foods and living tissues and including sugars, starch, and cellulose."
                    }
                ]
            },
            "innovation": {
                "meanings": [{"def": "the action or process of innovating."}]
            },
            "protein": {
                "meanings": [
                    {
                        "def": "any of a class of nitrogenous organic compounds that consist of large molecules composed of one or more long chains of amino acids and are an essential part of all living organisms."
                    }
                ]
            },
            "component": {
                "meanings": [{"def": "a part or element of a larger whole."}]
            },
            "knife": {
                "meanings": [
                    {
                        "def": "an instrument composed of a blade fixed into a handle, used for cutting or as a weapon."
                    }
                ]
            },
            "knives": {"meanings": [{"def": "plural of knife."}]},
            "recipe": {
                "meanings": [
                    {
                        "def": "a set of instructions for preparing a particular dish, including a list of the ingredients required."
                    }
                ]
            },
            "design": {
                "meanings": [
                    {
                        "def": "a plan or drawing produced to show the look and function or workings of a building, garment, or other object before it is made."
                    }
                ]
            },
            "linen": {"meanings": [{"def": "cloth woven from flax."}]},
            "sew": {
                "meanings": [
                    {
                        "def": "join, fasten, or repair (something) by making stitches with a needle and thread or a sewing machine."
                    }
                ]
            },
            "diet": {
                "meanings": [
                    {
                        "def": "the kinds of food that a person, animal, or community habitually eats."
                    }
                ]
            },
            "machine": {
                "meanings": [
                    {
                        "def": "an apparatus using or applying mechanical power and having several parts, each with a definite function and together performing a particular task."
                    }
                ]
            },
            "specification": {
                "meanings": [
                    {
                        "def": "an act of identifying something precisely or of stating a precise requirement."
                    }
                ]
            },
            "disassemble": {"meanings": [{"def": "take (something) apart."}]},
            "manufacture": {
                "meanings": [
                    {"def": "make (something) on a large scale using machinery."}
                ]
            },
            "technology": {
                "meanings": [
                    {
                        "def": "the application of scientific knowledge for practical purposes, especially in industry."
                    }
                ]
            },
            "evaluation": {
                "meanings": [
                    {
                        "def": "the making of a judgment about the amount, number, or value of something; assessment."
                    }
                ]
            },
            "mineral": {
                "meanings": [
                    {"def": "a solid inorganic substance of natural occurrence."}
                ]
            },
            "tension": {"meanings": [{"def": "the state of being stretched tight."}]},
            "fabric": {
                "meanings": [
                    {
                        "def": "cloth or other material produced by weaving or knitting fibers."
                    }
                ]
            },
            "natural": {
                "meanings": [
                    {
                        "def": "existing in or caused by nature; not made or caused by humankind."
                    }
                ]
            },
            "textile": {"meanings": [{"def": "a type of cloth or woven fabric."}]},
            "fibre": {
                "meanings": [
                    {
                        "def": "a thread or filament from which a vegetable tissue, mineral substance, or textile is formed."
                    }
                ]
            },
            "nutrition": {
                "meanings": [
                    {
                        "def": "the process of providing or obtaining the food necessary for health and growth."
                    }
                ]
            },
            "vitamin": {
                "meanings": [
                    {
                        "def": "any of a group of organic compounds that are essential for normal growth and nutrition and are required in small quantities in the diet because they cannot be synthesized by the body."
                    }
                ]
            },
            "flour": {
                "meanings": [
                    {
                        "def": "a powder obtained by grinding grain, typically wheat, and used to make bread, cakes, and pastry."
                    }
                ]
            },
            "polyester": {
                "meanings": [
                    {
                        "def": "a synthetic resin in which the polymer units are linked by ester groups, used in the manufacture of synthetic fibers."
                    }
                ]
            },
            "flowchart": {
                "meanings": [
                    {
                        "def": "a diagram of the sequence of movements or actions of people or things involved in a complex system or activity."
                    }
                ]
            },
            "portfolio": {
                "meanings": [
                    {
                        "def": "a large, thin, flat case for carrying loose papers or drawings."
                    }
                ]
            },
            "english": {
                "meanings": [{"def": "relating to England or its people or language."}]
            },
            "advertise": {
                "meanings": [
                    {
                        "def": "describe or draw attention to (a product, service, or event) in a public medium in order to promote sales or attendance."
                    }
                ]
            },
            "advertisement": {
                "meanings": [
                    {
                        "def": "a notice or announcement in a public medium promoting a product, service, or event or publicizing a job vacancy."
                    }
                ]
            },
            "figurative": {
                "meanings": [
                    {"def": "departing from a literal use of words; metaphorical."}
                ]
            },
            "preposition": {
                "meanings": [
                    {
                        "def": "a word governing, and usually preceding, a noun or pronoun and expressing a relation to another word or element in the clause."
                    }
                ]
            },
            "alliteration": {
                "meanings": [
                    {
                        "def": "the occurrence of the same letter or sound at the beginning of adjacent or closely connected words."
                    }
                ]
            },
            "genre": {
                "meanings": [
                    {"def": "a style or category of art, music, or literature."}
                ]
            },
            "resolution": {
                "meanings": [{"def": "a firm decision to do or not to do something."}]
            },
            "apostrophe": {
                "meanings": [
                    {
                        "def": "a punctuation mark (') used to indicate either possession or the omission of letters or numbers."
                    }
                ]
            },
            "grammar": {
                "meanings": [
                    {
                        "def": "the whole system and structure of a language or of languages in general, usually taken as consisting of syntax and morphology (including inflections) and sometimes also phonology and semantics."
                    }
                ]
            },
            "rhyme": {
                "meanings": [
                    {
                        "def": "correspondence of sound between words or the endings of words, especially when these are used at the ends of lines of poetry."
                    }
                ]
            },
            "atmosphere": {
                "meanings": [
                    {
                        "def": "the envelope of gases surrounding the earth or another planet."
                    }
                ]
            },
            "imagery": {
                "meanings": [
                    {
                        "def": "visually descriptive or figurative language, especially in a literary work."
                    }
                ]
            },
            "scene": {
                "meanings": [
                    {
                        "def": "the place where an incident in real life or fiction occurs or occurred."
                    }
                ]
            },
            "chorus": {
                "meanings": [
                    {
                        "def": "a large organized group of singers, especially one that performs in a concert or is attached to an opera."
                    }
                ]
            },
            "metaphor": {
                "meanings": [
                    {
                        "def": "a figure of speech in which a word or phrase is applied to an object or action to which it is not literally applicable."
                    }
                ]
            },
            "simile": {
                "meanings": [
                    {
                        "def": "a figure of speech involving the comparison of one thing with another thing of a different kind, used to make a description more emphatic or vivid."
                    }
                ]
            },
            "clause": {
                "meanings": [
                    {
                        "def": "a unit of grammatical organization next below the sentence in rank and in traditional grammar said to consist of a subject and predicate."
                    }
                ]
            },
            "myth": {
                "meanings": [
                    {
                        "def": "a traditional story, especially one concerning the early history of a people or explaining some natural or social phenomenon, and typically involving supernatural beings or events."
                    }
                ]
            },
            "soliloquy": {
                "meanings": [
                    {
                        "def": "an act of speaking one's thoughts aloud when by oneself or regardless of any hearers, especially by a character in a play."
                    }
                ]
            },
            "cliché": {
                "meanings": [
                    {
                        "def": "a phrase or opinion that is overused and betrays a lack of original thought."
                    }
                ]
            },
            "narrative": {
                "meanings": [
                    {"def": "a spoken or written account of connected events; a story."}
                ]
            },
            "narrator": {
                "meanings": [
                    {
                        "def": "a person who narrates something, especially a character who recounts the events of a novel or play."
                    }
                ]
            },
            "subordinate": {"meanings": [{"def": "lower in rank or position."}]},
            "comma": {
                "meanings": [
                    {
                        "def": "a punctuation mark (,) indicating a pause between parts of a sentence or separating items in a list."
                    }
                ]
            },
            "onomatopoeia": {
                "meanings": [
                    {
                        "def": "the formation of a word from a sound associated with what is named."
                    }
                ]
            },
            "suffix": {
                "meanings": [
                    {
                        "def": "a morpheme added at the end of a word to form a derivative."
                    }
                ]
            },
            "comparison": {"meanings": [{"def": "the act or instance of comparing."}]},
            "pamphlet": {
                "meanings": [
                    {
                        "def": "a small booklet or leaflet containing information or arguments about a single subject."
                    }
                ]
            },
            "synonym": {
                "meanings": [
                    {
                        "def": "a word or phrase that means exactly or nearly the same as another word or phrase in the same language."
                    }
                ]
            },
            "conjunction": {
                "meanings": [
                    {
                        "def": "a word used to connect clauses or sentences or to coordinate words in the same clause."
                    }
                ]
            },
            "paragraph": {
                "meanings": [
                    {
                        "def": "a distinct section of a piece of writing, usually dealing with a single theme and indicated by a new line, indentation, or numbering."
                    }
                ]
            },
            "tabloid": {
                "meanings": [
                    {
                        "def": "a newspaper having pages half the size of those of a standard newspaper, typically popular in style and dominated by sensational stories."
                    }
                ]
            },
            "consonant": {"meanings": [{"def": "a speech sound that is not a vowel."}]},
            "personification": {
                "meanings": [
                    {
                        "def": "the attribution of a personal nature or human characteristics to something non-human, or the representation of an abstract quality in human form."
                    }
                ]
            },
            "vocabulary": {
                "meanings": [{"def": "the set of words used in a particular language."}]
            },
            "dialogue": {
                "meanings": [
                    {
                        "def": "conversation between two or more people as a feature of a book, play, or film."
                    }
                ]
            },
            "playwright": {"meanings": [{"def": "a person who writes plays."}]},
            "vowel": {
                "meanings": [
                    {
                        "def": "a speech sound made with the vocal tract open, forming the nucleus of a syllable."
                    }
                ]
            },
            "exclamation": {
                "meanings": [
                    {
                        "def": "a sudden cry or remark, especially expressing surprise, anger, or pain."
                    }
                ]
            },
            "plural": {
                "meanings": [
                    {"def": "the form of a word that is used to denote more than one."}
                ]
            },
            "expression": {
                "meanings": [
                    {"def": "the process of making known one's thoughts or feelings."}
                ]
            },
            "prefix": {
                "meanings": [
                    {"def": "a word, letter, or number placed before another."}
                ]
            },
            "geography": {
                "meanings": [
                    {
                        "def": "the study of the physical features of the earth and its atmosphere, and of human activity as it affects and is affected by these."
                    }
                ]
            },
            "abroad": {
                "meanings": [{"def": "in or to a foreign country or countries."}]
            },
            "function": {
                "meanings": [
                    {
                        "def": "an activity or purpose natural to or intended for a person or thing."
                    }
                ]
            },
            "poverty": {"meanings": [{"def": "the state of being extremely poor."}]},
            "amenity": {
                "meanings": [
                    {
                        "def": "a desirable or useful feature or facility of a building or place."
                    }
                ]
            },
            "globe": {"meanings": [{"def": "the earth."}]},
            "provision": {
                "meanings": [
                    {"def": "the action of providing or supplying something for use."}
                ]
            },
            "atlas": {"meanings": [{"def": "a book of maps or charts."}]},
            "habitat": {
                "meanings": [
                    {
                        "def": "the natural home or environment of an animal, plant, or other organism."
                    }
                ]
            },
            "region": {
                "meanings": [
                    {
                        "def": "an area, especially part of a country or the world having definable characteristics but not always fixed boundaries."
                    }
                ]
            },
            "regional": {
                "meanings": [{"def": "relating to or characteristic of a region."}]
            },
            "authority": {
                "meanings": [
                    {
                        "def": "the power or right to give orders, make decisions, and enforce obedience."
                    }
                ]
            },
            "infrastructure": {
                "meanings": [
                    {
                        "def": "the basic physical and organizational structures and facilities needed for the operation of a society or enterprise."
                    }
                ]
            },
            "rural": {
                "meanings": [
                    {
                        "def": "in, relating to, or characteristic of the countryside rather than the town."
                    }
                ]
            },
            "climate": {
                "meanings": [
                    {
                        "def": "the weather conditions prevailing in an area in general or over a long period."
                    }
                ]
            },
            "international": {
                "meanings": [
                    {"def": "existing, occurring, or operating between nations."}
                ]
            },
            "settlement": {
                "meanings": [
                    {
                        "def": "an official agreement intended to resolve a dispute or conflict."
                    }
                ]
            },
            "contour": {
                "meanings": [
                    {
                        "def": "an outline, especially one representing or bounding the shape or form of something."
                    }
                ]
            },
            "situation": {
                "meanings": [
                    {
                        "def": "a set of circumstances in which one finds oneself; a state of affairs."
                    }
                ]
            },
            "country": {
                "meanings": [
                    {
                        "def": "a nation with its own government, occupying a particular territory."
                    }
                ]
            },
            "latitude": {
                "meanings": [
                    {
                        "def": "the angular distance of a place north or south of the earth's equator, or of a celestial object north or south of the celestial equator, usually expressed in degrees and minutes."
                    }
                ]
            },
            "tourist": {
                "meanings": [
                    {
                        "def": "a person who is traveling or visiting a place for pleasure."
                    }
                ]
            },
            "tourism": {
                "meanings": [
                    {
                        "def": "the commercial organization and operation of holidays and visits to places of interest."
                    }
                ]
            },
            "county": {
                "meanings": [
                    {
                        "def": "a territorial division of some countries, forming the chief unit of local administration."
                    }
                ]
            },
            "location": {"meanings": [{"def": "a particular place or position."}]},
            "transport": {
                "meanings": [
                    {
                        "def": "take or carry (people or goods) from one place to another by means of a vehicle, aircraft, or ship."
                    }
                ]
            },
            "transportation": {
                "meanings": [
                    {
                        "def": "the action of transporting someone or something or the process of being transported."
                    }
                ]
            },
            "desert": {
                "meanings": [
                    {
                        "def": "a barren area of landscape where little precipitation occurs and living conditions are hostile for plant and animal life."
                    }
                ]
            },
            "longitude": {
                "meanings": [
                    {
                        "def": "the angular distance of a place east or west of the meridian at Greenwich, England, or west of the standard meridian of a celestial object, usually expressed in degrees and minutes."
                    }
                ]
            },
            "urban": {
                "meanings": [
                    {"def": "in, relating to, or characteristic of a town or city."}
                ]
            },
            "employment": {"meanings": [{"def": "the condition of having paid work."}]},
            "nation": {
                "meanings": [
                    {
                        "def": "a large body of people united by common descent, history, culture, or language, inhabiting a particular country or territory."
                    }
                ]
            },
            "national": {
                "meanings": [
                    {
                        "def": "relating to a nation; common to or characteristic of a whole nation."
                    }
                ]
            },
            "wealth": {
                "meanings": [
                    {
                        "def": "an abundance of valuable resources or possessions; riches."
                    }
                ]
            },
            "erosion": {
                "meanings": [
                    {
                        "def": "the process of eroding or being eroded by wind, water, or other natural agents."
                    }
                ]
            },
            "physical": {
                "meanings": [{"def": "relating to the body as opposed to the mind."}]
            },
            "weather": {
                "meanings": [
                    {
                        "def": "the state of the atmosphere at a particular place and time as regards heat, cloudiness, dryness, sunshine, wind, rain, etc."
                    }
                ]
            },
            "estuary": {
                "meanings": [
                    {
                        "def": "the tidal mouth of a large river, where the tide meets the stream."
                    }
                ]
            },
            "pollution": {
                "meanings": [
                    {
                        "def": "the presence in or introduction into the environment of a substance which has harmful or poisonous effects."
                    }
                ]
            },
            "history": {
                "meanings": [
                    {"def": "the study of past events, particularly in human affairs."}
                ]
            },
            "agriculture": {
                "meanings": [
                    {
                        "def": "the science or practice of farming, including cultivation of the soil for the growing of crops and the rearing of animals to provide food, wool, and other products."
                    }
                ]
            },
            "agricultural": {
                "meanings": [{"def": "relating to farming or agriculture."}]
            },
            "defence": {
                "meanings": [
                    {"def": "the action of defending from or resisting attack."}
                ]
            },
            "politics": {
                "meanings": [
                    {
                        "def": "the activities associated with the governance of a country or area, especially the debate or conflict among individuals or parties having or hoping to achieve power."
                    }
                ]
            },
            "political": {
                "meanings": [
                    {
                        "def": "relating to the government or public affairs of a country."
                    }
                ]
            },
            "bias": {
                "meanings": [
                    {
                        "def": "prejudice in favor of or against one thing, person, or group compared with another, usually in a way considered to be unfair."
                    }
                ]
            },
            "disease": {
                "meanings": [
                    {
                        "def": "a disorder of structure or function in a human, animal, or plant, especially one that produces specific symptoms or that affects a specific location and is not simply a direct result of physical injury."
                    }
                ]
            },
            "priest": {
                "meanings": [
                    {
                        "def": "an ordained minister of the Christian Church having the authority to perform certain rites and administer certain sacraments."
                    }
                ]
            },
            "castle": {
                "meanings": [
                    {
                        "def": "a large building or group of buildings fortified against attack with thick walls, battlements, towers, and in many cases a moat."
                    }
                ]
            },
            "document": {
                "meanings": [
                    {
                        "def": "a piece of written, printed, or electronic matter that provides information or evidence or that serves as an official record."
                    }
                ]
            },
            "propaganda": {
                "meanings": [
                    {
                        "def": "information, especially of a biased or misleading nature, used to promote or publicize a particular political cause or point of view."
                    }
                ]
            },
            "cathedral": {
                "meanings": [
                    {
                        "def": "the principal church of a diocese, with which the bishop is officially associated."
                    }
                ]
            },
            "dynasty": {
                "meanings": [{"def": "a line of hereditary rulers of a country."}]
            },
            "protestant": {
                "meanings": [
                    {
                        "def": "a member of a Western Christian church whose faith and practice are founded on the principles of the Reformation, especially in the acceptance of the Bible as the sole source of revelation, the universal priesthood of all believers, and the doctrine of justification by faith alone."
                    }
                ]
            },
            "catholic": {"meanings": [{"def": "of the Roman Catholic faith."}]},
            "economy": {
                "meanings": [
                    {
                        "def": "the wealth and resources of a country or region, especially in terms of the production and consumption of goods and services."
                    }
                ]
            },
            "economic": {
                "meanings": [{"def": "relating to economics or the economy."}]
            },
            "rebel": {
                "meanings": [
                    {
                        "def": "a person who rises in opposition or armed resistance against an authority or government."
                    }
                ]
            },
            "rebellion": {
                "meanings": [
                    {"def": "an act of rebelling against authority or control."}
                ]
            },
            "chronology": {
                "meanings": [
                    {
                        "def": "the arrangement of events or dates in the order of their occurrence."
                    }
                ]
            },
            "chronological": {
                "meanings": [{"def": "following the order in which they occurred."}]
            },
            "emigration": {
                "meanings": [
                    {
                        "def": "the act of leaving one's own country to settle permanently in another."
                    }
                ]
            },
            "reign": {
                "meanings": [{"def": "the period during which a sovereign rules."}]
            },
            "citizen": {
                "meanings": [
                    {
                        "def": "a legally recognized subject or national of a state or commonwealth, either native or naturalized."
                    }
                ]
            },
            "government": {
                "meanings": [
                    {"def": "the governing body of a nation, state, or community."}
                ]
            },
            "religious": {
                "meanings": [{"def": "relating to or believing in a religion."}]
            },
            "civilisation": {
                "meanings": [
                    {
                        "def": "the stage of human social and cultural development and organization that is considered most advanced."
                    }
                ]
            },
            "immigrant": {
                "meanings": [
                    {
                        "def": "a person who comes to live permanently in a foreign country."
                    }
                ]
            },
            "republic": {
                "meanings": [
                    {
                        "def": "a form of government in which the country is considered a 'public matter', not the private concern or property of the rulers."
                    }
                ]
            },
            "colony": {
                "meanings": [
                    {
                        "def": "a country or area under the full or partial political control of another country, typically a distant one, and occupied by settlers from that country."
                    }
                ]
            },
            "colonisation": {
                "meanings": [
                    {
                        "def": "the action or process of settling among and establishing control over the indigenous people of an area."
                    }
                ]
            },
            "imperial": {"meanings": [{"def": "relating to an empire."}]},
            "imperialism": {
                "meanings": [
                    {
                        "def": "a policy of extending a country’s power and influence through colonization, use of military force, or other means."
                    }
                ]
            },
            "revolt": {
                "meanings": [{"def": "take part in a rebellion against authority."}]
            },
            "revolution": {
                "meanings": [
                    {
                        "def": "a forcible overthrow of a government or social order, in favor of a new system."
                    }
                ]
            },
            "conflict": {
                "meanings": [
                    {
                        "def": "a serious disagreement or argument, typically a protracted one."
                    }
                ]
            },
            "independence": {
                "meanings": [{"def": "the fact or state of being independent."}]
            },
            "siege": {
                "meanings": [
                    {
                        "def": "a military operation in which enemy forces surround a town or building, cutting off essential supplies, with the aim of compelling those inside to surrender."
                    }
                ]
            },
            "constitution": {
                "meanings": [
                    {
                        "def": "a body of fundamental principles or established precedents according to which a state or other organization is acknowledged to be governed."
                    }
                ]
            },
            "constitutional": {
                "meanings": [
                    {
                        "def": "relating to an established set of principles governing a state."
                    }
                ]
            },
            "invasion": {
                "meanings": [
                    {
                        "def": "an instance of invading a country or region with an armed force."
                    }
                ]
            },
            "source": {
                "meanings": [
                    {
                        "def": "a place, person, or thing from which something comes or can be obtained."
                    }
                ]
            },
            "contradict": {
                "meanings": [
                    {
                        "def": "deny the truth of (a statement), especially by asserting the opposite."
                    }
                ]
            },
            "contradiction": {
                "meanings": [
                    {
                        "def": "a combination of statements, ideas, or features which are opposed to one another."
                    }
                ]
            },
            "motive": {
                "meanings": [
                    {
                        "def": "a reason for doing something, especially one that is hidden or not obvious."
                    }
                ]
            },
            "trade": {
                "meanings": [
                    {"def": "the action of buying and selling goods and services."}
                ]
            },
            "current": {
                "meanings": [
                    {
                        "def": "belonging to the present time; happening or being used or done now."
                    }
                ]
            },
            "parliament": {
                "meanings": [
                    {
                        "def": "the highest legislature, consisting of the sovereign, the House of Lords, and the House of Commons."
                    }
                ]
            },
            "traitor": {
                "meanings": [
                    {
                        "def": "a person who betrays someone or something, such as a friend, cause, or principle."
                    }
                ]
            },
            "ict": {
                "meanings": [{"def": "information and communications technology."}]
            },
            "binary": {
                "meanings": [{"def": "relating to or consisting of two things."}]
            },
            "hardware": {
                "meanings": [{"def": "tools, machinery, and other durable equipment."}]
            },
            "network": {
                "meanings": [
                    {
                        "def": "an arrangement of intersecting horizontal and vertical lines."
                    }
                ]
            },
            "byte": {
                "meanings": [
                    {"def": "a unit of digital information that consists of 8 bits."}
                ]
            },
            "icon": {
                "meanings": [{"def": "a symbol or image that represents something."}]
            },
            "output": {
                "meanings": [
                    {
                        "def": "the amount of something produced by a person, machine, or industry."
                    }
                ]
            },
            "cable": {
                "meanings": [
                    {
                        "def": "a thick rope of wire or non-metallic fibers, typically used for construction, mooring ships, and towing vehicles."
                    }
                ]
            },
            "input": {
                "meanings": [
                    {
                        "def": "what is put in, taken in, or operated on by any process or system."
                    }
                ]
            },
            "password": {
                "meanings": [
                    {
                        "def": "a secret word or phrase that must be used to gain admission to a place."
                    }
                ]
            },
            "cartridge": {
                "meanings": [
                    {
                        "def": "a container holding a spool of film or magnetic tape for insertion into a camera or other device."
                    }
                ]
            },
            "interactive": {
                "meanings": [
                    {
                        "def": "allowing a two-way flow of information between a computer and a computer user; responding to the user's input."
                    }
                ]
            },
            "preview": {
                "meanings": [
                    {
                        "def": "a private showing of a film, play, etc., before its general release."
                    }
                ]
            },
            "cd-rom": {
                "meanings": [
                    {
                        "def": "a compact disc used as a read-only optical memory device for a computer system."
                    }
                ]
            },
            "interface": {
                "meanings": [
                    {
                        "def": "a point where two systems, subjects, organizations, etc., meet and interact."
                    }
                ]
            },
            "processor": {
                "meanings": [{"def": "a machine or person that processes something."}]
            },
            "computer": {
                "meanings": [
                    {
                        "def": "an electronic device for storing and processing data, typically in binary form, according to instructions given to it in a variable program."
                    }
                ]
            },
            "internet": {
                "meanings": [
                    {
                        "def": "a global computer network providing a variety of information and communication facilities, consisting of interconnected networks using standardized communication protocols."
                    }
                ]
            },
            "program": {
                "meanings": [
                    {"def": "a planned series of future events or performances."}
                ]
            },
            "connect": {
                "meanings": [
                    {
                        "def": "bring together or into contact so that a real or notional link is established."
                    }
                ]
            },
            "connection": {
                "meanings": [
                    {
                        "def": "a relationship in which a person, thing, or idea is linked or associated with something else."
                    }
                ]
            },
            "justify": {
                "meanings": [{"def": "show or prove to be right or reasonable."}]
            },
            "cursor": {
                "meanings": [
                    {
                        "def": "a movable indicator on a computer screen identifying the point that will be affected by input from the user."
                    }
                ]
            },
            "keyboard": {
                "meanings": [
                    {"def": "a panel of keys that operate a computer or typewriter."}
                ]
            },
            "sensor": {
                "meanings": [
                    {
                        "def": "a device that detects or measures a physical property and records, indicates, or otherwise responds to it."
                    }
                ]
            },
            "data": {
                "meanings": [
                    {
                        "def": "facts and statistics collected together for reference or analysis."
                    }
                ]
            },
            "database": {
                "meanings": [
                    {
                        "def": "a structured set of data held in a computer, especially one that is accessible in various ways."
                    }
                ]
            },
            "megabyte": {
                "meanings": [
                    {"def": "a unit of information equal to one million bytes."}
                ]
            },
            "server": {
                "meanings": [
                    {
                        "def": "a computer or computer program which manages access to a centralized resource or service in a network."
                    }
                ]
            },
            "delete": {
                "meanings": [
                    {
                        "def": "remove or obliterate (written or printed matter), especially by drawing a line through it."
                    }
                ]
            },
            "memory": {
                "meanings": [
                    {
                        "def": "the faculty by which the mind stores and remembers information."
                    }
                ]
            },
            "software": {
                "meanings": [
                    {
                        "def": "the programs and other operating information used by a computer."
                    }
                ]
            },
            "disk": {"meanings": [{"def": "a flat, thin, round object or plate."}]},
            "modem": {
                "meanings": [
                    {
                        "def": "a combined device for modulation and demodulation, for example, between the digital data of a computer and the analogue signal of a telephone line."
                    }
                ]
            },
            "spreadsheet": {
                "meanings": [
                    {
                        "def": "an electronic document in which data is arranged in the rows and columns of a grid and can be manipulated and used in calculations."
                    }
                ]
            },
            "module": {
                "meanings": [
                    {
                        "def": "each of a set of standardized parts or independent units that can be used to construct a more complex structure."
                    }
                ]
            },
            "virus": {
                "meanings": [
                    {
                        "def": "an infective agent that typically consists of a nucleic acid molecule in a protein coat, is too small to be seen by light microscopy, and is able to multiply only within the living cells of a host."
                    }
                ]
            },
            "electronic": {"meanings": [{"def": "relating to electronics."}]},
            "monitor": {
                "meanings": [
                    {
                        "def": "an instrument or device used for observing, checking, or keeping a continuous record of a process or quantity."
                    }
                ]
            },
            "graphic": {
                "meanings": [
                    {
                        "def": "relating to visual art, especially involving drawing, engraving, or lettering."
                    }
                ]
            },
            "multimedia": {
                "meanings": [
                    {"def": "the use of a variety of artistic or communicative media."}
                ]
            },
            "library": {
                "meanings": [
                    {
                        "def": "a building or room containing collections of books, periodicals, and sometimes films and recorded music for people to read, borrow, or refer to."
                    }
                ]
            },
            "alphabet": {
                "meanings": [
                    {
                        "def": "a set of letters or symbols in a fixed order used to represent the basic sounds of a language; in particular, the set of letters from A to Z."
                    }
                ]
            },
            "alphabetical": {"meanings": [{"def": "relating to the alphabet."}]},
            "encyclopaedia": {
                "meanings": [
                    {
                        "def": "a book or set of books giving information on many subjects or on many aspects of one subject and typically arranged alphabetically."
                    }
                ]
            },
            "novel": {
                "meanings": [
                    {
                        "def": "a fictitious prose narrative of book length, typically representing character and action with some degree of realism."
                    }
                ]
            },
            "anthology": {
                "meanings": [
                    {
                        "def": "a published collection of poems or other pieces of writing."
                    }
                ]
            },
            "extract": {
                "meanings": [
                    {
                        "def": "a short passage taken from a book, film, or piece of music."
                    }
                ]
            },
            "photocopy": {
                "meanings": [
                    {"def": "a photographic copy of printed or written material."}
                ]
            },
            "article": {"meanings": [{"def": "a particular item or object."}]},
            "fantasy": {
                "meanings": [
                    {
                        "def": "the faculty or activity of imagining things, especially things that are impossible or improbable."
                    }
                ]
            },
            "publisher": {
                "meanings": [
                    {
                        "def": "a person or company that prepares and issues books, journals, music, or other works for sale."
                    }
                ]
            },
            "author": {
                "meanings": [{"def": "a writer of a book, article, or report."}]
            },
            "relevant": {
                "meanings": [
                    {
                        "def": "closely connected or appropriate to what is being done or considered."
                    }
                ]
            },
            "relevance": {
                "meanings": [
                    {
                        "def": "the quality or state of being closely connected or appropriate."
                    }
                ]
            },
            "catalogue": {
                "meanings": [
                    {
                        "def": "a complete list of items, typically one in alphabetical or other systematic order."
                    }
                ]
            },
            "glossary": {
                "meanings": [
                    {
                        "def": "an alphabetical list of terms or words found in or relating to a specific subject, text, or dialect, with explanations; a brief dictionary."
                    }
                ]
            },
            "romance": {
                "meanings": [
                    {"def": "a feeling of excitement and mystery associated with love."}
                ]
            },
            "classification": {
                "meanings": [
                    {
                        "def": "the action or process of classifying something according to shared qualities or characteristics."
                    }
                ]
            },
            "index": {
                "meanings": [
                    {
                        "def": "an alphabetical list of names, subjects, etc., with references to the pages on which they are mentioned."
                    }
                ]
            },
            "section": {
                "meanings": [
                    {
                        "def": "any of the more or less distinct parts into which something is or may be divided or from which it is made up."
                    }
                ]
            },
            "content": {
                "meanings": [
                    {"def": "the things that are held or included in something."}
                ]
            },
            "irrelevant": {
                "meanings": [{"def": "not connected with or relevant to something."}]
            },
            "irrelevance": {
                "meanings": [
                    {"def": "lack of connection with or relevance to something."}
                ]
            },
            "series": {
                "meanings": [
                    {
                        "def": "a number of things, events, or people of a similar kind arranged in a sequence."
                    }
                ]
            },
            "copyright": {
                "meanings": [
                    {
                        "def": "the exclusive and assignable legal right, given to the originator for a fixed number of years, to print, publish, perform, film, or record literary, artistic, or musical material."
                    }
                ]
            },
            "librarian": {
                "meanings": [
                    {
                        "def": "a person who works in a library, especially one who is in charge of a department or section."
                    }
                ]
            },
            "system": {
                "meanings": [
                    {
                        "def": "a set of things working together as parts of a mechanism or an interconnecting network."
                    }
                ]
            },
            "dictionary": {
                "meanings": [
                    {
                        "def": "a book or resource that lists the words of a language and gives their meaning, or lists the words of one language and their equivalents in another."
                    }
                ]
            },
            "magazine": {
                "meanings": [
                    {
                        "def": "a periodical publication containing articles and illustrations, often on a particular subject or aimed at a particular readership."
                    }
                ]
            },
            "thesaurus": {
                "meanings": [
                    {
                        "def": "a book that lists words in groups of synonyms and related concepts."
                    }
                ]
            },
            "editor": {
                "meanings": [
                    {
                        "def": "a person who is in charge of and determines the final content of a newspaper, magazine, or multi-author book."
                    }
                ]
            },
            "non-fiction": {
                "meanings": [
                    {
                        "def": "prose writing that is informative or factual, rather than fictional."
                    }
                ]
            },
            "mathematics": {
                "meanings": [
                    {
                        "def": "the abstract science of number, quantity, and space, either as abstract concepts (pure mathematics), or as applied to other disciplines such as physics and engineering (applied mathematics)."
                    }
                ]
            },
            "addition": {
                "meanings": [
                    {
                        "def": "the action or process of adding something to something else."
                    }
                ]
            },
            "estimate": {
                "meanings": [
                    {
                        "def": "roughly calculate or judge the value, number, quantity, or extent of."
                    }
                ]
            },
            "positive": {
                "meanings": [
                    {
                        "def": "consisting in or characterized by the presence rather than the absence of distinguishing features."
                    }
                ]
            },
            "adjacent": {"meanings": [{"def": "next to or adjoining something else."}]},
            "equation": {
                "meanings": [
                    {
                        "def": "a statement that the values of two mathematical expressions are equal (indicated by the sign =)."
                    }
                ]
            },
            "quadrilateral": {"meanings": [{"def": "a four-sided polygon."}]},
            "alternate": {"meanings": [{"def": "every other; every second."}]},
            "fraction": {
                "meanings": [
                    {"def": "a numerical quantity that is not a whole number."}
                ]
            },
            "questionnaire": {
                "meanings": [
                    {
                        "def": "a set of printed or written questions with a choice of answers, devised for the purposes of a survey or statistical study."
                    }
                ]
            },
            "angle": {
                "meanings": [
                    {
                        "def": "the space (usually measured in degrees) between two intersecting lines or surfaces at or close to the point where they meet."
                    }
                ]
            },
            "graph": {
                "meanings": [
                    {
                        "def": "a diagram showing the relation between variable quantities, typically of two variables, each measured along one of a pair of axes at right angles."
                    }
                ]
            },
            "radius": {
                "meanings": [
                    {
                        "def": "a straight line from the center to the circumference of a circle or sphere."
                    }
                ]
            },
            "amount": {
                "meanings": [
                    {
                        "def": "a quantity of something, especially the total of a thing or things in number, size, value, or extent."
                    }
                ]
            },
            "guess": {
                "meanings": [
                    {
                        "def": "estimate or suppose (something) without sufficient information to be sure of being correct."
                    }
                ]
            },
            "ratio": {
                "meanings": [
                    {
                        "def": "the quantitative relation between two amounts showing the number of times one value contains or is contained within the other."
                    }
                ]
            },
            "approximately": {
                "meanings": [
                    {
                        "def": "used to show that something is almost, but not completely, accurate or exact; roughly."
                    }
                ]
            },
            "horizontal": {
                "meanings": [
                    {
                        "def": "parallel to the plane of the horizon; at right angles to the vertical."
                    }
                ]
            },
            "recurring": {
                "meanings": [{"def": "occurring again periodically or repeatedly."}]
            },
            "average": {
                "meanings": [
                    {
                        "def": "a number expressing the central or typical value in a set of data, in particular the mode, median, or (most commonly) the mean, which is calculated by dividing the sum of the values in the set by their number."
                    }
                ]
            },
            "isosceles": {"meanings": [{"def": "having two sides of equal length."}]},
            "reflect": {
                "meanings": [
                    {"def": "throw back (heat, light, or sound) without absorbing it."}
                ]
            },
            "reflection": {
                "meanings": [
                    {
                        "def": "the throwing back by a body or surface of light, heat, or sound without absorbing it."
                    }
                ]
            },
            "axis": {
                "meanings": [{"def": "an imaginary line about which a body rotates."}]
            },
            "axes": {"meanings": [{"def": "plural of axis."}]},
            "kilogram": {
                "meanings": [
                    {
                        "def": "the SI unit of mass, equivalent to the international prototype kept at Sèvres near Paris."
                    }
                ]
            },
            "regular": {
                "meanings": [
                    {
                        "def": "arranged in or constituting a constant or definite pattern, especially with the same space between individual instances."
                    }
                ]
            },
            "irregular": {
                "meanings": [{"def": "not even or balanced in shape or arrangement."}]
            },
            "calculate": {
                "meanings": [
                    {
                        "def": "determine (the amount or number of something) mathematically."
                    }
                ]
            },
            "kilometre": {
                "meanings": [
                    {"def": "a metric unit of measurement equal to 1,000 meters."}
                ]
            },
            "rhombus": {
                "meanings": [
                    {
                        "def": "a parallelogram with opposite equal acute angles, opposite equal obtuse angles, and four equal sides."
                    }
                ]
            },
            "centimetre": {
                "meanings": [
                    {
                        "def": "a metric unit of length, equal to one hundredth of a metre."
                    }
                ]
            },
            "litre": {
                "meanings": [
                    {
                        "def": "a metric unit of capacity, formerly defined as the volume of one kilogram of pure water under standard conditions; now equal to 1,000 cubic centimeters."
                    }
                ]
            },
            "rotate": {
                "meanings": [
                    {
                        "def": "move or cause to move in a circle around an axis or center."
                    }
                ]
            },
            "rotation": {
                "meanings": [
                    {"def": "the action of rotating around an axis or center."}
                ]
            },
            "circumference": {
                "meanings": [
                    {
                        "def": "the enclosing boundary of a curved geometric figure, especially a circle."
                    }
                ]
            },
            "measure": {
                "meanings": [
                    {
                        "def": "ascertain the size, amount, or degree of (something) by using an instrument or device marked in standard units."
                    }
                ]
            },
            "square": {
                "meanings": [
                    {
                        "def": "a plane figure with four equal straight sides and four right angles."
                    }
                ]
            },
            "corresponding": {
                "meanings": [
                    {"def": "analogous or equivalent in character, form, or function."}
                ]
            },
            "metre": {
                "meanings": [
                    {
                        "def": "the fundamental unit of length in the metric system, equal to the distance traveled by light in a vacuum in 1/299,792,458 seconds."
                    }
                ]
            },
            "subtraction": {
                "meanings": [
                    {
                        "def": "the process or skill of taking one number or amount away from another."
                    }
                ]
            },
            "co-ordinate": {
                "meanings": [
                    {
                        "def": "bring the different elements of (a complex activity or organization) into a harmonious or efficient relationship."
                    }
                ]
            },
            "minus": {"meanings": [{"def": "with the subtraction of."}]},
            "symmetry": {
                "meanings": [
                    {
                        "def": "the quality of being made up of exactly similar parts facing each other or around an axis."
                    }
                ]
            },
            "symmetrical": {
                "meanings": [
                    {
                        "def": "made up of exactly similar parts facing each other or around an axis."
                    }
                ]
            },
            "decimal": {
                "meanings": [
                    {
                        "def": "relating to or denoting a system of numbers and arithmetic based on the number ten, tenth parts, and powers of ten."
                    }
                ]
            },
            "multiply": {
                "meanings": [
                    {
                        "def": "obtain from (a number) another which contains the first number a specified number of times."
                    }
                ]
            },
            "multiplication": {
                "meanings": [{"def": "the process or skill of multiplying."}]
            },
            "triangle": {
                "meanings": [
                    {
                        "def": "a plane figure with three straight sides and three angles."
                    }
                ]
            },
            "triangular": {"meanings": [{"def": "shaped like a triangle."}]},
            "degree": {
                "meanings": [
                    {
                        "def": "a unit of measurement of angles, one three-hundred-and-sixtieth of the circumference of a circle."
                    }
                ]
            },
            "parallel": {
                "meanings": [
                    {
                        "def": "(of lines, planes, surfaces, or objects) side by side and having the same distance continuously between them."
                    }
                ]
            },
            "parallelogram": {
                "meanings": [
                    {
                        "def": "a four-sided plane rectilinear figure with opposite sides parallel."
                    }
                ]
            },
            "tonne": {
                "meanings": [{"def": "a unit of weight equal to 1,000 kilograms."}]
            },
            "denominator": {
                "meanings": [
                    {
                        "def": "the number below the line in a common fraction showing how many parts there are altogether."
                    }
                ]
            },
            "negative": {
                "meanings": [
                    {
                        "def": "consisting in or characterized by the absence rather than the presence of distinguishing features."
                    }
                ]
            },
            "vertex": {"meanings": [{"def": "the highest point; the top or apex."}]},
            "vertices": {"meanings": [{"def": "plural of vertex."}]},
            "diameter": {
                "meanings": [
                    {
                        "def": "a straight line passing from side to side through the center of a body or figure, especially a circle or sphere."
                    }
                ]
            },
            "numerator": {
                "meanings": [
                    {
                        "def": "the number above the line in a common fraction showing how many of the parts indicated by the denominator are taken."
                    }
                ]
            },
            "vertical": {
                "meanings": [
                    {
                        "def": "at right angles to the plane of the horizon or a base line."
                    }
                ]
            },
            "digit": {
                "meanings": [
                    {
                        "def": "any of the numerals from 0 to 9, especially when forming part of a number."
                    }
                ]
            },
            "percentage": {
                "meanings": [{"def": "a rate, number, or amount in each hundred."}]
            },
            "volume": {
                "meanings": [
                    {
                        "def": "the amount of space that a substance or object occupies, or that is enclosed within a container."
                    }
                ]
            },
            "divide": {"meanings": [{"def": "separate or be separated into parts."}]},
            "division": {
                "meanings": [
                    {
                        "def": "the action of separating something into parts or the process of being separated."
                    }
                ]
            },
            "perimeter": {
                "meanings": [
                    {
                        "def": "the continuous line forming the boundary of a closed geometrical figure."
                    }
                ]
            },
            "weight": {
                "meanings": [
                    {
                        "def": "a body's relative mass or the quantity of matter contained by it, giving rise to a downward force; the heaviness of a person or thing."
                    }
                ]
            },
            "equilateral": {
                "meanings": [{"def": "having all its sides of the same length."}]
            },
            "perpendicular": {
                "meanings": [
                    {"def": "at an angle of 90° to a given line, plane, or surface."}
                ]
            },
            "music": {
                "meanings": [
                    {
                        "def": "vocal or instrumental sounds (or both) combined in such a way as to produce beauty of form, harmony, and expression of emotion."
                    }
                ]
            },
            "choir": {
                "meanings": [
                    {
                        "def": "an organized group of singers, typically one that takes part in church services or performs regularly in public."
                    }
                ]
            },
            "minim": {
                "meanings": [
                    {
                        "def": "a musical note having the time value of two crotchets or one-half of a semibreve."
                    }
                ]
            },
            "score": {
                "meanings": [
                    {
                        "def": "the number of points, goals, runs, etc., achieved in a game or by a team or individual."
                    }
                ]
            },
            "chord": {
                "meanings": [
                    {
                        "def": "a group of (typically three or more) notes sounded together, as a basis of harmony."
                    }
                ]
            },
            "minor": {
                "meanings": [
                    {"def": "lesser in importance, seriousness, or significance."}
                ]
            },
            "semibreve": {
                "meanings": [
                    {
                        "def": "a musical note having the longest time value, equal to four crotchets or two minims."
                    }
                ]
            },
            "chromatic": {
                "meanings": [
                    {
                        "def": "relating to or using notes not belonging to the diatonic scale of the key in which a passage is written."
                    }
                ]
            },
            "musician": {
                "meanings": [
                    {
                        "def": "a person who plays a musical instrument, especially as a profession, or is musically talented."
                    }
                ]
            },
            "synchronise": {
                "meanings": [
                    {"def": "cause to occur or operate at the same time or rate."}
                ]
            },
            "composition": {
                "meanings": [
                    {
                        "def": "the nature of something's ingredients or constituents; the way in which a whole or mixture is made up."
                    }
                ]
            },
            "conductor": {
                "meanings": [
                    {
                        "def": "a person who directs the performance of an orchestra or choir."
                    }
                ]
            },
            "octave": {
                "meanings": [
                    {
                        "def": "a series of eight notes occupying the interval between (and including) two notes, one having twice or half the frequency of vibration of the other."
                    }
                ]
            },
            "syncopation": {
                "meanings": [
                    {
                        "def": "a displacement of the normal accent, usually by stressing a normally unstressed beat."
                    }
                ]
            },
            "crotchet": {
                "meanings": [
                    {
                        "def": "a musical note having the time value of a quarter of a whole note."
                    }
                ]
            },
            "orchestra": {
                "meanings": [
                    {
                        "def": "a large instrumental ensemble typical of classical music, with sections of strings, woodwind, brass, and percussion."
                    }
                ]
            },
            "orchestral": {"meanings": [{"def": "relating to an orchestra."}]},
            "tempo": {
                "meanings": [
                    {
                        "def": "the speed at which a passage of music is or should be played."
                    }
                ]
            },
            "dynamics": {"meanings": [{"def": "the volume of sound in music."}]},
            "ostinato": {
                "meanings": [
                    {"def": "a continually repeated musical phrase or rhythm."}
                ]
            },
            "ternary": {"meanings": [{"def": "composed of three parts."}]},
            "harmony": {
                "meanings": [
                    {
                        "def": "the combination of simultaneously sounded musical notes to produce chords and chord progressions having a pleasing effect."
                    }
                ]
            },
            "percussion": {
                "meanings": [
                    {
                        "def": "musical instruments played by striking with the hand or with a handheld or pedal-operated stick or beater, or by shaking, including drums, cymbals, xylophones, gongs, bells, and rattles."
                    }
                ]
            },
            "timbre": {
                "meanings": [
                    {
                        "def": "the character or quality of a musical sound or voice as distinct from its pitch and intensity."
                    }
                ]
            },
            "instrument": {
                "meanings": [
                    {"def": "a tool or implement, especially one for precision work."}
                ]
            },
            "instrumental": {
                "meanings": [
                    {"def": "serving as a means of pursuing an aim or policy."}
                ]
            },
            "pitch": {
                "meanings": [
                    {
                        "def": "the quality of a sound governed by the rate of vibrations producing it; the degree of highness or lowness of a tone."
                    }
                ]
            },
            "triad": {"meanings": [{"def": "a group of three."}]},
            "interval": {"meanings": [{"def": "an intervening period of time."}]},
            "quaver": {
                "meanings": [
                    {
                        "def": "a musical note having the time value of an eighth of a whole note."
                    }
                ]
            },
            "vocal": {"meanings": [{"def": "relating to the human voice."}]},
            "lyric": {
                "meanings": [
                    {
                        "def": "expressing the writer's emotions, usually briefly and in stanzas or recognized forms."
                    }
                ]
            },
            "rhythm": {
                "meanings": [
                    {"def": "a strong, regular, repeated pattern of movement or sound."}
                ]
            },
            "major": {"meanings": [{"def": "important, serious, or significant."}]},
            "scale": {
                "meanings": [
                    {
                        "def": "each of the small, thin horny or bony plates protecting the skin of fish and reptiles, typically overlapping one another."
                    }
                ]
            },
            "pe": {"meanings": [{"def": "physical education."}]},
            "active": {
                "meanings": [
                    {
                        "def": "engaging or ready to engage in physically energetic pursuits."
                    }
                ]
            },
            "activity": {
                "meanings": [
                    {
                        "def": "the condition in which things are happening or being done."
                    }
                ]
            },
            "injury": {
                "meanings": [
                    {
                        "def": "physical harm or damage to someone's body caused by an accident or an attack."
                    }
                ]
            },
            "qualify": {
                "meanings": [
                    {
                        "def": "be entitled to a particular benefit or privilege by fulfilling a necessary condition."
                    }
                ]
            },
            "agile": {"meanings": [{"def": "quick and well-coordinated in movement."}]},
            "agility": {"meanings": [{"def": "ability to move quickly and easily."}]},
            "league": {
                "meanings": [
                    {
                        "def": "a collection of people, countries, or groups that combine for a common action, especially a temporary alliance of political parties forming a government or of states."
                    }
                ]
            },
            "relay": {
                "meanings": [
                    {
                        "def": "a group of people or animals engaged in a task of conveying something by passing it in turn from one to another."
                    }
                ]
            },
            "athletic": {"meanings": [{"def": "physically strong, fit, and active."}]},
            "athlete": {
                "meanings": [
                    {
                        "def": "a person who is proficient in sports and other forms of physical exercise."
                    }
                ]
            },
            "medicine": {
                "meanings": [
                    {
                        "def": "the science or practice of the diagnosis, treatment, and prevention of disease."
                    }
                ]
            },
            "squad": {
                "meanings": [
                    {"def": "a small group of people having a particular task."}
                ]
            },
            "bicep": {
                "meanings": [
                    {
                        "def": "a muscle at the front of the upper arm that flexes the forearm."
                    }
                ]
            },
            "mobile": {
                "meanings": [{"def": "able to move or be moved freely or easily."}]
            },
            "mobility": {
                "meanings": [
                    {"def": "the ability to move or be moved freely and easily."}
                ]
            },
            "tactic": {
                "meanings": [
                    {
                        "def": "an action or strategy carefully planned to achieve a specific end."
                    }
                ]
            },
            "exercise": {
                "meanings": [
                    {
                        "def": "activity requiring physical effort, carried out to sustain or improve health and fitness."
                    }
                ]
            },
            "muscle": {
                "meanings": [
                    {
                        "def": "a band or bundle of fibrous tissue in a human or animal body that has the ability to contract, producing movement in or maintaining the position of parts of the body."
                    }
                ]
            },
            "tournament": {
                "meanings": [
                    {
                        "def": "a series of contests between a number of competitors, who compete for an overall prize."
                    }
                ]
            },
            "field": {
                "meanings": [
                    {
                        "def": "an area of open land, especially one planted with crops or pasture, typically bounded by hedges or fences."
                    }
                ]
            },
            "personal": {
                "meanings": [
                    {
                        "def": "belonging to or affecting a particular person rather than anyone else."
                    }
                ]
            },
            "triceps": {
                "meanings": [
                    {"def": "a muscle with three heads that extends the forearm."}
                ]
            },
            "gym": {"meanings": [{"def": "a gymnasium."}]},
            "gymnastic": {
                "meanings": [
                    {
                        "def": "relating to physical exercises and activities performed inside, often on specialized apparatus, as a sport."
                    }
                ]
            },
            "hamstring": {
                "meanings": [
                    {"def": "any of five tendons at the back of a person's knee."}
                ]
            },
            "quadriceps": {
                "meanings": [
                    {
                        "def": "a large muscle at the front of the thigh, which is divided into four distinct portions and acts to extend the leg."
                    }
                ]
            },
            "pshe": {
                "meanings": [
                    {"def": "personal, social, health and economic education."}
                ]
            },
            "able": {
                "meanings": [
                    {
                        "def": "having the power, skill, means, or opportunity to do something."
                    }
                ]
            },
            "ability": {
                "meanings": [
                    {"def": "possession of the means or skill to do something."}
                ]
            },
            "effort": {"meanings": [{"def": "a vigorous or determined attempt."}]},
            "reality": {
                "meanings": [
                    {
                        "def": "the state of things as they actually exist, as opposed to an idealistic or notional idea of them."
                    }
                ]
            },
            "achieve": {
                "meanings": [
                    {
                        "def": "successfully bring about or reach (a desired objective, level, or result) by effort, skill, or courage."
                    }
                ]
            },
            "achievement": {
                "meanings": [
                    {"def": "a thing done successfully with effort, skill, or courage."}
                ]
            },
            "emotion": {
                "meanings": [
                    {
                        "def": "a natural instinctive state of mind deriving from one's circumstances, mood, or relationships with others."
                    }
                ]
            },
            "emotional": {"meanings": [{"def": "relating to a person's emotions."}]},
            "relationship": {
                "meanings": [
                    {
                        "def": "the way in which two or more concepts, objects, or people are connected, or the state of being connected."
                    }
                ]
            },
            "addict": {
                "meanings": [
                    {
                        "def": "a person who is addicted to a particular substance, typically a drug."
                    }
                ]
            },
            "addiction": {
                "meanings": [
                    {
                        "def": "the fact or condition of being addicted to a particular substance, thing, or activity."
                    }
                ]
            },
            "encourage": {
                "meanings": [{"def": "give support, confidence, or hope to (someone)."}]
            },
            "encouragement": {
                "meanings": [
                    {
                        "def": "the action of giving someone support, confidence, or hope."
                    }
                ]
            },
            "represent": {
                "meanings": [
                    {
                        "def": "be entitled or appointed to act or speak for (someone), especially in an official capacity."
                    }
                ]
            },
            "representative": {
                "meanings": [
                    {
                        "def": "a person chosen or appointed to act or speak for another or others."
                    }
                ]
            },
            "approve": {
                "meanings": [{"def": "officially agree to or accept as satisfactory."}]
            },
            "approval": {
                "meanings": [
                    {
                        "def": "the action of officially agreeing to something or accepting something as satisfactory."
                    }
                ]
            },
            "gender": {
                "meanings": [
                    {
                        "def": "the state of being male or female (typically used with reference to social and cultural differences rather than biological ones)."
                    }
                ]
            },
            "reward": {
                "meanings": [
                    {
                        "def": "a thing given in recognition of one's service, effort, or achievement."
                    }
                ]
            },
            "communication": {
                "meanings": [
                    {
                        "def": "the imparting or exchanging of information by speaking, writing, or using some other medium."
                    }
                ]
            },
            "generous": {
                "meanings": [
                    {
                        "def": "showing a readiness to give more of something, as money or time, than is strictly necessary or expected."
                    }
                ]
            },
            "generosity": {
                "meanings": [{"def": "the quality of being kind and generous."}]
            },
            "sanction": {
                "meanings": [
                    {"def": "a threatened penalty for disobeying a law or rule."}
                ]
            },
            "control": {
                "meanings": [
                    {
                        "def": "the power to influence or direct people's behavior or the course of events."
                    }
                ]
            },
            "involve": {
                "meanings": [
                    {
                        "def": "have or include (something) as a necessary or integral part or result."
                    }
                ]
            },
            "involvement": {
                "meanings": [
                    {
                        "def": "the fact or condition of being involved with or participating in something."
                    }
                ]
            },
            "sexism": {
                "meanings": [
                    {
                        "def": "prejudice, stereotyping, or discrimination, typically against women, on the basis of sex."
                    }
                ]
            },
            "sexist": {
                "meanings": [
                    {
                        "def": "showing prejudice, stereotyping, or discrimination, typically against women, on the basis of sex."
                    }
                ]
            },
            "dependant": {"meanings": [{"def": "contingent on or determined by."}]},
            "dependency": {"meanings": [{"def": "dependence."}]},
            "prefer": {
                "meanings": [
                    {"def": "like (one thing or person better than another or others."}
                ]
            },
            "preference": {
                "meanings": [
                    {
                        "def": "a greater liking for one alternative over another or others."
                    }
                ]
            },
            "stereotype": {
                "meanings": [
                    {
                        "def": "a widely held but fixed and oversimplified image or idea of a particular type of person or thing."
                    }
                ]
            },
            "discipline": {
                "meanings": [
                    {
                        "def": "the practice of training people to obey rules or a code of behavior, using punishment to correct disobedience."
                    }
                ]
            },
            "pressure": {
                "meanings": [
                    {
                        "def": "continuous physical force exerted on or against an object by something in contact with it."
                    }
                ]
            },
            "discussion": {
                "meanings": [
                    {
                        "def": "the action or process of talking about something, typically in order to reach a decision or to exchange ideas."
                    }
                ]
            },
            "racism": {
                "meanings": [
                    {
                        "def": "prejudice, discrimination, or antagonism directed against someone of a different race based on the belief that one's own race is superior."
                    }
                ]
            },
            "racist": {
                "meanings": [
                    {
                        "def": "showing or feeling discrimination or prejudice against people of other races, or believing that a particular race is superior to another."
                    }
                ]
            },
            "re": {
                "meanings": [
                    {
                        "def": "in the matter of (used typically as the first word in the heading of an official document or to introduce a reference in a formal letter)."
                    }
                ]
            },
            "baptism": {
                "meanings": [
                    {
                        "def": "a Christian sacrament marked by ritual use of water and admitting the recipient to the Christian community."
                    }
                ]
            },
            "hindu": {"meanings": [{"def": "a person who adheres to Hinduism."}]},
            "hinduism": {
                "meanings": [
                    {
                        "def": "a major religion, originating in the Vedic tradition of India, characterized by a belief in reincarnation and a supreme being of many forms and natures, by the way of righteousness and truth, and by the liberation from the cycle of rebirth."
                    }
                ]
            },
            "prophet": {
                "meanings": [
                    {
                        "def": "a person regarded as an inspired teacher or proclaimer of the will of God."
                    }
                ]
            },
            "bible": {
                "meanings": [
                    {
                        "def": "the holy scripture of Christianity, a collection of ancient writings including the books of both the Old Testament and New Testament."
                    }
                ]
            },
            "biblical": {"meanings": [{"def": "of or relating to the Bible."}]},
            "hymn": {
                "meanings": [
                    {"def": "a religious song or poem of praise to God or a god."}
                ]
            },
            "religion": {
                "meanings": [
                    {
                        "def": "the belief in and worship of a superhuman controlling power, especially a personal God or gods."
                    }
                ]
            },
            "buddhist": {
                "meanings": [
                    {"def": "a follower of the religion founded by the Buddha."}
                ]
            },
            "buddhism": {
                "meanings": [
                    {
                        "def": "a widespread Asian religion or philosophy, founded by Siddartha Gautama (the Buddha) in India in the 5th century BC."
                    }
                ]
            },
            "immoral": {
                "meanings": [
                    {"def": "not conforming to accepted standards of morality."}
                ]
            },
            "immorality": {
                "meanings": [
                    {"def": "the state or quality of being immoral; wickedness."}
                ]
            },
            "shrine": {
                "meanings": [
                    {
                        "def": "a place regarded as holy because of its associations with a divinity or a sacred person or relic, marked by a building or other construction."
                    }
                ]
            },
            "burial": {
                "meanings": [
                    {"def": "the action or ceremony of placing a dead body in a grave."}
                ]
            },
            "islam": {
                "meanings": [
                    {
                        "def": "the religion of the Muslims, a monotheistic faith regarded as revealed through Muhammad as the Prophet of Allah."
                    }
                ]
            },
            "sign": {
                "meanings": [
                    {
                        "def": "an object, quality, or event whose presence or occurrence indicates the probable presence or occurrence of something else."
                    }
                ]
            },
            "celebrate": {
                "meanings": [
                    {
                        "def": "acknowledge (a significant or happy day or event) with a social gathering or enjoyable activity."
                    }
                ]
            },
            "celebration": {
                "meanings": [
                    {
                        "def": "the action of marking one's pleasure at an important event or occasion by engaging in enjoyable, typically social, activity."
                    }
                ]
            },
            "israel": {
                "meanings": [
                    {"def": "a country in Western Asia, on the Mediterranean Sea."}
                ]
            },
            "sikh": {"meanings": [{"def": "a follower of Sikhism."}]},
            "sikhism": {
                "meanings": [
                    {
                        "def": "a monotheistic religion founded in the Punjab region of India in the 15th century by Guru Nanak."
                    }
                ]
            },
            "ceremony": {
                "meanings": [
                    {
                        "def": "a formal religious or public occasion, especially one celebrating a particular event or anniversary."
                    }
                ]
            },
            "judaism": {
                "meanings": [
                    {
                        "def": "the monotheistic religion of the Jews, founded by Abraham and having its spiritual and ethical principles embodied chiefly in the Torah and the Talmud."
                    }
                ]
            },
            "jewish": {
                "meanings": [{"def": "relating to Jews or their culture or religion."}]
            },
            "special": {
                "meanings": [
                    {
                        "def": "better, greater, or otherwise different from what is usual."
                    }
                ]
            },
            "christian": {
                "meanings": [
                    {"def": "relating to or professing Christianity or its teachings."}
                ]
            },
            "marriage": {
                "meanings": [
                    {
                        "def": "the legally or formally recognized union of two people as partners in a personal relationship."
                    }
                ]
            },
            "spirit": {
                "meanings": [
                    {
                        "def": "the non-physical part of a person which is the seat of emotions and character; the soul."
                    }
                ]
            },
            "spiritual": {
                "meanings": [
                    {
                        "def": "relating to or affecting the human spirit or soul as opposed to material or physical things."
                    }
                ]
            },
            "commandment": {"meanings": [{"def": "an authoritative order."}]},
            "miracle": {
                "meanings": [
                    {
                        "def": "an extraordinary and welcome event that is not explicable by natural or scientific laws and is therefore attributed to a divine agency."
                    }
                ]
            },
            "symbol": {
                "meanings": [
                    {
                        "def": "a thing that represents or stands for something else, especially a material object representing something abstract."
                    }
                ]
            },
            "commitment": {
                "meanings": [
                    {
                        "def": "the state or quality of being dedicated to a cause, activity, etc."
                    }
                ]
            },
            "moral": {
                "meanings": [
                    {
                        "def": "concerned with the principles of right and wrong behavior."
                    }
                ]
            },
            "morality": {
                "meanings": [
                    {
                        "def": "principles concerning the distinction between right and wrong or good and bad behavior."
                    }
                ]
            },
            "synagogue": {
                "meanings": [
                    {
                        "def": "the building where a Jewish assembly or congregation meets for religious observance and instruction."
                    }
                ]
            },
            "creation": {
                "meanings": [
                    {
                        "def": "the action or process of bringing something into existence."
                    }
                ]
            },
            "muslim": {"meanings": [{"def": "a follower of the religion of Islam."}]},
            "temple": {
                "meanings": [
                    {
                        "def": "a building devoted to the worship, or regarded as the dwelling place, of a god or gods."
                    }
                ]
            },
            "disciple": {
                "meanings": [
                    {
                        "def": "a personal follower of Jesus during his life, especially one of the twelve Apostles."
                    }
                ]
            },
            "parable": {
                "meanings": [
                    {
                        "def": "a simple story used to illustrate a moral or spiritual lesson, as told by Jesus in the Gospels."
                    }
                ]
            },
            "wedding": {
                "meanings": [
                    {
                        "def": "a marriage ceremony, especially considered as including the associated celebrations."
                    }
                ]
            },
            "faith": {
                "meanings": [
                    {"def": "complete trust or confidence in someone or something."}
                ]
            },
            "pilgrim": {
                "meanings": [
                    {
                        "def": "a person who journeys to a sacred place for religious reasons."
                    }
                ]
            },
            "pilgrimage": {"meanings": [{"def": "a pilgrimage."}]},
            "worship": {
                "meanings": [
                    {
                        "def": "the feeling or expression of reverence and adoration for a deity."
                    }
                ]
            },
            "festival": {
                "meanings": [
                    {
                        "def": "a day or period of celebration, typically a religious commemoration."
                    }
                ]
            },
            "pray": {
                "meanings": [{"def": "address a prayer to God or another deity."}]
            },
            "prayer": {
                "meanings": [
                    {
                        "def": "a solemn request for help or expression of thanks addressed to God or another deity."
                    }
                ]
            },
            "funeral": {
                "meanings": [
                    {
                        "def": "a ceremony held in connection with the burial or cremation of a dead person."
                    }
                ]
            },
            "prejudice": {
                "meanings": [
                    {
                        "def": "preconceived opinion that is not based on reason or actual experience."
                    }
                ]
            },
            "science": {
                "meanings": [
                    {
                        "def": "the intellectual and practical activity encompassing the systematic study of the structure and behavior of the physical and natural world through observation and experiment."
                    }
                ]
            },
            "absorb": {
                "meanings": [
                    {
                        "def": "take in or soak up (energy, or a liquid or other substance) by chemical or physical action, typically gradually."
                    }
                ]
            },
            "exchange": {
                "meanings": [
                    {
                        "def": "an act of giving one thing and receiving another (especially of the same type or value) in return."
                    }
                ]
            },
            "organism": {
                "meanings": [
                    {"def": "an individual animal, plant, or single-celled life form."}
                ]
            },
            "acid": {
                "meanings": [
                    {
                        "def": "a chemical substance that neutralizes alkalis, dissolves some metals, and turns litmus red; typically, a corrosive or sour-tasting liquid of this kind."
                    }
                ]
            },
            "freeze": {
                "meanings": [
                    {
                        "def": "turn into ice or another solid as a result of extreme cold."
                    }
                ]
            },
            "oxygen": {
                "meanings": [
                    {
                        "def": "a reactive gas, the chemical element of atomic number 8 and the life-supporting component of the air."
                    }
                ]
            },
            "alkaline": {
                "meanings": [
                    {
                        "def": "having the properties of an alkali, or containing alkali; having a pH greater than 7."
                    }
                ]
            },
            "frequency": {
                "meanings": [
                    {
                        "def": "the rate at which something occurs or is repeated over a particular period of time or in a given sample."
                    }
                ]
            },
            "particles": {"meanings": [{"def": "a minute portion of matter."}]},
            "amphibian": {
                "meanings": [
                    {
                        "def": "a cold-blooded vertebrate animal of a class that comprises the frogs, toads, newts, and salamanders. They are distinguished by having an aquatic gill-breathing larval stage followed (typically) by a terrestrial lung-breathing adult stage."
                    }
                ]
            },
            "friction": {
                "meanings": [
                    {
                        "def": "the resistance that one surface or object encounters when moving over another."
                    }
                ]
            },
            "predator": {
                "meanings": [{"def": "an animal that naturally preys on others."}]
            },
            "apparatus": {
                "meanings": [
                    {
                        "def": "the technical equipment or machinery needed for a particular activity or purpose."
                    }
                ]
            },
            "chemical": {
                "meanings": [
                    {"def": "a substance produced by or used in a chemical process."}
                ]
            },
            "growth": {
                "meanings": [{"def": "the process of increasing in physical size."}]
            },
            "reproduce": {"meanings": [{"def": "produce a copy of."}]},
            "circulate": {
                "meanings": [
                    {
                        "def": "move continuously or freely through a closed system or area."
                    }
                ]
            },
            "circulation": {
                "meanings": [
                    {
                        "def": "the movement of blood around the body, pumped by the heart."
                    }
                ]
            },
            "hazard": {"meanings": [{"def": "a danger or risk."}]},
            "respire": {"meanings": [{"def": "breathe."}]},
            "respiration": {"meanings": [{"def": "the action of breathing."}]},
            "combustion": {"meanings": [{"def": "the process of burning something."}]},
            "insect": {
                "meanings": [
                    {
                        "def": "a small arthropod animal that has six legs and generally one or two pairs of wings."
                    }
                ]
            },
            "solution": {
                "meanings": [
                    {
                        "def": "a means of solving a problem or dealing with a difficult situation."
                    }
                ]
            },
            "condensation": {
                "meanings": [{"def": "the conversion of a vapor or gas to a liquid."}]
            },
            "laboratory": {
                "meanings": [
                    {
                        "def": "a room or building equipped for scientific experiments, research, or teaching, or for the manufacture of drugs or chemicals."
                    }
                ]
            },
            "temperature": {
                "meanings": [
                    {
                        "def": "the degree or intensity of heat present in a substance or object, especially as expressed according to a comparative scale and shown by a thermometer or perceived by touch."
                    }
                ]
            },
            "cycle": {
                "meanings": [
                    {
                        "def": "a series of events that are regularly repeated in the same order."
                    }
                ]
            },
            "liquid": {
                "meanings": [
                    {
                        "def": "a substance that flows freely but is of constant volume, having a consistency like that of water or oil."
                    }
                ]
            },
            "thermometer": {
                "meanings": [
                    {
                        "def": "an instrument for measuring and indicating temperature, typically one consisting of a narrow, hermetically sealed glass tube marked with a standardized scale and containing mercury or colored alcohol which expands and contracts with temperature changes."
                    }
                ]
            },
            "digest": {
                "meanings": [
                    {
                        "def": "break down (food) in the alimentary canal into substances that can be absorbed and used by the body."
                    }
                ]
            },
            "digestion": {
                "meanings": [
                    {
                        "def": "the process of breaking down food by mechanical and enzymatic action in the alimentary canal into substances that can be used by the body."
                    }
                ]
            },
            "mammal": {
                "meanings": [
                    {
                        "def": "a warm-blooded vertebrate animal of a class that is distinguished by the possession of hair or fur, the secretion of milk by females for the nourishment of the young, and (typically) the birth of live young."
                    }
                ]
            },
            "vertebrate": {
                "meanings": [
                    {
                        "def": "an animal of a large group distinguished by the possession of a backbone or spinal column, including mammals, birds, reptiles, amphibians, and fishes."
                    }
                ]
            },
            "element": {
                "meanings": [
                    {
                        "def": "an essential or characteristic part of something abstract."
                    }
                ]
            },
            "method": {
                "meanings": [
                    {
                        "def": "a particular form of procedure for accomplishing or approaching something, especially a systematic or established one."
                    }
                ]
            },
            "vessel": {"meanings": [{"def": "a ship or large boat."}]},
            "evaporation": {
                "meanings": [{"def": "the process of turning from liquid into vapor."}]
            },
            "nutrient": {
                "meanings": [
                    {
                        "def": "a substance that provides nourishment essential for growth and the maintenance of life."
                    }
                ]
            },
        }

    def get_words_by_length(self, min_length, max_length):
        """Get words within the specified length range."""
        return {
            word: details["meanings"][0].get("def", "")
            for word, details in self.dictionary.items()
            if min_length <= len(word) <= max_length and word.isalpha()
        }
