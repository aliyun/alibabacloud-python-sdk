# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class SearchMediaByAILabelResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        media_list: List[main_models.SearchMediaByAILabelResponseBodyMediaList] = None,
        request_id: str = None,
        success: str = None,
        total: int = None,
    ):
        # The status code returned.
        self.code = code
        # The media assets that contain the specified content.
        self.media_list = media_list
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success
        # The total number of audio and video files that meet the conditions.
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
        if self.code is not None:
            result['Code'] = self.code

        result['MediaList'] = []
        if self.media_list is not None:
            for k1 in self.media_list:
                result['MediaList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.media_list = []
        if m.get('MediaList') is not None:
            for k1 in m.get('MediaList'):
                temp_model = main_models.SearchMediaByAILabelResponseBodyMediaList()
                self.media_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class SearchMediaByAILabelResponseBodyMediaList(DaraModel):
    def __init__(
        self,
        ai_data: main_models.SearchMediaByAILabelResponseBodyMediaListAiData = None,
        app_id: str = None,
        cover_url: str = None,
        creation_time: str = None,
        description: str = None,
        duration: float = None,
        media_id: str = None,
        modification_time: str = None,
        size: int = None,
        snapshots: List[str] = None,
        status: str = None,
        storage_location: str = None,
        tags: str = None,
        title: str = None,
    ):
        # The details of the AI job.
        self.ai_data = ai_data
        # The ID of the application. Default value: app-1000000.
        self.app_id = app_id
        # The URL of the thumbnail.
        self.cover_url = cover_url
        # The time when the media asset was created. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The description of the media asset.
        self.description = description
        # The duration. Unit: seconds.
        self.duration = duration
        # The ID of the media asset.
        self.media_id = media_id
        # The time when the media asset was updated. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.modification_time = modification_time
        # The size of the source file. Unit: bytes.
        self.size = size
        # The array of video snapshot URLs.
        self.snapshots = snapshots
        # The status of the video.
        # 
        # Valid values:
        # 
        # *   PrepareFail
        # *   UploadFail
        # *   Init
        # *   UploadSucc
        # *   Transcoding
        # *   TranscodeFail
        # *   Deleted
        # *   Normal
        # *   Uploading
        # *   Preparing
        # *   Blocked
        # *   Checking
        self.status = status
        # The storage address.
        self.storage_location = storage_location
        # The tags of the media asset.
        self.tags = tags
        # The title of the media asset.
        self.title = title

    def validate(self):
        if self.ai_data:
            self.ai_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ai_data is not None:
            result['AiData'] = self.ai_data.to_map()

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.modification_time is not None:
            result['ModificationTime'] = self.modification_time

        if self.size is not None:
            result['Size'] = self.size

        if self.snapshots is not None:
            result['Snapshots'] = self.snapshots

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AiData') is not None:
            temp_model = main_models.SearchMediaByAILabelResponseBodyMediaListAiData()
            self.ai_data = temp_model.from_map(m.get('AiData'))

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('ModificationTime') is not None:
            self.modification_time = m.get('ModificationTime')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Snapshots') is not None:
            self.snapshots = m.get('Snapshots')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

class SearchMediaByAILabelResponseBodyMediaListAiData(DaraModel):
    def __init__(
        self,
        ai_label_info: List[main_models.SearchMediaByAILabelResponseBodyMediaListAiDataAiLabelInfo] = None,
        asr_info: List[main_models.SearchMediaByAILabelResponseBodyMediaListAiDataAsrInfo] = None,
        ocr_info: List[main_models.SearchMediaByAILabelResponseBodyMediaListAiDataOcrInfo] = None,
    ):
        # The tags of the AI job.
        self.ai_label_info = ai_label_info
        # The information about audio files.
        self.asr_info = asr_info
        # The information about subtitle files.
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
                temp_model = main_models.SearchMediaByAILabelResponseBodyMediaListAiDataAiLabelInfo()
                self.ai_label_info.append(temp_model.from_map(k1))

        self.asr_info = []
        if m.get('AsrInfo') is not None:
            for k1 in m.get('AsrInfo'):
                temp_model = main_models.SearchMediaByAILabelResponseBodyMediaListAiDataAsrInfo()
                self.asr_info.append(temp_model.from_map(k1))

        self.ocr_info = []
        if m.get('OcrInfo') is not None:
            for k1 in m.get('OcrInfo'):
                temp_model = main_models.SearchMediaByAILabelResponseBodyMediaListAiDataOcrInfo()
                self.ocr_info.append(temp_model.from_map(k1))

        return self

class SearchMediaByAILabelResponseBodyMediaListAiDataOcrInfo(DaraModel):
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
        # The content of the text.
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

class SearchMediaByAILabelResponseBodyMediaListAiDataAsrInfo(DaraModel):
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
        # The content of the audio.
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

class SearchMediaByAILabelResponseBodyMediaListAiDataAiLabelInfo(DaraModel):
    def __init__(
        self,
        category: str = None,
        face_id: str = None,
        label_id: str = None,
        label_name: str = None,
        label_type: str = None,
        occurrences: List[main_models.SearchMediaByAILabelResponseBodyMediaListAiDataAiLabelInfoOccurrences] = None,
        source: str = None,
    ):
        # The category.
        self.category = category
        # The ID of the face.
        self.face_id = face_id
        # The ID of the entity.
        self.label_id = label_id
        # The name of the entity.
        self.label_name = label_name
        # The type of the tag.
        self.label_type = label_type
        # The information about the clips.
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
                temp_model = main_models.SearchMediaByAILabelResponseBodyMediaListAiDataAiLabelInfoOccurrences()
                self.occurrences.append(temp_model.from_map(k1))

        if m.get('Source') is not None:
            self.source = m.get('Source')

        return self

class SearchMediaByAILabelResponseBodyMediaListAiDataAiLabelInfoOccurrences(DaraModel):
    def __init__(
        self,
        clip_id: str = None,
        content: str = None,
        finegrain_id: str = None,
        finegrain_name: str = None,
        from_: float = None,
        image: str = None,
        score: float = None,
        table_batch_seq_id: str = None,
        to: float = None,
        tracks: List[main_models.SearchMediaByAILabelResponseBodyMediaListAiDataAiLabelInfoOccurrencesTracks] = None,
    ):
        # The ID of the clip.
        self.clip_id = clip_id
        # The content of the text.
        self.content = content
        # The fine-grained ID of the entity.
        self.finegrain_id = finegrain_id
        # The fine-grained name of the entity.
        self.finegrain_name = finegrain_name
        # The start time of the clip.
        self.from_ = from_
        # The image that contains the most face information.
        self.image = image
        # The score.
        self.score = score
        # The sequence ID of the vector table.
        self.table_batch_seq_id = table_batch_seq_id
        # The end time of the clip.
        self.to = to
        # The tracks.
        self.tracks = tracks

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
        if self.clip_id is not None:
            result['ClipId'] = self.clip_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClipId') is not None:
            self.clip_id = m.get('ClipId')

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
                temp_model = main_models.SearchMediaByAILabelResponseBodyMediaListAiDataAiLabelInfoOccurrencesTracks()
                self.tracks.append(temp_model.from_map(k1))

        return self

class SearchMediaByAILabelResponseBodyMediaListAiDataAiLabelInfoOccurrencesTracks(DaraModel):
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

