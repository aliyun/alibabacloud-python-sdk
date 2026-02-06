# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class GetVideoInfosResponseBody(DaraModel):
    def __init__(
        self,
        non_exist_reference_ids: List[str] = None,
        non_exist_video_ids: List[str] = None,
        request_id: str = None,
        video_list: List[main_models.GetVideoInfosResponseBodyVideoList] = None,
    ):
        self.non_exist_reference_ids = non_exist_reference_ids
        # The IDs of the videos that do not exist.
        self.non_exist_video_ids = non_exist_video_ids
        # The ID of the request.
        self.request_id = request_id
        # The information about the audio or video files.
        self.video_list = video_list

    def validate(self):
        if self.video_list:
            for v1 in self.video_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.non_exist_reference_ids is not None:
            result['NonExistReferenceIds'] = self.non_exist_reference_ids

        if self.non_exist_video_ids is not None:
            result['NonExistVideoIds'] = self.non_exist_video_ids

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['VideoList'] = []
        if self.video_list is not None:
            for k1 in self.video_list:
                result['VideoList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NonExistReferenceIds') is not None:
            self.non_exist_reference_ids = m.get('NonExistReferenceIds')

        if m.get('NonExistVideoIds') is not None:
            self.non_exist_video_ids = m.get('NonExistVideoIds')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.video_list = []
        if m.get('VideoList') is not None:
            for k1 in m.get('VideoList'):
                temp_model = main_models.GetVideoInfosResponseBodyVideoList()
                self.video_list.append(temp_model.from_map(k1))

        return self

class GetVideoInfosResponseBodyVideoList(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        cate_id: int = None,
        cate_name: str = None,
        cover_url: str = None,
        creation_time: str = None,
        description: str = None,
        download_switch: str = None,
        duration: float = None,
        modification_time: str = None,
        reference_id: str = None,
        restore_expiration: str = None,
        restore_status: str = None,
        size: int = None,
        snapshots: List[str] = None,
        status: str = None,
        storage_class: str = None,
        storage_location: str = None,
        tags: str = None,
        template_group_id: str = None,
        title: str = None,
        user_data: str = None,
        video_id: str = None,
    ):
        # The ID of the application.
        self.app_id = app_id
        # The ID of the category.
        self.cate_id = cate_id
        # The name of the category.
        self.cate_name = cate_name
        # The thumbnail URL of the audio or video file.
        self.cover_url = cover_url
        # The time when the media file was created. The time is in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The description of the audio or video file.
        self.description = description
        # Indicates whether the offline download feature is enabled. If you enable the offline download feature, users can download and play videos by using the ApsaraVideo Player on a local PC. For more information, see [Configure download settings](https://help.aliyun.com/document_detail/86107.html). Valid values:
        # 
        # *   **on**: the offline download feature is enabled.
        # *   **off**: the offline download feature is not enabled.
        self.download_switch = download_switch
        # The duration of the audio or video file. Unit: seconds.
        self.duration = duration
        # The time when the audio or video file was last updated. The time is in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.modification_time = modification_time
        self.reference_id = reference_id
        # The period of time in which the audio file remains in the restored state.
        self.restore_expiration = restore_expiration
        # The restoration status of the audio file. Valid values:
        # 
        # *   **Processing**
        # *   **Success**
        # *   **Failed**
        self.restore_status = restore_status
        # The size of the source file. Unit: bytes.
        self.size = size
        # The video snapshot URLs.
        self.snapshots = snapshots
        # The status of the video. Valid values:
        # 
        # *   **Uploading**
        # *   **UploadFail**
        # *   **UploadSucc**
        # *   **Transcoding**
        # *   **TranscodeFail**
        # *   **Blocked**
        # *   **Normal**
        self.status = status
        # The storage class of the audio file. Valid values:
        # 
        # *   **Standard**: All media resources are stored as Standard objects.
        # *   **IA**: All media resources are stored as IA objects.
        # *   **Archive**: All media resources are stored as Archive objects.
        # *   **ColdArchive**: All media resources are stored as Cold Archive objects.
        # *   **SourceIA**: Only the source files are IA objects.
        # *   **SourceArchive**: Only the source files are Archive objects.
        # *   **SourceColdArchive**: Only the source file is stored as a Cold Archive object.
        # *   **Changing**: The storage class of the video file is being changed.
        # *   **SourceChanging**: The storage class of the source file is being changed.
        self.storage_class = storage_class
        # The storage address of the audio or video file.
        self.storage_location = storage_location
        # The tags of the audio or video file. Multiple tags are separated by commas (,).
        self.tags = tags
        # The ID of the transcoding template group.
        self.template_group_id = template_group_id
        # The title of the audio or video file.
        self.title = title
        # Custom settings. This is a JSON string that supports settings such as message callbacks and upload acceleration. For more information, please refer to [UserData](https://help.aliyun.com/document_detail/86952.html).
        self.user_data = user_data
        # The ID of the audio or video file.
        self.video_id = video_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.cate_id is not None:
            result['CateId'] = self.cate_id

        if self.cate_name is not None:
            result['CateName'] = self.cate_name

        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.download_switch is not None:
            result['DownloadSwitch'] = self.download_switch

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.modification_time is not None:
            result['ModificationTime'] = self.modification_time

        if self.reference_id is not None:
            result['ReferenceId'] = self.reference_id

        if self.restore_expiration is not None:
            result['RestoreExpiration'] = self.restore_expiration

        if self.restore_status is not None:
            result['RestoreStatus'] = self.restore_status

        if self.size is not None:
            result['Size'] = self.size

        if self.snapshots is not None:
            result['Snapshots'] = self.snapshots

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class

        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.template_group_id is not None:
            result['TemplateGroupId'] = self.template_group_id

        if self.title is not None:
            result['Title'] = self.title

        if self.user_data is not None:
            result['UserData'] = self.user_data

        if self.video_id is not None:
            result['VideoId'] = self.video_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')

        if m.get('CateName') is not None:
            self.cate_name = m.get('CateName')

        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DownloadSwitch') is not None:
            self.download_switch = m.get('DownloadSwitch')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('ModificationTime') is not None:
            self.modification_time = m.get('ModificationTime')

        if m.get('ReferenceId') is not None:
            self.reference_id = m.get('ReferenceId')

        if m.get('RestoreExpiration') is not None:
            self.restore_expiration = m.get('RestoreExpiration')

        if m.get('RestoreStatus') is not None:
            self.restore_status = m.get('RestoreStatus')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Snapshots') is not None:
            self.snapshots = m.get('Snapshots')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')

        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('TemplateGroupId') is not None:
            self.template_group_id = m.get('TemplateGroupId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')

        return self

