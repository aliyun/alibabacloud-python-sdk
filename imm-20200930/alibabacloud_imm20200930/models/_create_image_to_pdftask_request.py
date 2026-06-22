# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class CreateImageToPDFTaskRequest(DaraModel):
    def __init__(
        self,
        credential_config: main_models.CredentialConfig = None,
        notification: main_models.Notification = None,
        project_name: str = None,
        sources: List[main_models.CreateImageToPDFTaskRequestSources] = None,
        tags: Dict[str, Any] = None,
        target_uri: str = None,
        user_data: str = None,
    ):
        # **If you have no special requirements, leave this parameter empty.**
        # 
        # The chained authorization configuration. For more information, see [Use chained authorization to access resources of other entities](https://help.aliyun.com/document_detail/465340.html).
        self.credential_config = credential_config
        # The message notification configuration. For more information, click Notification. For the format of asynchronous notification messages, see [Asynchronous notification message format](https://help.aliyun.com/document_detail/2743997.html).
        self.notification = notification
        # The name of the project. For more information, see [Create a project](https://help.aliyun.com/document_detail/478153.html).
        # 
        # This parameter is required.
        self.project_name = project_name
        # A list of input images. The images are converted in the order of their URIs in this list.
        # 
        # This parameter is required.
        self.sources = sources
        # Custom tags used to search for and filter asynchronous tasks.
        self.tags = tags
        # The OSS address where the output PDF file is stored.
        # 
        # The address must be in the \\`oss\\://${bucketname}/${objectname}\\` format. \\`${bucketname}\\` must be an OSS bucket in the same region as the project. \\`${objectname}\\` must be the path of the file, including the file name.
        # 
        # This parameter is required.
        self.target_uri = target_uri
        # Custom user information that is returned in the asynchronous notification message. This helps you associate the notification message with your system. The maximum length is 2048 bytes.
        self.user_data = user_data

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()
        if self.notification:
            self.notification.validate()
        if self.sources:
            for v1 in self.sources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()

        if self.notification is not None:
            result['Notification'] = self.notification.to_map()

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        result['Sources'] = []
        if self.sources is not None:
            for k1 in self.sources:
                result['Sources'].append(k1.to_map() if k1 else None)

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.target_uri is not None:
            result['TargetURI'] = self.target_uri

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialConfig') is not None:
            temp_model = main_models.CredentialConfig()
            self.credential_config = temp_model.from_map(m.get('CredentialConfig'))

        if m.get('Notification') is not None:
            temp_model = main_models.Notification()
            self.notification = temp_model.from_map(m.get('Notification'))

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        self.sources = []
        if m.get('Sources') is not None:
            for k1 in m.get('Sources'):
                temp_model = main_models.CreateImageToPDFTaskRequestSources()
                self.sources.append(temp_model.from_map(k1))

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('TargetURI') is not None:
            self.target_uri = m.get('TargetURI')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class CreateImageToPDFTaskRequestSources(DaraModel):
    def __init__(
        self,
        rotate: int = None,
        uri: str = None,
    ):
        # The rotation angle of the image in degrees. Valid values:
        # 
        # - 0 (default)
        # 
        # - 90
        # 
        # - 180
        # 
        # - 270
        self.rotate = rotate
        # The OSS address of the source image.
        # 
        # The address must be in the \\`oss\\://${Bucket}/${Object}\\` format. \\``${Bucket}`\\` must be an OSS bucket in the same region as the project. \\``${Object}`\\` must be the full path of the file, including its file name extension.
        # 
        # Supported formats: JPG, JP2, PNG, TIFF, WebP, BMP, and SVG.
        # 
        # This parameter is required.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rotate is not None:
            result['Rotate'] = self.rotate

        if self.uri is not None:
            result['URI'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Rotate') is not None:
            self.rotate = m.get('Rotate')

        if m.get('URI') is not None:
            self.uri = m.get('URI')

        return self

