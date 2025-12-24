# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveStreamMergeResponseBody(DaraModel):
    def __init__(
        self,
        live_stream_merge_list: main_models.DescribeLiveStreamMergeResponseBodyLiveStreamMergeList = None,
        request_id: str = None,
    ):
        # Live stream information list.
        self.live_stream_merge_list = live_stream_merge_list
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.live_stream_merge_list:
            self.live_stream_merge_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.live_stream_merge_list is not None:
            result['LiveStreamMergeList'] = self.live_stream_merge_list.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LiveStreamMergeList') is not None:
            temp_model = main_models.DescribeLiveStreamMergeResponseBodyLiveStreamMergeList()
            self.live_stream_merge_list = temp_model.from_map(m.get('LiveStreamMergeList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeLiveStreamMergeResponseBodyLiveStreamMergeList(DaraModel):
    def __init__(
        self,
        live_stream_merge: List[main_models.DescribeLiveStreamMergeResponseBodyLiveStreamMergeListLiveStreamMerge] = None,
    ):
        self.live_stream_merge = live_stream_merge

    def validate(self):
        if self.live_stream_merge:
            for v1 in self.live_stream_merge:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LiveStreamMerge'] = []
        if self.live_stream_merge is not None:
            for k1 in self.live_stream_merge:
                result['LiveStreamMerge'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.live_stream_merge = []
        if m.get('LiveStreamMerge') is not None:
            for k1 in m.get('LiveStreamMerge'):
                temp_model = main_models.DescribeLiveStreamMergeResponseBodyLiveStreamMergeListLiveStreamMerge()
                self.live_stream_merge.append(temp_model.from_map(k1))

        return self

class DescribeLiveStreamMergeResponseBodyLiveStreamMergeListLiveStreamMerge(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        app_using: str = None,
        domain_name: str = None,
        end_time: str = None,
        extra_in_app_streams: str = None,
        in_app_name_1: str = None,
        in_app_name_2: str = None,
        in_stream_name_1: str = None,
        in_stream_name_2: str = None,
        live_merger: str = None,
        merge_parameters: str = None,
        protocol: str = None,
        start_time: str = None,
        stream_name: str = None,
        stream_using: str = None,
    ):
        # The name of the application that generates the output stream.
        self.app_name = app_name
        # The application that is being used.
        self.app_using = app_using
        # The streaming domain.
        self.domain_name = domain_name
        # The end time of the stream mixing.
        self.end_time = end_time
        # The names of the applications that generate the input additional streams other than the primary stream and secondary stream, and the names of these additional streams.
        self.extra_in_app_streams = extra_in_app_streams
        # The name of the application that generates the input primary stream.
        self.in_app_name_1 = in_app_name_1
        # The name of the application that generates the input secondary stream.
        self.in_app_name_2 = in_app_name_2
        # The name of the input primary stream.
        self.in_stream_name_1 = in_stream_name_1
        # The name of the input secondary stream.
        self.in_stream_name_2 = in_stream_name_2
        self.live_merger = live_merger
        self.merge_parameters = merge_parameters
        # The streaming protocol.
        self.protocol = protocol
        # The start time of the stream mixing.
        self.start_time = start_time
        # The name of the output stream.
        self.stream_name = stream_name
        # The stream that is being used.
        self.stream_using = stream_using

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.app_using is not None:
            result['AppUsing'] = self.app_using

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.extra_in_app_streams is not None:
            result['ExtraInAppStreams'] = self.extra_in_app_streams

        if self.in_app_name_1 is not None:
            result['InAppName1'] = self.in_app_name_1

        if self.in_app_name_2 is not None:
            result['InAppName2'] = self.in_app_name_2

        if self.in_stream_name_1 is not None:
            result['InStreamName1'] = self.in_stream_name_1

        if self.in_stream_name_2 is not None:
            result['InStreamName2'] = self.in_stream_name_2

        if self.live_merger is not None:
            result['LiveMerger'] = self.live_merger

        if self.merge_parameters is not None:
            result['MergeParameters'] = self.merge_parameters

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        if self.stream_using is not None:
            result['StreamUsing'] = self.stream_using

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AppUsing') is not None:
            self.app_using = m.get('AppUsing')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ExtraInAppStreams') is not None:
            self.extra_in_app_streams = m.get('ExtraInAppStreams')

        if m.get('InAppName1') is not None:
            self.in_app_name_1 = m.get('InAppName1')

        if m.get('InAppName2') is not None:
            self.in_app_name_2 = m.get('InAppName2')

        if m.get('InStreamName1') is not None:
            self.in_stream_name_1 = m.get('InStreamName1')

        if m.get('InStreamName2') is not None:
            self.in_stream_name_2 = m.get('InStreamName2')

        if m.get('LiveMerger') is not None:
            self.live_merger = m.get('LiveMerger')

        if m.get('MergeParameters') is not None:
            self.merge_parameters = m.get('MergeParameters')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        if m.get('StreamUsing') is not None:
            self.stream_using = m.get('StreamUsing')

        return self

