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
        # The remake parameters in JSON string format. The structure varies based on `RemakeType`. For `faithful-remake`, the structure is as follows:
        # 
        # - ComprehensionResult (string, required): The URL of the JSON file that contains the content understanding results.
        # 
        # - Product (object, required): The product information, including the original and new products.
        # 
        #   - OriginalProductName (string, required): The name of the product or brand in the original video to be replaced. This is used to locate and replace mentions of the original product in the script.
        # 
        #   - NewProduct (object, required): The new product information. 
        # 
        #     - ProductName (string, required): The name of the product or brand.
        #     - Description (string, required): The product description.
        #     - ProductKnowledge (string, required): The physical knowledge of the product, such as the material and usage instructions.
        #     - ProductImages (array<string>, required): The images of the new product. This array cannot be empty, and each item must be an HTTP or HTTPS URL.
        #     - SellingPoints (array<string>, optional): The list of product selling points.
        #     - OriginalPrice (string, optional): The original price.
        #     - CurrentPrice (string, optional): The current price.
        #     - Discount (string, optional): The discount information, such as "50 off for orders over 200" or "Buy one get one free".
        # 
        # - Avatar (object, required): The avatar information, including the original and new avatars.
        # 
        #     - NewAvatarImages (array<string>, required): The list of new avatar images. This array cannot be empty, and each item must be a media asset ID or an image URL. If a URL is provided, the system automatically registers it as a media asset. **Currently, only one image is supported** (only the first element of the array is used). The array format is reserved for future extensions.
        #     - OriginalAvatarName (string, required): The name of the avatar in the original video to be replaced. This is used to locate and replace the original avatar in the script or visuals.
        # 
        # - VoiceoverLanguage (string, optional): The voiceover language. Valid values: `zh` (Chinese), `en` (English), `es` (Spanish), `pt` (Portuguese), `fr` (French), `de` (German), `ja` (Japanese), `ko` (Korean), and `ar` (Arabic). Default value: `zh`.
        self.remake_params = remake_params
        # The remake type, which determines the structure of `RemakeParams`. Currently, only `faithful-remake` is supported, which replicates the original hit video structure paragraph by paragraph and replaces the product and avatar.
        self.remake_type = remake_type
        # The custom parameters in JSON string format. These parameters are returned as-is in the callback result, such as newsKey. The system reserves the NotifyAddress field for the callback URL, which is invoked after the task is completed.
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

