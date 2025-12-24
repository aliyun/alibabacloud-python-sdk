# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveStreamTranscodeStreamNumResponseBody(DaraModel):
    def __init__(
        self,
        lazy_transcoded_number: int = None,
        request_id: str = None,
        total: int = None,
        transcode_stream_count_details: List[main_models.DescribeLiveStreamTranscodeStreamNumResponseBodyTranscodeStreamCountDetails] = None,
        transcoded_number: int = None,
        untranscode_number: int = None,
    ):
        # The number of streams for which transcoding is triggered by stream pulling.
        self.lazy_transcoded_number = lazy_transcoded_number
        # The request ID.
        self.request_id = request_id
        # The total number of streams.
        self.total = total
        # The details about the transcoding templates.
        self.transcode_stream_count_details = transcode_stream_count_details
        # The number of streams that are transcoded.
        self.transcoded_number = transcoded_number
        # The number of streams that are not transcoded.
        self.untranscode_number = untranscode_number

    def validate(self):
        if self.transcode_stream_count_details:
            for v1 in self.transcode_stream_count_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lazy_transcoded_number is not None:
            result['LazyTranscodedNumber'] = self.lazy_transcoded_number

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        result['TranscodeStreamCountDetails'] = []
        if self.transcode_stream_count_details is not None:
            for k1 in self.transcode_stream_count_details:
                result['TranscodeStreamCountDetails'].append(k1.to_map() if k1 else None)

        if self.transcoded_number is not None:
            result['TranscodedNumber'] = self.transcoded_number

        if self.untranscode_number is not None:
            result['UntranscodeNumber'] = self.untranscode_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LazyTranscodedNumber') is not None:
            self.lazy_transcoded_number = m.get('LazyTranscodedNumber')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        self.transcode_stream_count_details = []
        if m.get('TranscodeStreamCountDetails') is not None:
            for k1 in m.get('TranscodeStreamCountDetails'):
                temp_model = main_models.DescribeLiveStreamTranscodeStreamNumResponseBodyTranscodeStreamCountDetails()
                self.transcode_stream_count_details.append(temp_model.from_map(k1))

        if m.get('TranscodedNumber') is not None:
            self.transcoded_number = m.get('TranscodedNumber')

        if m.get('UntranscodeNumber') is not None:
            self.untranscode_number = m.get('UntranscodeNumber')

        return self

class DescribeLiveStreamTranscodeStreamNumResponseBodyTranscodeStreamCountDetails(DaraModel):
    def __init__(
        self,
        count: int = None,
        template: str = None,
    ):
        # The number of streams that use the transcoding template.
        self.count = count
        # The name of the transcoding template.
        self.template = template

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.template is not None:
            result['Template'] = self.template

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        return self

