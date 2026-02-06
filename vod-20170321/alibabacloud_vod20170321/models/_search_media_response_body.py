# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class SearchMediaResponseBody(DaraModel):
    def __init__(
        self,
        media_list: List[main_models.SearchMediaResponseBodyMediaList] = None,
        request_id: str = None,
        scroll_token: str = None,
        total: int = None,
    ):
        # The information about the media assets.
        self.media_list = media_list
        # The ID of the request.
        self.request_id = request_id
        # The pagination identifier.
        self.scroll_token = scroll_token
        # The total number of data records that meet the specified filter criteria.
        self.total = total

    def validate(self):
        if self.media_list:
            for v1 in self.media_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MediaList'] = []
        if self.media_list is not None:
            for k1 in self.media_list:
                result['MediaList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.scroll_token is not None:
            result['ScrollToken'] = self.scroll_token

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.media_list = []
        if m.get('MediaList') is not None:
            for k1 in m.get('MediaList'):
                temp_model = main_models.SearchMediaResponseBodyMediaList()
                self.media_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ScrollToken') is not None:
            self.scroll_token = m.get('ScrollToken')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class SearchMediaResponseBodyMediaList(DaraModel):
    def __init__(
        self,
        ai_data: main_models.SearchMediaResponseBodyMediaListAiData = None,
        ai_rough_data: main_models.SearchMediaResponseBodyMediaListAiRoughData = None,
        attached_media: main_models.SearchMediaResponseBodyMediaListAttachedMedia = None,
        audio: main_models.SearchMediaResponseBodyMediaListAudio = None,
        creation_time: str = None,
        image: main_models.SearchMediaResponseBodyMediaListImage = None,
        media_id: str = None,
        media_type: str = None,
        video: main_models.SearchMediaResponseBodyMediaListVideo = None,
    ):
        # Details about AI data.
        self.ai_data = ai_data
        # The basic information about AI data.
        self.ai_rough_data = ai_rough_data
        # [The information about the auxiliary media asset](https://help.aliyun.com/document_detail/86991.html).
        self.attached_media = attached_media
        # [The information about the audio](https://help.aliyun.com/document_detail/86991.html).
        self.audio = audio
        # The time when the media asset was created. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*hh:mm:ss*Z format. The time is displayed in UTC.
        self.creation_time = creation_time
        # [The information about the image](https://help.aliyun.com/document_detail/86991.html).
        self.image = image
        # The ID of the file.
        self.media_id = media_id
        # The type of the media asset. Valid values:
        # 
        # *   **video**
        # *   **audio**
        # *   **image**
        # *   **attached**
        self.media_type = media_type
        # [The information about the video](https://help.aliyun.com/document_detail/86991.html).
        self.video = video

    def validate(self):
        if self.ai_data:
            self.ai_data.validate()
        if self.ai_rough_data:
            self.ai_rough_data.validate()
        if self.attached_media:
            self.attached_media.validate()
        if self.audio:
            self.audio.validate()
        if self.image:
            self.image.validate()
        if self.video:
            self.video.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ai_data is not None:
            result['AiData'] = self.ai_data.to_map()

        if self.ai_rough_data is not None:
            result['AiRoughData'] = self.ai_rough_data.to_map()

        if self.attached_media is not None:
            result['AttachedMedia'] = self.attached_media.to_map()

        if self.audio is not None:
            result['Audio'] = self.audio.to_map()

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.image is not None:
            result['Image'] = self.image.to_map()

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.media_type is not None:
            result['MediaType'] = self.media_type

        if self.video is not None:
            result['Video'] = self.video.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AiData') is not None:
            temp_model = main_models.SearchMediaResponseBodyMediaListAiData()
            self.ai_data = temp_model.from_map(m.get('AiData'))

        if m.get('AiRoughData') is not None:
            temp_model = main_models.SearchMediaResponseBodyMediaListAiRoughData()
            self.ai_rough_data = temp_model.from_map(m.get('AiRoughData'))

        if m.get('AttachedMedia') is not None:
            temp_model = main_models.SearchMediaResponseBodyMediaListAttachedMedia()
            self.attached_media = temp_model.from_map(m.get('AttachedMedia'))

        if m.get('Audio') is not None:
            temp_model = main_models.SearchMediaResponseBodyMediaListAudio()
            self.audio = temp_model.from_map(m.get('Audio'))

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Image') is not None:
            temp_model = main_models.SearchMediaResponseBodyMediaListImage()
            self.image = temp_model.from_map(m.get('Image'))

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')

        if m.get('Video') is not None:
            temp_model = main_models.SearchMediaResponseBodyMediaListVideo()
            self.video = temp_model.from_map(m.get('Video'))

        return self

class SearchMediaResponseBodyMediaListVideo(DaraModel):
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
        media_source: str = None,
        modification_time: str = None,
        preprocess_status: str = None,
        reference_id: str = None,
        restore_expiration: str = None,
        restore_status: str = None,
        size: int = None,
        snapshots: List[str] = None,
        sprite_snapshots: List[str] = None,
        status: str = None,
        storage_class: str = None,
        storage_location: str = None,
        tags: str = None,
        title: str = None,
        transcode_mode: str = None,
        video_id: str = None,
    ):
        # The ID of the application.
        self.app_id = app_id
        # The ID of the category.
        self.cate_id = cate_id
        # The name of the category.
        self.cate_name = cate_name
        # The URL of the thumbnail.
        self.cover_url = cover_url
        # The time when the video file was created. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*hh:mm:ss*Z format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The description of the video file.
        self.description = description
        # The download switch. The video file can be downloaded offline only when the download switch is turned on. Valid values:
        # 
        # *   **on**
        # *   **off**
        self.download_switch = download_switch
        # The duration of the video file. Unit: seconds.
        self.duration = duration
        # The source of the video file. Valid values:
        # 
        # *   **general**: The video file is uploaded by using ApsaraVideo VOD.
        # *   **short_video**: The video file is uploaded by using the short video SDK.
        # *   **editing**: The video file is produced after online editing.
        # *   **live**: The video stream is recorded and uploaded as a file.
        self.media_source = media_source
        # The time when the video file was updated. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*hh:mm:ss*Z format. The time is displayed in UTC.
        self.modification_time = modification_time
        # The preprocessing status. Valid values:
        # 
        # *   **UnPreprocess**
        # *   **Preprocessing**
        # *   **PreprocessSucceed**
        # *   **PreprocessFailed**
        self.preprocess_status = preprocess_status
        self.reference_id = reference_id
        # The period of time in which the video file remains in the restored state.
        self.restore_expiration = restore_expiration
        # The restoration status of the video file. Valid values:
        # 
        # *   **Processing**
        # *   **Success**
        # *   **Failed**
        self.restore_status = restore_status
        # The size of the video file.
        self.size = size
        # The automatic snapshots.
        self.snapshots = snapshots
        # The sprite snapshots.
        self.sprite_snapshots = sprite_snapshots
        # The status of the file. Valid values:
        # 
        # *   **Uploading**
        # *   **UploadFail**
        # *   **UploadSucc**
        # *   **Transcoding**
        # *   **TranscodeFail**
        # *   **Blocked**
        # *   **Normal**
        self.status = status
        # The storage class of the video file. Valid values:
        # 
        # *   **Standard**: All media resources are stored as Standard objects.
        # *   **IA**: All media resources are stored as IA objects.
        # *   **Archive**: All media resources are stored as Archive objects.
        # *   **ColdArchive**: All media resources are stored as Cold Archive objects.
        # *   **SourceIA**: Only the source file is stored as an IA object.
        # *   **SourceArchive**: Only the source file is stored as an Archive object.
        # *   **SourceColdArchive**: Only the source file is stored as a Cold Archive object.
        # *   **Changing**: The storage class of the video file is being changed.
        # *   **SourceChanging**: The storage class of the source file is being changed.
        self.storage_class = storage_class
        # The region in which the video is stored.
        self.storage_location = storage_location
        # The tags of the video file.
        self.tags = tags
        # The title of the video.
        self.title = title
        # The transcoding mode. Valid values:
        # 
        # *   **FastTranscode**: The video file is immediately transcoded after it is uploaded. You cannot play the file before it is transcoded.
        # *   **NoTranscode**: The video file can be played without being transcoded. You can immediately play the file after it is uploaded.
        # *   **AsyncTranscode**: The video file can be immediately played and asynchronously transcoded after it is uploaded.
        self.transcode_mode = transcode_mode
        # The ID of the video file.
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

        if self.media_source is not None:
            result['MediaSource'] = self.media_source

        if self.modification_time is not None:
            result['ModificationTime'] = self.modification_time

        if self.preprocess_status is not None:
            result['PreprocessStatus'] = self.preprocess_status

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

        if self.sprite_snapshots is not None:
            result['SpriteSnapshots'] = self.sprite_snapshots

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class

        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.title is not None:
            result['Title'] = self.title

        if self.transcode_mode is not None:
            result['TranscodeMode'] = self.transcode_mode

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

        if m.get('MediaSource') is not None:
            self.media_source = m.get('MediaSource')

        if m.get('ModificationTime') is not None:
            self.modification_time = m.get('ModificationTime')

        if m.get('PreprocessStatus') is not None:
            self.preprocess_status = m.get('PreprocessStatus')

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

        if m.get('SpriteSnapshots') is not None:
            self.sprite_snapshots = m.get('SpriteSnapshots')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')

        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('TranscodeMode') is not None:
            self.transcode_mode = m.get('TranscodeMode')

        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')

        return self

class SearchMediaResponseBodyMediaListImage(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        cate_id: int = None,
        cate_name: str = None,
        creation_time: str = None,
        description: str = None,
        image_id: str = None,
        modification_time: str = None,
        status: str = None,
        storage_location: str = None,
        tags: str = None,
        title: str = None,
        url: str = None,
    ):
        # The ID of the application.
        self.app_id = app_id
        # The ID of the category.
        self.cate_id = cate_id
        # The name of the category.
        self.cate_name = cate_name
        # The time when the image was created. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*hh:mm:ss*Z format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The description of the image file.
        self.description = description
        # The ID of the image file.
        self.image_id = image_id
        # The time when the image file was updated. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*hh:mm:ss*Z format. The time is displayed in UTC.
        self.modification_time = modification_time
        # The status of the image file.
        # 
        # *   **Uploading**
        # *   **Normal**
        # *   **UploadFail**
        self.status = status
        # The region in which the image is stored.
        self.storage_location = storage_location
        # The tags of the image file.
        self.tags = tags
        # The title of the image file.
        self.title = title
        # The URL of the image file.
        self.url = url

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

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.modification_time is not None:
            result['ModificationTime'] = self.modification_time

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.title is not None:
            result['Title'] = self.title

        if self.url is not None:
            result['URL'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')

        if m.get('CateName') is not None:
            self.cate_name = m.get('CateName')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ModificationTime') is not None:
            self.modification_time = m.get('ModificationTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('URL') is not None:
            self.url = m.get('URL')

        return self

class SearchMediaResponseBodyMediaListAudio(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        audio_id: str = None,
        cate_id: int = None,
        cate_name: str = None,
        cover_url: str = None,
        creation_time: str = None,
        description: str = None,
        download_switch: str = None,
        duration: float = None,
        media_source: str = None,
        modification_time: str = None,
        preprocess_status: str = None,
        reference_id: str = None,
        restore_expiration: str = None,
        restore_status: str = None,
        size: int = None,
        snapshots: List[str] = None,
        sprite_snapshots: List[str] = None,
        status: str = None,
        storage_class: str = None,
        storage_location: str = None,
        tags: str = None,
        title: str = None,
        transcode_mode: str = None,
    ):
        # The ID of the application.
        self.app_id = app_id
        # The ID of the audio file.
        self.audio_id = audio_id
        # The ID of the category.
        self.cate_id = cate_id
        # The name of the category.
        self.cate_name = cate_name
        # The URL of the thumbnail.
        self.cover_url = cover_url
        # The time when the audio stream was created. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*hh:mm:ss*Z format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The description of the audio file.
        self.description = description
        # The download switch. The audio file can be downloaded offline only when the download switch is turned on. Valid values:
        # 
        # *   **on**
        # *   **off**
        self.download_switch = download_switch
        # The duration of the audio file.
        self.duration = duration
        # The source of the audio file. Valid values:
        # 
        # *   **general**: The audio file is uploaded by using ApsaraVideo VOD.
        # *   **short_video**: The audio file is uploaded to ApsaraVideo VOD by using the short video SDK. For more information, see [Introduction](https://help.aliyun.com/document_detail/53407.html).
        # *   **editing**: The audio file is uploaded to ApsaraVideo VOD after online editing and production. For more information, see [ProduceEditingProjectVideo](https://help.aliyun.com/document_detail/68536.html).
        # *   **live**: The audio file is recorded and uploaded as a file to ApsaraVideo VOD.
        self.media_source = media_source
        # The time when the audio file was updated. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*hh:mm:ss*Z format. The time is displayed in UTC.
        self.modification_time = modification_time
        # The preprocessing status. Only preprocessed videos can be used for live streaming in the production studio. Valid values:
        # 
        # *   **UnPreprocess**
        # *   **Preprocessing**
        # *   **PreprocessSucceed**
        # *   **PreprocessFailed**
        self.preprocess_status = preprocess_status
        self.reference_id = reference_id
        # The period of time in which the audio file remains in the restored state.
        self.restore_expiration = restore_expiration
        # The restoration status of the audio file. Valid values:
        # 
        # *   **Processing**
        # *   **Success**
        # *   **Failed**
        self.restore_status = restore_status
        # The size of the audio file.
        self.size = size
        # The automatic snapshots.
        self.snapshots = snapshots
        # The sprite snapshots.
        self.sprite_snapshots = sprite_snapshots
        # The status of the audio file. Valid values:
        # 
        # *   **Uploading**
        # *   **Normal**
        # *   **UploadFail**
        # *   **Deleted**
        self.status = status
        # The storage class of the audio file. Valid values:
        # 
        # *   **Standard**: All media resources are stored as Standard objects.
        # *   **IA**: All media resources are stored as IA objects.
        # *   **Archive**: All media resources are stored as Archive objects.
        # *   **ColdArchive**: All media resources are stored as Cold Archive objects.
        # *   **SourceIA**: Only the source file is stored as an IA object.
        # *   **SourceArchive**: Only the source file is stored as an Archive object.
        # *   **SourceColdArchive**: Only the source file is stored as a Cold Archive object.
        # *   **Changing**: The storage class is being modified.
        self.storage_class = storage_class
        # The region in which the audio is stored.
        self.storage_location = storage_location
        # The tags of the audio file.
        self.tags = tags
        # The title of the audio file
        self.title = title
        # The transcoding mode. Valid values:
        # 
        # *   **FastTranscode**: The audio file is immediately transcoded after it is uploaded. You cannot play the file before it is transcoded.
        # *   **NoTranscode**: The audio file can be played without being transcoded. You can immediately play the file after it is uploaded.
        # *   **AsyncTranscode**: The audio file can be immediately played and asynchronously transcoded after it is uploaded.
        self.transcode_mode = transcode_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.audio_id is not None:
            result['AudioId'] = self.audio_id

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

        if self.media_source is not None:
            result['MediaSource'] = self.media_source

        if self.modification_time is not None:
            result['ModificationTime'] = self.modification_time

        if self.preprocess_status is not None:
            result['PreprocessStatus'] = self.preprocess_status

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

        if self.sprite_snapshots is not None:
            result['SpriteSnapshots'] = self.sprite_snapshots

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class

        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.title is not None:
            result['Title'] = self.title

        if self.transcode_mode is not None:
            result['TranscodeMode'] = self.transcode_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AudioId') is not None:
            self.audio_id = m.get('AudioId')

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

        if m.get('MediaSource') is not None:
            self.media_source = m.get('MediaSource')

        if m.get('ModificationTime') is not None:
            self.modification_time = m.get('ModificationTime')

        if m.get('PreprocessStatus') is not None:
            self.preprocess_status = m.get('PreprocessStatus')

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

        if m.get('SpriteSnapshots') is not None:
            self.sprite_snapshots = m.get('SpriteSnapshots')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')

        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('TranscodeMode') is not None:
            self.transcode_mode = m.get('TranscodeMode')

        return self

class SearchMediaResponseBodyMediaListAttachedMedia(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        business_type: str = None,
        categories: List[main_models.SearchMediaResponseBodyMediaListAttachedMediaCategories] = None,
        creation_time: str = None,
        description: str = None,
        media_id: str = None,
        modification_time: str = None,
        status: str = None,
        storage_location: str = None,
        tags: str = None,
        title: str = None,
        url: str = None,
    ):
        # The ID of the application.
        self.app_id = app_id
        # The type of the auxiliary media asset. Valid values:
        # 
        # *   **watermark**
        # *   **subtitle**
        # *   **material**
        self.business_type = business_type
        # The list of category IDs.
        self.categories = categories
        # The time when the auxiliary media asset was created. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*hh:mm:ss*Z format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The description of the auxiliary media asset.
        self.description = description
        # The ID of the auxiliary media asset.
        self.media_id = media_id
        # The time when the auxiliary media asset was updated. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*hh:mm:ss*Z format. The time is displayed in UTC.
        self.modification_time = modification_time
        # The status of the auxiliary media asset. Valid values:
        # 
        # *   **Uploading**
        # *   **Normal**
        # *   **UploadFail**
        self.status = status
        # The region in which the auxiliary media asset is stored.
        self.storage_location = storage_location
        # The tags of the auxiliary media asset.
        self.tags = tags
        # The title of the auxiliary media asset.
        self.title = title
        # The URL of the auxiliary media asset.
        self.url = url

    def validate(self):
        if self.categories:
            for v1 in self.categories:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.business_type is not None:
            result['BusinessType'] = self.business_type

        result['Categories'] = []
        if self.categories is not None:
            for k1 in self.categories:
                result['Categories'].append(k1.to_map() if k1 else None)

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.modification_time is not None:
            result['ModificationTime'] = self.modification_time

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.title is not None:
            result['Title'] = self.title

        if self.url is not None:
            result['URL'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')

        self.categories = []
        if m.get('Categories') is not None:
            for k1 in m.get('Categories'):
                temp_model = main_models.SearchMediaResponseBodyMediaListAttachedMediaCategories()
                self.categories.append(temp_model.from_map(k1))

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('ModificationTime') is not None:
            self.modification_time = m.get('ModificationTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('URL') is not None:
            self.url = m.get('URL')

        return self

class SearchMediaResponseBodyMediaListAttachedMediaCategories(DaraModel):
    def __init__(
        self,
        cate_id: int = None,
        cate_name: str = None,
        level: int = None,
        parent_id: int = None,
    ):
        # The category ID of the auxiliary media asset.
        self.cate_id = cate_id
        # The name of the category.
        self.cate_name = cate_name
        # The level of the category.
        self.level = level
        # The ID of the parent node.
        self.parent_id = parent_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cate_id is not None:
            result['CateId'] = self.cate_id

        if self.cate_name is not None:
            result['CateName'] = self.cate_name

        if self.level is not None:
            result['Level'] = self.level

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')

        if m.get('CateName') is not None:
            self.cate_name = m.get('CateName')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        return self

class SearchMediaResponseBodyMediaListAiRoughData(DaraModel):
    def __init__(
        self,
        ai_category: str = None,
        ai_job_id: str = None,
        save_type: str = None,
        status: str = None,
    ):
        # The AI category.
        self.ai_category = ai_category
        # The ID of the AI task.
        self.ai_job_id = ai_job_id
        # The save type.
        self.save_type = save_type
        # The data status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ai_category is not None:
            result['AiCategory'] = self.ai_category

        if self.ai_job_id is not None:
            result['AiJobId'] = self.ai_job_id

        if self.save_type is not None:
            result['SaveType'] = self.save_type

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AiCategory') is not None:
            self.ai_category = m.get('AiCategory')

        if m.get('AiJobId') is not None:
            self.ai_job_id = m.get('AiJobId')

        if m.get('SaveType') is not None:
            self.save_type = m.get('SaveType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class SearchMediaResponseBodyMediaListAiData(DaraModel):
    def __init__(
        self,
        ai_label_info: List[main_models.SearchMediaResponseBodyMediaListAiDataAiLabelInfo] = None,
        ocr_info: List[main_models.SearchMediaResponseBodyMediaListAiDataOcrInfo] = None,
    ):
        # The AI tags.
        self.ai_label_info = ai_label_info
        # The information about subtitles.
        self.ocr_info = ocr_info

    def validate(self):
        if self.ai_label_info:
            for v1 in self.ai_label_info:
                 if v1:
                    v1.validate()
        if self.ocr_info:
            for v1 in self.ocr_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AiLabelInfo'] = []
        if self.ai_label_info is not None:
            for k1 in self.ai_label_info:
                result['AiLabelInfo'].append(k1.to_map() if k1 else None)

        result['OcrInfo'] = []
        if self.ocr_info is not None:
            for k1 in self.ocr_info:
                result['OcrInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ai_label_info = []
        if m.get('AiLabelInfo') is not None:
            for k1 in m.get('AiLabelInfo'):
                temp_model = main_models.SearchMediaResponseBodyMediaListAiDataAiLabelInfo()
                self.ai_label_info.append(temp_model.from_map(k1))

        self.ocr_info = []
        if m.get('OcrInfo') is not None:
            for k1 in m.get('OcrInfo'):
                temp_model = main_models.SearchMediaResponseBodyMediaListAiDataOcrInfo()
                self.ocr_info.append(temp_model.from_map(k1))

        return self

class SearchMediaResponseBodyMediaListAiDataOcrInfo(DaraModel):
    def __init__(
        self,
        content: str = None,
        from_: float = None,
        to: float = None,
    ):
        # The text content.
        self.content = content
        # The start time of the subtitle.
        self.from_ = from_
        # The end time of the subtitle.
        self.to = to

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.from_ is not None:
            result['From'] = self.from_

        if self.to is not None:
            result['To'] = self.to

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('To') is not None:
            self.to = m.get('To')

        return self

class SearchMediaResponseBodyMediaListAiDataAiLabelInfo(DaraModel):
    def __init__(
        self,
        category: str = None,
        label_id: str = None,
        label_name: str = None,
        occurrences: List[main_models.SearchMediaResponseBodyMediaListAiDataAiLabelInfoOccurrences] = None,
    ):
        # The category.
        self.category = category
        # The ID of the tag.
        self.label_id = label_id
        # The name of the tag.
        self.label_name = label_name
        # The clips.
        self.occurrences = occurrences

    def validate(self):
        if self.occurrences:
            for v1 in self.occurrences:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.label_id is not None:
            result['LabelId'] = self.label_id

        if self.label_name is not None:
            result['LabelName'] = self.label_name

        result['Occurrences'] = []
        if self.occurrences is not None:
            for k1 in self.occurrences:
                result['Occurrences'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('LabelId') is not None:
            self.label_id = m.get('LabelId')

        if m.get('LabelName') is not None:
            self.label_name = m.get('LabelName')

        self.occurrences = []
        if m.get('Occurrences') is not None:
            for k1 in m.get('Occurrences'):
                temp_model = main_models.SearchMediaResponseBodyMediaListAiDataAiLabelInfoOccurrences()
                self.occurrences.append(temp_model.from_map(k1))

        return self

class SearchMediaResponseBodyMediaListAiDataAiLabelInfoOccurrences(DaraModel):
    def __init__(
        self,
        from_: float = None,
        score: float = None,
        to: float = None,
    ):
        # The start time of the clip.
        self.from_ = from_
        # The score.
        self.score = score
        # The end time of the clip.
        self.to = to

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_ is not None:
            result['From'] = self.from_

        if self.score is not None:
            result['Score'] = self.score

        if self.to is not None:
            result['To'] = self.to

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('To') is not None:
            self.to = m.get('To')

        return self

