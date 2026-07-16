# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class CreateCompressPointCloudTaskRequest(DaraModel):
    def __init__(
        self,
        compress_method: str = None,
        credential_config: main_models.CredentialConfig = None,
        kdtree_option: main_models.KdtreeOption = None,
        notification: main_models.Notification = None,
        octree_option: main_models.OctreeOption = None,
        point_cloud_fields: List[str] = None,
        point_cloud_file_format: str = None,
        project_name: str = None,
        source_uri: str = None,
        tags: Dict[str, Any] = None,
        target_uri: str = None,
        user_data: str = None,
    ):
        # The compression algorithm. Valid values:
        # 
        # - octree: octree
        # 
        # - kdtree: K-d tree
        # 
        # This parameter is required.
        self.compress_method = compress_method
        # **Leave this parameter empty unless you have special requirements.**
        # 
        # The China authorization configuration. This parameter is optional. For more information, see [Use chained authorization to access resources of other entities](https://help.aliyun.com/document_detail/465340.html).
        self.credential_config = credential_config
        # The K-d tree compression parameters.
        self.kdtree_option = kdtree_option
        # The message notification configuration. For more information, click Notification. For information about the format of asynchronous notification messages, see [Asynchronous notification message format](https://help.aliyun.com/document_detail/2743997.html).
        # 
        # > Intelligent Media Management does not support specifying a callback URL for API call callbacks. Use Message Service (MNS) instead.
        # >
        self.notification = notification
        # The octree compression parameters.
        self.octree_option = octree_option
        # The PCD attribute fields that participate in compression and the compression order. After compression, data is decompressed in this order.
        # 
        # - If you use PCL library octree compression, ["xyz"] is supported.
        # 
        # - If you use Draco library K-d tree compression, ["xyz"] or ["xyz", "intensity"] is supported.
        # 
        # This parameter is required.
        self.point_cloud_fields = point_cloud_fields
        # The point cloud file format. Only PCD format is supported. Default value: pcd.
        self.point_cloud_file_format = point_cloud_file_format
        # The project name. For information about how to obtain the project name, see [Create a project](https://help.aliyun.com/document_detail/478153.html).
        # 
        # This parameter is required.
        self.project_name = project_name
        # The OSS URI of the point cloud file.
        # 
        # The OSS URI follows the format oss://${Bucket}/${Object}, where `${Bucket}` is the name of an OSS bucket in the same region as the current project, and `${Object}` is the full path of the file including the file name extension.
        # 
        # This parameter is required.
        self.source_uri = source_uri
        # The custom tags that are used to search for and filter asynchronous tasks.
        self.tags = tags
        # The OSS URI of the compressed output file.
        # 
        # The OSS URI follows the format oss://${Bucket}/${Object}, where `${Bucket}` is the name of an OSS bucket in the same region as the current project, and `${Object}` is the full path of the file including the file name extension.
        # 
        # This parameter is required.
        self.target_uri = target_uri
        # The custom information, which is returned in asynchronous message notifications to help you associate message notifications within your system. Maximum length: 2,048 bytes.
        self.user_data = user_data

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()
        if self.kdtree_option:
            self.kdtree_option.validate()
        if self.notification:
            self.notification.validate()
        if self.octree_option:
            self.octree_option.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compress_method is not None:
            result['CompressMethod'] = self.compress_method

        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()

        if self.kdtree_option is not None:
            result['KdtreeOption'] = self.kdtree_option.to_map()

        if self.notification is not None:
            result['Notification'] = self.notification.to_map()

        if self.octree_option is not None:
            result['OctreeOption'] = self.octree_option.to_map()

        if self.point_cloud_fields is not None:
            result['PointCloudFields'] = self.point_cloud_fields

        if self.point_cloud_file_format is not None:
            result['PointCloudFileFormat'] = self.point_cloud_file_format

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.target_uri is not None:
            result['TargetURI'] = self.target_uri

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompressMethod') is not None:
            self.compress_method = m.get('CompressMethod')

        if m.get('CredentialConfig') is not None:
            temp_model = main_models.CredentialConfig()
            self.credential_config = temp_model.from_map(m.get('CredentialConfig'))

        if m.get('KdtreeOption') is not None:
            temp_model = main_models.KdtreeOption()
            self.kdtree_option = temp_model.from_map(m.get('KdtreeOption'))

        if m.get('Notification') is not None:
            temp_model = main_models.Notification()
            self.notification = temp_model.from_map(m.get('Notification'))

        if m.get('OctreeOption') is not None:
            temp_model = main_models.OctreeOption()
            self.octree_option = temp_model.from_map(m.get('OctreeOption'))

        if m.get('PointCloudFields') is not None:
            self.point_cloud_fields = m.get('PointCloudFields')

        if m.get('PointCloudFileFormat') is not None:
            self.point_cloud_file_format = m.get('PointCloudFileFormat')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('TargetURI') is not None:
            self.target_uri = m.get('TargetURI')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

