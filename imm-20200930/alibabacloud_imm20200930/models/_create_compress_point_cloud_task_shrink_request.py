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
        # The compression algorithm. Valid values:
        # 
        # *   octree
        # *   kdtree
        # 
        # This parameter is required.
        self.compress_method = compress_method
        # **If you have no special requirements, leave this parameter empty.**
        # 
        # The configurations of authorization chains. This parameter is optional. For more information, see [Use authorization chains to access resources of other entities](https://help.aliyun.com/document_detail/465340.html).
        self.credential_config_shrink = credential_config_shrink
        # The k-d tree compression options.
        self.kdtree_option_shrink = kdtree_option_shrink
        # The notification settings. For information about the asynchronous notification format, see [Asynchronous message examples](https://help.aliyun.com/document_detail/2743997.html).
        # 
        # >  The IMM operation does not support a callback URL. We recommend that you use Simple Message Queue (SMQ) to receive notifications.
        self.notification_shrink = notification_shrink
        # The octree compression options.
        self.octree_option_shrink = octree_option_shrink
        # The PCD property fields and the compression order in which the data is decompressed after the compression is complete.
        # 
        # *   If octree of Point Cloud Library (PCL) is used for compression, ["xyz"] is supported.
        # *   If Draco k-dimensional (k-d) tree is used for compression, ["xyz"] and ["xyz", "intensity"] are supported.
        # 
        # This parameter is required.
        self.point_cloud_fields_shrink = point_cloud_fields_shrink
        # The file format. Set the value to the default value: pcd.
        self.point_cloud_file_format = point_cloud_file_format
        # The name of the project. For more information, see [CreateProject](https://help.aliyun.com/document_detail/478153.html).
        # 
        # This parameter is required.
        self.project_name = project_name
        # The OSS URL of the PCD file.
        # 
        # Specify the value in the oss://${Bucket}/${Object} format. `${Bucket}` specifies the name of the OSS bucket that resides in the same region as the current project. `${Object}` specifies the path of the object with the extension included.
        # 
        # This parameter is required.
        self.source_uri = source_uri
        # The custom tags, which can be used to search for and filter asynchronous tasks.
        self.tags_shrink = tags_shrink
        # The OSS URL of the output file after compression.
        # 
        # Specify the value in the oss://${Bucket}/${Object} format. `${Bucket}` specifies the name of the OSS bucket that resides in the same region as the current project. `${Object}` specifies the path of the object with the extension included.
        # 
        # This parameter is required.
        self.target_uri = target_uri
        # The custom data, which is returned in an asynchronous notification and facilitates notification management. The maximum length is 2,048 bytes.
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

