# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCompressPointCloudTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        compress_method: str = None,
        credential_config_shrink: str = None,
        kdtree_option_shrink: str = None,
        notification_shrink: str = None,
        octree_option_shrink: str = None,
        point_cloud_fields_shrink: str = None,
        point_cloud_file_format: str = None,
        project_name: str = None,
        source_uri: str = None,
        tags_shrink: str = None,
        target_uri: str = None,
        user_data: str = None,
    ):
        # The name of the compression algorithm. Valid values:
        # 
        # - octree: octree
        # 
        # - kdtree: K-d tree
        # 
        # This parameter is required.
        self.compress_method = compress_method
        # **If you do not have special requirements, leave this parameter empty.**
        # 
        # The chained authorization configuration. This parameter is not required. For more information, see [Use chained authorization to access other entity resources](https://help.aliyun.com/document_detail/465340.html).
        self.credential_config_shrink = credential_config_shrink
        # The parameters for K-d tree compression.
        self.kdtree_option_shrink = kdtree_option_shrink
        # The notification configuration. For more information, click Notification. For the format of asynchronous notification messages, see [Asynchronous notification message format](https://help.aliyun.com/document_detail/2743997.html).
        # 
        # > Intelligent Media Management API callbacks do not support specifying a webhook address. Use MNS instead.
        self.notification_shrink = notification_shrink
        # The parameters for Octree compression.
        self.octree_option_shrink = octree_option_shrink
        # The PCD property fields to compress and the compression order. After compression, the data is decompressed in this order.
        # 
        # - If you use Octree compression from the Point Cloud Library (PCL), only ["xyz"] is supported.
        # 
        # - If you use K-d tree compression from the Draco library, ["xyz"] or ["xyz", "intensity"] is supported.
        # 
        # This parameter is required.
        self.point_cloud_fields_shrink = point_cloud_fields_shrink
        # The format of the point cloud file. Only the PCD format is supported. The default value is pcd.
        self.point_cloud_file_format = point_cloud_file_format
        # The project name. For more information, see [Create a project](https://help.aliyun.com/document_detail/478153.html).
        # 
        # This parameter is required.
        self.project_name = project_name
        # The OSS URI of the point cloud file.
        # 
        # The URI must be in the format oss\\://${Bucket}/${Object}. ${Bucket} is the name of the OSS bucket in the same region as the project. ${Object} is the full path of the file, including the file name extension.
        # 
        # This parameter is required.
        self.source_uri = source_uri
        # Custom tags to search for and filter asynchronous tasks.
        self.tags_shrink = tags_shrink
        # The OSS URI of the output file after compression.
        # 
        # The URI must be in the format oss\\://${Bucket}/${Object}. ${Bucket} is the name of the OSS bucket in the same region as the project. ${Object} is the full path of the file, including the file name extension.
        # 
        # This parameter is required.
        self.target_uri = target_uri
        # Custom information that is returned in the asynchronous notification message. You can use this information to associate notification messages in your system. The maximum length is 2048 bytes.
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compress_method is not None:
            result['CompressMethod'] = self.compress_method

        if self.credential_config_shrink is not None:
            result['CredentialConfig'] = self.credential_config_shrink

        if self.kdtree_option_shrink is not None:
            result['KdtreeOption'] = self.kdtree_option_shrink

        if self.notification_shrink is not None:
            result['Notification'] = self.notification_shrink

        if self.octree_option_shrink is not None:
            result['OctreeOption'] = self.octree_option_shrink

        if self.point_cloud_fields_shrink is not None:
            result['PointCloudFields'] = self.point_cloud_fields_shrink

        if self.point_cloud_file_format is not None:
            result['PointCloudFileFormat'] = self.point_cloud_file_format

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri

        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink

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
            self.credential_config_shrink = m.get('CredentialConfig')

        if m.get('KdtreeOption') is not None:
            self.kdtree_option_shrink = m.get('KdtreeOption')

        if m.get('Notification') is not None:
            self.notification_shrink = m.get('Notification')

        if m.get('OctreeOption') is not None:
            self.octree_option_shrink = m.get('OctreeOption')

        if m.get('PointCloudFields') is not None:
            self.point_cloud_fields_shrink = m.get('PointCloudFields')

        if m.get('PointCloudFileFormat') is not None:
            self.point_cloud_file_format = m.get('PointCloudFileFormat')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')

        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')

        if m.get('TargetURI') is not None:
            self.target_uri = m.get('TargetURI')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

