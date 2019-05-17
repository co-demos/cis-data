Available styles (cf. `co-demos/ApiViz/…/frontend/styles/commons-cis.scss`):
- Links:
  - class `colored`: underlined in color A on color B + on hover box in color B on color A
  - and
  - class `link-primary`: link in `apiviz-primary` on white
  - class `link-on-primary`: link in white on `apiviz-primary`
  - cf. https://github.com/entrepreneur-interet-general/CIS-front/issues/140
  
- Buttons:
  - `is-primary` and `is-primary is-outlined` are provided by Bulma + overridden in `co-demos/ApiViz/…/frontend/styles/custom-bulma.scss`
  - cf. https://github.com/entrepreneur-interet-general/CIS-front/issues/140
  
- Carousels: activated by `utils.js` in `co-demos/ApiViz` (cf. 
  - classes `.carousel.is-6`: half-width carousel
  - classes `.carousel.is-8`: centered carousel on page width
  - :warning: you may need to adapt/fix the icons in CSS (fine tuning of positions or icons…)
  - and
  - class `carousel-item` to style the cards
  - cf. https://github.com/entrepreneur-interet-general/CIS-front/issues/104
  - cf. https://github.com/co-demos/ApiViz/issues/72
  - 
  
- Backgrounds:
  - classes `primary-bg-plain` and `grey-bg-plain` for uniform colored backgrounds
  - `primary-bg-img` and `grey-bg-img` for backgrounds defined with illustrations

- Texts:
  - classes `is-primary`, `is-primary-invert`, `is-secondary` to change colors
  - `is-centered`, `is-left`, `is-bold` are doing what they say

- Effects:
  - on `navbar` and `cis-tabs`: bar filling itself when hovered, see code in `commons-cis.scss` if you wish to use it else where
