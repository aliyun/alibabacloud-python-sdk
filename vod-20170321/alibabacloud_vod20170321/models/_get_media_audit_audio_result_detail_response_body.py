# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class GetMediaAuditAudioResultDetailResponseBody(DaraModel):
    def __init__(
        self,
        media_audit_audio_result_detail: main_models.GetMediaAuditAudioResultDetailResponseBodyMediaAuditAudioResultDetail = None,
        request_id: str = None,
    ):
        # Details of review results.
        self.media_audit_audio_result_detail = media_audit_audio_result_detail
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.media_audit_audio_result_detail:
            self.media_audit_audio_result_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media_audit_audio_result_detail is not None:
            result['MediaAuditAudioResultDetail'] = self.media_audit_audio_result_detail.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaAuditAudioResultDetail') is not None:
            temp_model = main_models.GetMediaAuditAudioResultDetailResponseBodyMediaAuditAudioResultDetail()
            self.media_audit_audio_result_detail = temp_model.from_map(m.get('MediaAuditAudioResultDetail'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetMediaAuditAudioResultDetailResponseBodyMediaAuditAudioResultDetail(DaraModel):
    def __init__(
        self,
        list: List[main_models.GetMediaAuditAudioResultDetailResponseBodyMediaAuditAudioResultDetailList] = None,
        page_total: int = None,
        total: int = None,
    ):
        # The list of results.
        self.list = list
        # The page number of the returned page.
        self.page_total = page_total
        # The total number of pages returned.
        self.total = total

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.page_total is not None:
            result['PageTotal'] = self.page_total

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.GetMediaAuditAudioResultDetailResponseBodyMediaAuditAudioResultDetailList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageTotal') is not None:
            self.page_total = m.get('PageTotal')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class GetMediaAuditAudioResultDetailResponseBodyMediaAuditAudioResultDetailList(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        label: str = None,
        start_time: int = None,
        text: str = None,
    ):
        # The end time of the audio that failed the review. Unit: seconds.
        self.end_time = end_time
        # The review results. Valid values:
        # *   **spam**
        # *   **ad**
        # *   **abuse**
        # *   **flood**
        # *   **contraband**
        # *   **meaningless**
        # *   **normal**
        self.label = label
        # The start time of the audio that failed the review. Unit: seconds.
        self.start_time = start_time
        # The text that corresponds to the audio.
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.label is not None:
            result['Label'] = self.label

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.text is not None:
            result['Text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        return self

