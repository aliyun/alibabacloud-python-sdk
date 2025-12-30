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
        # The configurations of the media fingerprint analysis job. The value is a JSON object. If you specify this parameter, the template parameters are overwritten.
        self.config = config
        # The ID of the media fingerprint library. If you do not specify this parameter, the default media fingerprint library is used. For more information about how to create a media fingerprint library, see [CreateDNADB](https://help.aliyun.com/document_detail/479275.html).
        # 
        # This parameter is required.
        self.dbid = dbid
        # The input file for media fingerprint analysis.
        # 
        # This parameter is required.
        self.input = input
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the ApsaraVideo Media Processing (MPS) queue to which the media fingerprint analysis job is submitted.
        self.pipeline_id = pipeline_id
        # The primary key of the video. You must make sure that each primary key is unique.
        # 
        # This parameter is required.
        self.primary_key = primary_key
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The template ID.
        self.template_id = template_id
        # The user-defined data. The data can be up to 128 bytes in length.
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
        # The input file. The file can be an OSS object or a media asset. You can specify the path of an OSS object in one of the following formats:
        # 
        # 1\\. oss://bucket/object
        # 
        # 2\\. http(s)://bucket.oss-[regionId].aliyuncs.com/object
        # 
        # In the preceding paths, bucket indicates an OSS bucket that resides in the same region as the current project, and object indicates the path of the object in the bucket.
        # 
        # This parameter is required.
        self.media = media
        # The type of the input file. Valid values:
        # 
        # 1.  OSS: Object Storage Service (OSS) object.
        # 2.  Media: media asset.
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

