# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class GetMediaDNAResultResponseBody(DaraModel):
    def __init__(
        self,
        dnaresult: main_models.GetMediaDNAResultResponseBodyDNAResult = None,
        request_id: str = None,
    ):
        # The media fingerprinting results.
        self.dnaresult = dnaresult
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.dnaresult:
            self.dnaresult.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dnaresult is not None:
            result['DNAResult'] = self.dnaresult.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DNAResult') is not None:
            temp_model = main_models.GetMediaDNAResultResponseBodyDNAResult()
            self.dnaresult = temp_model.from_map(m.get('DNAResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetMediaDNAResultResponseBodyDNAResult(DaraModel):
    def __init__(
        self,
        video_dna: List[main_models.GetMediaDNAResultResponseBodyDNAResultVideoDNA] = None,
    ):
        # The video fingerprint recognition result.
        self.video_dna = video_dna

    def validate(self):
        if self.video_dna:
            for v1 in self.video_dna:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['VideoDNA'] = []
        if self.video_dna is not None:
            for k1 in self.video_dna:
                result['VideoDNA'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.video_dna = []
        if m.get('VideoDNA') is not None:
            for k1 in m.get('VideoDNA'):
                temp_model = main_models.GetMediaDNAResultResponseBodyDNAResultVideoDNA()
                self.video_dna.append(temp_model.from_map(k1))

        return self

class GetMediaDNAResultResponseBodyDNAResultVideoDNA(DaraModel):
    def __init__(
        self,
        detail: List[main_models.GetMediaDNAResultResponseBodyDNAResultVideoDNADetail] = None,
        primary_key: str = None,
        similarity: str = None,
    ):
        # The details of the matched video. Information such as the location and duration of the video is returned.
        self.detail = detail
        # The ID of the video that has a similar fingerprint.
        self.primary_key = primary_key
        # The similarity between the fingerprints of the input video and the matched video. 1 indicates that the fingerprints of the two videos are the same.
        self.similarity = similarity

    def validate(self):
        if self.detail:
            for v1 in self.detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Detail'] = []
        if self.detail is not None:
            for k1 in self.detail:
                result['Detail'].append(k1.to_map() if k1 else None)

        if self.primary_key is not None:
            result['PrimaryKey'] = self.primary_key

        if self.similarity is not None:
            result['Similarity'] = self.similarity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detail = []
        if m.get('Detail') is not None:
            for k1 in m.get('Detail'):
                temp_model = main_models.GetMediaDNAResultResponseBodyDNAResultVideoDNADetail()
                self.detail.append(temp_model.from_map(k1))

        if m.get('PrimaryKey') is not None:
            self.primary_key = m.get('PrimaryKey')

        if m.get('Similarity') is not None:
            self.similarity = m.get('Similarity')

        return self

class GetMediaDNAResultResponseBodyDNAResultVideoDNADetail(DaraModel):
    def __init__(
        self,
        duplication: main_models.GetMediaDNAResultResponseBodyDNAResultVideoDNADetailDuplication = None,
        input: main_models.GetMediaDNAResultResponseBodyDNAResultVideoDNADetailInput = None,
    ):
        # The start time and duration of the matched video.
        self.duplication = duplication
        # The start time and duration of the input video.
        self.input = input

    def validate(self):
        if self.duplication:
            self.duplication.validate()
        if self.input:
            self.input.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duplication is not None:
            result['Duplication'] = self.duplication.to_map()

        if self.input is not None:
            result['Input'] = self.input.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duplication') is not None:
            temp_model = main_models.GetMediaDNAResultResponseBodyDNAResultVideoDNADetailDuplication()
            self.duplication = temp_model.from_map(m.get('Duplication'))

        if m.get('Input') is not None:
            temp_model = main_models.GetMediaDNAResultResponseBodyDNAResultVideoDNADetailInput()
            self.input = temp_model.from_map(m.get('Input'))

        return self

class GetMediaDNAResultResponseBodyDNAResultVideoDNADetailInput(DaraModel):
    def __init__(
        self,
        duration: str = None,
        start: str = None,
    ):
        # The duration of the video. Unit: seconds.
        self.duration = duration
        # The start time of the video. Unit: seconds.
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['Duration'] = self.duration

        if self.start is not None:
            result['Start'] = self.start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Start') is not None:
            self.start = m.get('Start')

        return self

class GetMediaDNAResultResponseBodyDNAResultVideoDNADetailDuplication(DaraModel):
    def __init__(
        self,
        duration: str = None,
        start: str = None,
    ):
        # The duration of the video. Unit: seconds.
        self.duration = duration
        # The start time of the video. Unit: seconds.
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['Duration'] = self.duration

        if self.start is not None:
            result['Start'] = self.start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Start') is not None:
            self.start = m.get('Start')

        return self

