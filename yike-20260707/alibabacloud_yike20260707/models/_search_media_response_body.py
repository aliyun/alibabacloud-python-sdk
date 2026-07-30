# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yike20260707 import models as main_models
from darabonba.model import DaraModel

class SearchMediaResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        media_info_list: List[main_models.SearchMediaResponseBodyMediaInfoList] = None,
        request_id: str = None,
        scroll_token: str = None,
        success: str = None,
        total: int = None,
    ):
        # The return code.
        self.code = code
        # The collection of media assets that meet the specified criteria.
        self.media_info_list = media_info_list
        # The request ID.
        self.request_id = request_id
        # The pagination token.
        self.scroll_token = scroll_token
        # Indicates whether the call was successful.
        self.success = success
        # The total number of media assets that meet the specified criteria.
        self.total = total

    def validate(self):
        if self.media_info_list:
            for v1 in self.media_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['MediaInfoList'] = []
        if self.media_info_list is not None:
            for k1 in self.media_info_list:
                result['MediaInfoList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.scroll_token is not None:
            result['ScrollToken'] = self.scroll_token

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.media_info_list = []
        if m.get('MediaInfoList') is not None:
            for k1 in m.get('MediaInfoList'):
                temp_model = main_models.SearchMediaResponseBodyMediaInfoList()
                self.media_info_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ScrollToken') is not None:
            self.scroll_token = m.get('ScrollToken')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class SearchMediaResponseBodyMediaInfoList(DaraModel):
    def __init__(
        self,
        file_info_list: List[main_models.SearchMediaResponseBodyMediaInfoListFileInfoList] = None,
        media_basic_info: main_models.SearchMediaResponseBodyMediaInfoListMediaBasicInfo = None,
        media_dynamic_info: main_models.SearchMediaResponseBodyMediaInfoListMediaDynamicInfo = None,
        media_id: str = None,
    ):
        # The list of media files.
        self.file_info_list = file_info_list
        # The basic information of the media asset.
        self.media_basic_info = media_basic_info
        # The dynamic data of the media asset.
        self.media_dynamic_info = media_dynamic_info
        # The media asset ID.
        self.media_id = media_id

    def validate(self):
        if self.file_info_list:
            for v1 in self.file_info_list:
                 if v1:
                    v1.validate()
        if self.media_basic_info:
            self.media_basic_info.validate()
        if self.media_dynamic_info:
            self.media_dynamic_info.validate()

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

        if self.media_dynamic_info is not None:
            result['MediaDynamicInfo'] = self.media_dynamic_info.to_map()

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.file_info_list = []
        if m.get('FileInfoList') is not None:
            for k1 in m.get('FileInfoList'):
                temp_model = main_models.SearchMediaResponseBodyMediaInfoListFileInfoList()
                self.file_info_list.append(temp_model.from_map(k1))

        if m.get('MediaBasicInfo') is not None:
            temp_model = main_models.SearchMediaResponseBodyMediaInfoListMediaBasicInfo()
            self.media_basic_info = temp_model.from_map(m.get('MediaBasicInfo'))

        if m.get('MediaDynamicInfo') is not None:
            temp_model = main_models.SearchMediaResponseBodyMediaInfoListMediaDynamicInfo()
            self.media_dynamic_info = temp_model.from_map(m.get('MediaDynamicInfo'))

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        return self

class SearchMediaResponseBodyMediaInfoListMediaDynamicInfo(DaraModel):
    def __init__(
        self,
        dynamic_meta_data: main_models.SearchMediaResponseBodyMediaInfoListMediaDynamicInfoDynamicMetaData = None,
    ):
        # The dynamic metadata.
        self.dynamic_meta_data = dynamic_meta_data

    def validate(self):
        if self.dynamic_meta_data:
            self.dynamic_meta_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dynamic_meta_data is not None:
            result['DynamicMetaData'] = self.dynamic_meta_data.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DynamicMetaData') is not None:
            temp_model = main_models.SearchMediaResponseBodyMediaInfoListMediaDynamicInfoDynamicMetaData()
            self.dynamic_meta_data = temp_model.from_map(m.get('DynamicMetaData'))

        return self

class SearchMediaResponseBodyMediaInfoListMediaDynamicInfoDynamicMetaData(DaraModel):
    def __init__(
        self,
        data: str = None,
        entity_id: str = None,
    ):
        # The dynamic metadata content.
        self.data = data
        # The entity ID.
        self.entity_id = entity_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data

        if self.entity_id is not None:
            result['EntityId'] = self.entity_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')

        return self

class SearchMediaResponseBodyMediaInfoListMediaBasicInfo(DaraModel):
    def __init__(
        self,
        business_type: str = None,
        category_id: int = None,
        category_name: str = None,
        cover_url: str = None,
        create_time: str = None,
        description: str = None,
        entity_id: str = None,
        input_url: str = None,
        media_id: str = None,
        media_tags: str = None,
        media_type: str = None,
        modified_time: str = None,
        snapshots: str = None,
        source: str = None,
        sprite_images: str = None,
        status: str = None,
        title: str = None,
        transcode_status: str = None,
        upload_source: str = None,
        user_data: str = None,
    ):
        # The business type of the media asset.
        self.business_type = business_type
        # The category ID.
        self.category_id = category_id
        # The category name.
        self.category_name = category_name
        # The cover URL.
        self.cover_url = cover_url
        # The time when the media asset was created.
        self.create_time = create_time
        # The content description.
        self.description = description
        # The entity ID.
        self.entity_id = entity_id
        # The media asset URL.
        self.input_url = input_url
        # The media asset ID.
        self.media_id = media_id
        # The tags.
        self.media_tags = media_tags
        # The media type of the media asset.
        self.media_type = media_type
        # The time when the media asset was last modified.
        self.modified_time = modified_time
        # The snapshots.
        self.snapshots = snapshots
        # The source of the media asset.
        self.source = source
        # The sprite images.
        self.sprite_images = sprite_images
        # The resource status.
        self.status = status
        # The title.
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
        if self.business_type is not None:
            result['BusinessType'] = self.business_type

        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.category_name is not None:
            result['CategoryName'] = self.category_name

        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.entity_id is not None:
            result['EntityId'] = self.entity_id

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
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')

        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')

        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')

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

class SearchMediaResponseBodyMediaInfoListFileInfoList(DaraModel):
    def __init__(
        self,
        file_basic_info: main_models.SearchMediaResponseBodyMediaInfoListFileInfoListFileBasicInfo = None,
    ):
        # The basic file information, including duration and size.
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
            temp_model = main_models.SearchMediaResponseBodyMediaInfoListFileInfoListFileBasicInfo()
            self.file_basic_info = temp_model.from_map(m.get('FileBasicInfo'))

        return self

class SearchMediaResponseBodyMediaInfoListFileInfoListFileBasicInfo(DaraModel):
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
        images_input: str = None,
        modified_time: str = None,
        region: str = None,
        width: str = None,
    ):
        # The bitrate.
        self.bitrate = bitrate
        # The creation time.
        self.create_time = create_time
        # The duration.
        self.duration = duration
        # The file name.
        self.file_name = file_name
        # The file size, in bytes.
        self.file_size = file_size
        # The file status.
        self.file_status = file_status
        # The file type.
        self.file_type = file_type
        # The OSS URL of the file.
        self.file_url = file_url
        # The container format.
        self.format_name = format_name
        # The height.
        self.height = height
        # The image set information.
        self.images_input = images_input
        # The modification time.
        self.modified_time = modified_time
        # The storage region of the file.
        self.region = region
        # The width.
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

        if self.images_input is not None:
            result['ImagesInput'] = self.images_input

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

        if m.get('ImagesInput') is not None:
            self.images_input = m.get('ImagesInput')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

