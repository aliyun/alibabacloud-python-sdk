# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dysmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class ModifySmsSignRequest(DaraModel):
    def __init__(
        self,
        owner_id: int = None,
        remark: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sign_file_list: List[main_models.ModifySmsSignRequestSignFileList] = None,
        sign_name: str = None,
        sign_source: int = None,
        sign_type: int = None,
    ):
        self.owner_id = owner_id
        # The description of the SMS signature application. The description cannot exceed 200 characters in length.
        # 
        # The description is used as a reference for signature review. A complete description helps reviewers understand your business scenario and improves review efficiency. Guidelines:
        # 
        # - Provide the use case of a service that is already online.
        # - Provide an SMS example from a real scenario to illustrate your business scenario.
        # - Provide the values passed for variables, and describe the business scenario in detail and the reason for choosing the variable attributes.
        # - Provide the website URL of the actual service, a filed domain name, or an app store download link.
        # - For logon scenarios, provide a test account and password.
        # 
        # This parameter is required.
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The list of signature files.
        # 
        # This parameter is required.
        self.sign_file_list = sign_file_list
        # The signature name.
        # 
        # > You can modify a signature that has been approved, but you cannot change its name. The modified signature must be reviewed and approved before it can be used. The original signature cannot be used until the review is complete.
        # 
        # This parameter is required.
        self.sign_name = sign_name
        # The signature source. Valid values:
        # 
        # - **0**: full name or abbreviation of an enterprise or public institution.
        # - **1**: full name or abbreviation of a website filed with the Ministry of Industry and Information Technology (MIIT).
        # - **2**: full name or abbreviation of an app.
        # - **3**: full name or abbreviation of an official account or mini program.
        # - **4**: full name or abbreviation of a store on an e-commerce platform.
        # - **5**: full name or abbreviation of a trademark.
        # 
        # This parameter is required.
        self.sign_source = sign_source
        # The signature type. Valid values:
        # 
        # - **0**: verification code.
        # 
        # - **1**: general.
        self.sign_type = sign_type

    def validate(self):
        if self.sign_file_list:
            for v1 in self.sign_file_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        result['SignFileList'] = []
        if self.sign_file_list is not None:
            for k1 in self.sign_file_list:
                result['SignFileList'].append(k1.to_map() if k1 else None)

        if self.sign_name is not None:
            result['SignName'] = self.sign_name

        if self.sign_source is not None:
            result['SignSource'] = self.sign_source

        if self.sign_type is not None:
            result['SignType'] = self.sign_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        self.sign_file_list = []
        if m.get('SignFileList') is not None:
            for k1 in m.get('SignFileList'):
                temp_model = main_models.ModifySmsSignRequestSignFileList()
                self.sign_file_list.append(temp_model.from_map(k1))

        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')

        if m.get('SignSource') is not None:
            self.sign_source = m.get('SignSource')

        if m.get('SignType') is not None:
            self.sign_type = m.get('SignType')

        return self

class ModifySmsSignRequestSignFileList(DaraModel):
    def __init__(
        self,
        file_contents: str = None,
        file_suffix: str = None,
    ):
        # 签名的纸质证明文件经base64编码后的字符串。图片不超过2 MB。
        # 
        # 个别场景下，申请签名需要上传证明文件。详细说明，请参见[短信签名规范](https://help.aliyun.com/document_detail/108076.html)。
        # 
        # This parameter is required.
        self.file_contents = file_contents
        # 签名的证明文件格式，支持上传多张图片。当前支持JPG、PNG、GIF或JPEG格式的图片。
        # 
        # 个别场景下，申请签名需要上传证明文件。详细说明，请参见[短信签名规范](https://help.aliyun.com/document_detail/108076.html)。
        # > 如果签名用途为他用或个人认证用户的自用签名来源为企事业单位名时，还需上传证明文件和委托授权书，详情请参见[证明文件](https://help.aliyun.com/document_detail/108076.html)和[授权委托书](https://help.aliyun.com/document_detail/56741.html)。
        # 
        # This parameter is required.
        self.file_suffix = file_suffix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_contents is not None:
            result['FileContents'] = self.file_contents

        if self.file_suffix is not None:
            result['FileSuffix'] = self.file_suffix

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileContents') is not None:
            self.file_contents = m.get('FileContents')

        if m.get('FileSuffix') is not None:
            self.file_suffix = m.get('FileSuffix')

        return self

