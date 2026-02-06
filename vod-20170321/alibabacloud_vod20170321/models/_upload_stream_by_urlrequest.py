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
        # The quality of the video stream.
        # 
        # For more information about valid values of this parameter, see [Parameters for media assets](https://help.aliyun.com/document_detail/124671.html).
        # 
        # This parameter is required.
        self.definition = definition
        # The file name extension of the transcoded stream.
        # 
        # For more information, see the Supported media file formats section in [Overview](https://help.aliyun.com/document_detail/55396.html).
        # 
        # If you set a value for this parameter, the file name extension specified in StreamURL is overwritten.
        # 
        # >  This parameter is required if you do not specify a file name extension in StreamURL.
        self.file_extension = file_extension
        # The HDR type of the transcoded stream. Valid values:
        # 
        # *   HDR
        # *   HDR10
        # *   HLG
        # *   DolbyVision
        # *   HDRVivid
        # *   SDR+
        # 
        # > 
        # 
        # *   The HDR type of the transcoded stream is not case-sensitive.
        # 
        # *   You can leave this parameter empty for non-HDR streams.
        self.hdrtype = hdrtype
        # The media ID in ApsaraVideo VOD.
        # 
        # This parameter is required.
        self.media_id = media_id
        # The URL of the transcoded stream.
        # 
        # If URL authentication is required, you must pass authentication information in this parameter and make sure that the URL can be accessed over the Internet.
        # 
        # This parameter is required.
        self.stream_url = stream_url
        # Metadata information for uploading media files, in JSON string format.
        # 
        # For more information, please refer to the table below for UploadMetadata.
        self.upload_metadata = upload_metadata
        # The user-defined parameter. For more information, see the "UserData: specifies the custom configurations for media upload" section of the [Request parameters](https://help.aliyun.com/document_detail/86952.html) topic.
        # 
        # >  The callback configurations you specify for this parameter take effect only after you specify the HTTP callback URL and select specific callback events in the ApsaraVideo VOD console. For more information about how to configure HTTP callback settings in the ApsaraVideo VOD console, see [Configure callback settings](https://help.aliyun.com/document_detail/86071.html).
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

