from pydantic import BaseModel
from typing import List, Union, Optional
from src.facets.schemes import Facet
from src.variaton_themes.schemes import VariationTheme
from bson import ObjectId
from src.schemes import PyObjectId


class FacetCreateForm(Facet):
    categories: Optional[Union[List[PyObjectId], str]]


class VariationThemeCreateForm(VariationTheme):
    categories: Optional[Union[List[PyObjectId], str]]

class ProductCreateForm(BaseModel):
    """Model that contains facets and variation themes to create a product"""
    facets: List[FacetCreateForm]
    variation_themes: List[VariationThemeCreateForm]

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True  # required for the _id
        json_encoders = {ObjectId: str}
