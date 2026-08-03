# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_outboundbot20191226 import models as main_models
from darabonba.model import DaraModel

class DownloadRecordingResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        download_params: main_models.DownloadRecordingResponseBodyDownloadParams = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The interface status code.
        self.code = code
        # The download URL of the file.
        self.download_params = download_params
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The interface prompt message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.download_params:
            self.download_params.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.download_params is not None:
            result['DownloadParams'] = self.download_params.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DownloadParams') is not None:
            temp_model = main_models.DownloadRecordingResponseBodyDownloadParams()
            self.download_params = temp_model.from_map(m.get('DownloadParams'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DownloadRecordingResponseBodyDownloadParams(DaraModel):
    def __init__(
        self,
        early_media_signature_url: str = None,
        file_name: str = None,
        signature_url: str = None,
        voice_slice_recording_list_json: str = None,
    ):
        self.early_media_signature_url = early_media_signature_url
        # The recording file name, which is typically a UUID.
        self.file_name = file_name
        # A URL that points to the recording file. Use HTTP to download the file.
        self.signature_url = signature_url
        # The list of segmented recordings, including file names and file URLs.
        self.voice_slice_recording_list_json = voice_slice_recording_list_json

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.early_media_signature_url is not None:
            result['EarlyMediaSignatureUrl'] = self.early_media_signature_url

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.signature_url is not None:
            result['SignatureUrl'] = self.signature_url

        if self.voice_slice_recording_list_json is not None:
            result['VoiceSliceRecordingListJson'] = self.voice_slice_recording_list_json

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EarlyMediaSignatureUrl') is not None:
            self.early_media_signature_url = m.get('EarlyMediaSignatureUrl')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('SignatureUrl') is not None:
            self.signature_url = m.get('SignatureUrl')

        if m.get('VoiceSliceRecordingListJson') is not None:
            self.voice_slice_recording_list_json = m.get('VoiceSliceRecordingListJson')

        return self

