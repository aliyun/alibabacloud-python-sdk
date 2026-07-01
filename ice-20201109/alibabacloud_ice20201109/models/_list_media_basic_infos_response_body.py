# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class ListMediaBasicInfosResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        media_infos: List[main_models.ListMediaBasicInfosResponseBodyMediaInfos] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The maximum number of entries returned per page.
        self.max_results = max_results
        # The list of matching media assets.
        self.media_infos = media_infos
        # The token for retrieving the next page of results. If this parameter is not returned, all results have been retrieved.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of matching entries.
        self.total_count = total_count

    def validate(self):
        if self.media_infos:
            for v1 in self.media_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        result['MediaInfos'] = []
        if self.media_infos is not None:
            for k1 in self.media_infos:
                result['MediaInfos'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        self.media_infos = []
        if m.get('MediaInfos') is not None:
            for k1 in m.get('MediaInfos'):
                temp_model = main_models.ListMediaBasicInfosResponseBodyMediaInfos()
                self.media_infos.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListMediaBasicInfosResponseBodyMediaInfos(DaraModel):
    def __init__(
        self,
        file_info_list: List[main_models.ListMediaBasicInfosResponseBodyMediaInfosFileInfoList] = None,
        media_basic_info: main_models.ListMediaBasicInfosResponseBodyMediaInfosMediaBasicInfo = None,
        media_id: str = None,
    ):
        # A list of file information objects.
        self.file_info_list = file_info_list
        # The basic information about the media asset.
        self.media_basic_info = media_basic_info
        # The media asset ID.
        self.media_id = media_id

    def validate(self):
        if self.file_info_list:
            for v1 in self.file_info_list:
                 if v1:
                    v1.validate()
        if self.media_basic_info:
            self.media_basic_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FileInfoList'] = []
        if self.file_info_list is not None:
            for k1 in self.file_info_list:
                result['FileInfoList'].append(k1.to_map() if k1 else None)

        if self.media_basic_info is not None:
            result['MediaBasicInfo'] = self.media_basic_info.to_map()

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.file_info_list = []
        if m.get('FileInfoList') is not None:
            for k1 in m.get('FileInfoList'):
                temp_model = main_models.ListMediaBasicInfosResponseBodyMediaInfosFileInfoList()
                self.file_info_list.append(temp_model.from_map(k1))

        if m.get('MediaBasicInfo') is not None:
            temp_model = main_models.ListMediaBasicInfosResponseBodyMediaInfosMediaBasicInfo()
            self.media_basic_info = temp_model.from_map(m.get('MediaBasicInfo'))

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        return self

class ListMediaBasicInfosResponseBodyMediaInfosMediaBasicInfo(DaraModel):
    def __init__(
        self,
        biz: str = None,
        business_type: str = None,
        cate_id: int = None,
        category: str = None,
        cover_url: str = None,
        create_time: str = None,
        deleted_time: str = None,
        description: str = None,
        input_url: str = None,
        media_id: str = None,
        media_tags: str = None,
        media_type: str = None,
        modified_time: str = None,
        reference_id: str = None,
        snapshots: str = None,
        source: str = None,
        sprite_images: str = None,
        status: str = None,
        title: str = None,
        transcode_status: str = None,
        upload_source: str = None,
        user_data: str = None,
    ):
        # The associated business.
        self.biz = biz
        # The business type.
        self.business_type = business_type
        # The category ID.
        self.cate_id = cate_id
        # The category of the media asset.
        self.category = category
        # The cover URL.
        self.cover_url = cover_url
        # The time the media asset was created.
        self.create_time = create_time
        # The time the media asset was deleted.
        self.deleted_time = deleted_time
        # The description of the media asset.
        self.description = description
        # The source URL of the media asset.
        self.input_url = input_url
        # The media asset ID.
        self.media_id = media_id
        # Tags associated with the media asset.
        self.media_tags = media_tags
        # The media type.
        self.media_type = media_type
        # The time the media asset was last modified.
        self.modified_time = modified_time
        # A user-defined ID that must be unique within your account. The ID must be 6 to 64 characters in length and can contain only letters, digits, hyphens (-), and underscores (_).
        self.reference_id = reference_id
        # Information about the snapshots.
        self.snapshots = snapshots
        # The source of the media asset.
        self.source = source
        # Information about the image sprites.
        self.sprite_images = sprite_images
        # The status of the media asset.
        self.status = status
        # The title of the media asset.
        self.title = title
        # The transcoding status.
        self.transcode_status = transcode_status
        # The upload source of the media asset.
        self.upload_source = upload_source
        # The user data.
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz is not None:
            result['Biz'] = self.biz

        if self.business_type is not None:
            result['BusinessType'] = self.business_type

        if self.cate_id is not None:
            result['CateId'] = self.cate_id

        if self.category is not None:
            result['Category'] = self.category

        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.deleted_time is not None:
            result['DeletedTime'] = self.deleted_time

        if self.description is not None:
            result['Description'] = self.description

        if self.input_url is not None:
            result['InputURL'] = self.input_url

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.media_tags is not None:
            result['MediaTags'] = self.media_tags

        if self.media_type is not None:
            result['MediaType'] = self.media_type

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.reference_id is not None:
            result['ReferenceId'] = self.reference_id

        if self.snapshots is not None:
            result['Snapshots'] = self.snapshots

        if self.source is not None:
            result['Source'] = self.source

        if self.sprite_images is not None:
            result['SpriteImages'] = self.sprite_images

        if self.status is not None:
            result['Status'] = self.status

        if self.title is not None:
            result['Title'] = self.title

        if self.transcode_status is not None:
            result['TranscodeStatus'] = self.transcode_status

        if self.upload_source is not None:
            result['UploadSource'] = self.upload_source

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Biz') is not None:
            self.biz = m.get('Biz')

        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')

        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DeletedTime') is not None:
            self.deleted_time = m.get('DeletedTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InputURL') is not None:
            self.input_url = m.get('InputURL')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('MediaTags') is not None:
            self.media_tags = m.get('MediaTags')

        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('ReferenceId') is not None:
            self.reference_id = m.get('ReferenceId')

        if m.get('Snapshots') is not None:
            self.snapshots = m.get('Snapshots')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SpriteImages') is not None:
            self.sprite_images = m.get('SpriteImages')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('TranscodeStatus') is not None:
            self.transcode_status = m.get('TranscodeStatus')

        if m.get('UploadSource') is not None:
            self.upload_source = m.get('UploadSource')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class ListMediaBasicInfosResponseBodyMediaInfosFileInfoList(DaraModel):
    def __init__(
        self,
        file_basic_info: main_models.ListMediaBasicInfosResponseBodyMediaInfosFileInfoListFileBasicInfo = None,
    ):
        # Basic information about the file, such as its duration and size.
        self.file_basic_info = file_basic_info

    def validate(self):
        if self.file_basic_info:
            self.file_basic_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_basic_info is not None:
            result['FileBasicInfo'] = self.file_basic_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileBasicInfo') is not None:
            temp_model = main_models.ListMediaBasicInfosResponseBodyMediaInfosFileInfoListFileBasicInfo()
            self.file_basic_info = temp_model.from_map(m.get('FileBasicInfo'))

        return self

class ListMediaBasicInfosResponseBodyMediaInfosFileInfoListFileBasicInfo(DaraModel):
    def __init__(
        self,
        bitrate: str = None,
        create_time: str = None,
        duration: str = None,
        file_name: str = None,
        file_size: str = None,
        file_status: str = None,
        file_type: str = None,
        file_url: str = None,
        format_name: str = None,
        height: str = None,
        modified_time: str = None,
        region: str = None,
        width: str = None,
    ):
        # The bitrate of the file, in Kbit/s.
        self.bitrate = bitrate
        # The time the file was created.
        self.create_time = create_time
        # The duration of the file, in seconds.
        self.duration = duration
        # The name of the file.
        self.file_name = file_name
        # The size of the file, in bytes.
        self.file_size = file_size
        # The status of the file.
        self.file_status = file_status
        # The type of the file.
        self.file_type = file_type
        # The Object Storage Service (OSS) URL of the file.
        self.file_url = file_url
        # The container format.
        self.format_name = format_name
        # The height of the video, in pixels.
        self.height = height
        # The time the file was last modified.
        self.modified_time = modified_time
        # The region where the file is stored.
        self.region = region
        # The width of the video, in pixels.
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_size is not None:
            result['FileSize'] = self.file_size

        if self.file_status is not None:
            result['FileStatus'] = self.file_status

        if self.file_type is not None:
            result['FileType'] = self.file_type

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.format_name is not None:
            result['FormatName'] = self.format_name

        if self.height is not None:
            result['Height'] = self.height

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.region is not None:
            result['Region'] = self.region

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')

        if m.get('FileStatus') is not None:
            self.file_status = m.get('FileStatus')

        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('FormatName') is not None:
            self.format_name = m.get('FormatName')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

