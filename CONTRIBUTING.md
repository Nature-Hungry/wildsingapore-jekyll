
# Content structure
In Jekyll, each page is made out of 2 sections, the frontmatter and the content.
## Frontmatter
The frontmatter contains important information about a page.
It is written in a language called yaml.
It is declared in a section marked by "---" in the beginning of the file.

The format of the fields goes like this ➜ fieldname ➜ ":" ➜ `<space>` ➜ fieldvalue

[10 minute read on how to use this language](https://www.cloudbees.com/blog/yaml-tutorial-everything-you-need-get-started)
 #### Example:
```yaml
---
title: ""
description: ""
keywords: ""
layout: entry
attributes: []
family: Pomacentridae
genus: Pomacentrus
species: tripunctatus
inat_id: 55185
stateofmatter: Life
kingdom: Animalia
phylum: Chordata
subphylum: Vertebrata
class: Actinopterygii
superorder: Acanthomorpha
order: Blenniiformes
subfamily: Pomacentrinae
updated: Oct 2020
forms:
- juvenile:
		img: ""
		summary: ""
		size:
		- 2.0
		- 3.0
coverimg: ""
galleries: {}
links_references: ''
location: []
size:
- 20.0
- 12.0
- 15.0
rdb: LC
zone:
- intertidal
- marine
authors:
- '[Ria Tan](https://www.facebook.com/wildsingapore/)'
---

** Content goes here **
```
### Special fields
#### Links & References
It is a multiple line string that is formatted in the markdown language(same as the content section)
```yaml
links_references: |
	**Links** 
	- [Sea Squirt *Polycarpa*]http://mangrove.nus.edu.sg/pub/seashore/text/226) Tan, Leo W. H. & Ng, Peter K. L., 1988. - [*A Guide to Seashore Life*](http://mangrove.nus.edu.sg/pub/seashore/). The Singapore Science Centre, Singapore. 160 pp. - [Ascidiacea World Database (http://www.marinespecies.org/ascidiacea/index.php): technical fact sheets 
	- [The Dutch Ascidians Homepage](http://www.ascidians.com/)by Arjan Gittenberger: general introduction and photos of a wide range of ascidians.
	- [Ascidians: Sea Squirts, Tunicates](http://www.seaslugforum.net/ascidian) on the Sea Slug Forum by Dr Bill Rudman: an introduction with close-up photos. 
	- [Ascidians](http://www.mesa.edu.au/friends/seashores/ascidians.html) on [Life on Australian Seashores (http://www.mesa.edu.au/friends/seashores/page1.html) by Keith Davey on the Marine Education Society of Australia website: a fabulous goldmine of a site which covers various kinds of intertidal habitats and their inhabitants. Fact sheet on ascidians with lovely diagrams showing the changes that the larva goes through as it develops into an adult, and details on a species found in Australia.
	- on the wild shores of singapore blog - [Blobs in the sea help us understand human health issues (http://wildshores.blogspot.com/2011/04/blobs-in-sea-help-us-understand-human.html)
	**References** 
	- Serina S-C Lee, Janlin Y-H Chan, Serena L-M Teo & Gretchen Lambert. State of knowledge of ascidian diversity in South China Sea and new records for Singapore. 29 June 2016. Raffles Bulletin of Zoology Supplement No. 34: 718-743. - Tan Siong Kiat, Rene Ong & Toh Chay Hoon. 4 December 2015. *Records of Lamellaria snails in Singapore*. Singapore Biodiversity Records 2015: 193-195 
	- Monniot, Claude, Francoise Monniot and Pierre Laboute 1991. *Coral Reef Ascidians of New Caledonia*. Editions de Porstom.pp. 247 - Edward E. Ruppert, Richard S. Fox, Robert D. Barnes. 2004. *Invertebrate Zoology* Brooks/Cole of Thomson Learning Inc., 7th Edition. pp. 963 - Pechenik, Jan A., 2005. Biology of the Invertebrates. 5th edition. McGraw-Hill Book Co., Singapore. 578 pp. 
	- Wee Y.C. and Peter K. L. Ng. 1994. A First Look at Biodiversity in Singapore. National Council on the Environment. 163pp. - Ng, P. K. L. & Y. C. Wee, 1994. The Singapore Red Data Book: Threatened Plants and Animals of Singapore. The Nature Society (Singapore),Singapore. 343 pp.

```
## Content
The content is written in a language called markdown. It is very simple and easy to learn.
### Headers 
use the `#` symbol followed by a space to create headings. The number of hashes corresponds to the heading level (up to 6)
```markdown
# Heading 1 
## Heading 2 
### Heading 3 
#### Heading 4 
##### Heading 5 
###### Heading 6
```

### Text Emphasis
```markdown
*Italic text* or _Italic text_ 
**Bold text** or __Bold text__ 
***Bold and italic text*** 
~~Strikethrough text~~
```
*Italic text* or _Italic text_ 
**Bold text** or __Bold text__ 
***Bold and italic text*** 
~~Strikethrough text~~
### Links
```markdown
Visit the official [Markdown Guide](https://www.markdownguide.org/).
```
Visit the official [Markdown Guide](https://www.markdownguide.org/).
### Horizontal lines
```markdown
Written using 3 asteriks "***"
or 3 dashes "---"
```
***


### Image galleries
To add images to the page, we use the img-wrap-group widget

You first have to declare the images that you are going to use in the frontmatter
```yaml
---
galleries:
	gallery1:
	- url: ""		# Link of the image uploaded to a cloud service
	  caption: ""	# Optional caption of image
	- url: ""		# Each dash represents another image
	  caption: ""	# Take note of the number of spaces before the field
---
```

Then in the content section, add this piece of code and modify the `items` field in the widget tag. In this case, we are using gallery1, so we would add `page.galleries.gallery1` to the `items=` fields.

```markdown
{% include img-wrap-group.html items=page.galleries.gallery1 %}
```

## Collection Types
Currently there 2 collections, entries and photoindexes. Entries are for pages that write about a specific species or any other higher level taxa. Photoindexes are for aggregating multiple entries and grouping entries with similar features.
### Entries
Found in the `_entries` folder
The field `layout` must be `entry`
```yaml
layout: entry
```
Each entry must have a title and coverimg.
Fill in the taxa ranks as far down as possible.

The size field is a list of the possible size range in centimeters, so for something that is between 1cm and 10cm, write this 
```yaml
size:
- 1.0
- 10.0
```
The habitats field which is missing from most entries will be an array of either of these habitats
```yaml
habitats:
- "mangrove"
- "mudflat"
- "coastal forest"
- "rocky shore"
- "sandy shore"
- "seagrass meadow"
- "coral rubble"
- "coral reef"
- "native forest"
- "exotic forest"
- "grassland"
- "scrubland"
- "urban park"
- "built-up"
- "freshwater swamp"
- "freshwater marsh"
```
The zone field has 4 options
```yaml
zone:
- terrestrial
- freshwater
- intertidal
- marine
```

Attributes field is a list of numbers from the attributes map file which can be found in `/_data/attribute_map.yaml`.
```yaml
attributes:
- 130
- 131
- 139
- 150
- 129
```

### Photo indexes
Found in the `_photoindexes` folder

For photo indexes, copy the format below. Modify everything except for the `{% for row in page.child_pages %}` ... `{% endfor %}` block.

For the child pages, their labels are rendered using markdown too. For now you can leave the links in them empty

The attributes field uses numbers from the attribute map file which can be found in `/_data/attribute_map.yaml`.
``` yaml
---
title: "Sea anemones and anemone-like animals"
description: ""
keywords: ""
layout: default
coverimgs:
- https://f003.backblazeb2.com/file/naturehungry/cnidaria/others/zoanthid/zoanthus/040828skdd5545ma.jpg
- https://live.staticflickr.com/65535/51397335434_46fe365f82_m.jpg
- https://live.staticflickr.com/2902/14364258483_1d5b79510e_m.jpg
- https://live.staticflickr.com/65535/50350364478_e6cdfa8d26_m.jpg
- https://live.staticflickr.com/1772/42236481640_0f74392243_m.jpg
attributes:
- 129
- 130
- 153
- 130
- 133
- 134
child_pages:
- label: "[Diameter < 3cm](/photoindexes/cnidaria/actiniara/anemone_lt3)<br>including small ones on snail shells"
  images:
  - url: "https://f003.backblazeb2.com/file/naturehungry/cnidaria/actiniaria/beadbanded/050527srbd3486m.jpg"
  - url: "https://f003.backblazeb2.com/file/naturehungry/cnidaria/others/zoanthid/tuberculosa/040123sisd0133m.jpg"
  - url: "https://f003.backblazeb2.com/file/naturehungry/cnidaria/actiniaria/hermitbig/040701chgd1385m.jpg"
  - url: "https://f003.backblazeb2.com/file/naturehungry/cnidaria/others/zoanthid/zoanthus/040828skdd5545ma.jpg"
- label: "[Diameter < 3-5cm Long tentacles]()"
  images:
  - url: "https://f003.backblazeb2.com/file/naturehungry/cnidaria/actiniaria/sandstripe/060429skdd1375m.jpg"
  - url: "https://f003.backblazeb2.com/file/naturehungry/cnidaria/actiniaria/spoke/050509hntg5945m.jpg"
  - url: "https://f003.backblazeb2.com/file/naturehungry/cnidaria/actiniaria/star/060401ulrd0828m.jpg"
  - url: "https://f003.backblazeb2.com/file/naturehungry/cnidaria/actiniaria/mangrove/060627krjd3666ma.jpg"
- label: "[Diameter < 3-5cm Short tentacles]()<br>"
  images:
  - url: "https://f003.backblazeb2.com/file/naturehungry/cnidaria/others/corallimorphs/whitetip/120721tptd7882m.jpg"
  - url: "https://f003.backblazeb2.com/file/naturehungry/cnidaria/others/corallimorphs/ridged/050807sjid5570m.jpg"
  - url: "https://f003.backblazeb2.com/file/naturehungry/cnidaria/others/corallimorphs/beaded/060527sjig6070ma.jpg"
  - url: "https://f003.backblazeb2.com/file/naturehungry/cnidaria/others/corallimorphs/stubby/040705sisd2131m.jpg"
 
- label: "[Diameter 5-10cm]()<br>"
  images:
  - url: "https://f003.backblazeb2.com/file/naturehungry/cnidaria/actiniaria/boloceroididae/060624skdg6189m.jpg"
  - url: "https://f003.backblazeb2.com/file/naturehungry/cnidaria/actiniaria/tiger/050818chgg1345m.jpg"
  - url: "https://f003.backblazeb2.com/file/naturehungry/cnidaria/actiniaria/pearly/091206tmd5757m.jpg"
  - url: "https://f003.backblazeb2.com/file/naturehungry/cnidaria/actiniaria/pimply/080408chgd0640m.jpg"

- label: "[Diameter > 10cm smooth tentacles]()<br>"
  images:
  - url: https://f003.backblazeb2.com/file/naturehungry/cnidaria/actiniaria/gigantea/040606kusg0481m.jpg
  - url: https://f003.backblazeb2.com/file/naturehungry/cnidaria/actiniaria/actinostephanus/090210trysvpd0133m.jpg
  - url: https://f003.backblazeb2.com/file/naturehungry/cnidaria/actiniaria/doreensis/050821bbd5815m.jpg
  - url: https://f003.backblazeb2.com/file/naturehungry/cnidaria/actiniaria/entacmaea/040410sisbd017m.jpg

- label: "[Diameter > 10cm frilly tentacles]()<br>"
  images:
  - url: https://f003.backblazeb2.com/file/naturehungry/cnidaria/actiniaria/cryptodendrum/060811rlhd5835m.jpg
  - url: https://f003.backblazeb2.com/file/naturehungry/cnidaria/actiniaria/actinodendron/030714bbd0002m.jpg
  - url: https://f003.backblazeb2.com/file/naturehungry/cnidaria/actiniaria/phymanthus/band/050808sntg0904m.jpg
  - url: https://f003.backblazeb2.com/file/naturehungry/cnidaria/actiniaria/phymanthus/sixpoint/070602sjig9829m.jpg
  
- label: "[Cerianthids]()<br>also known as peacock or tube anemones"
  images:
  - url: https://f003.backblazeb2.com/file/naturehungry/cnidaria/others/ceriantharia/common/030927cjd0058m.jpg
  - url: https://f003.backblazeb2.com/file/naturehungry/cnidaria/others/ceriantharia/common/040701chgd1388m.jpg
  - url: https://f003.backblazeb2.com/file/naturehungry/cnidaria/others/ceriantharia/shy/070901sjid6472m.jpg
  - url: https://f003.backblazeb2.com/file/naturehungry/cnidaria/others/ceriantharia/blackmouth/050820bbg1690m.jpg

---
a central mouth; a ring of tentacles, or a disk covered with short tentacles (sometimes just bumps).
on sand, stuck to hard surfaces (stones, seagrasses, other animals).

<p> Other cnidarians <a href="">text index</a> | <a href="">photo index</a> </p>

<br>
{% for row in page.child_pages %}
<div class="photo-index-images-text-row">
{% include img-grid.html items=row.images cols=4 %}
  <div>
    <p>{{ row.label | markdownify}}</p>
  
  </div>
</div>
{% endfor %}
---

## These are NOT sea anemones

<div class="flex flex-wrap gap-1">
{% assign entry = site.entries | where : "title","Brain anchor coral" | first %}
{% include entry-summary-card.html item=entry %}
{% assign entry = site.entries | where : "title","White-tipped mushroom coral" | first %}
{% include entry-summary-card.html item=entry %}
{% assign entry = site.entries | where : "title","Anemone coral" | first %}
{% include entry-summary-card.html item=entry %}
{% assign entry = site.entries | where : "title","Sunflower mushroom coral" | first %}
{% include entry-summary-card.html item=entry %}
{% assign entry = site.entries | where : "title","Broad feathery soft coral" | first %}
{% include entry-summary-card.html item=entry %}
</div>

---

how to tell apart

- [large 'hairy' cnidarians](cflargecnidarians.htm)
- [animals with a ring of smooth tentacles](cfringtentacles.htm)
- [animals with a ring of feathery arm](../glossary/feathery.htm)


```