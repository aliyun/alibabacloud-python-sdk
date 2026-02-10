# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dysmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class CreateDigitalSmsTemplateRequest(DaraModel):
    def __init__(
        self,
        owner_id: int = None,
        remark: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sign_name: str = None,
        template_contents: List[main_models.CreateDigitalSmsTemplateRequestTemplateContents] = None,
        template_name: str = None,
    ):
        self.owner_id = owner_id
        # This parameter is required.
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.sign_name = sign_name
        # This parameter is required.
        self.template_contents = template_contents
        # This parameter is required.
        self.template_name = template_name

    def validate(self):
        if self.template_contents:
            for v1 in self.template_contents:
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

        if self.sign_name is not None:
            result['SignName'] = self.sign_name

        result['TemplateContents'] = []
        if self.template_contents is not None:
            for k1 in self.template_contents:
                result['TemplateContents'].append(k1.to_map() if k1 else None)

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

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

        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')

        self.template_contents = []
        if m.get('TemplateContents') is not None:
            for k1 in m.get('TemplateContents'):
                temp_model = main_models.CreateDigitalSmsTemplateRequestTemplateContents()
                self.template_contents.append(temp_model.from_map(k1))

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        return self

class CreateDigitalSmsTemplateRequestTemplateContents(DaraModel):
    def __init__(
        self,
        file_contents: str = None,
        file_name: str = None,
        file_size: int = None,
        file_suffix: str = None,
    ):
        self.file_contents = file_contents
        self.file_name = file_name
        self.file_size = file_size
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

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_size is not None:
            result['FileSize'] = self.file_size

        if self.file_suffix is not None:
            result['FileSuffix'] = self.file_suffix

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileContents') is not None:
            self.file_contents = m.get('FileContents')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')

        if m.get('FileSuffix') is not None:
            self.file_suffix = m.get('FileSuffix')

        return self

