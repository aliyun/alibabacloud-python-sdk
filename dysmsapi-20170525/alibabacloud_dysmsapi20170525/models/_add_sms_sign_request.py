# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dysmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class AddSmsSignRequest(DaraModel):
    def __init__(
        self,
        owner_id: int = None,
        remark: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sign_file_list: List[main_models.AddSmsSignRequestSignFileList] = None,
        sign_name: str = None,
        sign_source: int = None,
        sign_type: int = None,
    ):
        self.owner_id = owner_id
        # The description of the SMS signature scenario. The description cannot exceed 200 characters in length.
        # 
        # This is reference information for signature review. Providing a complete application description helps reviewers understand your business scenario and improves review efficiency. Guidelines for filling in:
        # 
        # - You can provide the use cases of a business that has been launched.
        # 
        # - You can provide real-world SMS message examples to reflect your business scenarios.
        # 
        # - You can provide the parameter values passed to variables and describe the business use cases and the reasons for choosing these variable attributes in detail.
        # 
        # - You can provide the website links, registered domain names, or app store download links of your actual business.
        # 
        # - For login scenarios, you can provide a test account and password.
        # 
        # This parameter is required.
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The list of signature files.
        # 
        # This parameter is required.
        self.sign_file_list = sign_file_list
        # The signature name. The signature name must comply with the [Signature specifications](~~108076#section-0p8-qn8-mmy~~).
        # 
        # > - Signature names are case-insensitive. For example, [Aliyun Communication] and [aliyun communication] are considered the same name.
        # > - When your verification code signature and general-purpose signature have the same name, the system uses the general-purpose signature to send SMS messages by default.
        # 
        # This parameter is required.
        self.sign_name = sign_name
        # The source of the signature. Valid values:
        # 
        # -  **0**: Full name or abbreviation of an enterprise or public institution.
        # -  **1**: Full name or abbreviation of a website registered with the Ministry of Industry and Information Technology (MIIT).
        # -  **2**: Full name or abbreviation of an app.
        # -  **3**: Full name or abbreviation of an official account or mini program.
        # -  **4**: Full name or abbreviation of an e-commerce platform store name.
        # -  **5**: Full name or abbreviation of a trademark name.
        # 
        # For detailed descriptions of signature sources, see [Signature source](https://help.aliyun.com/en/sms/user-guide/signature-specifications-1?spm=a2c4g.11186623.0.0.4f9710fder2gR7#section-xup-k46-yi4).
        # 
        # >This API does not support applying for signatures whose signature source is **Test or learning** or **Online trial**. If you need to apply for signatures with these two sources, go to the [Short Message Service (SMS) console](https://dysms.console.aliyun.com/domestic/text/sign/add/qualification) to submit your application.
        # 
        # This parameter is required.
        self.sign_source = sign_source
        # The type of the signature.
        # 
        # - **0**: Verification code
        # - **1**: General-purpose
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
                temp_model = main_models.AddSmsSignRequestSignFileList()
                self.sign_file_list.append(temp_model.from_map(k1))

        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')

        if m.get('SignSource') is not None:
            self.sign_source = m.get('SignSource')

        if m.get('SignType') is not None:
            self.sign_type = m.get('SignType')

        return self

class AddSmsSignRequestSignFileList(DaraModel):
    def __init__(
        self,
        file_contents: str = None,
        file_suffix: str = None,
    ):
        # The Base64-encoded string of the qualification certificate file for the signature. The image size cannot exceed 2 MB. In some scenarios, you need to upload a certificate file when you apply for a signature.
        # 
        # For detailed specifications, see [File upload specifications](https://help.aliyun.com/document_detail/463316.html).
        # 
        # This parameter is required.
        self.file_contents = file_contents
        # The format of the signature certificate file. Multiple images can be uploaded. Currently, JPG, PNG, GIF, and JPEG formats are supported. In some scenarios, you need to upload a certificate file when you apply for a signature.
        # 
        # > If the signature is for third-party use or if you are an individual-certified user whose self-use signature source is an enterprise or public institution name, you also need to upload a certificate file and a power of attorney. For more information, see [Certificate file](https://help.aliyun.com/document_detail/108076.html) and [Power of attorney](https://help.aliyun.com/document_detail/56741.html).
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

