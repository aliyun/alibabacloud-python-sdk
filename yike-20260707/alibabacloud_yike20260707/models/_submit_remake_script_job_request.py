# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitRemakeScriptJobRequest(DaraModel):
    def __init__(
        self,
        remake_params: str = None,
        remake_type: str = None,
        user_data: str = None,
    ):
        # The remake parameters (JSON string). The structure varies depending on `RemakeType`. For `faithful-remake`, the structure is as follows:
        # 
        # - ComprehensionResult (string, required): The content comprehension result. A URL to a JSON file.
        # 
        # - Product (Object, required): The product information (original product + new product).
        # 
        #   - OriginalProductName (String, required): The product or brand name in the original video (the object to be replaced). Used to locate and replace mentions of the original product in the script.
        # 
        #   - NewProduct (Object, required): The new product information. 
        # 
        #     - ProductName (String, required): The product or brand name.
        #     - Description (String, required): The product description.
        #     - ProductKnowledge (String, required): The physical knowledge of the product, such as material and usage instructions.
        #     - ProductImages (Array\\<String\\>, required): The images of the new product. Must not be empty. Each item is an http(s) URL.
        #     - SellingPoints (Array\\<String\\>, optional): The list of product selling points.
        #     - OriginalPrice (String, optional): The original price.
        #     - CurrentPrice (String, optional): The current price.
        #     - Discount (String, optional): The discount information, such as "50 off 200" or "buy one get one free".
        # 
        # - Avatar (Object, required): The model information (original model + new model).
        # 
        #     - NewAvatarImages (Array\\<String\\>, required): The list of new model images. Must not be empty. Each item is a media asset ID or an image URL (when a URL is provided, the system automatically registers it as a media asset). **Currently, only 1 image is supported** (only the first element of the array is used). The array format is reserved for future expansion.
        #     - OriginalAvatarName (String, required): The name of the model in the original video (the object to be replaced). Used to locate and replace the original model in the script and visuals.
        # 
        # -   VoiceoverLanguage (String, optional): The voiceover language. Valid values: `zh` (Chinese), `en` (English), `es` (Spanish), `pt` (Portuguese), `fr` (French), `de` (German), `ja` (Japanese), `ko` (Korean), `ar` (Arabic). Default value: `zh`.
        self.remake_params = remake_params
        # The remake type, which determines the structure of `RemakeParams`. Currently, only `faithful-remake` is supported (faithful remake: remakes the original hit video segment by segment, replacing the product and model).
        self.remake_type = remake_type
        # The custom parameters in JSON format. These parameters are returned as-is in the callback result (for example, newsKey). The system reserved field NotifyAddress specifies the callback URL. The system sends a callback to this URL after the task is completed.
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.remake_params is not None:
            result['RemakeParams'] = self.remake_params

        if self.remake_type is not None:
            result['RemakeType'] = self.remake_type

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RemakeParams') is not None:
            self.remake_params = m.get('RemakeParams')

        if m.get('RemakeType') is not None:
            self.remake_type = m.get('RemakeType')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

