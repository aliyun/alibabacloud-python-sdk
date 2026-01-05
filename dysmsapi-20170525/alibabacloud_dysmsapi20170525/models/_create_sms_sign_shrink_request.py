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
        self.app_icp_record_id = app_icp_record_id
        # Application scenarios, instructions as follows:
        # - For registered websites, enter the domain name with HTTP or HTTPS that has been registered with the MIIT.
        # 
        # - For launched apps, provide a display link from the app store with HTTP or HTTPS, ensuring the app is online.
        # 
        # - For public accounts or mini-programs, input the full name, ensuring they are online.
        # 
        # - For e-commerce platform store names, applicable only to enterprise users, provide a display link with HTTP or HTTPS for the store.
        self.apply_scene_content = apply_scene_content
        self.authorization_letter_id = authorization_letter_id
        # Additional information to supplement uploaded business proof documents or screenshots, which helps reviewers understand your business details.
        # 
        # This parameter is optional; please fill it out based on your actual needs.
        self.more_data_shrink = more_data_shrink
        self.owner_id = owner_id
        # Approved or under-review qualification ID.
        # 
        # > - Before applying for an SMS signature, please first [Apply for Qualification](https://help.aliyun.com/zh/sms/user-guide/new-qualification?spm=a2c4g.11186623.0.0.718d187bbkpMRK).
        # > - You can view the qualification ID on the [Qualification Management](https://dysms.console.aliyun.com/domestic/text/qualification) page.
        # 
        # This parameter is required.
        self.qualification_id = qualification_id
        # Explanation of the SMS signature scenario, with a maximum length of 200 characters.
        # 
        # > The scenario explanation is one of the reference materials for signature review. Please provide a detailed description of the usage scenarios for your live services, along with links to verify these services such as website URLs with MIIT备案, app store display links, full names of public accounts or mini-programs, etc. For login scenarios, test account credentials are also required. A comprehensive application explanation enhances the efficiency of signature and template reviews. Refer to the **Application Scenario** column in the [Signature Source](https://help.aliyun.com/zh/sms/user-guide/signature-specifications-1?spm=a2c4g.11186623.0.i2#section-xup-k46-yi4) table for filling in SMS scenarios.
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Signature name. Please adhere to the [Signature Specifications](https://help.aliyun.com/zh/sms/user-guide/signature-specifications-1?spm=a2c4g.11186623.0.0.4f9710fder2gR7#section-0p8-qn8-mmy).
        # 
        # > - Signature names are case-insensitive; e.g., 【Aliyun Communication】 and 【aliyun communication】 are considered identical.
        # > - If your verification code signature and general signature names are the same, the system defaults to using the general signature for sending SMS messages.
        # 
        # This parameter is required.
        self.sign_name = sign_name
        # Signature source. Values:
        # 
        # - **0**: Full name or abbreviation of an enterprise or institution.
        # - **1**: Full name or abbreviation of a MIIT-registered website.
        # - **2**: Full name or abbreviation of an App.
        # - **3**: Full name or abbreviation of an official account or mini-program.
        # - **4**: Full name or abbreviation of an e-commerce platform store.
        # - **5**: Full name or abbreviation of a trademark.
        # 
        # For detailed information on signature sources, refer to [Signature Source](https://help.aliyun.com/zh/sms/user-guide/signature-specifications-1?spm=a2c4g.11186623.0.0.4f9710fder2gR7#section-xup-k46-yi4).
        # 
        # > This interface does not support applying for signatures with sources as **Test or Learning** and **Trial Use**. If you need to apply for signatures with these sources, please go to the [SMS Service Console](https://dysms.console.aliyun.com/domestic/text/sign/add/qualification).
        # 
        # This parameter is required.
        self.sign_source = sign_source
        # Signature type. Values:
        # 
        # - **0**: Verification Code
        # 
        # - **1**: General (Default)
        # 
        # > It is recommended to use the default value: **General**.
        self.sign_type = sign_type
        # Choose whether the applied signature is for self-use or third-party use.
        # 
        # - false: Self-use (default)
        # 
        # - true: Third-party use
        # >Notice: Please select self-use qualification ID when the signature is for self-use; choose third-party use qualification ID when it\\"s for third-party use.
        self.third_party = third_party
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

