# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
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
        # The status code returned.
        self.code = code
        # The media assets that meet the requirements.
        self.media_info_list = media_info_list
        # The ID of the request.
        self.request_id = request_id
        # The pagination identifier.
        self.scroll_token = scroll_token
        # Indicates whether the request was successful.
        self.success = success
        # The total number of media assets that meet the conditions.
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
        ai_data: main_models.SearchMediaResponseBodyMediaInfoListAiData = None,
        ai_rough_data: main_models.SearchMediaResponseBodyMediaInfoListAiRoughData = None,
        custom_fields: str = None,
        file_info_list: List[main_models.SearchMediaResponseBodyMediaInfoListFileInfoList] = None,
        index_status_list: List[main_models.SearchMediaResponseBodyMediaInfoListIndexStatusList] = None,
        media_basic_info: main_models.SearchMediaResponseBodyMediaInfoListMediaBasicInfo = None,
        media_id: str = None,
    ):
        # The details of the intelligent AI job.
        self.ai_data = ai_data
        # The description of the AI job.
        self.ai_rough_data = ai_rough_data
        self.custom_fields = custom_fields
        # The information about the files.
        self.file_info_list = file_info_list
        self.index_status_list = index_status_list
        # The basic information about the media asset.
        self.media_basic_info = media_basic_info
        # The ID of the media asset.
        self.media_id = media_id

    def validate(self):
        if self.ai_data:
            self.ai_data.validate()
        if self.ai_rough_data:
            self.ai_rough_data.validate()
        if self.file_info_list:
            for v1 in self.file_info_list:
                 if v1:
                    v1.validate()
        if self.index_status_list:
            for v1 in self.index_status_list:
                 if v1:
                    v1.validate()
        if self.media_basic_info:
            self.media_basic_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ai_data is not None:
            result['AiData'] = self.ai_data.to_map()

        if self.ai_rough_data is not None:
            result['AiRoughData'] = self.ai_rough_data.to_map()

        if self.custom_fields is not None:
            result['CustomFields'] = self.custom_fields

        result['FileInfoList'] = []
        if self.file_info_list is not None:
            for k1 in self.file_info_list:
                result['FileInfoList'].append(k1.to_map() if k1 else None)

        result['IndexStatusList'] = []
        if self.index_status_list is not None:
            for k1 in self.index_status_list:
                result['IndexStatusList'].append(k1.to_map() if k1 else None)

        if self.media_basic_info is not None:
            result['MediaBasicInfo'] = self.media_basic_info.to_map()

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AiData') is not None:
            temp_model = main_models.SearchMediaResponseBodyMediaInfoListAiData()
            self.ai_data = temp_model.from_map(m.get('AiData'))

        if m.get('AiRoughData') is not None:
            temp_model = main_models.SearchMediaResponseBodyMediaInfoListAiRoughData()
            self.ai_rough_data = temp_model.from_map(m.get('AiRoughData'))

        if m.get('CustomFields') is not None:
            self.custom_fields = m.get('CustomFields')

        self.file_info_list = []
        if m.get('FileInfoList') is not None:
            for k1 in m.get('FileInfoList'):
                temp_model = main_models.SearchMediaResponseBodyMediaInfoListFileInfoList()
                self.file_info_list.append(temp_model.from_map(k1))

        self.index_status_list = []
        if m.get('IndexStatusList') is not None:
            for k1 in m.get('IndexStatusList'):
                temp_model = main_models.SearchMediaResponseBodyMediaInfoListIndexStatusList()
                self.index_status_list.append(temp_model.from_map(k1))

        if m.get('MediaBasicInfo') is not None:
            temp_model = main_models.SearchMediaResponseBodyMediaInfoListMediaBasicInfo()
            self.media_basic_info = temp_model.from_map(m.get('MediaBasicInfo'))

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        return self

class SearchMediaResponseBodyMediaInfoListMediaBasicInfo(DaraModel):
    def __init__(
        self,
        biz: str = None,
        business_type: str = None,
        cate_id: int = None,
        cate_name: str = None,
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
        namespace: str = None,
        reference_id: str = None,
        snapshots: str = None,
        source: str = None,
        sprite_images: str = None,
        status: str = None,
        stream_status: str = None,
        title: str = None,
        transcode_status: str = None,
        upload_source: str = None,
        user_data: str = None,
        vision_description: str = None,
    ):
        # The business to which the media asset belongs.
        self.biz = biz
        # The business type of the media asset.
        self.business_type = business_type
        # The ID of the category.
        self.cate_id = cate_id
        # The name of the category.
        self.cate_name = cate_name
        # The category of the media asset.
        self.category = category
        # The thumbnail URL of the media asset.
        self.cover_url = cover_url
        # The time when the media asset was created.
        self.create_time = create_time
        # The time when the media asset was deleted.
        self.deleted_time = deleted_time
        # The description of the media asset.
        self.description = description
        # The address of the media asset that is waiting to be registered.
        self.input_url = input_url
        # The ID of the media asset.
        self.media_id = media_id
        # The tags of the media asset.
        self.media_tags = media_tags
        # The type of the media asset.
        self.media_type = media_type
        # The time when the media asset was modified.
        self.modified_time = modified_time
        self.namespace = namespace
        # The custom ID of the media asset. The ID is a string that contains 6 to 64 characters. Only letters, digits, hyphens (-), and underscores (_) are supported. Each custom ID is unique.
        self.reference_id = reference_id
        # The snapshots of the media asset.
        self.snapshots = snapshots
        # The source of the media asset.
        self.source = source
        # The image sprite of the media asset
        self.sprite_images = sprite_images
        # The state of the media asset.
        self.status = status
        self.stream_status = stream_status
        # The title of the media asset.
        self.title = title
        # The transcoding status of the media asset.
        self.transcode_status = transcode_status
        # The upload source of the media asset.
        self.upload_source = upload_source
        # The user data.
        self.user_data = user_data
        self.vision_description = vision_description

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

        if self.cate_name is not None:
            result['CateName'] = self.cate_name

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

        if self.namespace is not None:
            result['Namespace'] = self.namespace

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

        if self.stream_status is not None:
            result['StreamStatus'] = self.stream_status

        if self.title is not None:
            result['Title'] = self.title

        if self.transcode_status is not None:
            result['TranscodeStatus'] = self.transcode_status

        if self.upload_source is not None:
            result['UploadSource'] = self.upload_source

        if self.user_data is not None:
            result['UserData'] = self.user_data

        if self.vision_description is not None:
            result['VisionDescription'] = self.vision_description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Biz') is not None:
            self.biz = m.get('Biz')

        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')

        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')

        if m.get('CateName') is not None:
            self.cate_name = m.get('CateName')

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

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

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

        if m.get('StreamStatus') is not None:
            self.stream_status = m.get('StreamStatus')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('TranscodeStatus') is not None:
            self.transcode_status = m.get('TranscodeStatus')

        if m.get('UploadSource') is not None:
            self.upload_source = m.get('UploadSource')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('VisionDescription') is not None:
            self.vision_description = m.get('VisionDescription')

        return self

class SearchMediaResponseBodyMediaInfoListIndexStatusList(DaraModel):
    def __init__(
        self,
        index_status: str = None,
        index_type: str = None,
    ):
        self.index_status = index_status
        self.index_type = index_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.index_status is not None:
            result['IndexStatus'] = self.index_status

        if self.index_type is not None:
            result['IndexType'] = self.index_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IndexStatus') is not None:
            self.index_status = m.get('IndexStatus')

        if m.get('IndexType') is not None:
            self.index_type = m.get('IndexType')

        return self

class SearchMediaResponseBodyMediaInfoListFileInfoList(DaraModel):
    def __init__(
        self,
        file_basic_info: main_models.SearchMediaResponseBodyMediaInfoListFileInfoListFileBasicInfo = None,
    ):
        # The basic information about the file, such as the duration and size.
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
        # The bitrate of the file.
        self.bitrate = bitrate
        # The time when the file was created.
        self.create_time = create_time
        # The duration of the file.
        self.duration = duration
        # The name of the file.
        self.file_name = file_name
        # The size of the file in bytes.
        self.file_size = file_size
        # The status of the file.
        self.file_status = file_status
        # The type of the file.
        self.file_type = file_type
        # The Object Storage Service (OSS) URL of the file.
        self.file_url = file_url
        # The encapsulation format of the file.
        self.format_name = format_name
        # The height of the file.
        self.height = height
        self.images_input = images_input
        # The time when the file was last modified.
        self.modified_time = modified_time
        # The region in which the file is stored.
        self.region = region
        # The width of the file.
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

class SearchMediaResponseBodyMediaInfoListAiRoughData(DaraModel):
    def __init__(
        self,
        ai_category: str = None,
        ai_job_id: str = None,
        result: str = None,
        save_type: str = None,
        status: str = None,
    ):
        # TV Series
        self.ai_category = ai_category
        # The ID of the AI job.
        self.ai_job_id = ai_job_id
        # The results of the AI job.
        self.result = result
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

        if self.result is not None:
            result['Result'] = self.result

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

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('SaveType') is not None:
            self.save_type = m.get('SaveType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class SearchMediaResponseBodyMediaInfoListAiData(DaraModel):
    def __init__(
        self,
        ai_label_info: List[main_models.SearchMediaResponseBodyMediaInfoListAiDataAiLabelInfo] = None,
        asr_info: List[main_models.SearchMediaResponseBodyMediaInfoListAiDataAsrInfo] = None,
        ocr_info: List[main_models.SearchMediaResponseBodyMediaInfoListAiDataOcrInfo] = None,
    ):
        # The tags of the intelligent AI job.
        self.ai_label_info = ai_label_info
        # The information about audio files.
        self.asr_info = asr_info
        # The subtitles.
        self.ocr_info = ocr_info

    def validate(self):
        if self.ai_label_info:
            for v1 in self.ai_label_info:
                 if v1:
                    v1.validate()
        if self.asr_info:
            for v1 in self.asr_info:
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

        result['AsrInfo'] = []
        if self.asr_info is not None:
            for k1 in self.asr_info:
                result['AsrInfo'].append(k1.to_map() if k1 else None)

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
                temp_model = main_models.SearchMediaResponseBodyMediaInfoListAiDataAiLabelInfo()
                self.ai_label_info.append(temp_model.from_map(k1))

        self.asr_info = []
        if m.get('AsrInfo') is not None:
            for k1 in m.get('AsrInfo'):
                temp_model = main_models.SearchMediaResponseBodyMediaInfoListAiDataAsrInfo()
                self.asr_info.append(temp_model.from_map(k1))

        self.ocr_info = []
        if m.get('OcrInfo') is not None:
            for k1 in m.get('OcrInfo'):
                temp_model = main_models.SearchMediaResponseBodyMediaInfoListAiDataOcrInfo()
                self.ocr_info.append(temp_model.from_map(k1))

        return self

class SearchMediaResponseBodyMediaInfoListAiDataOcrInfo(DaraModel):
    def __init__(
        self,
        clip_id: str = None,
        content: str = None,
        from_: float = None,
        timestamp: float = None,
        to: float = None,
    ):
        # The ID of the clip.
        self.clip_id = clip_id
        # The text content.
        self.content = content
        # The start time of the clip.
        self.from_ = from_
        # The timestamp of the clip.
        self.timestamp = timestamp
        # The end time of the clip.
        self.to = to

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.clip_id is not None:
            result['ClipId'] = self.clip_id

        if self.content is not None:
            result['Content'] = self.content

        if self.from_ is not None:
            result['From'] = self.from_

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.to is not None:
            result['To'] = self.to

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClipId') is not None:
            self.clip_id = m.get('ClipId')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('To') is not None:
            self.to = m.get('To')

        return self

class SearchMediaResponseBodyMediaInfoListAiDataAsrInfo(DaraModel):
    def __init__(
        self,
        clip_id: str = None,
        content: str = None,
        from_: float = None,
        timestamp: float = None,
        to: float = None,
    ):
        # The ID of the clip.
        self.clip_id = clip_id
        # The text content.
        self.content = content
        # The start time of the clip.
        self.from_ = from_
        # The timestamp of the clip.
        self.timestamp = timestamp
        # The end time of the clip.
        self.to = to

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.clip_id is not None:
            result['ClipId'] = self.clip_id

        if self.content is not None:
            result['Content'] = self.content

        if self.from_ is not None:
            result['From'] = self.from_

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.to is not None:
            result['To'] = self.to

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClipId') is not None:
            self.clip_id = m.get('ClipId')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('To') is not None:
            self.to = m.get('To')

        return self

class SearchMediaResponseBodyMediaInfoListAiDataAiLabelInfo(DaraModel):
    def __init__(
        self,
        category: str = None,
        face_id: str = None,
        label_id: str = None,
        label_name: str = None,
        label_type: str = None,
        occurrences: List[main_models.SearchMediaResponseBodyMediaInfoListAiDataAiLabelInfoOccurrences] = None,
        source: str = None,
    ):
        # The category.
        self.category = category
        # The face ID.
        self.face_id = face_id
        # The ID of the entity.
        self.label_id = label_id
        # The name of the entity.
        self.label_name = label_name
        # The type of the tag.
        self.label_type = label_type
        # The clips.
        self.occurrences = occurrences
        # The source.
        self.source = source

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

        if self.face_id is not None:
            result['FaceId'] = self.face_id

        if self.label_id is not None:
            result['LabelId'] = self.label_id

        if self.label_name is not None:
            result['LabelName'] = self.label_name

        if self.label_type is not None:
            result['LabelType'] = self.label_type

        result['Occurrences'] = []
        if self.occurrences is not None:
            for k1 in self.occurrences:
                result['Occurrences'].append(k1.to_map() if k1 else None)

        if self.source is not None:
            result['Source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('FaceId') is not None:
            self.face_id = m.get('FaceId')

        if m.get('LabelId') is not None:
            self.label_id = m.get('LabelId')

        if m.get('LabelName') is not None:
            self.label_name = m.get('LabelName')

        if m.get('LabelType') is not None:
            self.label_type = m.get('LabelType')

        self.occurrences = []
        if m.get('Occurrences') is not None:
            for k1 in m.get('Occurrences'):
                temp_model = main_models.SearchMediaResponseBodyMediaInfoListAiDataAiLabelInfoOccurrences()
                self.occurrences.append(temp_model.from_map(k1))

        if m.get('Source') is not None:
            self.source = m.get('Source')

        return self

class SearchMediaResponseBodyMediaInfoListAiDataAiLabelInfoOccurrences(DaraModel):
    def __init__(
        self,
        content: str = None,
        finegrain_id: str = None,
        finegrain_name: str = None,
        from_: float = None,
        image: str = None,
        score: float = None,
        table_batch_seq_id: str = None,
        to: float = None,
        tracks: List[main_models.SearchMediaResponseBodyMediaInfoListAiDataAiLabelInfoOccurrencesTracks] = None,
        clip_id: str = None,
    ):
        # The text content.
        self.content = content
        # The fine-grained ID of the entity.
        self.finegrain_id = finegrain_id
        # The fine-grained name of the entity.
        self.finegrain_name = finegrain_name
        # The start time of the clip.
        self.from_ = from_
        # The optimal face image encoded in Base64.
        self.image = image
        # The score.
        self.score = score
        # The sequence ID of the vector table.
        self.table_batch_seq_id = table_batch_seq_id
        # The end time of the clip.
        self.to = to
        # The track sequence.
        self.tracks = tracks
        # The ID of the clip.
        self.clip_id = clip_id

    def validate(self):
        if self.tracks:
            for v1 in self.tracks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.finegrain_id is not None:
            result['FinegrainId'] = self.finegrain_id

        if self.finegrain_name is not None:
            result['FinegrainName'] = self.finegrain_name

        if self.from_ is not None:
            result['From'] = self.from_

        if self.image is not None:
            result['Image'] = self.image

        if self.score is not None:
            result['Score'] = self.score

        if self.table_batch_seq_id is not None:
            result['TableBatchSeqId'] = self.table_batch_seq_id

        if self.to is not None:
            result['To'] = self.to

        result['Tracks'] = []
        if self.tracks is not None:
            for k1 in self.tracks:
                result['Tracks'].append(k1.to_map() if k1 else None)

        if self.clip_id is not None:
            result['clipId'] = self.clip_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('FinegrainId') is not None:
            self.finegrain_id = m.get('FinegrainId')

        if m.get('FinegrainName') is not None:
            self.finegrain_name = m.get('FinegrainName')

        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('Image') is not None:
            self.image = m.get('Image')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('TableBatchSeqId') is not None:
            self.table_batch_seq_id = m.get('TableBatchSeqId')

        if m.get('To') is not None:
            self.to = m.get('To')

        self.tracks = []
        if m.get('Tracks') is not None:
            for k1 in m.get('Tracks'):
                temp_model = main_models.SearchMediaResponseBodyMediaInfoListAiDataAiLabelInfoOccurrencesTracks()
                self.tracks.append(temp_model.from_map(k1))

        if m.get('clipId') is not None:
            self.clip_id = m.get('clipId')

        return self

class SearchMediaResponseBodyMediaInfoListAiDataAiLabelInfoOccurrencesTracks(DaraModel):
    def __init__(
        self,
        position: str = None,
        size: float = None,
        timestamp: float = None,
    ):
        # The coordinates of the bounding box.
        self.position = position
        # The size of the bounding box.
        self.size = size
        # The timestamp of the track.
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.position is not None:
            result['Position'] = self.position

        if self.size is not None:
            result['Size'] = self.size

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Position') is not None:
            self.position = m.get('Position')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

