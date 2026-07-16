# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class SubmitDNAJobRequest(DaraModel):
    def __init__(
        self,
        config: str = None,
        dbid: str = None,
        input: main_models.SubmitDNAJobRequestInput = None,
        owner_account: str = None,
        owner_id: int = None,
        pipeline_id: str = None,
        primary_key: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        template_id: str = None,
        user_data: str = None,
    ):
        # The DNA configuration in JSON format. If specified, these settings override the corresponding template parameters.
        self.config = config
        # The DNA library ID. To create a DNA library, see [CreateDNADB](https://help.aliyun.com/document_detail/479275.html).
        # 
        # This parameter is required.
        self.dbid = dbid
        # The input DNA file.
        # 
        # This parameter is required.
        self.input = input
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The pipeline ID.
        self.pipeline_id = pipeline_id
        # The unique primary key for the video. You are responsible for ensuring its uniqueness.
        # 
        # This parameter is required.
        self.primary_key = primary_key
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The template ID.
        self.template_id = template_id
        # The user-defined data. The maximum length is 128 bytes.
        self.user_data = user_data

    def validate(self):
        if self.input:
            self.input.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.dbid is not None:
            result['DBId'] = self.dbid

        if self.input is not None:
            result['Input'] = self.input.to_map()

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id

        if self.primary_key is not None:
            result['PrimaryKey'] = self.primary_key

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('DBId') is not None:
            self.dbid = m.get('DBId')

        if m.get('Input') is not None:
            temp_model = main_models.SubmitDNAJobRequestInput()
            self.input = temp_model.from_map(m.get('Input'))

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')

        if m.get('PrimaryKey') is not None:
            self.primary_key = m.get('PrimaryKey')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class SubmitDNAJobRequestInput(DaraModel):
    def __init__(
        self,
        media: str = None,
        type: str = None,
    ):
        # The media ID or OSS file url of the input file.
        # 
        # 1\\. `oss://bucket/object`
        # 
        # 2\\. `http(s)://bucket.oss-[regionId].aliyuncs.com/object`
        # 
        # In these formats, `bucket` is the name of an OSS bucket in the same region as your project, and `object` is the file path.
        # 
        # This parameter is required.
        self.media = media
        # The type of the input file. Valid values:
        # 
        # 1. `OSS`: The input is an OSS file url.
        # 
        # 2. `Media`: The input is a media ID.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media is not None:
            result['Media'] = self.media

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Media') is not None:
            self.media = m.get('Media')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

