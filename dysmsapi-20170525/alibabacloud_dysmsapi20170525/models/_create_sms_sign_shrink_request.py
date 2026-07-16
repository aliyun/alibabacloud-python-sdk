# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSmsSignShrinkRequest(DaraModel):
    def __init__(
        self,
        app_icp_record_id: int = None,
        apply_scene_content: str = None,
        authorization_letter_id: int = None,
        more_data_shrink: str = None,
        owner_id: int = None,
        qualification_id: int = None,
        remark: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sign_name: str = None,
        sign_source: int = None,
        sign_type: int = None,
        third_party: bool = None,
        trademark_id: int = None,
    ):
        # The APP-ICP filing entity ID.
        # > - This parameter is required when SignSource is set to 2.
        # > - You can obtain the filing entity ID by calling the [CreateSmsAppIcpRecord](~~CreateSmsAppIcpRecord~~) operation.
        self.app_icp_record_id = app_icp_record_id
        # >Notice:  The signature source of launched apps is no longer supported.
        # The app store link. If the signature source is a launched app, that is, SignSource is set to 2, specify a link that starts with http:// or https:// and make sure the app is already launched.
        self.apply_scene_content = apply_scene_content
        # The ID of the power of attorney. When the signature is for third-party use, this parameter is required. Otherwise, the signature review will not pass. The unified social credit code in the power of attorney must match the unified social credit code in the qualification information bound to the signature. Otherwise, the signature creation fails.
        self.authorization_letter_id = authorization_letter_id
        # The supplementary materials. Upload business proof files or business screenshots to help reviewers understand your business details. See [Signature application materials](~~108076#section-xup-k46-yi4~~) and upload the relevant materials.
        self.more_data_shrink = more_data_shrink
        self.owner_id = owner_id
        # The ID of the approved qualification.
        # 
        # > - Before applying for an SMS signature, [apply for a qualification](https://help.aliyun.com/document_detail/2539801.html).
        # > - You can view the qualification ID on the [Qualification Management](https://dysms.console.aliyun.com/domestic/text/qualification) page.
        # 
        # This parameter is required.
        self.qualification_id = qualification_id
        # The description of the SMS signature scenario. This is one of the reference materials for signature review. The description can be up to 200 characters in length.
        # >  - You can describe the scenarios of your online service and provide links to the actual business website or marketplace download page.
        # >  - You can provide a complete SMS example that reflects your business scenario.
        # >  - You can provide the pass parameter content of variables and describe in detail the business scenario and the reason for selecting the variable property.
        # >  - If the signature involves a government or public institution, specify the landline phone number of the institution.
        # 
        # A well-documented application description improves the review efficiency for signatures and templates. Failure to follow the specifications or leaving this field empty may affect the approval of your signature.
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The signature name. The signature name must comply with the [signature specifications](~~108076#section-0p8-qn8-mmy~~):
        # 
        # - The name must be 2 to 12 characters in length and cannot contain words such as "test".
        # 
        # - The name cannot contain symbols such as 【】, (), or []. Special characters such as commas, periods, and spaces are not supported.
        # 
        # > - Signature names are case-sensitive. For example, 【Aliyun通信】 and 【aliyun通信】 are treated as two different signatures.
        # > - If your verification code signature and general-purpose signature have the same name, the system uses the general-purpose signature to send SMS messages by default.
        # 
        # This parameter is required.
        self.sign_name = sign_name
        # The signature source. Valid values:
        # 
        # -  **0**: full name or abbreviation of an enterprise or public institution. **(Recommended)**
        # -  **5**: full name or abbreviation of a trademark.
        # -  **2**: full name or abbreviation of an app. **(Not recommended)**
        # 
        # For more information about signature sources, see [Signature sources](~~108076#section-fow-bfu-wo9~~).
        # 
        # This parameter is required.
        self.sign_source = sign_source
        # The signature type. Valid values:
        # 
        # - **0**: verification code.
        # 
        # - **1**: general-purpose (default).
        # 
        # We recommend that you use the default value: **general-purpose**.
        self.sign_type = sign_type
        # The signature purpose. Valid values:
        # 
        # - false: for personal use (default). The signature is the enterprise name, website, or product name verified under this account.
        # 
        # - true: for third-party use. The signature is the enterprise name, website, or product name not verified under this account.
        # >Notice: If the signature is for personal use, select a qualification ID for personal use. If the signature is for third-party use, select a qualification ID for third-party use..
        self.third_party = third_party
        # The trademark entity ID.
        # > - 1. This parameter is required when SignSource is set to 5.
        # > - 2. You can obtain the trademark entity ID by calling the [CreateSmsTrademark](~~CreateSmsTrademark~~) operation.
        # > - 3. Based on carrier real-name registration requirements, provide the relevant field information. Otherwise, the probability of review rejection or carrier registration failure increases significantly.
        self.trademark_id = trademark_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_icp_record_id is not None:
            result['AppIcpRecordId'] = self.app_icp_record_id

        if self.apply_scene_content is not None:
            result['ApplySceneContent'] = self.apply_scene_content

        if self.authorization_letter_id is not None:
            result['AuthorizationLetterId'] = self.authorization_letter_id

        if self.more_data_shrink is not None:
            result['MoreData'] = self.more_data_shrink

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.qualification_id is not None:
            result['QualificationId'] = self.qualification_id

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.sign_name is not None:
            result['SignName'] = self.sign_name

        if self.sign_source is not None:
            result['SignSource'] = self.sign_source

        if self.sign_type is not None:
            result['SignType'] = self.sign_type

        if self.third_party is not None:
            result['ThirdParty'] = self.third_party

        if self.trademark_id is not None:
            result['TrademarkId'] = self.trademark_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppIcpRecordId') is not None:
            self.app_icp_record_id = m.get('AppIcpRecordId')

        if m.get('ApplySceneContent') is not None:
            self.apply_scene_content = m.get('ApplySceneContent')

        if m.get('AuthorizationLetterId') is not None:
            self.authorization_letter_id = m.get('AuthorizationLetterId')

        if m.get('MoreData') is not None:
            self.more_data_shrink = m.get('MoreData')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('QualificationId') is not None:
            self.qualification_id = m.get('QualificationId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')

        if m.get('SignSource') is not None:
            self.sign_source = m.get('SignSource')

        if m.get('SignType') is not None:
            self.sign_type = m.get('SignType')

        if m.get('ThirdParty') is not None:
            self.third_party = m.get('ThirdParty')

        if m.get('TrademarkId') is not None:
            self.trademark_id = m.get('TrademarkId')

        return self

