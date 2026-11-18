# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitVideoRemakeJobRequest(DaraModel):
    def __init__(
        self,
        input: str = None,
        remake_params: str = None,
        user_data: str = None,
    ):
        # The input materials. The value is a JSON string with the following structure:
        # 
        # - Medias (Array<Object>, required): A non-empty list of media assets. This operation uses the first video in the list and does not support batch remakes. The first item contains the following fields:
        #   - Type (String, required): The type of the media asset. For this operation, set the value to video for the first item. The value is case-insensitive.
        #   - Url (String, mutually exclusive with MediaId): The URL of the media asset. The URL must start with http:// or https:// and cannot exceed 2,048 characters in length. Unregistered URLs are automatically registered as media assets.
        #   - MediaId (String, mutually exclusive with Url): The ID of the registered media asset. If both Url and MediaId are specified, MediaId takes precedence.
        self.input = input
        # The remake parameters. The value is a JSON string with the following structure:
        # 
        # - Product (Object, required): The product information, including the original product and the new product.
        #   - OriginalProductName (String, optional): The name of the product or brand in the original video. This is used to locate and replace mentions of the original product.
        #   - NewProduct (Object, required): The information about the new product.
        #     - ProductName (String, required): The name of the product or brand.
        #     - Description (String, optional): The description of the product.
        #     - ProductKnowledge (String, optional): The physical knowledge of the product, such as the material and usage.
        #     - ProductImages (Array\\<String\\>, required): The images of the new product. The list cannot be empty. Each item is an HTTP or HTTPS URL.
        #     - SellingPoints (Array\\<String\\>, optional): The list of selling points of the product.
        #     - OriginalPrice (String, optional): The original price.
        #     - CurrentPrice (String, optional): The current price.
        #     - Discount (String, optional): The discount information, such as "50 off for orders over 200" or "buy one get one free".
        # - AvatarList (Array\\<Object\\>, optional): The list of character replacements. Single-character and multi-character replacements are supported. Pass one item for single-character replacement and two to five items for multi-character replacement. Each item is an object that describes the replacement relationship between an original character and a new character. If this parameter is not passed or is an empty array, no characters are replaced.
        #   - OriginalAvatarImage (String, required for each item in multi-character replacement, optional for single-character replacement): The reference image of the target character in the original video. HTTP and HTTPS URLs or registered image MediaIds are supported. The value cannot be duplicated within the same list.
        #   - NewAvatarImages (Array\\<String\\>, required for each item): The list of reference images for the new character. The list cannot be empty. HTTP and HTTPS URLs or registered image MediaIds are supported.
        #   - AvatarName (String, optional for each item): The role name of the replaced character in the generated script.
        # - VoiceoverLanguage (String, optional): The voiceover language. Explicitly specify the language, such as zh for Chinese or en for English.
        # - AdditionalRequirements (String, optional): Additional remake requirements.
        self.remake_params = remake_params
        # The user-defined data.
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input is not None:
            result['Input'] = self.input

        if self.remake_params is not None:
            result['RemakeParams'] = self.remake_params

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Input') is not None:
            self.input = m.get('Input')

        if m.get('RemakeParams') is not None:
            self.remake_params = m.get('RemakeParams')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

