# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateSmsSignShrinkRequest(DaraModel):
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
        # The ID of the app\\"s ICP filing entity.
        # 
        # > - This parameter is required if `SignSource` is set to 2.
        # >
        # > - You can obtain the filing entity ID by calling the [Create ICP Filing Entity](~~CreateSmsAppIcpRecord~~) operation.
        self.app_icp_record_id = app_icp_record_id
        # The app store link. This parameter is required if the signature source (`SignSource`) is an app (the value is 2). The link must start with `http://` or `https://`, and the app must be published in the app store.
        self.apply_scene_content = apply_scene_content
        # The authorization letter ID. This parameter is required if the signature is for third-party use (`ThirdParty` is set to `true`). The Unified Social Credit Code on the authorization letter must match the code in the selected qualification\\"s information.
        self.authorization_letter_id = authorization_letter_id
        # Additional supporting materials. You can upload supporting business documents or business screenshots to help with the review. For details on what to upload, see [Signature application materials](~~108076#section-xup-k46-yi4~~).
        self.more_data_shrink = more_data_shrink
        self.owner_id = owner_id
        # The ID of the approved qualification.
        # 
        # > - You must [apply for a qualification](https://help.aliyun.com/zh/sms/user-guide/new-qualification?spm=a2c4g.11186623.0.0.718d187bbkpMRK) before applying for an SMS signature.
        # >
        # > - You can find the qualification ID on the [qualification management](https://dysms.console.aliyun.com/domestic/text/qualification) page.
        # 
        # This parameter is required.
        self.qualification_id = qualification_id
        # A description of the SMS signature\\"s use case. This information is used during the review and must be 200 characters or less.
        # 
        # > - Describe the use case for your live service. Include relevant links, such as a website link or an app store link.
        # >
        # > - Provide a complete example of an SMS message that reflects your use case.
        # >
        # > - Provide the values for any variables. Describe the use case in detail and explain why the variables are necessary.
        # >
        # > - If the signature involves a government agency or public institution, provide its official landline number.
        # 
        # Providing complete and accurate information accelerates the review process. If you do not provide the required information, your signature application may be rejected.
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The name of the rejected SMS signature. You can find rejected SMS signatures on the [Domestic Messages > Signature Management](https://dysms.console.aliyun.com/domestic/text/sign) page in the console, or by calling the [QuerySmsSignList](~~QuerySmsSignList~~) operation.
        # 
        # This parameter is required.
        self.sign_name = sign_name
        # The signature source. Valid values:
        # 
        # - **0**: The full or abbreviated name of an enterprise or public institution. **(Recommended)**
        # 
        # - **5**: The full or abbreviated trademark name.
        # 
        # - **2**: The full or abbreviated name of an app. **(Not recommended)**
        # 
        # For more information, see [signature source](~~108076#section-fow-bfu-wo9~~).
        # 
        # This parameter is required.
        self.sign_source = sign_source
        # The signature type. Valid values:
        # 
        # - **0**: verification code.
        # 
        # - **1**: general (default).
        # 
        # We recommend that you use the default value, **general**.
        self.sign_type = sign_type
        # The signature purpose. Valid values:
        # 
        # - false: for own use (default). The signature is for a business, website, or product owned by your account\\"s verified entity.
        # 
        # - true: for third-party use. The signature is for a business, website, or product not owned by your account\\"s verified entity.
        #   >Notice: Ensure the selected qualification ID matches the signature purpose (for own use or for third-party use).
        self.third_party = third_party
        # The trademark entity ID.
        # 
        # > - This parameter is required if `SignSource` is set to 5.
        # >
        # > - You can obtain the trademark entity ID by calling the [Create Trademark Entity](~~CreateSmsTrademark~~) operation.
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

