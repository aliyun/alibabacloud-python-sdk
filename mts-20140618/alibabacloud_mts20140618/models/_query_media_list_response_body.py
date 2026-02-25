# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mts20140618 import models as main_models
from darabonba.model import DaraModel

class QueryMediaListResponseBody(DaraModel):
    def __init__(
        self,
        media_list: main_models.QueryMediaListResponseBodyMediaList = None,
        non_exist_media_ids: main_models.QueryMediaListResponseBodyNonExistMediaIds = None,
        request_id: str = None,
    ):
        self.media_list = media_list
        self.non_exist_media_ids = non_exist_media_ids
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.media_list:
            self.media_list.validate()
        if self.non_exist_media_ids:
            self.non_exist_media_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media_list is not None:
            result['MediaList'] = self.media_list.to_map()

        if self.non_exist_media_ids is not None:
            result['NonExistMediaIds'] = self.non_exist_media_ids.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaList') is not None:
            temp_model = main_models.QueryMediaListResponseBodyMediaList()
            self.media_list = temp_model.from_map(m.get('MediaList'))

        if m.get('NonExistMediaIds') is not None:
            temp_model = main_models.QueryMediaListResponseBodyNonExistMediaIds()
            self.non_exist_media_ids = temp_model.from_map(m.get('NonExistMediaIds'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryMediaListResponseBodyNonExistMediaIds(DaraModel):
    def __init__(
        self,
        media_id: List[str] = None,
    ):
        self.media_id = media_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media_id is not None:
            result['MediaId'] = self.media_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        return self

class QueryMediaListResponseBodyMediaList(DaraModel):
    def __init__(
        self,
        media: List[main_models.QueryMediaListResponseBodyMediaListMedia] = None,
    ):
        self.media = media

    def validate(self):
        if self.media:
            for v1 in self.media:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Media'] = []
        if self.media is not None:
            for k1 in self.media:
                result['Media'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.media = []
        if m.get('Media') is not None:
            for k1 in m.get('Media'):
                temp_model = main_models.QueryMediaListResponseBodyMediaListMedia()
                self.media.append(temp_model.from_map(k1))

        return self

class QueryMediaListResponseBodyMediaListMedia(DaraModel):
    def __init__(
        self,
        bitrate: str = None,
        cate_id: int = None,
        censor_state: str = None,
        cover_url: str = None,
        creation_time: str = None,
        description: str = None,
        duration: str = None,
        file: main_models.QueryMediaListResponseBodyMediaListMediaFile = None,
        format: str = None,
        fps: str = None,
        height: str = None,
        media_id: str = None,
        media_info: main_models.QueryMediaListResponseBodyMediaListMediaMediaInfo = None,
        play_list: main_models.QueryMediaListResponseBodyMediaListMediaPlayList = None,
        publish_state: str = None,
        run_id_list: main_models.QueryMediaListResponseBodyMediaListMediaRunIdList = None,
        size: str = None,
        snapshot_list: main_models.QueryMediaListResponseBodyMediaListMediaSnapshotList = None,
        summary_list: main_models.QueryMediaListResponseBodyMediaListMediaSummaryList = None,
        tags: main_models.QueryMediaListResponseBodyMediaListMediaTags = None,
        title: str = None,
        width: str = None,
    ):
        self.bitrate = bitrate
        self.cate_id = cate_id
        self.censor_state = censor_state
        self.cover_url = cover_url
        self.creation_time = creation_time
        self.description = description
        self.duration = duration
        self.file = file
        self.format = format
        self.fps = fps
        self.height = height
        self.media_id = media_id
        self.media_info = media_info
        self.play_list = play_list
        self.publish_state = publish_state
        self.run_id_list = run_id_list
        self.size = size
        self.snapshot_list = snapshot_list
        self.summary_list = summary_list
        self.tags = tags
        self.title = title
        self.width = width

    def validate(self):
        if self.file:
            self.file.validate()
        if self.media_info:
            self.media_info.validate()
        if self.play_list:
            self.play_list.validate()
        if self.run_id_list:
            self.run_id_list.validate()
        if self.snapshot_list:
            self.snapshot_list.validate()
        if self.summary_list:
            self.summary_list.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate

        if self.cate_id is not None:
            result['CateId'] = self.cate_id

        if self.censor_state is not None:
            result['CensorState'] = self.censor_state

        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.file is not None:
            result['File'] = self.file.to_map()

        if self.format is not None:
            result['Format'] = self.format

        if self.fps is not None:
            result['Fps'] = self.fps

        if self.height is not None:
            result['Height'] = self.height

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.media_info is not None:
            result['MediaInfo'] = self.media_info.to_map()

        if self.play_list is not None:
            result['PlayList'] = self.play_list.to_map()

        if self.publish_state is not None:
            result['PublishState'] = self.publish_state

        if self.run_id_list is not None:
            result['RunIdList'] = self.run_id_list.to_map()

        if self.size is not None:
            result['Size'] = self.size

        if self.snapshot_list is not None:
            result['SnapshotList'] = self.snapshot_list.to_map()

        if self.summary_list is not None:
            result['SummaryList'] = self.summary_list.to_map()

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.title is not None:
            result['Title'] = self.title

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')

        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')

        if m.get('CensorState') is not None:
            self.censor_state = m.get('CensorState')

        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('File') is not None:
            temp_model = main_models.QueryMediaListResponseBodyMediaListMediaFile()
            self.file = temp_model.from_map(m.get('File'))

        if m.get('Format') is not None:
            self.format = m.get('Format')

        if m.get('Fps') is not None:
            self.fps = m.get('Fps')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('MediaInfo') is not None:
            temp_model = main_models.QueryMediaListResponseBodyMediaListMediaMediaInfo()
            self.media_info = temp_model.from_map(m.get('MediaInfo'))

        if m.get('PlayList') is not None:
            temp_model = main_models.QueryMediaListResponseBodyMediaListMediaPlayList()
            self.play_list = temp_model.from_map(m.get('PlayList'))

        if m.get('PublishState') is not None:
            self.publish_state = m.get('PublishState')

        if m.get('RunIdList') is not None:
            temp_model = main_models.QueryMediaListResponseBodyMediaListMediaRunIdList()
            self.run_id_list = temp_model.from_map(m.get('RunIdList'))

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('SnapshotList') is not None:
            temp_model = main_models.QueryMediaListResponseBodyMediaListMediaSnapshotList()
            self.snapshot_list = temp_model.from_map(m.get('SnapshotList'))

        if m.get('SummaryList') is not None:
            temp_model = main_models.QueryMediaListResponseBodyMediaListMediaSummaryList()
            self.summary_list = temp_model.from_map(m.get('SummaryList'))

        if m.get('Tags') is not None:
            temp_model = main_models.QueryMediaListResponseBodyMediaListMediaTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

class QueryMediaListResponseBodyMediaListMediaTags(DaraModel):
    def __init__(
        self,
        tag: List[str] = None,
    ):
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag is not None:
            result['Tag'] = self.tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        return self

class QueryMediaListResponseBodyMediaListMediaSummaryList(DaraModel):
    def __init__(
        self,
        summary: List[main_models.QueryMediaListResponseBodyMediaListMediaSummaryListSummary] = None,
    ):
        self.summary = summary

    def validate(self):
        if self.summary:
            for v1 in self.summary:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Summary'] = []
        if self.summary is not None:
            for k1 in self.summary:
                result['Summary'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.summary = []
        if m.get('Summary') is not None:
            for k1 in m.get('Summary'):
                temp_model = main_models.QueryMediaListResponseBodyMediaListMediaSummaryListSummary()
                self.summary.append(temp_model.from_map(k1))

        return self

class QueryMediaListResponseBodyMediaListMediaSummaryListSummary(DaraModel):
    def __init__(
        self,
        activity_name: str = None,
        file: main_models.QueryMediaListResponseBodyMediaListMediaSummaryListSummaryFile = None,
        media_workflow_id: str = None,
        media_workflow_name: str = None,
        type: str = None,
    ):
        self.activity_name = activity_name
        self.file = file
        self.media_workflow_id = media_workflow_id
        self.media_workflow_name = media_workflow_name
        self.type = type

    def validate(self):
        if self.file:
            self.file.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activity_name is not None:
            result['ActivityName'] = self.activity_name

        if self.file is not None:
            result['File'] = self.file.to_map()

        if self.media_workflow_id is not None:
            result['MediaWorkflowId'] = self.media_workflow_id

        if self.media_workflow_name is not None:
            result['MediaWorkflowName'] = self.media_workflow_name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityName') is not None:
            self.activity_name = m.get('ActivityName')

        if m.get('File') is not None:
            temp_model = main_models.QueryMediaListResponseBodyMediaListMediaSummaryListSummaryFile()
            self.file = temp_model.from_map(m.get('File'))

        if m.get('MediaWorkflowId') is not None:
            self.media_workflow_id = m.get('MediaWorkflowId')

        if m.get('MediaWorkflowName') is not None:
            self.media_workflow_name = m.get('MediaWorkflowName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class QueryMediaListResponseBodyMediaListMediaSummaryListSummaryFile(DaraModel):
    def __init__(
        self,
        state: str = None,
        url: str = None,
    ):
        self.state = state
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.state is not None:
            result['State'] = self.state

        if self.url is not None:
            result['URL'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('URL') is not None:
            self.url = m.get('URL')

        return self

class QueryMediaListResponseBodyMediaListMediaSnapshotList(DaraModel):
    def __init__(
        self,
        snapshot: List[main_models.QueryMediaListResponseBodyMediaListMediaSnapshotListSnapshot] = None,
    ):
        self.snapshot = snapshot

    def validate(self):
        if self.snapshot:
            for v1 in self.snapshot:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Snapshot'] = []
        if self.snapshot is not None:
            for k1 in self.snapshot:
                result['Snapshot'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.snapshot = []
        if m.get('Snapshot') is not None:
            for k1 in m.get('Snapshot'):
                temp_model = main_models.QueryMediaListResponseBodyMediaListMediaSnapshotListSnapshot()
                self.snapshot.append(temp_model.from_map(k1))

        return self

class QueryMediaListResponseBodyMediaListMediaSnapshotListSnapshot(DaraModel):
    def __init__(
        self,
        activity_name: str = None,
        count: str = None,
        file: main_models.QueryMediaListResponseBodyMediaListMediaSnapshotListSnapshotFile = None,
        media_workflow_id: str = None,
        media_workflow_name: str = None,
        type: str = None,
    ):
        self.activity_name = activity_name
        self.count = count
        self.file = file
        self.media_workflow_id = media_workflow_id
        self.media_workflow_name = media_workflow_name
        self.type = type

    def validate(self):
        if self.file:
            self.file.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activity_name is not None:
            result['ActivityName'] = self.activity_name

        if self.count is not None:
            result['Count'] = self.count

        if self.file is not None:
            result['File'] = self.file.to_map()

        if self.media_workflow_id is not None:
            result['MediaWorkflowId'] = self.media_workflow_id

        if self.media_workflow_name is not None:
            result['MediaWorkflowName'] = self.media_workflow_name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityName') is not None:
            self.activity_name = m.get('ActivityName')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('File') is not None:
            temp_model = main_models.QueryMediaListResponseBodyMediaListMediaSnapshotListSnapshotFile()
            self.file = temp_model.from_map(m.get('File'))

        if m.get('MediaWorkflowId') is not None:
            self.media_workflow_id = m.get('MediaWorkflowId')

        if m.get('MediaWorkflowName') is not None:
            self.media_workflow_name = m.get('MediaWorkflowName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class QueryMediaListResponseBodyMediaListMediaSnapshotListSnapshotFile(DaraModel):
    def __init__(
        self,
        state: str = None,
        url: str = None,
    ):
        self.state = state
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.state is not None:
            result['State'] = self.state

        if self.url is not None:
            result['URL'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('URL') is not None:
            self.url = m.get('URL')

        return self

class QueryMediaListResponseBodyMediaListMediaRunIdList(DaraModel):
    def __init__(
        self,
        run_id: List[str] = None,
    ):
        self.run_id = run_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.run_id is not None:
            result['RunId'] = self.run_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RunId') is not None:
            self.run_id = m.get('RunId')

        return self

class QueryMediaListResponseBodyMediaListMediaPlayList(DaraModel):
    def __init__(
        self,
        play: List[main_models.QueryMediaListResponseBodyMediaListMediaPlayListPlay] = None,
    ):
        self.play = play

    def validate(self):
        if self.play:
            for v1 in self.play:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Play'] = []
        if self.play is not None:
            for k1 in self.play:
                result['Play'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.play = []
        if m.get('Play') is not None:
            for k1 in m.get('Play'):
                temp_model = main_models.QueryMediaListResponseBodyMediaListMediaPlayListPlay()
                self.play.append(temp_model.from_map(k1))

        return self

class QueryMediaListResponseBodyMediaListMediaPlayListPlay(DaraModel):
    def __init__(
        self,
        activity_name: str = None,
        bitrate: str = None,
        duration: str = None,
        encryption: str = None,
        file: main_models.QueryMediaListResponseBodyMediaListMediaPlayListPlayFile = None,
        format: str = None,
        fps: str = None,
        height: str = None,
        media_workflow_id: str = None,
        media_workflow_name: str = None,
        size: str = None,
        width: str = None,
    ):
        self.activity_name = activity_name
        self.bitrate = bitrate
        self.duration = duration
        self.encryption = encryption
        self.file = file
        self.format = format
        self.fps = fps
        self.height = height
        self.media_workflow_id = media_workflow_id
        self.media_workflow_name = media_workflow_name
        self.size = size
        self.width = width

    def validate(self):
        if self.file:
            self.file.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activity_name is not None:
            result['ActivityName'] = self.activity_name

        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.encryption is not None:
            result['Encryption'] = self.encryption

        if self.file is not None:
            result['File'] = self.file.to_map()

        if self.format is not None:
            result['Format'] = self.format

        if self.fps is not None:
            result['Fps'] = self.fps

        if self.height is not None:
            result['Height'] = self.height

        if self.media_workflow_id is not None:
            result['MediaWorkflowId'] = self.media_workflow_id

        if self.media_workflow_name is not None:
            result['MediaWorkflowName'] = self.media_workflow_name

        if self.size is not None:
            result['Size'] = self.size

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityName') is not None:
            self.activity_name = m.get('ActivityName')

        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Encryption') is not None:
            self.encryption = m.get('Encryption')

        if m.get('File') is not None:
            temp_model = main_models.QueryMediaListResponseBodyMediaListMediaPlayListPlayFile()
            self.file = temp_model.from_map(m.get('File'))

        if m.get('Format') is not None:
            self.format = m.get('Format')

        if m.get('Fps') is not None:
            self.fps = m.get('Fps')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('MediaWorkflowId') is not None:
            self.media_workflow_id = m.get('MediaWorkflowId')

        if m.get('MediaWorkflowName') is not None:
            self.media_workflow_name = m.get('MediaWorkflowName')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

class QueryMediaListResponseBodyMediaListMediaPlayListPlayFile(DaraModel):
    def __init__(
        self,
        state: str = None,
        url: str = None,
    ):
        self.state = state
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.state is not None:
            result['State'] = self.state

        if self.url is not None:
            result['URL'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('URL') is not None:
            self.url = m.get('URL')

        return self

class QueryMediaListResponseBodyMediaListMediaMediaInfo(DaraModel):
    def __init__(
        self,
        format: main_models.QueryMediaListResponseBodyMediaListMediaMediaInfoFormat = None,
        streams: main_models.QueryMediaListResponseBodyMediaListMediaMediaInfoStreams = None,
    ):
        self.format = format
        self.streams = streams

    def validate(self):
        if self.format:
            self.format.validate()
        if self.streams:
            self.streams.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.format is not None:
            result['Format'] = self.format.to_map()

        if self.streams is not None:
            result['Streams'] = self.streams.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Format') is not None:
            temp_model = main_models.QueryMediaListResponseBodyMediaListMediaMediaInfoFormat()
            self.format = temp_model.from_map(m.get('Format'))

        if m.get('Streams') is not None:
            temp_model = main_models.QueryMediaListResponseBodyMediaListMediaMediaInfoStreams()
            self.streams = temp_model.from_map(m.get('Streams'))

        return self

class QueryMediaListResponseBodyMediaListMediaMediaInfoStreams(DaraModel):
    def __init__(
        self,
        audio_stream_list: main_models.QueryMediaListResponseBodyMediaListMediaMediaInfoStreamsAudioStreamList = None,
        subtitle_stream_list: main_models.QueryMediaListResponseBodyMediaListMediaMediaInfoStreamsSubtitleStreamList = None,
        video_stream_list: main_models.QueryMediaListResponseBodyMediaListMediaMediaInfoStreamsVideoStreamList = None,
    ):
        self.audio_stream_list = audio_stream_list
        self.subtitle_stream_list = subtitle_stream_list
        self.video_stream_list = video_stream_list

    def validate(self):
        if self.audio_stream_list:
            self.audio_stream_list.validate()
        if self.subtitle_stream_list:
            self.subtitle_stream_list.validate()
        if self.video_stream_list:
            self.video_stream_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio_stream_list is not None:
            result['AudioStreamList'] = self.audio_stream_list.to_map()

        if self.subtitle_stream_list is not None:
            result['SubtitleStreamList'] = self.subtitle_stream_list.to_map()

        if self.video_stream_list is not None:
            result['VideoStreamList'] = self.video_stream_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioStreamList') is not None:
            temp_model = main_models.QueryMediaListResponseBodyMediaListMediaMediaInfoStreamsAudioStreamList()
            self.audio_stream_list = temp_model.from_map(m.get('AudioStreamList'))

        if m.get('SubtitleStreamList') is not None:
            temp_model = main_models.QueryMediaListResponseBodyMediaListMediaMediaInfoStreamsSubtitleStreamList()
            self.subtitle_stream_list = temp_model.from_map(m.get('SubtitleStreamList'))

        if m.get('VideoStreamList') is not None:
            temp_model = main_models.QueryMediaListResponseBodyMediaListMediaMediaInfoStreamsVideoStreamList()
            self.video_stream_list = temp_model.from_map(m.get('VideoStreamList'))

        return self

class QueryMediaListResponseBodyMediaListMediaMediaInfoStreamsVideoStreamList(DaraModel):
    def __init__(
        self,
        video_stream: List[main_models.QueryMediaListResponseBodyMediaListMediaMediaInfoStreamsVideoStreamListVideoStream] = None,
    ):
        self.video_stream = video_stream

    def validate(self):
        if self.video_stream:
            for v1 in self.video_stream:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['VideoStream'] = []
        if self.video_stream is not None:
            for k1 in self.video_stream:
                result['VideoStream'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.video_stream = []
        if m.get('VideoStream') is not None:
            for k1 in m.get('VideoStream'):
                temp_model = main_models.QueryMediaListResponseBodyMediaListMediaMediaInfoStreamsVideoStreamListVideoStream()
                self.video_stream.append(temp_model.from_map(k1))

        return self

class QueryMediaListResponseBodyMediaListMediaMediaInfoStreamsVideoStreamListVideoStream(DaraModel):
    def __init__(
        self,
        avg_fps: str = None,
        bitrate: str = None,
        codec_long_name: str = None,
        codec_name: str = None,
        codec_tag: str = None,
        codec_tag_string: str = None,
        codec_time_base: str = None,
        dar: str = None,
        duration: str = None,
        fps: str = None,
        has_bframes: str = None,
        height: str = None,
        index: str = None,
        lang: str = None,
        level: str = None,
        network_cost: main_models.QueryMediaListResponseBodyMediaListMediaMediaInfoStreamsVideoStreamListVideoStreamNetworkCost = None,
        num_frames: str = None,
        pix_fmt: str = None,
        profile: str = None,
        rotate: str = None,
        sar: str = None,
        start_time: str = None,
        timebase: str = None,
        width: str = None,
    ):
        self.avg_fps = avg_fps
        self.bitrate = bitrate
        self.codec_long_name = codec_long_name
        self.codec_name = codec_name
        self.codec_tag = codec_tag
        self.codec_tag_string = codec_tag_string
        self.codec_time_base = codec_time_base
        self.dar = dar
        self.duration = duration
        self.fps = fps
        self.has_bframes = has_bframes
        self.height = height
        self.index = index
        self.lang = lang
        self.level = level
        self.network_cost = network_cost
        self.num_frames = num_frames
        self.pix_fmt = pix_fmt
        self.profile = profile
        self.rotate = rotate
        self.sar = sar
        self.start_time = start_time
        self.timebase = timebase
        self.width = width

    def validate(self):
        if self.network_cost:
            self.network_cost.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avg_fps is not None:
            result['AvgFPS'] = self.avg_fps

        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate

        if self.codec_long_name is not None:
            result['CodecLongName'] = self.codec_long_name

        if self.codec_name is not None:
            result['CodecName'] = self.codec_name

        if self.codec_tag is not None:
            result['CodecTag'] = self.codec_tag

        if self.codec_tag_string is not None:
            result['CodecTagString'] = self.codec_tag_string

        if self.codec_time_base is not None:
            result['CodecTimeBase'] = self.codec_time_base

        if self.dar is not None:
            result['Dar'] = self.dar

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.fps is not None:
            result['Fps'] = self.fps

        if self.has_bframes is not None:
            result['HasBFrames'] = self.has_bframes

        if self.height is not None:
            result['Height'] = self.height

        if self.index is not None:
            result['Index'] = self.index

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.level is not None:
            result['Level'] = self.level

        if self.network_cost is not None:
            result['NetworkCost'] = self.network_cost.to_map()

        if self.num_frames is not None:
            result['NumFrames'] = self.num_frames

        if self.pix_fmt is not None:
            result['PixFmt'] = self.pix_fmt

        if self.profile is not None:
            result['Profile'] = self.profile

        if self.rotate is not None:
            result['Rotate'] = self.rotate

        if self.sar is not None:
            result['Sar'] = self.sar

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.timebase is not None:
            result['Timebase'] = self.timebase

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvgFPS') is not None:
            self.avg_fps = m.get('AvgFPS')

        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')

        if m.get('CodecLongName') is not None:
            self.codec_long_name = m.get('CodecLongName')

        if m.get('CodecName') is not None:
            self.codec_name = m.get('CodecName')

        if m.get('CodecTag') is not None:
            self.codec_tag = m.get('CodecTag')

        if m.get('CodecTagString') is not None:
            self.codec_tag_string = m.get('CodecTagString')

        if m.get('CodecTimeBase') is not None:
            self.codec_time_base = m.get('CodecTimeBase')

        if m.get('Dar') is not None:
            self.dar = m.get('Dar')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Fps') is not None:
            self.fps = m.get('Fps')

        if m.get('HasBFrames') is not None:
            self.has_bframes = m.get('HasBFrames')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('NetworkCost') is not None:
            temp_model = main_models.QueryMediaListResponseBodyMediaListMediaMediaInfoStreamsVideoStreamListVideoStreamNetworkCost()
            self.network_cost = temp_model.from_map(m.get('NetworkCost'))

        if m.get('NumFrames') is not None:
            self.num_frames = m.get('NumFrames')

        if m.get('PixFmt') is not None:
            self.pix_fmt = m.get('PixFmt')

        if m.get('Profile') is not None:
            self.profile = m.get('Profile')

        if m.get('Rotate') is not None:
            self.rotate = m.get('Rotate')

        if m.get('Sar') is not None:
            self.sar = m.get('Sar')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Timebase') is not None:
            self.timebase = m.get('Timebase')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

class QueryMediaListResponseBodyMediaListMediaMediaInfoStreamsVideoStreamListVideoStreamNetworkCost(DaraModel):
    def __init__(
        self,
        avg_bitrate: str = None,
        cost_bandwidth: str = None,
        preload_time: str = None,
    ):
        self.avg_bitrate = avg_bitrate
        self.cost_bandwidth = cost_bandwidth
        self.preload_time = preload_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avg_bitrate is not None:
            result['AvgBitrate'] = self.avg_bitrate

        if self.cost_bandwidth is not None:
            result['CostBandwidth'] = self.cost_bandwidth

        if self.preload_time is not None:
            result['PreloadTime'] = self.preload_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvgBitrate') is not None:
            self.avg_bitrate = m.get('AvgBitrate')

        if m.get('CostBandwidth') is not None:
            self.cost_bandwidth = m.get('CostBandwidth')

        if m.get('PreloadTime') is not None:
            self.preload_time = m.get('PreloadTime')

        return self

class QueryMediaListResponseBodyMediaListMediaMediaInfoStreamsSubtitleStreamList(DaraModel):
    def __init__(
        self,
        subtitle_stream: List[main_models.QueryMediaListResponseBodyMediaListMediaMediaInfoStreamsSubtitleStreamListSubtitleStream] = None,
    ):
        self.subtitle_stream = subtitle_stream

    def validate(self):
        if self.subtitle_stream:
            for v1 in self.subtitle_stream:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SubtitleStream'] = []
        if self.subtitle_stream is not None:
            for k1 in self.subtitle_stream:
                result['SubtitleStream'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.subtitle_stream = []
        if m.get('SubtitleStream') is not None:
            for k1 in m.get('SubtitleStream'):
                temp_model = main_models.QueryMediaListResponseBodyMediaListMediaMediaInfoStreamsSubtitleStreamListSubtitleStream()
                self.subtitle_stream.append(temp_model.from_map(k1))

        return self

class QueryMediaListResponseBodyMediaListMediaMediaInfoStreamsSubtitleStreamListSubtitleStream(DaraModel):
    def __init__(
        self,
        index: str = None,
        lang: str = None,
    ):
        self.index = index
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.index is not None:
            result['Index'] = self.index

        if self.lang is not None:
            result['Lang'] = self.lang

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        return self

class QueryMediaListResponseBodyMediaListMediaMediaInfoStreamsAudioStreamList(DaraModel):
    def __init__(
        self,
        audio_stream: List[main_models.QueryMediaListResponseBodyMediaListMediaMediaInfoStreamsAudioStreamListAudioStream] = None,
    ):
        self.audio_stream = audio_stream

    def validate(self):
        if self.audio_stream:
            for v1 in self.audio_stream:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AudioStream'] = []
        if self.audio_stream is not None:
            for k1 in self.audio_stream:
                result['AudioStream'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.audio_stream = []
        if m.get('AudioStream') is not None:
            for k1 in m.get('AudioStream'):
                temp_model = main_models.QueryMediaListResponseBodyMediaListMediaMediaInfoStreamsAudioStreamListAudioStream()
                self.audio_stream.append(temp_model.from_map(k1))

        return self

class QueryMediaListResponseBodyMediaListMediaMediaInfoStreamsAudioStreamListAudioStream(DaraModel):
    def __init__(
        self,
        bitrate: str = None,
        channel_layout: str = None,
        channels: str = None,
        codec_long_name: str = None,
        codec_name: str = None,
        codec_tag: str = None,
        codec_tag_string: str = None,
        codec_time_base: str = None,
        duration: str = None,
        index: str = None,
        lang: str = None,
        num_frames: str = None,
        sample_fmt: str = None,
        samplerate: str = None,
        start_time: str = None,
        timebase: str = None,
    ):
        self.bitrate = bitrate
        self.channel_layout = channel_layout
        self.channels = channels
        self.codec_long_name = codec_long_name
        self.codec_name = codec_name
        self.codec_tag = codec_tag
        self.codec_tag_string = codec_tag_string
        self.codec_time_base = codec_time_base
        self.duration = duration
        self.index = index
        self.lang = lang
        self.num_frames = num_frames
        self.sample_fmt = sample_fmt
        self.samplerate = samplerate
        self.start_time = start_time
        self.timebase = timebase

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate

        if self.channel_layout is not None:
            result['ChannelLayout'] = self.channel_layout

        if self.channels is not None:
            result['Channels'] = self.channels

        if self.codec_long_name is not None:
            result['CodecLongName'] = self.codec_long_name

        if self.codec_name is not None:
            result['CodecName'] = self.codec_name

        if self.codec_tag is not None:
            result['CodecTag'] = self.codec_tag

        if self.codec_tag_string is not None:
            result['CodecTagString'] = self.codec_tag_string

        if self.codec_time_base is not None:
            result['CodecTimeBase'] = self.codec_time_base

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.index is not None:
            result['Index'] = self.index

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.num_frames is not None:
            result['NumFrames'] = self.num_frames

        if self.sample_fmt is not None:
            result['SampleFmt'] = self.sample_fmt

        if self.samplerate is not None:
            result['Samplerate'] = self.samplerate

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.timebase is not None:
            result['Timebase'] = self.timebase

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')

        if m.get('ChannelLayout') is not None:
            self.channel_layout = m.get('ChannelLayout')

        if m.get('Channels') is not None:
            self.channels = m.get('Channels')

        if m.get('CodecLongName') is not None:
            self.codec_long_name = m.get('CodecLongName')

        if m.get('CodecName') is not None:
            self.codec_name = m.get('CodecName')

        if m.get('CodecTag') is not None:
            self.codec_tag = m.get('CodecTag')

        if m.get('CodecTagString') is not None:
            self.codec_tag_string = m.get('CodecTagString')

        if m.get('CodecTimeBase') is not None:
            self.codec_time_base = m.get('CodecTimeBase')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('NumFrames') is not None:
            self.num_frames = m.get('NumFrames')

        if m.get('SampleFmt') is not None:
            self.sample_fmt = m.get('SampleFmt')

        if m.get('Samplerate') is not None:
            self.samplerate = m.get('Samplerate')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Timebase') is not None:
            self.timebase = m.get('Timebase')

        return self

class QueryMediaListResponseBodyMediaListMediaMediaInfoFormat(DaraModel):
    def __init__(
        self,
        bitrate: str = None,
        duration: str = None,
        format_long_name: str = None,
        format_name: str = None,
        num_programs: str = None,
        num_streams: str = None,
        size: str = None,
        start_time: str = None,
    ):
        self.bitrate = bitrate
        self.duration = duration
        self.format_long_name = format_long_name
        self.format_name = format_name
        self.num_programs = num_programs
        self.num_streams = num_streams
        self.size = size
        self.start_time = start_time

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

        if self.format_long_name is not None:
            result['FormatLongName'] = self.format_long_name

        if self.format_name is not None:
            result['FormatName'] = self.format_name

        if self.num_programs is not None:
            result['NumPrograms'] = self.num_programs

        if self.num_streams is not None:
            result['NumStreams'] = self.num_streams

        if self.size is not None:
            result['Size'] = self.size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('FormatLongName') is not None:
            self.format_long_name = m.get('FormatLongName')

        if m.get('FormatName') is not None:
            self.format_name = m.get('FormatName')

        if m.get('NumPrograms') is not None:
            self.num_programs = m.get('NumPrograms')

        if m.get('NumStreams') is not None:
            self.num_streams = m.get('NumStreams')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class QueryMediaListResponseBodyMediaListMediaFile(DaraModel):
    def __init__(
        self,
        state: str = None,
        url: str = None,
    ):
        self.state = state
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.state is not None:
            result['State'] = self.state

        if self.url is not None:
            result['URL'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('URL') is not None:
            self.url = m.get('URL')

        return self

