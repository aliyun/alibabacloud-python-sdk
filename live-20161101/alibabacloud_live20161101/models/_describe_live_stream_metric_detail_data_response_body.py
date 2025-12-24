# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveStreamMetricDetailDataResponseBody(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        next_page_token: str = None,
        page_size: int = None,
        request_id: str = None,
        start_time: str = None,
        stream_detail_data: main_models.DescribeLiveStreamMetricDetailDataResponseBodyStreamDetailData = None,
    ):
        # The accelerated domain name.
        self.domain_name = domain_name
        # The end of the time range during which data was queried.
        self.end_time = end_time
        # The token that determines the start point of the next query. This parameter is returned if more data results are available.
        self.next_page_token = next_page_token
        # The number of rows returned.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The beginning of the time range during which data was queried.
        self.start_time = start_time
        # The data array returned.
        self.stream_detail_data = stream_detail_data

    def validate(self):
        if self.stream_detail_data:
            self.stream_detail_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.next_page_token is not None:
            result['NextPageToken'] = self.next_page_token

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.stream_detail_data is not None:
            result['StreamDetailData'] = self.stream_detail_data.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('NextPageToken') is not None:
            self.next_page_token = m.get('NextPageToken')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StreamDetailData') is not None:
            temp_model = main_models.DescribeLiveStreamMetricDetailDataResponseBodyStreamDetailData()
            self.stream_detail_data = temp_model.from_map(m.get('StreamDetailData'))

        return self

class DescribeLiveStreamMetricDetailDataResponseBodyStreamDetailData(DaraModel):
    def __init__(
        self,
        stream_data: List[main_models.DescribeLiveStreamMetricDetailDataResponseBodyStreamDetailDataStreamData] = None,
    ):
        self.stream_data = stream_data

    def validate(self):
        if self.stream_data:
            for v1 in self.stream_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['StreamData'] = []
        if self.stream_data is not None:
            for k1 in self.stream_data:
                result['StreamData'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.stream_data = []
        if m.get('StreamData') is not None:
            for k1 in m.get('StreamData'):
                temp_model = main_models.DescribeLiveStreamMetricDetailDataResponseBodyStreamDetailDataStreamData()
                self.stream_data.append(temp_model.from_map(k1))

        return self

class DescribeLiveStreamMetricDetailDataResponseBodyStreamDetailDataStreamData(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        bps: float = None,
        count: int = None,
        flv_bps: float = None,
        flv_count: int = None,
        flv_traffic: int = None,
        hls_bps: float = None,
        hls_count: int = None,
        hls_traffic: int = None,
        new_conns: str = None,
        p_2p_bps: float = None,
        p_2p_count: int = None,
        p_2p_traffic: int = None,
        rtmp_bps: float = None,
        rtmp_count: int = None,
        rtmp_traffic: int = None,
        rts_bps: float = None,
        rts_count: int = None,
        rts_traffic: int = None,
        stream_name: str = None,
        time_stamp: str = None,
        traffic: int = None,
    ):
        # The name of the application.
        self.app_name = app_name
        # The total bandwidth consumed by the stream per minute. Unit: bit/s.
        self.bps = bps
        # The total number of online viewers for the stream per minute.
        self.count = count
        # The bandwidth over the Flash Video (FLV) protocol. Unit: bit/s.
        # 
        # >  This parameter is not returned if no traffic is generated over the protocol.
        self.flv_bps = flv_bps
        # The number of online viewers over the FLV protocol.
        # 
        # >  This parameter is not returned if no traffic is generated over the protocol.
        self.flv_count = flv_count
        # The amount of traffic over the FLV protocol. Unit: bytes.
        # 
        # >  This parameter is not returned if no traffic is generated over the protocol.
        self.flv_traffic = flv_traffic
        # The bandwidth over the HTTP Live Streaming (HLS) protocol. Unit: bit/s.
        # 
        # >  This parameter is not returned if no traffic is generated over the protocol.
        self.hls_bps = hls_bps
        # The number of online viewers over the HLS protocol.
        # 
        # >  Currently, this parameter is not supported.
        self.hls_count = hls_count
        # The amount of traffic over the HLS protocol. Unit: bytes.
        # 
        # >  This parameter is not returned if no traffic is generated over the protocol.
        self.hls_traffic = hls_traffic
        # Number of new connections established per minute.
        self.new_conns = new_conns
        # The bandwidth over the P2P protocol. Unit: bit/s.
        # 
        # >  This parameter is not returned if no traffic is generated over the protocol.
        self.p_2p_bps = p_2p_bps
        # The number of online viewers over the P2P protocol.
        # 
        # >  This parameter is not returned if no traffic is generated over the protocol.
        self.p_2p_count = p_2p_count
        # The amount of traffic over the peer-to-peer (P2P) protocol. Unit: bytes.
        # 
        # >  This parameter is not returned if no traffic is generated over the protocol.
        self.p_2p_traffic = p_2p_traffic
        # The bandwidth over the Real-Time Messaging Protocol (RTMP) protocol. Unit: bit/s.
        # 
        # >  This parameter is not returned if no traffic is generated over the protocol.
        self.rtmp_bps = rtmp_bps
        # The number of online viewers over the RTMP protocol.
        # 
        # >  This parameter is not returned if no traffic is generated over the protocol.
        self.rtmp_count = rtmp_count
        # The amount of traffic over the RTMP protocol. Unit: bytes.
        # 
        # >  This parameter is not returned if no traffic is generated over the protocol.
        self.rtmp_traffic = rtmp_traffic
        # The bandwidth over the RTS protocol. Unit: bit/s.
        # 
        # >  This parameter is not returned if no traffic is generated over the protocol.
        self.rts_bps = rts_bps
        # The number of online viewers over the Real-Time Streaming (RTS) protocol.
        # 
        # >  This parameter is not returned if no traffic is generated over the protocol.
        self.rts_count = rts_count
        # The amount of traffic over the RTS protocol. Unit: bytes.
        # 
        # >  This parameter is not returned if no traffic is generated over the protocol.
        self.rts_traffic = rts_traffic
        # The name of the stream.
        self.stream_name = stream_name
        # The timestamp of the returned data.
        self.time_stamp = time_stamp
        # The total amount of traffic consumed by the stream per minute. Unit: bytes.
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

