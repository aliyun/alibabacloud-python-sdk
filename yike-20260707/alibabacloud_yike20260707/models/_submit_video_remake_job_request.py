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
        # The JSON object string for the original video input. The Type of the first item in Medias is video, and a MediaId or HTTP(S) URL is provided.
        self.input = input
        # The remake parameters in JSON string format. The structure is as follows:
        # 
        # - Product (Object, required): The product information, including the original and new products.
        #   - OriginalProductName (String, optional): The product or brand name in the original video, used to locate and replace mentions of the original product.
        #   - NewProduct (Object, required): The new product information.
        #     - ProductName (String, required): The product or brand name.
        #     - Description (String, optional): The product description.
        #     - ProductKnowledge (String, optional): The physical knowledge of the product, such as material and usage.
        #     - ProductImages (Array<String>, required): A non-empty list of new product images, where each item is an HTTP(S) URL.
        #     - SellingPoints (Array<String>, optional): The list of product selling points.
        #     - OriginalPrice (String, optional): The original price.
        #     - CurrentPrice (String, optional): The current price.
        #     - Discount (String, optional): The discount information, such as "$50 off for orders over $200" or "Buy one get one free".
        # - AvatarList (Array<Object>, optional): The character replacement list, supporting 1 to 5 items. Each item describes the replacement relationship between an original character and a new character. If this parameter is not passed or is an empty array, no characters are replaced.
        #   - OriginalAvatarImage (String, required for each item when there are multiple characters, optional for a single character): The reference image of the target character in the original video. An HTTP(S) URL or a registered image MediaId is supported. Duplicates are not allowed in the same list.
        #   - NewAvatarImages (Array<String>, required for each item): A non-empty list of reference images for the new character. An HTTP(S) URL or a registered image MediaId is supported.
        #   - AvatarName (String, optional for each item): The role name of the replaced character in the generated script.
        # - VoiceoverLanguage (String, optional): The voiceover language. Default value: zh.
        # - AdditionalRequirements (String, optional): Additional remake requirements.
        # 
        # This operation uses AvatarList and does not use the legacy Avatar or OriginalAvatarName from the standalone scripting interface. The two character structures are not interchangeable.
        self.remake_params = remake_params
        # The user-defined JSON object string, which is returned as-is when queried. NotifyAddress is the callback URL for the final state of the task.
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

