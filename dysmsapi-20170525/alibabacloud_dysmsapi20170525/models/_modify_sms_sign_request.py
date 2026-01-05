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
        # The scenario description of your released services. Provide the information of your services, such as a website URL, a domain name with an ICP filing, an app download URL, or the name of your WeChat official account or mini program. For sign-in scenarios, you must also provide an account and password for tests. A detailed description can improve the review efficiency of signatures and templates.
        # 
        # > The description can be up to 200 characters in length.
        # 
        # This parameter is required.
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The list of signature files.
        # 
        # This parameter is required.
        self.sign_file_list = sign_file_list
        # The signature.
        # 
        # This parameter is required.
        self.sign_name = sign_name
        # The source of the signature. Valid values:
        # 
        # *   **0**: full name or abbreviation of an enterprise or institution.
        # *   **1**: full name or abbreviation of a website with Ministry of Industry and Information Technology (MIIT) filing.
        # *   **2**: full name or abbreviation of an app.
        # *   **3**: full name or abbreviation of a WeChat official account or applet.
        # *   **4**: full name or abbreviation of an e-commerce store.
        # *   **5**: full name or abbreviation of a trademark.
        # 
        # This parameter is required.
        self.sign_source = sign_source
        # The type of the signature. Valid values:
        # 
        # *   **0**: verification-code signature
        # *   **1**: general-purpose signature
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
        # The base64-encoded string of the signed files. The size of the image cannot exceed 2 MB.
        # 
        # In some scenarios, documents are required to prove your identity. For more information, see [Signature specifications](https://help.aliyun.com/document_detail/108076.html).
        # 
        # This parameter is required.
        self.file_contents = file_contents
        # The format of the documents. You can upload multiple images. JPG, PNG, GIF, and JPEG are supported.
        # 
        # In some scenarios, documents are required to prove your identity. For more information, see [Signature specifications](https://help.aliyun.com/document_detail/108076.html).
        # 
        # > If the signature is used for other purposes or the signature source is an enterprise or public institution, you must upload some documents and an authorization letter. For more information, see [Documents](https://help.aliyun.com/document_detail/108076.html) and [Letter of authorization](https://help.aliyun.com/document_detail/56741.html).
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

