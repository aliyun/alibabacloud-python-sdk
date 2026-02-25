# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mts20140618 import models as main_models
from darabonba.model import DaraModel

class UpdateMediaResponseBody(DaraModel):
    def __init__(
        self,
        media: main_models.UpdateMediaResponseBodyMedia = None,
        request_id: str = None,
    ):
        # The information about the media file.
        self.media = media
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.media:
            self.media.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media is not None:
            result['Media'] = self.media.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Media') is not None:
            temp_model = main_models.UpdateMediaResponseBodyMedia()
            self.media = temp_model.from_map(m.get('Media'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class UpdateMediaResponseBodyMedia(DaraModel):
    def __init__(
        self,
        bitrate: str = None,
        cate_id: int = None,
        censor_state: str = None,
        cover_url: str = None,
        creation_time: str = None,
        description: str = None,
        duration: str = None,
        file: main_models.UpdateMediaResponseBodyMediaFile = None,
        format: str = None,
        fps: str = None,
        height: str = None,
        media_id: str = None,
        publish_state: str = None,
        run_id_list: main_models.UpdateMediaResponseBodyMediaRunIdList = None,
        size: str = None,
        tags: main_models.UpdateMediaResponseBodyMediaTags = None,
        title: str = None,
        width: str = None,
    ):
        # The bitrate of the media file.
        self.bitrate = bitrate
        # The ID of the category to which the media file belongs.
        self.cate_id = cate_id
        # The review state of the media file. Valid values:
        # 
        # *   **Initiated**: The media file is uploaded but not reviewed.
        # *   **Pass**: The media file is uploaded and passes the review.
        self.censor_state = censor_state
        # The URL of the thumbnail.
        self.cover_url = cover_url
        # The time when the media file was created.
        self.creation_time = creation_time
        # The description of the media file.
        self.description = description
        # The duration of the media file.
        self.duration = duration
        # The information about the input file.
        self.file = file
        # The format of the media file. Valid values: mov, mp4, m4a, 3gp, 3g2, and mj2.
        self.format = format
        # The frame rate of the media file.
        self.fps = fps
        # The height of the media file.
        self.height = height
        # The ID of the media file.
        self.media_id = media_id
        # The publishing state of the media file. Valid values:
        # 
        # *   **Initiated**: The media file is in the initial state.
        # *   **UnPublish**: The media file has not been published, and the playback permission on the OSS object is Private.
        # *   **Published**: The media file has been published, and the playback permission on the OSS object is Default.
        # *   **Deleted**: The media file is deleted.
        self.publish_state = publish_state
        self.run_id_list = run_id_list
        # The size of the media file.
        self.size = size
        self.tags = tags
        # The title of the media file.
        self.title = title
        # The width of the media file.
        self.width = width

    def validate(self):
        if self.file:
            self.file.validate()
        if self.run_id_list:
            self.run_id_list.validate()
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

        if self.publish_state is not None:
            result['PublishState'] = self.publish_state

        if self.run_id_list is not None:
            result['RunIdList'] = self.run_id_list.to_map()

        if self.size is not None:
            result['Size'] = self.size

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
            temp_model = main_models.UpdateMediaResponseBodyMediaFile()
            self.file = temp_model.from_map(m.get('File'))

        if m.get('Format') is not None:
            self.format = m.get('Format')

        if m.get('Fps') is not None:
            self.fps = m.get('Fps')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('PublishState') is not None:
            self.publish_state = m.get('PublishState')

        if m.get('RunIdList') is not None:
            temp_model = main_models.UpdateMediaResponseBodyMediaRunIdList()
            self.run_id_list = temp_model.from_map(m.get('RunIdList'))

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Tags') is not None:
            temp_model = main_models.UpdateMediaResponseBodyMediaTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

class UpdateMediaResponseBodyMediaTags(DaraModel):
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

class UpdateMediaResponseBodyMediaRunIdList(DaraModel):
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

class UpdateMediaResponseBodyMediaFile(DaraModel):
    def __init__(
        self,
        state: str = None,
        url: str = None,
    ):
        # The state of the input file. Valid values:
        # 
        # *   **Normal**: The input file is normal.
        # *   **Deleted**: The input file is deleted.
        self.state = state
        # The name of the OSS bucket in which the input media file is stored.
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

