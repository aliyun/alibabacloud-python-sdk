# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateSmsSignRequest(DaraModel):
    def __init__(
        self,
        app_icp_record_id: int = None,
        apply_scene_content: str = None,
        authorization_letter_id: int = None,
        more_data: List[str] = None,
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
        # - For registered websites, please enter the domain name registered with MIIT, including HTTP or HTTPS.
        # - For launched apps, provide the display link from the app store with HTTP or HTTPS, ensuring the app is online.
        # - For public accounts or mini-programs, fill in the full name, ensuring they are online.
        # - For e-commerce platform store names (for enterprise users only), provide the display link with HTTP or HTTPS.
        self.apply_scene_content = apply_scene_content
        self.authorization_letter_id = authorization_letter_id
        # Additional materials, such as uploading business proof documents or screenshots of business operations, to help reviewers understand your business details.
        self.more_data = more_data
        self.owner_id = owner_id
        # Approved or under-review qualification ID.
        # 
        # > - Before applying for an SMS signature, please first [apply for qualifications](https://help.aliyun.com/zh/sms/user-guide/new-qualification?spm=a2c4g.11186623.0.0.718d187bbkpMRK).
        # > - You can view the qualification ID on the [Qualification Management](https://dysms.console.aliyun.com/domestic/text/qualification) page.
        # 
        # This parameter is required.
        self.qualification_id = qualification_id
        # Explanation of the SMS signature scenario, with a maximum length of 200 characters.
        # 
        # > The scenario explanation is one of the reference information for signature review. Please provide a detailed description of the usage scenarios of the launched business, along with verifiable information such as website links, registered domain addresses, app store download links, full names of public accounts or mini-programs, etc. For login scenarios, test account credentials are also required. A well-informed application explanation will enhance the efficiency of signature and template reviews. Refer to the **Application Scenarios** column in the [Signature Source](https://help.aliyun.com/zh/sms/user-guide/signature-specifications-1?spm=a2c4g.11186623.0.i2#section-xup-k46-yi4) table for filling in SMS scenarios.
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Signature not yet approved.
        # 
        # This parameter is required.
        self.sign_name = sign_name
        # Source of the signature. Values:
        # 
        # - **0**: Full name or abbreviation of enterprises and institutions.
        # - **1**: Full name or abbreviation of MIIT-registered websites.
        # - **2**: Full name or abbreviation of app applications.
        # - **3**: Full name or abbreviation of public accounts or mini-programs.
        # - **4**: Full name or abbreviation of e-commerce platform store names.
        # - **5**: Full name or abbreviation of trademarks.
        # 
        # This parameter is required.
        self.sign_source = sign_source
        # Signature type. It is recommended to use the default value.
        # 
        # - **0**: Verification code
        # - **1**: General (default)
        self.sign_type = sign_type
        # Whether the signature is for self-use or others.
        # 
        # - false: Self-use
        # - true: Others
        # >Notice: When the signature is for self-use, select the self-use qualification ID; when it\\"s for others, choose the others\\" qualification ID.
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

        if self.more_data is not None:
            result['MoreData'] = self.more_data

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
            self.more_data = m.get('MoreData')

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

