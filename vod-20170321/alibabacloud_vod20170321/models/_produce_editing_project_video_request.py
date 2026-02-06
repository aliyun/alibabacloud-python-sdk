# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ProduceEditingProjectVideoRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        cover_url: str = None,
        description: str = None,
        media_metadata: str = None,
        owner_id: int = None,
        produce_config: str = None,
        project_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        timeline: str = None,
        title: str = None,
        user_data: str = None,
    ):
        # The ID of the application. Default value: **app-1000000**. For more information, see [Multi-application service](https://help.aliyun.com/document_detail/113600.html).
        self.app_id = app_id
        # The thumbnail URL of the online editing project.
        self.cover_url = cover_url
        # The description of the online editing project.
        self.description = description
        # The video metadata. The value must be in JSON format. For more information about the parameter structure, see [MediaMetadata](~~52839#title_rtf_ry5_gjp~~).
        self.media_metadata = media_metadata
        self.owner_id = owner_id
        # The configuration of video production. The value must be in the JSON format. For more information about the parameter structure, see [ProduceConfig](~~52839#title-ybl-7cs-y7d~~).
        # 
        # >  StorageLocation is required if you produce videos in a region other than China (Shanghai).
        self.produce_config = produce_config
        # The ID of the online editing project. You can use one of the following methods to obtain the ID of the online editing project:
        # 
        # *   Log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com). In the left-side navigation pane, choose **Production Center** > **Video Editing** to view the ID of the online editing project.
        # *   Obtain the value of ProjectId from the response to the [AddEditingProject](https://help.aliyun.com/document_detail/69048.html) operation.
        self.project_id = project_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The timeline of the online editing project. The value must be in JSON format. For more information about the parameter structure, see [Timeline](~~52839#07bc7fe0f2xuh~~).
        self.timeline = timeline
        # The title of the online editing project.
        self.title = title
        # The custom configurations, such as the callback configuration. The value must be a JSON string. For more information about the parameter structure, see [UserData](~~86952#title_vz7_xzs_0c5~~).
        # 
        # > The callback configurations take effect only after you specify an HTTP URL for receiving callback notifications and select the event types in the ApsaraVideo VOD console.
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url

        if self.description is not None:
            result['Description'] = self.description

        if self.media_metadata is not None:
            result['MediaMetadata'] = self.media_metadata

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.produce_config is not None:
            result['ProduceConfig'] = self.produce_config

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.timeline is not None:
            result['Timeline'] = self.timeline

        if self.title is not None:
            result['Title'] = self.title

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('MediaMetadata') is not None:
            self.media_metadata = m.get('MediaMetadata')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ProduceConfig') is not None:
            self.produce_config = m.get('ProduceConfig')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Timeline') is not None:
            self.timeline = m.get('Timeline')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

