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
        # The description of the signature application. The description cannot exceed 200 characters in length. The description is one of the reference information for signature review. We recommend that you describe the use scenarios of your services in detail, and provide information that can verify the services, such as a website URL, a domain name with an ICP filing, an app download URL, an official account name, or a mini program name. For sign-in scenarios, you must also provide an account and password for tests. A detailed description can improve the review efficiency of signatures and templates.
        # 
        # This parameter is required.
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The signature files.
        # 
        # This parameter is required.
        self.sign_file_list = sign_file_list
        # The name of the signature.
        # 
        # > 
        # 
        # *   The signature name is not case-sensitive. For example, [Alibaba Cloud Communication] and [alibaba cloud communication] are considered as the same name.
        # 
        # *   If your verification code signature and general-purpose signature have the same name, the system uses the general-purpose signature to send messages by default.
        # 
        # This parameter is required.
        self.sign_name = sign_name
        # The source of the signature. Valid values:
        # 
        # *   **0**: the full name or abbreviation of an enterprise or institution
        # *   **1**: the full name or abbreviation of a website that has obtained an ICP filing from the Ministry of Industry and Information Technology (MIIT) of China
        # *   **2**: the full name or abbreviation of an app
        # *   **3**: the full name or abbreviation of an official account or mini-program
        # *   **4**: the full name or abbreviation of an e-commerce store
        # *   **5**: the full name or abbreviation of a trademark
        # 
        # This parameter is required.
        self.sign_source = sign_source
        # The type of the signature. Valid values:
        # 
        # *   **0**: verification code
        # *   **1**: general-purpose
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
        # The Base64-encoded string of the qualification document. An image cannot exceed 2 MB in size. In some scenarios, you must upload supporting documents to apply for signatures. For more information, see [SMS signature specifications](https://help.aliyun.com/document_detail/108076.html).
        # 
        # This parameter is required.
        self.file_contents = file_contents
        # The format of the qualification document. You can upload multiple images. Images in JPG, PNG, GIF, or JPEG format are supported.
        # 
        # In some scenarios, you must upload supporting documents to apply for signatures. For more information, see [SMS signature specifications](https://help.aliyun.com/document_detail/108076.html).
        # 
        # > If you apply for a signature for other users or if the signature source is the name of an enterprise or public institution, you must upload a certificate and a letter of authorization. For more information, see [Certificate](https://help.aliyun.com/document_detail/108076.html) and [Letter of authorization](https://help.aliyun.com/document_detail/56741.html).
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

