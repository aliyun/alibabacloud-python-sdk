# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yike20260319 import models as main_models
from darabonba.model import DaraModel

class BatchGetYikeAssetMediaInfosResponseBody(DaraModel):
    def __init__(
        self,
        ignored_list: List[str] = None,
        media_infos: List[main_models.BatchGetYikeAssetMediaInfosResponseBodyMediaInfos] = None,
        request_id: str = None,
    ):
        self.ignored_list = ignored_list
        self.media_infos = media_infos
        # Id of the request
        self.request_id = request_id

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
        if self.ignored_list is not None:
            result['IgnoredList'] = self.ignored_list

        result['MediaInfos'] = []
        if self.media_infos is not None:
            for k1 in self.media_infos:
                result['MediaInfos'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IgnoredList') is not None:
            self.ignored_list = m.get('IgnoredList')

        self.media_infos = []
        if m.get('MediaInfos') is not None:
            for k1 in m.get('MediaInfos'):
                temp_model = main_models.BatchGetYikeAssetMediaInfosResponseBodyMediaInfos()
                self.media_infos.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class BatchGetYikeAssetMediaInfosResponseBodyMediaInfos(DaraModel):
    def __init__(
        self,
        biz_data: main_models.BatchGetYikeAssetMediaInfosResponseBodyMediaInfosBizData = None,
        file_info_list: List[main_models.BatchGetYikeAssetMediaInfosResponseBodyMediaInfosFileInfoList] = None,
        media_basic_info: main_models.BatchGetYikeAssetMediaInfosResponseBodyMediaInfosMediaBasicInfo = None,
        media_id: str = None,
    ):
        self.biz_data = biz_data
        # FileInfos
        self.file_info_list = file_info_list
        # BasicInfo
        self.media_basic_info = media_basic_info
        self.media_id = media_id

    def validate(self):
        if self.biz_data:
            self.biz_data.validate()
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
        if self.biz_data is not None:
            result['BizData'] = self.biz_data.to_map()

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
        if m.get('BizData') is not None:
            temp_model = main_models.BatchGetYikeAssetMediaInfosResponseBodyMediaInfosBizData()
            self.biz_data = temp_model.from_map(m.get('BizData'))

        self.file_info_list = []
        if m.get('FileInfoList') is not None:
            for k1 in m.get('FileInfoList'):
                temp_model = main_models.BatchGetYikeAssetMediaInfosResponseBodyMediaInfosFileInfoList()
                self.file_info_list.append(temp_model.from_map(k1))

        if m.get('MediaBasicInfo') is not None:
            temp_model = main_models.BatchGetYikeAssetMediaInfosResponseBodyMediaInfosMediaBasicInfo()
            self.media_basic_info = temp_model.from_map(m.get('MediaBasicInfo'))

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        return self

class BatchGetYikeAssetMediaInfosResponseBodyMediaInfosMediaBasicInfo(DaraModel):
    def __init__(
        self,
        biz: str = None,
        business_type: str = None,
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
        snapshots: str = None,
        source: str = None,
        sprite_images: str = None,
        status: str = None,
        title: str = None,
        transcode_status: str = None,
        user_data: str = None,
    ):
        self.biz = biz
        self.business_type = business_type
        self.category = category
        self.cover_url = cover_url
        self.create_time = create_time
        self.deleted_time = deleted_time
        self.description = description
        self.input_url = input_url
        # MediaId
        self.media_id = media_id
        self.media_tags = media_tags
        self.media_type = media_type
        self.modified_time = modified_time
        self.snapshots = snapshots
        self.source = source
        self.sprite_images = sprite_images
        self.status = status
        self.title = title
        self.transcode_status = transcode_status
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

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Biz') is not None:
            self.biz = m.get('Biz')

        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')

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

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class BatchGetYikeAssetMediaInfosResponseBodyMediaInfosFileInfoList(DaraModel):
    def __init__(
        self,
        file_basic_info: main_models.BatchGetYikeAssetMediaInfosResponseBodyMediaInfosFileInfoListFileBasicInfo = None,
    ):
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
            temp_model = main_models.BatchGetYikeAssetMediaInfosResponseBodyMediaInfosFileInfoListFileBasicInfo()
            self.file_basic_info = temp_model.from_map(m.get('FileBasicInfo'))

        return self

class BatchGetYikeAssetMediaInfosResponseBodyMediaInfosFileInfoListFileBasicInfo(DaraModel):
    def __init__(
        self,
        bitrate: str = None,
        duration: str = None,
        file_name: str = None,
        file_size: str = None,
        file_status: str = None,
        file_type: str = None,
        file_url: str = None,
        format_name: str = None,
        height: str = None,
        region: str = None,
        width: str = None,
    ):
        self.bitrate = bitrate
        self.duration = duration
        self.file_name = file_name
        self.file_size = file_size
        self.file_status = file_status
        self.file_type = file_type
        self.file_url = file_url
        self.format_name = format_name
        self.height = height
        self.region = region
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

        if self.region is not None:
            result['Region'] = self.region

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')

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

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

class BatchGetYikeAssetMediaInfosResponseBodyMediaInfosBizData(DaraModel):
    def __init__(
        self,
        audit_blocked_label: str = None,
        audit_status: str = None,
        creation_job_id: str = None,
        folder_id: str = None,
        is_favorite: str = None,
        is_logical_deleted: str = None,
        media_asset_sub_type: str = None,
        media_asset_type: str = None,
        production_id: str = None,
        source_id: str = None,
        source_name: str = None,
        source_type: str = None,
    ):
        self.audit_blocked_label = audit_blocked_label
        self.audit_status = audit_status
        self.creation_job_id = creation_job_id
        self.folder_id = folder_id
        self.is_favorite = is_favorite
        self.is_logical_deleted = is_logical_deleted
        self.media_asset_sub_type = media_asset_sub_type
        self.media_asset_type = media_asset_type
        self.production_id = production_id
        self.source_id = source_id
        self.source_name = source_name
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audit_blocked_label is not None:
            result['AuditBlockedLabel'] = self.audit_blocked_label

        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status

        if self.creation_job_id is not None:
            result['CreationJobId'] = self.creation_job_id

        if self.folder_id is not None:
            result['FolderId'] = self.folder_id

        if self.is_favorite is not None:
            result['IsFavorite'] = self.is_favorite

        if self.is_logical_deleted is not None:
            result['IsLogicalDeleted'] = self.is_logical_deleted

        if self.media_asset_sub_type is not None:
            result['MediaAssetSubType'] = self.media_asset_sub_type

        if self.media_asset_type is not None:
            result['MediaAssetType'] = self.media_asset_type

        if self.production_id is not None:
            result['ProductionId'] = self.production_id

        if self.source_id is not None:
            result['SourceId'] = self.source_id

        if self.source_name is not None:
            result['SourceName'] = self.source_name

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditBlockedLabel') is not None:
            self.audit_blocked_label = m.get('AuditBlockedLabel')

        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')

        if m.get('CreationJobId') is not None:
            self.creation_job_id = m.get('CreationJobId')

        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')

        if m.get('IsFavorite') is not None:
            self.is_favorite = m.get('IsFavorite')

        if m.get('IsLogicalDeleted') is not None:
            self.is_logical_deleted = m.get('IsLogicalDeleted')

        if m.get('MediaAssetSubType') is not None:
            self.media_asset_sub_type = m.get('MediaAssetSubType')

        if m.get('MediaAssetType') is not None:
            self.media_asset_type = m.get('MediaAssetType')

        if m.get('ProductionId') is not None:
            self.production_id = m.get('ProductionId')

        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')

        if m.get('SourceName') is not None:
            self.source_name = m.get('SourceName')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        return self

