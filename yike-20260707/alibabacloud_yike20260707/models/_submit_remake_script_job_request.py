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
        # The remake parameters in JSON string format. The structure varies depending on the RemakeType. For faithful-remake, the structure is as follows:
        # 
        # - ComprehensionResult (String, required): The content understanding result, which is the URL of a JSON file.
        # - Product (Object, required): The product information, including the original and new products.
        #   - OriginalProductName (String, required): The product or brand name in the original video, used to locate and replace mentions of the original product.
        #   - NewProduct (Object, required): The new product information.
        #     - ProductName (String, required): The product or brand name.
        #     - Description (String, required): The product description.
        #     - ProductKnowledge (String, optional): The physical knowledge of the product, such as the material and usage.
        #     - ProductImages (Array<String>, required): The images of the new product. This array cannot be empty, and each item must be an HTTP or HTTPS URL.
        #     - SellingPoints (Array<String>, optional): The list of product selling points.
        #     - OriginalPrice (String, optional): The original price.
        #     - CurrentPrice (String, optional): The current price.
        #     - Discount (String, optional): The discount information, such as "50 off for orders over 200" or "buy one get one free".
        # - AvatarList (Array<Object>, optional): The list of avatar replacements, supporting single and multiple avatar replacements. We recommend using this field. Pass one item for a single avatar and two to five items for multiple avatars. Each item is an object that describes the replacement relationship between an original avatar and a new avatar:
        #   - OriginalAvatarName (String, required for each item): The name of the avatar to be replaced in the original video. Use the avatar name from the video breakdown result to locate the replacement target in the script or video. The original avatar names in the same list cannot be duplicated.
        #   - NewAvatarImages (Array<String>, required for each item): The list of reference images for the new avatar. This array cannot be empty. Images can be HTTP or HTTPS URLs or registered image MediaIds. Currently, only the first image is used.
        #   - AvatarName (String, optional for each item): The role name of the replaced avatar in the generated script.
        # - Avatar (Object, optional): The single avatar replacement information compatible with historical calls, retained as a transitional field. We recommend using AvatarList for new integrations and subsequent calls. The field structure is the same as a single item in AvatarList. When using this field, OriginalAvatarName and NewAvatarImages are required, and AvatarName is optional.
        # - VoiceoverLanguage (String, optional): The voiceover language. Valid values: zh (Chinese), en (English), es (Spanish), pt (Portuguese), fr (French), de (German), ja (Japanese), ko (Korean), and ar (Arabic). We recommend explicitly specifying this parameter.
        # - AdditionalRequirements (String, optional): Additional remake requirements.
        self.remake_params = remake_params
        # The remake type, which determines the structure of RemakeParams. Currently, only faithful-remake is supported. This type faithfully remakes the original viral video structure segment by segment, replacing the product and avatar.
        self.remake_type = remake_type
        # The custom parameters in JSON string format, which are returned as-is in the callback result, such as newsKey. The system reserves the NotifyAddress field for the callback URL, which is invoked after the task is completed.
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

