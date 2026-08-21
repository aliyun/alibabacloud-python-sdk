# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UploadStreamByURLRequest(DaraModel):
    def __init__(
        self,
        definition: str = None,
        file_extension: str = None,
        hdrtype: str = None,
        media_id: str = None,
        stream_url: str = None,
        upload_metadata: str = None,
        user_data: str = None,
    ):
        # The definition of the video stream.
        # 
        # For valid values of this parameter, see [Media asset parameter description - Definition](https://help.aliyun.com/document_detail/124671.html).
        # 
        # This parameter is required.
        self.definition = definition
        # The file name extension of the transcoded stream file.
        # 
        # For supported audio and video file formats, see [Overview](https://help.aliyun.com/document_detail/55396.html).
        # 
        # If this parameter is not empty, it overwrites the file name extension in the StreamURL.
        # 
        # >Notice: This parameter is required if the StreamURL does not contain a file name extension.
        self.file_extension = file_extension
        # The HDR type of the transcoded stream. Valid values:
        # - HDR
        # - HDR10
        # - HLG
        # - DolbyVision
        # - HDRVivid
        # - SDR+
        # > - Case-insensitive.
        # > - Leave this parameter empty for non-HDR videos.
        self.hdrtype = hdrtype
        # The ID of the ApsaraVideo VOD media asset that corresponds to the transcoded stream.
        # 
        # This parameter is required.
        self.media_id = media_id
        # The URL of the transcoded stream file.
        # 
        # If the URL of the transcoded stream requires authentication, include the authentication parameters in StreamURL and make sure the URL is accessible through public network access.
        # >You can obtain the audio or video URL from the console or by invoking the GetPlayInfo operation.
        # 
        # This parameter is required.
        self.stream_url = stream_url
        # The metadata of the media file to upload. The value is a JSON string.
        # - For more information, see the **UploadMetadata** table below.
        self.upload_metadata = upload_metadata
        # The custom parameter. For more information, see [UserData](https://help.aliyun.com/document_detail/86952.html).
        # > To use the message callback in this parameter, configure the HTTP callback URL and select the corresponding callback event types in the console. Otherwise, the callback settings do not take effect. For information about how to configure HTTP callbacks in the console, see [Callback settings](https://help.aliyun.com/document_detail/86071.html).
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.definition is not None:
            result['Definition'] = self.definition

        if self.file_extension is not None:
            result['FileExtension'] = self.file_extension

        if self.hdrtype is not None:
            result['HDRType'] = self.hdrtype

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.stream_url is not None:
            result['StreamURL'] = self.stream_url

        if self.upload_metadata is not None:
            result['UploadMetadata'] = self.upload_metadata

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Definition') is not None:
            self.definition = m.get('Definition')

        if m.get('FileExtension') is not None:
            self.file_extension = m.get('FileExtension')

        if m.get('HDRType') is not None:
            self.hdrtype = m.get('HDRType')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('StreamURL') is not None:
            self.stream_url = m.get('StreamURL')

        if m.get('UploadMetadata') is not None:
            self.upload_metadata = m.get('UploadMetadata')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

