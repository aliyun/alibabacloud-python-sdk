# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveUserStreamMetricDataResponseBody(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        start_time: str = None,
        stream_detail_data: List[main_models.DescribeLiveUserStreamMetricDataResponseBodyStreamDetailData] = None,
        total_count: int = None,
    ):
        # The streaming domain information.
        self.domain_name = domain_name
        # YYYY-MM-DDThh:mm:ssZ
        self.end_time = end_time
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The beginning of the time range to query. The time is in the ISO 8601 standard in the `YYYY-MM-DDThh:mm:ssZ` format in UTC.
        self.start_time = start_time
        # The traffic data for each time interval.
        self.stream_detail_data = stream_detail_data
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.stream_detail_data:
            for v1 in self.stream_detail_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        result['StreamDetailData'] = []
        if self.stream_detail_data is not None:
            for k1 in self.stream_detail_data:
                result['StreamDetailData'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        self.stream_detail_data = []
        if m.get('StreamDetailData') is not None:
            for k1 in m.get('StreamDetailData'):
                temp_model = main_models.DescribeLiveUserStreamMetricDataResponseBodyStreamDetailData()
                self.stream_detail_data.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeLiveUserStreamMetricDataResponseBodyStreamDetailData(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        bps: float = None,
        count: int = None,
        flv_bps: float = None,
        flv_count: int = None,
        flv_traffic: float = None,
        hls_bps: float = None,
        hls_count: int = None,
        hls_traffic: float = None,
        new_conns: int = None,
        p_2p_bps: float = None,
        p_2p_count: int = None,
        p_2p_traffic: float = None,
        rtmp_bps: float = None,
        rtmp_count: int = None,
        rtmp_traffic: float = None,
        rts_bps: float = None,
        rts_count: int = None,
        rts_traffic: float = None,
        stream_name: str = None,
        time_stamp: str = None,
        traffic: float = None,
    ):
        # The application name. This value is returned regardless of whether it is specified.
        self.app_name = app_name
        # The total bandwidth per minute for the stream, in bps.
        self.bps = bps
        # The total number of concurrent connections per minute for the stream.
        # 
        # > **Concurrent connections** refers to the count of client process connections to the same stream within a unit of time.
        self.count = count
        # The bandwidth for the FLV protocol, in bps. This field is not returned if the specified protocol does not match.
        self.flv_bps = flv_bps
        # The number of concurrent connections for the FLV protocol. This field is not returned if the specified protocol does not match.
        self.flv_count = flv_count
        # The traffic for the FLV protocol, in bytes. This field is not returned if the specified protocol does not match.
        self.flv_traffic = flv_traffic
        # The bandwidth for the HLS protocol, in bps. This field is not returned if the specified protocol does not match.
        self.hls_bps = hls_bps
        # The number of concurrent connections for the HLS protocol. This field is not returned if the specified protocol does not match.
        self.hls_count = hls_count
        # The traffic for the HLS protocol, in bytes. This field is not returned if the specified protocol does not match.
        self.hls_traffic = hls_traffic
        # The number of new connections per minute for the stream.
        self.new_conns = new_conns
        # The bandwidth for the P2P protocol, in bps. This field is not returned if the specified protocol does not match.
        self.p_2p_bps = p_2p_bps
        # The number of concurrent connections for the P2P protocol. This field is not returned if the specified protocol does not match.
        self.p_2p_count = p_2p_count
        # The traffic for the P2P protocol, in bytes. This field is not returned if the specified protocol does not match.
        self.p_2p_traffic = p_2p_traffic
        # The bandwidth for the RTMP protocol, in bps. This field is not returned if the specified protocol does not match.
        self.rtmp_bps = rtmp_bps
        # The number of concurrent connections for the RTMP protocol. This field is not returned if the specified protocol does not match.
        self.rtmp_count = rtmp_count
        # The traffic for the RTMP protocol, in bytes. This field is not returned if the specified protocol does not match.
        self.rtmp_traffic = rtmp_traffic
        # The bandwidth for the RTS protocol, in bps. This field is not returned if the specified protocol does not match.
        self.rts_bps = rts_bps
        # The number of concurrent connections for the RTS protocol. This field is not returned if the specified protocol does not match.
        self.rts_count = rts_count
        # The traffic for the RTS protocol, in bytes. This field is not returned if the specified protocol does not match.
        self.rts_traffic = rts_traffic
        # The stream name. This value is returned regardless of whether it is specified.
        self.stream_name = stream_name
        # The start time of the time slice. The time is in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format in UTC+0.
        self.time_stamp = time_stamp
        # The total traffic per minute for the stream, in bytes.
        self.traffic = traffic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.bps is not None:
            result['Bps'] = self.bps

        if self.count is not None:
            result['Count'] = self.count

        if self.flv_bps is not None:
            result['FlvBps'] = self.flv_bps

        if self.flv_count is not None:
            result['FlvCount'] = self.flv_count

        if self.flv_traffic is not None:
            result['FlvTraffic'] = self.flv_traffic

        if self.hls_bps is not None:
            result['HlsBps'] = self.hls_bps

        if self.hls_count is not None:
            result['HlsCount'] = self.hls_count

        if self.hls_traffic is not None:
            result['HlsTraffic'] = self.hls_traffic

        if self.new_conns is not None:
            result['NewConns'] = self.new_conns

        if self.p_2p_bps is not None:
            result['P2pBps'] = self.p_2p_bps

        if self.p_2p_count is not None:
            result['P2pCount'] = self.p_2p_count

        if self.p_2p_traffic is not None:
            result['P2pTraffic'] = self.p_2p_traffic

        if self.rtmp_bps is not None:
            result['RtmpBps'] = self.rtmp_bps

        if self.rtmp_count is not None:
            result['RtmpCount'] = self.rtmp_count

        if self.rtmp_traffic is not None:
            result['RtmpTraffic'] = self.rtmp_traffic

        if self.rts_bps is not None:
            result['RtsBps'] = self.rts_bps

        if self.rts_count is not None:
            result['RtsCount'] = self.rts_count

        if self.rts_traffic is not None:
            result['RtsTraffic'] = self.rts_traffic

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        if self.traffic is not None:
            result['Traffic'] = self.traffic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Bps') is not None:
            self.bps = m.get('Bps')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('FlvBps') is not None:
            self.flv_bps = m.get('FlvBps')

        if m.get('FlvCount') is not None:
            self.flv_count = m.get('FlvCount')

        if m.get('FlvTraffic') is not None:
            self.flv_traffic = m.get('FlvTraffic')

        if m.get('HlsBps') is not None:
            self.hls_bps = m.get('HlsBps')

        if m.get('HlsCount') is not None:
            self.hls_count = m.get('HlsCount')

        if m.get('HlsTraffic') is not None:
            self.hls_traffic = m.get('HlsTraffic')

        if m.get('NewConns') is not None:
            self.new_conns = m.get('NewConns')

        if m.get('P2pBps') is not None:
            self.p_2p_bps = m.get('P2pBps')

        if m.get('P2pCount') is not None:
            self.p_2p_count = m.get('P2pCount')

        if m.get('P2pTraffic') is not None:
            self.p_2p_traffic = m.get('P2pTraffic')

        if m.get('RtmpBps') is not None:
            self.rtmp_bps = m.get('RtmpBps')

        if m.get('RtmpCount') is not None:
            self.rtmp_count = m.get('RtmpCount')

        if m.get('RtmpTraffic') is not None:
            self.rtmp_traffic = m.get('RtmpTraffic')

        if m.get('RtsBps') is not None:
            self.rts_bps = m.get('RtsBps')

        if m.get('RtsCount') is not None:
            self.rts_count = m.get('RtsCount')

        if m.get('RtsTraffic') is not None:
            self.rts_traffic = m.get('RtsTraffic')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        if m.get('Traffic') is not None:
            self.traffic = m.get('Traffic')

        return self

