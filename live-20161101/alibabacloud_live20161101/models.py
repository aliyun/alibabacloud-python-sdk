# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
try:
    from typing import List
except ImportError:
    pass


class AddLiveASRConfigRequest(TeaModel):
    def __init__(self, domain_name=None, app_name=None, stream_name=None, mns_topic=None, mns_region=None,
                 period=None, http_callback_url=None):
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str
        self.stream_name = stream_name  # type: str
        self.mns_topic = mns_topic      # type: str
        self.mns_region = mns_region    # type: str
        self.period = period            # type: int
        self.http_callback_url = http_callback_url  # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.app_name, 'app_name')
        self.validate_required(self.stream_name, 'stream_name')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        result['StreamName'] = self.stream_name
        result['MnsTopic'] = self.mns_topic
        result['MnsRegion'] = self.mns_region
        result['Period'] = self.period
        result['HttpCallbackURL'] = self.http_callback_url
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        self.stream_name = map.get('StreamName')
        self.mns_topic = map.get('MnsTopic')
        self.mns_region = map.get('MnsRegion')
        self.period = map.get('Period')
        self.http_callback_url = map.get('HttpCallbackURL')
        return self


class AddLiveASRConfigResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeLiveAsrConfigRequest(TeaModel):
    def __init__(self, domain_name=None, app_name=None, stream_name=None):
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str
        self.stream_name = stream_name  # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        result['StreamName'] = self.stream_name
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        self.stream_name = map.get('StreamName')
        return self


class DescribeLiveAsrConfigResponse(TeaModel):
    def __init__(self, request_id=None, live_asr_config=None):
        self.request_id = request_id    # type: str
        self.live_asr_config = live_asr_config  # type: DescribeLiveAsrConfigResponseLiveAsrConfig

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.live_asr_config, 'live_asr_config')
        if self.live_asr_config:
            self.live_asr_config.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.live_asr_config is not None:
            result['LiveAsrConfig'] = self.live_asr_config.to_map()
        else:
            result['LiveAsrConfig'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('LiveAsrConfig') is not None:
            temp_model = DescribeLiveAsrConfigResponseLiveAsrConfig()
            self.live_asr_config = temp_model.from_map(map['LiveAsrConfig'])
        else:
            self.live_asr_config = None
        return self


class DescribeLiveAsrConfigResponseLiveAsrConfigLiveAsrConfigList(TeaModel):
    def __init__(self, domain_name=None, app_name=None, stream_name=None, period=None, mns_topic=None,
                 mns_region=None, http_callback_url=None):
        self.domain_name = domain_name  # type: int
        self.app_name = app_name        # type: str
        self.stream_name = stream_name  # type: str
        self.period = period            # type: int
        self.mns_topic = mns_topic      # type: str
        self.mns_region = mns_region    # type: str
        self.http_callback_url = http_callback_url  # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.app_name, 'app_name')
        self.validate_required(self.stream_name, 'stream_name')
        self.validate_required(self.period, 'period')
        self.validate_required(self.mns_topic, 'mns_topic')
        self.validate_required(self.mns_region, 'mns_region')
        self.validate_required(self.http_callback_url, 'http_callback_url')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        result['StreamName'] = self.stream_name
        result['Period'] = self.period
        result['MnsTopic'] = self.mns_topic
        result['MnsRegion'] = self.mns_region
        result['HttpCallbackURL'] = self.http_callback_url
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        self.stream_name = map.get('StreamName')
        self.period = map.get('Period')
        self.mns_topic = map.get('MnsTopic')
        self.mns_region = map.get('MnsRegion')
        self.http_callback_url = map.get('HttpCallbackURL')
        return self


class DescribeLiveAsrConfigResponseLiveAsrConfig(TeaModel):
    def __init__(self, live_asr_config_list=None):
        self.live_asr_config_list = live_asr_config_list  # type: List[DescribeLiveAsrConfigResponseLiveAsrConfigLiveAsrConfigList]

    def validate(self):
        self.validate_required(self.live_asr_config_list, 'live_asr_config_list')
        if self.live_asr_config_list:
            for k in self.live_asr_config_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['LiveAsrConfigList'] = []
        if self.live_asr_config_list is not None:
            for k in self.live_asr_config_list:
                result['LiveAsrConfigList'].append(k.to_map() if k else None)
        else:
            result['LiveAsrConfigList'] = None
        return result

    def from_map(self, map={}):
        self.live_asr_config_list = []
        if map.get('LiveAsrConfigList') is not None:
            for k in map.get('LiveAsrConfigList'):
                temp_model = DescribeLiveAsrConfigResponseLiveAsrConfigLiveAsrConfigList()
                self.live_asr_config_list.append(temp_model.from_map(k))
        else:
            self.live_asr_config_list = None
        return self


class DeleteLiveASRConfigRequest(TeaModel):
    def __init__(self, domain_name=None, app_name=None, stream_name=None):
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str
        self.stream_name = stream_name  # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.app_name, 'app_name')
        self.validate_required(self.stream_name, 'stream_name')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        result['StreamName'] = self.stream_name
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        self.stream_name = map.get('StreamName')
        return self


class DeleteLiveASRConfigResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class UpdateLiveASRConfigRequest(TeaModel):
    def __init__(self, domain_name=None, app_name=None, stream_name=None, mns_topic=None, mns_region=None,
                 period=None, http_callback_url=None):
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str
        self.stream_name = stream_name  # type: str
        self.mns_topic = mns_topic      # type: str
        self.mns_region = mns_region    # type: str
        self.period = period            # type: int
        self.http_callback_url = http_callback_url  # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.app_name, 'app_name')
        self.validate_required(self.stream_name, 'stream_name')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        result['StreamName'] = self.stream_name
        result['MnsTopic'] = self.mns_topic
        result['MnsRegion'] = self.mns_region
        result['Period'] = self.period
        result['HttpCallbackURL'] = self.http_callback_url
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        self.stream_name = map.get('StreamName')
        self.mns_topic = map.get('MnsTopic')
        self.mns_region = map.get('MnsRegion')
        self.period = map.get('Period')
        self.http_callback_url = map.get('HttpCallbackURL')
        return self


class UpdateLiveASRConfigResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DeleteMixStreamRequest(TeaModel):
    def __init__(self, domain_name=None, app_name=None, stream_name=None, mix_stream_id=None):
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str
        self.stream_name = stream_name  # type: str
        self.mix_stream_id = mix_stream_id  # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.mix_stream_id, 'mix_stream_id')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        result['StreamName'] = self.stream_name
        result['MixStreamId'] = self.mix_stream_id
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        self.stream_name = map.get('StreamName')
        self.mix_stream_id = map.get('MixStreamId')
        return self


class DeleteMixStreamResponse(TeaModel):
    def __init__(self, request_id=None, mix_stream_id=None):
        self.request_id = request_id    # type: str
        self.mix_stream_id = mix_stream_id  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.mix_stream_id, 'mix_stream_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['MixStreamId'] = self.mix_stream_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.mix_stream_id = map.get('MixStreamId')
        return self


class UpdateMixStreamRequest(TeaModel):
    def __init__(self, domain_name=None, mix_stream_id=None, input_stream_list=None, layout_id=None):
        self.domain_name = domain_name  # type: str
        self.mix_stream_id = mix_stream_id  # type: str
        self.input_stream_list = input_stream_list  # type: str
        self.layout_id = layout_id      # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.mix_stream_id, 'mix_stream_id')
        self.validate_required(self.input_stream_list, 'input_stream_list')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['MixStreamId'] = self.mix_stream_id
        result['InputStreamList'] = self.input_stream_list
        result['LayoutId'] = self.layout_id
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.mix_stream_id = map.get('MixStreamId')
        self.input_stream_list = map.get('InputStreamList')
        self.layout_id = map.get('LayoutId')
        return self


class UpdateMixStreamResponse(TeaModel):
    def __init__(self, request_id=None, mix_stream_id=None):
        self.request_id = request_id    # type: str
        self.mix_stream_id = mix_stream_id  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.mix_stream_id, 'mix_stream_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['MixStreamId'] = self.mix_stream_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.mix_stream_id = map.get('MixStreamId')
        return self


class CreateMixStreamRequest(TeaModel):
    def __init__(self, domain_name=None, layout_id=None, input_stream_list=None, output_config=None,
                 callback_config=None):
        self.domain_name = domain_name  # type: str
        self.layout_id = layout_id      # type: str
        self.input_stream_list = input_stream_list  # type: str
        self.output_config = output_config  # type: str
        self.callback_config = callback_config  # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.layout_id, 'layout_id')
        self.validate_required(self.input_stream_list, 'input_stream_list')
        self.validate_required(self.output_config, 'output_config')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['LayoutId'] = self.layout_id
        result['InputStreamList'] = self.input_stream_list
        result['OutputConfig'] = self.output_config
        result['CallbackConfig'] = self.callback_config
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.layout_id = map.get('LayoutId')
        self.input_stream_list = map.get('InputStreamList')
        self.output_config = map.get('OutputConfig')
        self.callback_config = map.get('CallbackConfig')
        return self


class CreateMixStreamResponse(TeaModel):
    def __init__(self, request_id=None, mix_stream_id=None):
        self.request_id = request_id    # type: str
        self.mix_stream_id = mix_stream_id  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.mix_stream_id, 'mix_stream_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['MixStreamId'] = self.mix_stream_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.mix_stream_id = map.get('MixStreamId')
        return self


class DescribeMixStreamListRequest(TeaModel):
    def __init__(self, domain_name=None, app_name=None, stream_name=None, mix_stream_id=None, start_time=None,
                 end_time=None, page_no=None, page_size=None):
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str
        self.stream_name = stream_name  # type: str
        self.mix_stream_id = mix_stream_id  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.page_no = page_no          # type: int
        self.page_size = page_size      # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        result['StreamName'] = self.stream_name
        result['MixStreamId'] = self.mix_stream_id
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['PageNo'] = self.page_no
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        self.stream_name = map.get('StreamName')
        self.mix_stream_id = map.get('MixStreamId')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.page_no = map.get('PageNo')
        self.page_size = map.get('PageSize')
        return self


class DescribeMixStreamListResponse(TeaModel):
    def __init__(self, request_id=None, total=None, mix_stream_list=None):
        self.request_id = request_id    # type: str
        self.total = total              # type: int
        self.mix_stream_list = mix_stream_list  # type: List[DescribeMixStreamListResponseMixStreamList]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total, 'total')
        self.validate_required(self.mix_stream_list, 'mix_stream_list')
        if self.mix_stream_list:
            for k in self.mix_stream_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Total'] = self.total
        result['MixStreamList'] = []
        if self.mix_stream_list is not None:
            for k in self.mix_stream_list:
                result['MixStreamList'].append(k.to_map() if k else None)
        else:
            result['MixStreamList'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total = map.get('Total')
        self.mix_stream_list = []
        if map.get('MixStreamList') is not None:
            for k in map.get('MixStreamList'):
                temp_model = DescribeMixStreamListResponseMixStreamList()
                self.mix_stream_list.append(temp_model.from_map(k))
        else:
            self.mix_stream_list = None
        return self


class DescribeMixStreamListResponseMixStreamList(TeaModel):
    def __init__(self, mixstream_id=None, domain_name=None, app_name=None, stream_name=None, layout_id=None,
                 input_stream_number=None, mix_stream_template=None, gmt_create=None, gmt_modified=None):
        self.mixstream_id = mixstream_id  # type: str
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str
        self.stream_name = stream_name  # type: str
        self.layout_id = layout_id      # type: str
        self.input_stream_number = input_stream_number  # type: int
        self.mix_stream_template = mix_stream_template  # type: str
        self.gmt_create = gmt_create    # type: str
        self.gmt_modified = gmt_modified  # type: str

    def validate(self):
        self.validate_required(self.mixstream_id, 'mixstream_id')
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.app_name, 'app_name')
        self.validate_required(self.stream_name, 'stream_name')
        self.validate_required(self.layout_id, 'layout_id')
        self.validate_required(self.input_stream_number, 'input_stream_number')
        self.validate_required(self.mix_stream_template, 'mix_stream_template')
        self.validate_required(self.gmt_create, 'gmt_create')
        self.validate_required(self.gmt_modified, 'gmt_modified')

    def to_map(self):
        result = {}
        result['MixstreamId'] = self.mixstream_id
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        result['StreamName'] = self.stream_name
        result['LayoutId'] = self.layout_id
        result['InputStreamNumber'] = self.input_stream_number
        result['MixStreamTemplate'] = self.mix_stream_template
        result['GmtCreate'] = self.gmt_create
        result['GmtModified'] = self.gmt_modified
        return result

    def from_map(self, map={}):
        self.mixstream_id = map.get('MixstreamId')
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        self.stream_name = map.get('StreamName')
        self.layout_id = map.get('LayoutId')
        self.input_stream_number = map.get('InputStreamNumber')
        self.mix_stream_template = map.get('MixStreamTemplate')
        self.gmt_create = map.get('GmtCreate')
        self.gmt_modified = map.get('GmtModified')
        return self


class AddRtsLiveStreamTranscodeRequest(TeaModel):
    def __init__(self, domain=None, app=None, template=None, template_type=None, height=None, width=None, fps=None,
                 video_bitrate=None, audio_bitrate=None, gop=None, delete_bframes=None, opus=None, profile=None,
                 audio_profile=None, audio_codec=None, audio_rate=None, audio_channel_num=None, lazy=None):
        self.domain = domain            # type: str
        self.app = app                  # type: str
        self.template = template        # type: str
        self.template_type = template_type  # type: str
        self.height = height            # type: int
        self.width = width              # type: int
        self.fps = fps                  # type: int
        self.video_bitrate = video_bitrate  # type: int
        self.audio_bitrate = audio_bitrate  # type: int
        self.gop = gop                  # type: str
        self.delete_bframes = delete_bframes  # type: bool
        self.opus = opus                # type: bool
        self.profile = profile          # type: int
        self.audio_profile = audio_profile  # type: str
        self.audio_codec = audio_codec  # type: str
        self.audio_rate = audio_rate    # type: int
        self.audio_channel_num = audio_channel_num  # type: int
        self.lazy = lazy                # type: str

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.app, 'app')
        self.validate_required(self.template, 'template')
        self.validate_required(self.template_type, 'template_type')

    def to_map(self):
        result = {}
        result['Domain'] = self.domain
        result['App'] = self.app
        result['Template'] = self.template
        result['TemplateType'] = self.template_type
        result['Height'] = self.height
        result['Width'] = self.width
        result['FPS'] = self.fps
        result['VideoBitrate'] = self.video_bitrate
        result['AudioBitrate'] = self.audio_bitrate
        result['Gop'] = self.gop
        result['DeleteBframes'] = self.delete_bframes
        result['Opus'] = self.opus
        result['Profile'] = self.profile
        result['AudioProfile'] = self.audio_profile
        result['AudioCodec'] = self.audio_codec
        result['AudioRate'] = self.audio_rate
        result['AudioChannelNum'] = self.audio_channel_num
        result['Lazy'] = self.lazy
        return result

    def from_map(self, map={}):
        self.domain = map.get('Domain')
        self.app = map.get('App')
        self.template = map.get('Template')
        self.template_type = map.get('TemplateType')
        self.height = map.get('Height')
        self.width = map.get('Width')
        self.fps = map.get('FPS')
        self.video_bitrate = map.get('VideoBitrate')
        self.audio_bitrate = map.get('AudioBitrate')
        self.gop = map.get('Gop')
        self.delete_bframes = map.get('DeleteBframes')
        self.opus = map.get('Opus')
        self.profile = map.get('Profile')
        self.audio_profile = map.get('AudioProfile')
        self.audio_codec = map.get('AudioCodec')
        self.audio_rate = map.get('AudioRate')
        self.audio_channel_num = map.get('AudioChannelNum')
        self.lazy = map.get('Lazy')
        return self


class AddRtsLiveStreamTranscodeResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeLiveDomainTimeShiftDataRequest(TeaModel):
    def __init__(self, domain_name=None, start_time=None, end_time=None, interval=None):
        self.domain_name = domain_name  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.interval = interval        # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['Interval'] = self.interval
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.interval = map.get('Interval')
        return self


class DescribeLiveDomainTimeShiftDataResponse(TeaModel):
    def __init__(self, request_id=None, time_shift_data=None):
        self.request_id = request_id    # type: str
        self.time_shift_data = time_shift_data  # type: DescribeLiveDomainTimeShiftDataResponseTimeShiftData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.time_shift_data, 'time_shift_data')
        if self.time_shift_data:
            self.time_shift_data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.time_shift_data is not None:
            result['TimeShiftData'] = self.time_shift_data.to_map()
        else:
            result['TimeShiftData'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('TimeShiftData') is not None:
            temp_model = DescribeLiveDomainTimeShiftDataResponseTimeShiftData()
            self.time_shift_data = temp_model.from_map(map['TimeShiftData'])
        else:
            self.time_shift_data = None
        return self


class DescribeLiveDomainTimeShiftDataResponseTimeShiftDataDataModule(TeaModel):
    def __init__(self, time_stamp=None, size=None, type=None):
        self.time_stamp = time_stamp    # type: str
        self.size = size                # type: str
        self.type = type                # type: str

    def validate(self):
        self.validate_required(self.time_stamp, 'time_stamp')
        self.validate_required(self.size, 'size')
        self.validate_required(self.type, 'type')

    def to_map(self):
        result = {}
        result['TimeStamp'] = self.time_stamp
        result['Size'] = self.size
        result['Type'] = self.type
        return result

    def from_map(self, map={}):
        self.time_stamp = map.get('TimeStamp')
        self.size = map.get('Size')
        self.type = map.get('Type')
        return self


class DescribeLiveDomainTimeShiftDataResponseTimeShiftData(TeaModel):
    def __init__(self, data_module=None):
        self.data_module = data_module  # type: List[DescribeLiveDomainTimeShiftDataResponseTimeShiftDataDataModule]

    def validate(self):
        self.validate_required(self.data_module, 'data_module')
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        else:
            result['DataModule'] = None
        return result

    def from_map(self, map={}):
        self.data_module = []
        if map.get('DataModule') is not None:
            for k in map.get('DataModule'):
                temp_model = DescribeLiveDomainTimeShiftDataResponseTimeShiftDataDataModule()
                self.data_module.append(temp_model.from_map(k))
        else:
            self.data_module = None
        return self


class DeleteHtmlResourceRequest(TeaModel):
    def __init__(self, html_resource_id=None, html_url=None, caster_id=None):
        self.html_resource_id = html_resource_id  # type: str
        self.html_url = html_url        # type: str
        self.caster_id = caster_id      # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['HtmlResourceId'] = self.html_resource_id
        result['htmlUrl'] = self.html_url
        result['CasterId'] = self.caster_id
        return result

    def from_map(self, map={}):
        self.html_resource_id = map.get('HtmlResourceId')
        self.html_url = map.get('htmlUrl')
        self.caster_id = map.get('CasterId')
        return self


class DeleteHtmlResourceResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeHtmlResourceRequest(TeaModel):
    def __init__(self, html_resource_id=None, html_url=None, caster_id=None):
        self.html_resource_id = html_resource_id  # type: str
        self.html_url = html_url        # type: str
        self.caster_id = caster_id      # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['HtmlResourceId'] = self.html_resource_id
        result['htmlUrl'] = self.html_url
        result['CasterId'] = self.caster_id
        return result

    def from_map(self, map={}):
        self.html_resource_id = map.get('HtmlResourceId')
        self.html_url = map.get('htmlUrl')
        self.caster_id = map.get('CasterId')
        return self


class DescribeHtmlResourceResponse(TeaModel):
    def __init__(self, request_id=None, html_resource=None):
        self.request_id = request_id    # type: str
        self.html_resource = html_resource  # type: DescribeHtmlResourceResponseHtmlResource

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.html_resource, 'html_resource')
        if self.html_resource:
            self.html_resource.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.html_resource is not None:
            result['HtmlResource'] = self.html_resource.to_map()
        else:
            result['HtmlResource'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('HtmlResource') is not None:
            temp_model = DescribeHtmlResourceResponseHtmlResource()
            self.html_resource = temp_model.from_map(map['HtmlResource'])
        else:
            self.html_resource = None
        return self


class DescribeHtmlResourceResponseHtmlResource(TeaModel):
    def __init__(self, html_resource_id=None, html_url=None, html_content=None, caster_id=None, config=None,
                 stream_id=None):
        self.html_resource_id = html_resource_id  # type: str
        self.html_url = html_url        # type: str
        self.html_content = html_content  # type: str
        self.caster_id = caster_id      # type: str
        self.config = config            # type: str
        self.stream_id = stream_id      # type: str

    def validate(self):
        self.validate_required(self.html_resource_id, 'html_resource_id')
        self.validate_required(self.html_url, 'html_url')
        self.validate_required(self.html_content, 'html_content')
        self.validate_required(self.caster_id, 'caster_id')
        self.validate_required(self.config, 'config')
        self.validate_required(self.stream_id, 'stream_id')

    def to_map(self):
        result = {}
        result['HtmlResourceId'] = self.html_resource_id
        result['HtmlUrl'] = self.html_url
        result['HtmlContent'] = self.html_content
        result['CasterId'] = self.caster_id
        result['Config'] = self.config
        result['StreamId'] = self.stream_id
        return result

    def from_map(self, map={}):
        self.html_resource_id = map.get('HtmlResourceId')
        self.html_url = map.get('HtmlUrl')
        self.html_content = map.get('HtmlContent')
        self.caster_id = map.get('CasterId')
        self.config = map.get('Config')
        self.stream_id = map.get('StreamId')
        return self


class ControlHtmlResourceRequest(TeaModel):
    def __init__(self, html_resource_id=None, html_url=None, caster_id=None, operate=None):
        self.html_resource_id = html_resource_id  # type: str
        self.html_url = html_url        # type: str
        self.caster_id = caster_id      # type: str
        self.operate = operate          # type: str

    def validate(self):
        self.validate_required(self.operate, 'operate')

    def to_map(self):
        result = {}
        result['HtmlResourceId'] = self.html_resource_id
        result['htmlUrl'] = self.html_url
        result['CasterId'] = self.caster_id
        result['Operate'] = self.operate
        return result

    def from_map(self, map={}):
        self.html_resource_id = map.get('HtmlResourceId')
        self.html_url = map.get('htmlUrl')
        self.caster_id = map.get('CasterId')
        self.operate = map.get('Operate')
        return self


class ControlHtmlResourceResponse(TeaModel):
    def __init__(self, request_id=None, stream_id=None):
        self.request_id = request_id    # type: str
        self.stream_id = stream_id      # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.stream_id, 'stream_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['StreamId'] = self.stream_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.stream_id = map.get('StreamId')
        return self


class EditHtmlResourceRequest(TeaModel):
    def __init__(self, html_resource_id=None, caster_id=None, html_url=None, html_content=None, config=None):
        self.html_resource_id = html_resource_id  # type: str
        self.caster_id = caster_id      # type: str
        self.html_url = html_url        # type: str
        self.html_content = html_content  # type: str
        self.config = config            # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['HtmlResourceId'] = self.html_resource_id
        result['CasterId'] = self.caster_id
        result['HtmlUrl'] = self.html_url
        result['htmlContent'] = self.html_content
        result['Config'] = self.config
        return result

    def from_map(self, map={}):
        self.html_resource_id = map.get('HtmlResourceId')
        self.caster_id = map.get('CasterId')
        self.html_url = map.get('HtmlUrl')
        self.html_content = map.get('htmlContent')
        self.config = map.get('Config')
        return self


class EditHtmlResourceResponse(TeaModel):
    def __init__(self, request_id=None, html_resource_id=None):
        self.request_id = request_id    # type: str
        self.html_resource_id = html_resource_id  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.html_resource_id, 'html_resource_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['HtmlResourceId'] = self.html_resource_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.html_resource_id = map.get('HtmlResourceId')
        return self


class DescribeLiveUserTagsRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        result = {}
        return result

    def from_map(self, map={}):
        return self


class DescribeLiveUserTagsResponse(TeaModel):
    def __init__(self, request_id=None, tags=None):
        self.request_id = request_id    # type: str
        self.tags = tags                # type: List[DescribeLiveUserTagsResponseTags]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.tags, 'tags')
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        else:
            result['Tags'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.tags = []
        if map.get('Tags') is not None:
            for k in map.get('Tags'):
                temp_model = DescribeLiveUserTagsResponseTags()
                self.tags.append(temp_model.from_map(k))
        else:
            self.tags = None
        return self


class DescribeLiveUserTagsResponseTags(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key                  # type: str
        self.value = value              # type: List[str]

    def validate(self):
        self.validate_required(self.key, 'key')
        self.validate_required(self.value, 'value')

    def to_map(self):
        result = {}
        result['Key'] = self.key
        result['Value'] = self.value
        return result

    def from_map(self, map={}):
        self.key = map.get('Key')
        self.value = map.get('Value')
        return self


class UnTagLiveResourcesRequest(TeaModel):
    def __init__(self, resource_id=None, resource_type=None, tag_key=None, all=None):
        self.resource_id = resource_id  # type: List[str]
        self.resource_type = resource_type  # type: str
        self.tag_key = tag_key          # type: List[str]
        self.all = all                  # type: bool

    def validate(self):
        self.validate_required(self.resource_id, 'resource_id')
        self.validate_required(self.resource_type, 'resource_type')

    def to_map(self):
        result = {}
        result['ResourceId'] = self.resource_id
        result['ResourceType'] = self.resource_type
        result['TagKey'] = self.tag_key
        result['All'] = self.all
        return result

    def from_map(self, map={}):
        self.resource_id = map.get('ResourceId')
        self.resource_type = map.get('ResourceType')
        self.tag_key = map.get('TagKey')
        self.all = map.get('All')
        return self


class UnTagLiveResourcesResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class TagLiveResourcesRequest(TeaModel):
    def __init__(self, resource_id=None, resource_type=None, tag=None):
        self.resource_id = resource_id  # type: List[str]
        self.resource_type = resource_type  # type: str
        self.tag = tag                  # type: List[TagLiveResourcesRequestTag]

    def validate(self):
        self.validate_required(self.resource_id, 'resource_id')
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.tag, 'tag')
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['ResourceId'] = self.resource_id
        result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        else:
            result['Tag'] = None
        return result

    def from_map(self, map={}):
        self.resource_id = map.get('ResourceId')
        self.resource_type = map.get('ResourceType')
        self.tag = []
        if map.get('Tag') is not None:
            for k in map.get('Tag'):
                temp_model = TagLiveResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        else:
            self.tag = None
        return self


class TagLiveResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key                  # type: str
        self.value = value              # type: str

    def validate(self):
        self.validate_required(self.key, 'key')

    def to_map(self):
        result = {}
        result['Key'] = self.key
        result['Value'] = self.value
        return result

    def from_map(self, map={}):
        self.key = map.get('Key')
        self.value = map.get('Value')
        return self


class TagLiveResourcesResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeLiveTagResourcesRequest(TeaModel):
    def __init__(self, resource_id=None, resource_type=None, tag=None):
        self.resource_id = resource_id  # type: List[str]
        self.resource_type = resource_type  # type: str
        self.tag = tag                  # type: List[DescribeLiveTagResourcesRequestTag]

    def validate(self):
        self.validate_required(self.resource_id, 'resource_id')
        self.validate_required(self.resource_type, 'resource_type')
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['ResourceId'] = self.resource_id
        result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        else:
            result['Tag'] = None
        return result

    def from_map(self, map={}):
        self.resource_id = map.get('ResourceId')
        self.resource_type = map.get('ResourceType')
        self.tag = []
        if map.get('Tag') is not None:
            for k in map.get('Tag'):
                temp_model = DescribeLiveTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        else:
            self.tag = None
        return self


class DescribeLiveTagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key                  # type: str
        self.value = value              # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['Key'] = self.key
        result['Value'] = self.value
        return result

    def from_map(self, map={}):
        self.key = map.get('Key')
        self.value = map.get('Value')
        return self


class DescribeLiveTagResourcesResponse(TeaModel):
    def __init__(self, request_id=None, tag_resources=None):
        self.request_id = request_id    # type: str
        self.tag_resources = tag_resources  # type: List[DescribeLiveTagResourcesResponseTagResources]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.tag_resources, 'tag_resources')
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['TagResources'].append(k.to_map() if k else None)
        else:
            result['TagResources'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.tag_resources = []
        if map.get('TagResources') is not None:
            for k in map.get('TagResources'):
                temp_model = DescribeLiveTagResourcesResponseTagResources()
                self.tag_resources.append(temp_model.from_map(k))
        else:
            self.tag_resources = None
        return self


class DescribeLiveTagResourcesResponseTagResourcesTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key                  # type: str
        self.value = value              # type: str

    def validate(self):
        self.validate_required(self.key, 'key')
        self.validate_required(self.value, 'value')

    def to_map(self):
        result = {}
        result['Key'] = self.key
        result['Value'] = self.value
        return result

    def from_map(self, map={}):
        self.key = map.get('Key')
        self.value = map.get('Value')
        return self


class DescribeLiveTagResourcesResponseTagResources(TeaModel):
    def __init__(self, resource_id=None, tag=None):
        self.resource_id = resource_id  # type: str
        self.tag = tag                  # type: List[DescribeLiveTagResourcesResponseTagResourcesTag]

    def validate(self):
        self.validate_required(self.resource_id, 'resource_id')
        self.validate_required(self.tag, 'tag')
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        else:
            result['Tag'] = None
        return result

    def from_map(self, map={}):
        self.resource_id = map.get('ResourceId')
        self.tag = []
        if map.get('Tag') is not None:
            for k in map.get('Tag'):
                temp_model = DescribeLiveTagResourcesResponseTagResourcesTag()
                self.tag.append(temp_model.from_map(k))
        else:
            self.tag = None
        return self


class AddLiveAudioAuditConfigRequest(TeaModel):
    def __init__(self, domain_name=None, app_name=None, stream_name=None, oss_bucket=None, oss_endpoint=None,
                 oss_object=None, biz_type=None):
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str
        self.stream_name = stream_name  # type: str
        self.oss_bucket = oss_bucket    # type: str
        self.oss_endpoint = oss_endpoint  # type: str
        self.oss_object = oss_object    # type: str
        self.biz_type = biz_type        # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.app_name, 'app_name')
        self.validate_required(self.stream_name, 'stream_name')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        result['StreamName'] = self.stream_name
        result['OssBucket'] = self.oss_bucket
        result['OssEndpoint'] = self.oss_endpoint
        result['OssObject'] = self.oss_object
        result['BizType'] = self.biz_type
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        self.stream_name = map.get('StreamName')
        self.oss_bucket = map.get('OssBucket')
        self.oss_endpoint = map.get('OssEndpoint')
        self.oss_object = map.get('OssObject')
        self.biz_type = map.get('BizType')
        return self


class AddLiveAudioAuditConfigResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DeleteLiveAudioAuditConfigRequest(TeaModel):
    def __init__(self, domain_name=None, app_name=None, stream_name=None):
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str
        self.stream_name = stream_name  # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.app_name, 'app_name')
        self.validate_required(self.stream_name, 'stream_name')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        result['StreamName'] = self.stream_name
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        self.stream_name = map.get('StreamName')
        return self


class DeleteLiveAudioAuditConfigResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeLiveAudioAuditConfigRequest(TeaModel):
    def __init__(self, domain_name=None, app_name=None, stream_name=None):
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str
        self.stream_name = stream_name  # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        result['StreamName'] = self.stream_name
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        self.stream_name = map.get('StreamName')
        return self


class DescribeLiveAudioAuditConfigResponse(TeaModel):
    def __init__(self, request_id=None, live_audio_audit_config_list=None):
        self.request_id = request_id    # type: str
        self.live_audio_audit_config_list = live_audio_audit_config_list  # type: DescribeLiveAudioAuditConfigResponseLiveAudioAuditConfigList

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.live_audio_audit_config_list, 'live_audio_audit_config_list')
        if self.live_audio_audit_config_list:
            self.live_audio_audit_config_list.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.live_audio_audit_config_list is not None:
            result['LiveAudioAuditConfigList'] = self.live_audio_audit_config_list.to_map()
        else:
            result['LiveAudioAuditConfigList'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('LiveAudioAuditConfigList') is not None:
            temp_model = DescribeLiveAudioAuditConfigResponseLiveAudioAuditConfigList()
            self.live_audio_audit_config_list = temp_model.from_map(map['LiveAudioAuditConfigList'])
        else:
            self.live_audio_audit_config_list = None
        return self


class DescribeLiveAudioAuditConfigResponseLiveAudioAuditConfigListLiveAudioAuditConfigScenes(TeaModel):
    def __init__(self, scene=None):
        # scene
        self.scene = scene              # type: List[str]

    def validate(self):
        self.validate_required(self.scene, 'scene')

    def to_map(self):
        result = {}
        result['scene'] = self.scene
        return result

    def from_map(self, map={}):
        self.scene = map.get('scene')
        return self


class DescribeLiveAudioAuditConfigResponseLiveAudioAuditConfigListLiveAudioAuditConfig(TeaModel):
    def __init__(self, domain_name=None, app_name=None, stream_name=None, biz_type=None, scenes=None):
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str
        self.stream_name = stream_name  # type: str
        self.biz_type = biz_type        # type: str
        self.scenes = scenes            # type: DescribeLiveAudioAuditConfigResponseLiveAudioAuditConfigListLiveAudioAuditConfigScenes

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.app_name, 'app_name')
        self.validate_required(self.stream_name, 'stream_name')
        self.validate_required(self.biz_type, 'biz_type')
        self.validate_required(self.scenes, 'scenes')
        if self.scenes:
            self.scenes.validate()

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        result['StreamName'] = self.stream_name
        result['BizType'] = self.biz_type
        if self.scenes is not None:
            result['Scenes'] = self.scenes.to_map()
        else:
            result['Scenes'] = None
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        self.stream_name = map.get('StreamName')
        self.biz_type = map.get('BizType')
        if map.get('Scenes') is not None:
            temp_model = DescribeLiveAudioAuditConfigResponseLiveAudioAuditConfigListLiveAudioAuditConfigScenes()
            self.scenes = temp_model.from_map(map['Scenes'])
        else:
            self.scenes = None
        return self


class DescribeLiveAudioAuditConfigResponseLiveAudioAuditConfigList(TeaModel):
    def __init__(self, live_audio_audit_config=None):
        self.live_audio_audit_config = live_audio_audit_config  # type: List[DescribeLiveAudioAuditConfigResponseLiveAudioAuditConfigListLiveAudioAuditConfig]

    def validate(self):
        self.validate_required(self.live_audio_audit_config, 'live_audio_audit_config')
        if self.live_audio_audit_config:
            for k in self.live_audio_audit_config:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['LiveAudioAuditConfig'] = []
        if self.live_audio_audit_config is not None:
            for k in self.live_audio_audit_config:
                result['LiveAudioAuditConfig'].append(k.to_map() if k else None)
        else:
            result['LiveAudioAuditConfig'] = None
        return result

    def from_map(self, map={}):
        self.live_audio_audit_config = []
        if map.get('LiveAudioAuditConfig') is not None:
            for k in map.get('LiveAudioAuditConfig'):
                temp_model = DescribeLiveAudioAuditConfigResponseLiveAudioAuditConfigListLiveAudioAuditConfig()
                self.live_audio_audit_config.append(temp_model.from_map(k))
        else:
            self.live_audio_audit_config = None
        return self


class UpdateLiveAudioAuditConfigRequest(TeaModel):
    def __init__(self, domain_name=None, app_name=None, stream_name=None, oss_bucket=None, oss_endpoint=None,
                 oss_object=None, biz_type=None):
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str
        self.stream_name = stream_name  # type: str
        self.oss_bucket = oss_bucket    # type: str
        self.oss_endpoint = oss_endpoint  # type: str
        self.oss_object = oss_object    # type: str
        self.biz_type = biz_type        # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.app_name, 'app_name')
        self.validate_required(self.stream_name, 'stream_name')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        result['StreamName'] = self.stream_name
        result['OssBucket'] = self.oss_bucket
        result['OssEndpoint'] = self.oss_endpoint
        result['OssObject'] = self.oss_object
        result['BizType'] = self.biz_type
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        self.stream_name = map.get('StreamName')
        self.oss_bucket = map.get('OssBucket')
        self.oss_endpoint = map.get('OssEndpoint')
        self.oss_object = map.get('OssObject')
        self.biz_type = map.get('BizType')
        return self


class UpdateLiveAudioAuditConfigResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class AddLiveAudioAuditNotifyConfigRequest(TeaModel):
    def __init__(self, domain_name=None, callback=None, callback_template=None):
        self.domain_name = domain_name  # type: str
        self.callback = callback        # type: str
        self.callback_template = callback_template  # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['Callback'] = self.callback
        result['CallbackTemplate'] = self.callback_template
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.callback = map.get('Callback')
        self.callback_template = map.get('CallbackTemplate')
        return self


class AddLiveAudioAuditNotifyConfigResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DeleteLiveAudioAuditNotifyConfigRequest(TeaModel):
    def __init__(self, domain_name=None):
        self.domain_name = domain_name  # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        return self


class DeleteLiveAudioAuditNotifyConfigResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeLiveAudioAuditNotifyConfigRequest(TeaModel):
    def __init__(self, domain_name=None):
        self.domain_name = domain_name  # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        return self


class DescribeLiveAudioAuditNotifyConfigResponse(TeaModel):
    def __init__(self, request_id=None, live_audio_audit_notify_config_list=None):
        self.request_id = request_id    # type: str
        self.live_audio_audit_notify_config_list = live_audio_audit_notify_config_list  # type: DescribeLiveAudioAuditNotifyConfigResponseLiveAudioAuditNotifyConfigList

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.live_audio_audit_notify_config_list, 'live_audio_audit_notify_config_list')
        if self.live_audio_audit_notify_config_list:
            self.live_audio_audit_notify_config_list.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.live_audio_audit_notify_config_list is not None:
            result['LiveAudioAuditNotifyConfigList'] = self.live_audio_audit_notify_config_list.to_map()
        else:
            result['LiveAudioAuditNotifyConfigList'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('LiveAudioAuditNotifyConfigList') is not None:
            temp_model = DescribeLiveAudioAuditNotifyConfigResponseLiveAudioAuditNotifyConfigList()
            self.live_audio_audit_notify_config_list = temp_model.from_map(map['LiveAudioAuditNotifyConfigList'])
        else:
            self.live_audio_audit_notify_config_list = None
        return self


class DescribeLiveAudioAuditNotifyConfigResponseLiveAudioAuditNotifyConfigListLiveAudioAuditNotifyConfig(TeaModel):
    def __init__(self, domain_name=None, callback=None, callback_template=None):
        self.domain_name = domain_name  # type: str
        self.callback = callback        # type: str
        self.callback_template = callback_template  # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.callback, 'callback')
        self.validate_required(self.callback_template, 'callback_template')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['Callback'] = self.callback
        result['CallbackTemplate'] = self.callback_template
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.callback = map.get('Callback')
        self.callback_template = map.get('CallbackTemplate')
        return self


class DescribeLiveAudioAuditNotifyConfigResponseLiveAudioAuditNotifyConfigList(TeaModel):
    def __init__(self, live_audio_audit_notify_config=None):
        self.live_audio_audit_notify_config = live_audio_audit_notify_config  # type: List[DescribeLiveAudioAuditNotifyConfigResponseLiveAudioAuditNotifyConfigListLiveAudioAuditNotifyConfig]

    def validate(self):
        self.validate_required(self.live_audio_audit_notify_config, 'live_audio_audit_notify_config')
        if self.live_audio_audit_notify_config:
            for k in self.live_audio_audit_notify_config:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['LiveAudioAuditNotifyConfig'] = []
        if self.live_audio_audit_notify_config is not None:
            for k in self.live_audio_audit_notify_config:
                result['LiveAudioAuditNotifyConfig'].append(k.to_map() if k else None)
        else:
            result['LiveAudioAuditNotifyConfig'] = None
        return result

    def from_map(self, map={}):
        self.live_audio_audit_notify_config = []
        if map.get('LiveAudioAuditNotifyConfig') is not None:
            for k in map.get('LiveAudioAuditNotifyConfig'):
                temp_model = DescribeLiveAudioAuditNotifyConfigResponseLiveAudioAuditNotifyConfigListLiveAudioAuditNotifyConfig()
                self.live_audio_audit_notify_config.append(temp_model.from_map(k))
        else:
            self.live_audio_audit_notify_config = None
        return self


class UpdateLiveAudioAuditNotifyConfigRequest(TeaModel):
    def __init__(self, domain_name=None, callback=None, callback_template=None):
        self.domain_name = domain_name  # type: str
        self.callback = callback        # type: str
        self.callback_template = callback_template  # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['Callback'] = self.callback
        result['CallbackTemplate'] = self.callback_template
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.callback = map.get('Callback')
        self.callback_template = map.get('CallbackTemplate')
        return self


class UpdateLiveAudioAuditNotifyConfigResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeLiveDomainPushTrafficDataRequest(TeaModel):
    def __init__(self, domain_name=None, start_time=None, end_time=None, interval=None, isp_name_en=None,
                 location_name_en=None):
        self.domain_name = domain_name  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.interval = interval        # type: str
        self.isp_name_en = isp_name_en  # type: str
        self.location_name_en = location_name_en  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['Interval'] = self.interval
        result['IspNameEn'] = self.isp_name_en
        result['LocationNameEn'] = self.location_name_en
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.interval = map.get('Interval')
        self.isp_name_en = map.get('IspNameEn')
        self.location_name_en = map.get('LocationNameEn')
        return self


class DescribeLiveDomainPushTrafficDataResponse(TeaModel):
    def __init__(self, request_id=None, domain_name=None, start_time=None, end_time=None, data_interval=None,
                 traffic_data_per_interval=None):
        self.request_id = request_id    # type: str
        self.domain_name = domain_name  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.data_interval = data_interval  # type: str
        self.traffic_data_per_interval = traffic_data_per_interval  # type: DescribeLiveDomainPushTrafficDataResponseTrafficDataPerInterval

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.data_interval, 'data_interval')
        self.validate_required(self.traffic_data_per_interval, 'traffic_data_per_interval')
        if self.traffic_data_per_interval:
            self.traffic_data_per_interval.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DomainName'] = self.domain_name
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['DataInterval'] = self.data_interval
        if self.traffic_data_per_interval is not None:
            result['TrafficDataPerInterval'] = self.traffic_data_per_interval.to_map()
        else:
            result['TrafficDataPerInterval'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.domain_name = map.get('DomainName')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.data_interval = map.get('DataInterval')
        if map.get('TrafficDataPerInterval') is not None:
            temp_model = DescribeLiveDomainPushTrafficDataResponseTrafficDataPerInterval()
            self.traffic_data_per_interval = temp_model.from_map(map['TrafficDataPerInterval'])
        else:
            self.traffic_data_per_interval = None
        return self


class DescribeLiveDomainPushTrafficDataResponseTrafficDataPerIntervalDataModule(TeaModel):
    def __init__(self, time_stamp=None, traffic_value=None):
        self.time_stamp = time_stamp    # type: str
        self.traffic_value = traffic_value  # type: str

    def validate(self):
        self.validate_required(self.time_stamp, 'time_stamp')
        self.validate_required(self.traffic_value, 'traffic_value')

    def to_map(self):
        result = {}
        result['TimeStamp'] = self.time_stamp
        result['TrafficValue'] = self.traffic_value
        return result

    def from_map(self, map={}):
        self.time_stamp = map.get('TimeStamp')
        self.traffic_value = map.get('TrafficValue')
        return self


class DescribeLiveDomainPushTrafficDataResponseTrafficDataPerInterval(TeaModel):
    def __init__(self, data_module=None):
        self.data_module = data_module  # type: List[DescribeLiveDomainPushTrafficDataResponseTrafficDataPerIntervalDataModule]

    def validate(self):
        self.validate_required(self.data_module, 'data_module')
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        else:
            result['DataModule'] = None
        return result

    def from_map(self, map={}):
        self.data_module = []
        if map.get('DataModule') is not None:
            for k in map.get('DataModule'):
                temp_model = DescribeLiveDomainPushTrafficDataResponseTrafficDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        else:
            self.data_module = None
        return self


class DescribeLiveDomainPushBpsDataRequest(TeaModel):
    def __init__(self, domain_name=None, start_time=None, end_time=None, interval=None, isp_name_en=None,
                 location_name_en=None):
        self.domain_name = domain_name  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.interval = interval        # type: str
        self.isp_name_en = isp_name_en  # type: str
        self.location_name_en = location_name_en  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['Interval'] = self.interval
        result['IspNameEn'] = self.isp_name_en
        result['LocationNameEn'] = self.location_name_en
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.interval = map.get('Interval')
        self.isp_name_en = map.get('IspNameEn')
        self.location_name_en = map.get('LocationNameEn')
        return self


class DescribeLiveDomainPushBpsDataResponse(TeaModel):
    def __init__(self, request_id=None, domain_name=None, start_time=None, end_time=None, data_interval=None,
                 bps_data_per_interval=None):
        self.request_id = request_id    # type: str
        self.domain_name = domain_name  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.data_interval = data_interval  # type: str
        self.bps_data_per_interval = bps_data_per_interval  # type: DescribeLiveDomainPushBpsDataResponseBpsDataPerInterval

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.data_interval, 'data_interval')
        self.validate_required(self.bps_data_per_interval, 'bps_data_per_interval')
        if self.bps_data_per_interval:
            self.bps_data_per_interval.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DomainName'] = self.domain_name
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['DataInterval'] = self.data_interval
        if self.bps_data_per_interval is not None:
            result['BpsDataPerInterval'] = self.bps_data_per_interval.to_map()
        else:
            result['BpsDataPerInterval'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.domain_name = map.get('DomainName')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.data_interval = map.get('DataInterval')
        if map.get('BpsDataPerInterval') is not None:
            temp_model = DescribeLiveDomainPushBpsDataResponseBpsDataPerInterval()
            self.bps_data_per_interval = temp_model.from_map(map['BpsDataPerInterval'])
        else:
            self.bps_data_per_interval = None
        return self


class DescribeLiveDomainPushBpsDataResponseBpsDataPerIntervalDataModule(TeaModel):
    def __init__(self, time_stamp=None, bps_value=None):
        self.time_stamp = time_stamp    # type: str
        self.bps_value = bps_value      # type: str

    def validate(self):
        self.validate_required(self.time_stamp, 'time_stamp')
        self.validate_required(self.bps_value, 'bps_value')

    def to_map(self):
        result = {}
        result['TimeStamp'] = self.time_stamp
        result['BpsValue'] = self.bps_value
        return result

    def from_map(self, map={}):
        self.time_stamp = map.get('TimeStamp')
        self.bps_value = map.get('BpsValue')
        return self


class DescribeLiveDomainPushBpsDataResponseBpsDataPerInterval(TeaModel):
    def __init__(self, data_module=None):
        self.data_module = data_module  # type: List[DescribeLiveDomainPushBpsDataResponseBpsDataPerIntervalDataModule]

    def validate(self):
        self.validate_required(self.data_module, 'data_module')
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        else:
            result['DataModule'] = None
        return result

    def from_map(self, map={}):
        self.data_module = []
        if map.get('DataModule') is not None:
            for k in map.get('DataModule'):
                temp_model = DescribeLiveDomainPushBpsDataResponseBpsDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        else:
            self.data_module = None
        return self


class SetCasterSyncGroupRequest(TeaModel):
    def __init__(self, caster_id=None, sync_group=None):
        self.caster_id = caster_id      # type: str
        self.sync_group = sync_group    # type: List[SetCasterSyncGroupRequestSyncGroup]

    def validate(self):
        self.validate_required(self.caster_id, 'caster_id')
        if self.sync_group:
            for k in self.sync_group:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['CasterId'] = self.caster_id
        result['SyncGroup'] = []
        if self.sync_group is not None:
            for k in self.sync_group:
                result['SyncGroup'].append(k.to_map() if k else None)
        else:
            result['SyncGroup'] = None
        return result

    def from_map(self, map={}):
        self.caster_id = map.get('CasterId')
        self.sync_group = []
        if map.get('SyncGroup') is not None:
            for k in map.get('SyncGroup'):
                temp_model = SetCasterSyncGroupRequestSyncGroup()
                self.sync_group.append(temp_model.from_map(k))
        else:
            self.sync_group = None
        return self


class SetCasterSyncGroupRequestSyncGroup(TeaModel):
    def __init__(self, mode=None, sync_delay_threshold=None, host_resource_id=None, resource_ids=None):
        self.mode = mode                # type: int
        self.sync_delay_threshold = sync_delay_threshold  # type: int
        self.host_resource_id = host_resource_id  # type: str
        self.resource_ids = resource_ids  # type: List[str]

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['Mode'] = self.mode
        result['SyncDelayThreshold'] = self.sync_delay_threshold
        result['HostResourceId'] = self.host_resource_id
        result['ResourceIds'] = self.resource_ids
        return result

    def from_map(self, map={}):
        self.mode = map.get('Mode')
        self.sync_delay_threshold = map.get('SyncDelayThreshold')
        self.host_resource_id = map.get('HostResourceId')
        self.resource_ids = map.get('ResourceIds')
        return self


class SetCasterSyncGroupResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeCasterSyncGroupRequest(TeaModel):
    def __init__(self, caster_id=None):
        self.caster_id = caster_id      # type: str

    def validate(self):
        self.validate_required(self.caster_id, 'caster_id')

    def to_map(self):
        result = {}
        result['CasterId'] = self.caster_id
        return result

    def from_map(self, map={}):
        self.caster_id = map.get('CasterId')
        return self


class DescribeCasterSyncGroupResponse(TeaModel):
    def __init__(self, request_id=None, caster_id=None, sync_groups=None):
        self.request_id = request_id    # type: str
        self.caster_id = caster_id      # type: str
        self.sync_groups = sync_groups  # type: DescribeCasterSyncGroupResponseSyncGroups

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.caster_id, 'caster_id')
        self.validate_required(self.sync_groups, 'sync_groups')
        if self.sync_groups:
            self.sync_groups.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['CasterId'] = self.caster_id
        if self.sync_groups is not None:
            result['SyncGroups'] = self.sync_groups.to_map()
        else:
            result['SyncGroups'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.caster_id = map.get('CasterId')
        if map.get('SyncGroups') is not None:
            temp_model = DescribeCasterSyncGroupResponseSyncGroups()
            self.sync_groups = temp_model.from_map(map['SyncGroups'])
        else:
            self.sync_groups = None
        return self


class DescribeCasterSyncGroupResponseSyncGroupsSyncGroupResourceIds(TeaModel):
    def __init__(self, resource_id=None):
        # ResourceId
        self.resource_id = resource_id  # type: List[str]

    def validate(self):
        self.validate_required(self.resource_id, 'resource_id')

    def to_map(self):
        result = {}
        result['ResourceId'] = self.resource_id
        return result

    def from_map(self, map={}):
        self.resource_id = map.get('ResourceId')
        return self


class DescribeCasterSyncGroupResponseSyncGroupsSyncGroup(TeaModel):
    def __init__(self, mode=None, host_resource_id=None, resource_ids=None):
        self.mode = mode                # type: int
        self.host_resource_id = host_resource_id  # type: str
        self.resource_ids = resource_ids  # type: DescribeCasterSyncGroupResponseSyncGroupsSyncGroupResourceIds

    def validate(self):
        self.validate_required(self.mode, 'mode')
        self.validate_required(self.host_resource_id, 'host_resource_id')
        self.validate_required(self.resource_ids, 'resource_ids')
        if self.resource_ids:
            self.resource_ids.validate()

    def to_map(self):
        result = {}
        result['Mode'] = self.mode
        result['HostResourceId'] = self.host_resource_id
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids.to_map()
        else:
            result['ResourceIds'] = None
        return result

    def from_map(self, map={}):
        self.mode = map.get('Mode')
        self.host_resource_id = map.get('HostResourceId')
        if map.get('ResourceIds') is not None:
            temp_model = DescribeCasterSyncGroupResponseSyncGroupsSyncGroupResourceIds()
            self.resource_ids = temp_model.from_map(map['ResourceIds'])
        else:
            self.resource_ids = None
        return self


class DescribeCasterSyncGroupResponseSyncGroups(TeaModel):
    def __init__(self, sync_group=None):
        self.sync_group = sync_group    # type: List[DescribeCasterSyncGroupResponseSyncGroupsSyncGroup]

    def validate(self):
        self.validate_required(self.sync_group, 'sync_group')
        if self.sync_group:
            for k in self.sync_group:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['SyncGroup'] = []
        if self.sync_group is not None:
            for k in self.sync_group:
                result['SyncGroup'].append(k.to_map() if k else None)
        else:
            result['SyncGroup'] = None
        return result

    def from_map(self, map={}):
        self.sync_group = []
        if map.get('SyncGroup') is not None:
            for k in map.get('SyncGroup'):
                temp_model = DescribeCasterSyncGroupResponseSyncGroupsSyncGroup()
                self.sync_group.append(temp_model.from_map(k))
        else:
            self.sync_group = None
        return self


class DescribeLiveDetectPornDataRequest(TeaModel):
    def __init__(self, domain_name=None, start_time=None, end_time=None, app=None, stream=None, fee=None, scene=None,
                 region=None, split_by=None):
        self.domain_name = domain_name  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.app = app                  # type: str
        self.stream = stream            # type: str
        self.fee = fee                  # type: str
        self.scene = scene              # type: str
        self.region = region            # type: str
        self.split_by = split_by        # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['App'] = self.app
        result['Stream'] = self.stream
        result['Fee'] = self.fee
        result['Scene'] = self.scene
        result['Region'] = self.region
        result['SplitBy'] = self.split_by
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.app = map.get('App')
        self.stream = map.get('Stream')
        self.fee = map.get('Fee')
        self.scene = map.get('Scene')
        self.region = map.get('Region')
        self.split_by = map.get('SplitBy')
        return self


class DescribeLiveDetectPornDataResponse(TeaModel):
    def __init__(self, request_id=None, detect_porn_data=None):
        self.request_id = request_id    # type: str
        self.detect_porn_data = detect_porn_data  # type: DescribeLiveDetectPornDataResponseDetectPornData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.detect_porn_data, 'detect_porn_data')
        if self.detect_porn_data:
            self.detect_porn_data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.detect_porn_data is not None:
            result['DetectPornData'] = self.detect_porn_data.to_map()
        else:
            result['DetectPornData'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('DetectPornData') is not None:
            temp_model = DescribeLiveDetectPornDataResponseDetectPornData()
            self.detect_porn_data = temp_model.from_map(map['DetectPornData'])
        else:
            self.detect_porn_data = None
        return self


class DescribeLiveDetectPornDataResponseDetectPornDataDataModule(TeaModel):
    def __init__(self, time_stamp=None, app=None, domain=None, stream=None, fee=None, scene=None, region=None,
                 count=None):
        self.time_stamp = time_stamp    # type: str
        self.app = app                  # type: str
        self.domain = domain            # type: str
        self.stream = stream            # type: str
        self.fee = fee                  # type: str
        self.scene = scene              # type: str
        self.region = region            # type: str
        self.count = count              # type: int

    def validate(self):
        self.validate_required(self.time_stamp, 'time_stamp')
        self.validate_required(self.app, 'app')
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.stream, 'stream')
        self.validate_required(self.fee, 'fee')
        self.validate_required(self.scene, 'scene')
        self.validate_required(self.region, 'region')
        self.validate_required(self.count, 'count')

    def to_map(self):
        result = {}
        result['TimeStamp'] = self.time_stamp
        result['App'] = self.app
        result['Domain'] = self.domain
        result['Stream'] = self.stream
        result['Fee'] = self.fee
        result['Scene'] = self.scene
        result['Region'] = self.region
        result['Count'] = self.count
        return result

    def from_map(self, map={}):
        self.time_stamp = map.get('TimeStamp')
        self.app = map.get('App')
        self.domain = map.get('Domain')
        self.stream = map.get('Stream')
        self.fee = map.get('Fee')
        self.scene = map.get('Scene')
        self.region = map.get('Region')
        self.count = map.get('Count')
        return self


class DescribeLiveDetectPornDataResponseDetectPornData(TeaModel):
    def __init__(self, data_module=None):
        self.data_module = data_module  # type: List[DescribeLiveDetectPornDataResponseDetectPornDataDataModule]

    def validate(self):
        self.validate_required(self.data_module, 'data_module')
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        else:
            result['DataModule'] = None
        return result

    def from_map(self, map={}):
        self.data_module = []
        if map.get('DataModule') is not None:
            for k in map.get('DataModule'):
                temp_model = DescribeLiveDetectPornDataResponseDetectPornDataDataModule()
                self.data_module.append(temp_model.from_map(k))
        else:
            self.data_module = None
        return self


class DeleteLiveRealTimeLogLogstoreRequest(TeaModel):
    def __init__(self, project=None, logstore=None, region=None):
        self.project = project          # type: str
        self.logstore = logstore        # type: str
        self.region = region            # type: str

    def validate(self):
        self.validate_required(self.project, 'project')
        self.validate_required(self.logstore, 'logstore')
        self.validate_required(self.region, 'region')

    def to_map(self):
        result = {}
        result['Project'] = self.project
        result['Logstore'] = self.logstore
        result['Region'] = self.region
        return result

    def from_map(self, map={}):
        self.project = map.get('Project')
        self.logstore = map.get('Logstore')
        self.region = map.get('Region')
        return self


class DeleteLiveRealTimeLogLogstoreResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DisableLiveRealtimeLogDeliveryRequest(TeaModel):
    def __init__(self, domain_name=None):
        self.domain_name = domain_name  # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        return self


class DisableLiveRealtimeLogDeliveryResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class EnableLiveRealtimeLogDeliveryRequest(TeaModel):
    def __init__(self, domain_name=None):
        self.domain_name = domain_name  # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        return self


class EnableLiveRealtimeLogDeliveryResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ListLiveRealtimeLogDeliveryDomainsRequest(TeaModel):
    def __init__(self, project=None, logstore=None, region=None):
        self.project = project          # type: str
        self.logstore = logstore        # type: str
        self.region = region            # type: str

    def validate(self):
        self.validate_required(self.project, 'project')
        self.validate_required(self.logstore, 'logstore')
        self.validate_required(self.region, 'region')

    def to_map(self):
        result = {}
        result['Project'] = self.project
        result['Logstore'] = self.logstore
        result['Region'] = self.region
        return result

    def from_map(self, map={}):
        self.project = map.get('Project')
        self.logstore = map.get('Logstore')
        self.region = map.get('Region')
        return self


class ListLiveRealtimeLogDeliveryDomainsResponse(TeaModel):
    def __init__(self, request_id=None, content=None):
        self.request_id = request_id    # type: str
        self.content = content          # type: ListLiveRealtimeLogDeliveryDomainsResponseContent

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.content, 'content')
        if self.content:
            self.content.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.content is not None:
            result['Content'] = self.content.to_map()
        else:
            result['Content'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Content') is not None:
            temp_model = ListLiveRealtimeLogDeliveryDomainsResponseContent()
            self.content = temp_model.from_map(map['Content'])
        else:
            self.content = None
        return self


class ListLiveRealtimeLogDeliveryDomainsResponseContentDomains(TeaModel):
    def __init__(self, domain_name=None, status=None):
        self.domain_name = domain_name  # type: str
        self.status = status            # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.status, 'status')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['Status'] = self.status
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.status = map.get('Status')
        return self


class ListLiveRealtimeLogDeliveryDomainsResponseContent(TeaModel):
    def __init__(self, domains=None):
        self.domains = domains          # type: List[ListLiveRealtimeLogDeliveryDomainsResponseContentDomains]

    def validate(self):
        self.validate_required(self.domains, 'domains')
        if self.domains:
            for k in self.domains:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Domains'] = []
        if self.domains is not None:
            for k in self.domains:
                result['Domains'].append(k.to_map() if k else None)
        else:
            result['Domains'] = None
        return result

    def from_map(self, map={}):
        self.domains = []
        if map.get('Domains') is not None:
            for k in map.get('Domains'):
                temp_model = ListLiveRealtimeLogDeliveryDomainsResponseContentDomains()
                self.domains.append(temp_model.from_map(k))
        else:
            self.domains = None
        return self


class ModifyLiveRealtimeLogDeliveryRequest(TeaModel):
    def __init__(self, project=None, logstore=None, region=None, domain_name=None):
        self.project = project          # type: str
        self.logstore = logstore        # type: str
        self.region = region            # type: str
        self.domain_name = domain_name  # type: str

    def validate(self):
        self.validate_required(self.project, 'project')
        self.validate_required(self.logstore, 'logstore')
        self.validate_required(self.region, 'region')
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = {}
        result['Project'] = self.project
        result['Logstore'] = self.logstore
        result['Region'] = self.region
        result['DomainName'] = self.domain_name
        return result

    def from_map(self, map={}):
        self.project = map.get('Project')
        self.logstore = map.get('Logstore')
        self.region = map.get('Region')
        self.domain_name = map.get('DomainName')
        return self


class ModifyLiveRealtimeLogDeliveryResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeLiveRealtimeDeliveryAccRequest(TeaModel):
    def __init__(self, start_time=None, end_time=None, interval=None, project=None, log_store=None):
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.interval = interval        # type: str
        self.project = project          # type: str
        self.log_store = log_store      # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['Interval'] = self.interval
        result['Project'] = self.project
        result['LogStore'] = self.log_store
        return result

    def from_map(self, map={}):
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.interval = map.get('Interval')
        self.project = map.get('Project')
        self.log_store = map.get('LogStore')
        return self


class DescribeLiveRealtimeDeliveryAccResponse(TeaModel):
    def __init__(self, request_id=None, real_time_delivery_acc_data=None):
        self.request_id = request_id    # type: str
        self.real_time_delivery_acc_data = real_time_delivery_acc_data  # type: DescribeLiveRealtimeDeliveryAccResponseRealTimeDeliveryAccData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.real_time_delivery_acc_data, 'real_time_delivery_acc_data')
        if self.real_time_delivery_acc_data:
            self.real_time_delivery_acc_data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.real_time_delivery_acc_data is not None:
            result['RealTimeDeliveryAccData'] = self.real_time_delivery_acc_data.to_map()
        else:
            result['RealTimeDeliveryAccData'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('RealTimeDeliveryAccData') is not None:
            temp_model = DescribeLiveRealtimeDeliveryAccResponseRealTimeDeliveryAccData()
            self.real_time_delivery_acc_data = temp_model.from_map(map['RealTimeDeliveryAccData'])
        else:
            self.real_time_delivery_acc_data = None
        return self


class DescribeLiveRealtimeDeliveryAccResponseRealTimeDeliveryAccDataAccData(TeaModel):
    def __init__(self, time_stamp=None, success_num=None, failed_num=None):
        self.time_stamp = time_stamp    # type: str
        self.success_num = success_num  # type: int
        self.failed_num = failed_num    # type: int

    def validate(self):
        self.validate_required(self.time_stamp, 'time_stamp')
        self.validate_required(self.success_num, 'success_num')
        self.validate_required(self.failed_num, 'failed_num')

    def to_map(self):
        result = {}
        result['TimeStamp'] = self.time_stamp
        result['SuccessNum'] = self.success_num
        result['FailedNum'] = self.failed_num
        return result

    def from_map(self, map={}):
        self.time_stamp = map.get('TimeStamp')
        self.success_num = map.get('SuccessNum')
        self.failed_num = map.get('FailedNum')
        return self


class DescribeLiveRealtimeDeliveryAccResponseRealTimeDeliveryAccData(TeaModel):
    def __init__(self, acc_data=None):
        self.acc_data = acc_data        # type: List[DescribeLiveRealtimeDeliveryAccResponseRealTimeDeliveryAccDataAccData]

    def validate(self):
        self.validate_required(self.acc_data, 'acc_data')
        if self.acc_data:
            for k in self.acc_data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['AccData'] = []
        if self.acc_data is not None:
            for k in self.acc_data:
                result['AccData'].append(k.to_map() if k else None)
        else:
            result['AccData'] = None
        return result

    def from_map(self, map={}):
        self.acc_data = []
        if map.get('AccData') is not None:
            for k in map.get('AccData'):
                temp_model = DescribeLiveRealtimeDeliveryAccResponseRealTimeDeliveryAccDataAccData()
                self.acc_data.append(temp_model.from_map(k))
        else:
            self.acc_data = None
        return self


class DescribeLiveRealtimeLogAuthorizedRequest(TeaModel):
    def __init__(self, live_openapi_reserve=None):
        self.live_openapi_reserve = live_openapi_reserve  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['LiveOpenapiReserve'] = self.live_openapi_reserve
        return result

    def from_map(self, map={}):
        self.live_openapi_reserve = map.get('LiveOpenapiReserve')
        return self


class DescribeLiveRealtimeLogAuthorizedResponse(TeaModel):
    def __init__(self, request_id=None, authorized_status=None):
        self.request_id = request_id    # type: str
        self.authorized_status = authorized_status  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.authorized_status, 'authorized_status')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['AuthorizedStatus'] = self.authorized_status
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.authorized_status = map.get('AuthorizedStatus')
        return self


class ListLiveRealtimeLogDeliveryRequest(TeaModel):
    def __init__(self, live_openapi_reserve=None):
        self.live_openapi_reserve = live_openapi_reserve  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['LiveOpenapiReserve'] = self.live_openapi_reserve
        return result

    def from_map(self, map={}):
        self.live_openapi_reserve = map.get('LiveOpenapiReserve')
        return self


class ListLiveRealtimeLogDeliveryResponse(TeaModel):
    def __init__(self, request_id=None, content=None):
        self.request_id = request_id    # type: str
        self.content = content          # type: ListLiveRealtimeLogDeliveryResponseContent

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.content, 'content')
        if self.content:
            self.content.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.content is not None:
            result['Content'] = self.content.to_map()
        else:
            result['Content'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Content') is not None:
            temp_model = ListLiveRealtimeLogDeliveryResponseContent()
            self.content = temp_model.from_map(map['Content'])
        else:
            self.content = None
        return self


class ListLiveRealtimeLogDeliveryResponseContentRealtimeLogDeliveryInfo(TeaModel):
    def __init__(self, project=None, logstore=None, region=None, domain_name=None, dm_id=None, status=None):
        self.project = project          # type: str
        self.logstore = logstore        # type: str
        self.region = region            # type: str
        self.domain_name = domain_name  # type: str
        self.dm_id = dm_id              # type: int
        self.status = status            # type: str

    def validate(self):
        self.validate_required(self.project, 'project')
        self.validate_required(self.logstore, 'logstore')
        self.validate_required(self.region, 'region')
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.dm_id, 'dm_id')
        self.validate_required(self.status, 'status')

    def to_map(self):
        result = {}
        result['Project'] = self.project
        result['Logstore'] = self.logstore
        result['Region'] = self.region
        result['DomainName'] = self.domain_name
        result['DmId'] = self.dm_id
        result['Status'] = self.status
        return result

    def from_map(self, map={}):
        self.project = map.get('Project')
        self.logstore = map.get('Logstore')
        self.region = map.get('Region')
        self.domain_name = map.get('DomainName')
        self.dm_id = map.get('DmId')
        self.status = map.get('Status')
        return self


class ListLiveRealtimeLogDeliveryResponseContent(TeaModel):
    def __init__(self, realtime_log_delivery_info=None):
        self.realtime_log_delivery_info = realtime_log_delivery_info  # type: List[ListLiveRealtimeLogDeliveryResponseContentRealtimeLogDeliveryInfo]

    def validate(self):
        self.validate_required(self.realtime_log_delivery_info, 'realtime_log_delivery_info')
        if self.realtime_log_delivery_info:
            for k in self.realtime_log_delivery_info:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RealtimeLogDeliveryInfo'] = []
        if self.realtime_log_delivery_info is not None:
            for k in self.realtime_log_delivery_info:
                result['RealtimeLogDeliveryInfo'].append(k.to_map() if k else None)
        else:
            result['RealtimeLogDeliveryInfo'] = None
        return result

    def from_map(self, map={}):
        self.realtime_log_delivery_info = []
        if map.get('RealtimeLogDeliveryInfo') is not None:
            for k in map.get('RealtimeLogDeliveryInfo'):
                temp_model = ListLiveRealtimeLogDeliveryResponseContentRealtimeLogDeliveryInfo()
                self.realtime_log_delivery_info.append(temp_model.from_map(k))
        else:
            self.realtime_log_delivery_info = None
        return self


class ListLiveRealtimeLogDeliveryInfosRequest(TeaModel):
    def __init__(self, live_openapi_reserve=None):
        self.live_openapi_reserve = live_openapi_reserve  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['LiveOpenapiReserve'] = self.live_openapi_reserve
        return result

    def from_map(self, map={}):
        self.live_openapi_reserve = map.get('LiveOpenapiReserve')
        return self


class ListLiveRealtimeLogDeliveryInfosResponse(TeaModel):
    def __init__(self, request_id=None, content=None):
        self.request_id = request_id    # type: str
        self.content = content          # type: ListLiveRealtimeLogDeliveryInfosResponseContent

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.content, 'content')
        if self.content:
            self.content.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.content is not None:
            result['Content'] = self.content.to_map()
        else:
            result['Content'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Content') is not None:
            temp_model = ListLiveRealtimeLogDeliveryInfosResponseContent()
            self.content = temp_model.from_map(map['Content'])
        else:
            self.content = None
        return self


class ListLiveRealtimeLogDeliveryInfosResponseContentRealtimeLogDeliveryInfos(TeaModel):
    def __init__(self, project=None, logstore=None, region=None):
        self.project = project          # type: str
        self.logstore = logstore        # type: str
        self.region = region            # type: str

    def validate(self):
        self.validate_required(self.project, 'project')
        self.validate_required(self.logstore, 'logstore')
        self.validate_required(self.region, 'region')

    def to_map(self):
        result = {}
        result['Project'] = self.project
        result['Logstore'] = self.logstore
        result['Region'] = self.region
        return result

    def from_map(self, map={}):
        self.project = map.get('Project')
        self.logstore = map.get('Logstore')
        self.region = map.get('Region')
        return self


class ListLiveRealtimeLogDeliveryInfosResponseContent(TeaModel):
    def __init__(self, realtime_log_delivery_infos=None):
        self.realtime_log_delivery_infos = realtime_log_delivery_infos  # type: List[ListLiveRealtimeLogDeliveryInfosResponseContentRealtimeLogDeliveryInfos]

    def validate(self):
        self.validate_required(self.realtime_log_delivery_infos, 'realtime_log_delivery_infos')
        if self.realtime_log_delivery_infos:
            for k in self.realtime_log_delivery_infos:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RealtimeLogDeliveryInfos'] = []
        if self.realtime_log_delivery_infos is not None:
            for k in self.realtime_log_delivery_infos:
                result['RealtimeLogDeliveryInfos'].append(k.to_map() if k else None)
        else:
            result['RealtimeLogDeliveryInfos'] = None
        return result

    def from_map(self, map={}):
        self.realtime_log_delivery_infos = []
        if map.get('RealtimeLogDeliveryInfos') is not None:
            for k in map.get('RealtimeLogDeliveryInfos'):
                temp_model = ListLiveRealtimeLogDeliveryInfosResponseContentRealtimeLogDeliveryInfos()
                self.realtime_log_delivery_infos.append(temp_model.from_map(k))
        else:
            self.realtime_log_delivery_infos = None
        return self


class DescribeLiveDomainRealtimeLogDeliveryRequest(TeaModel):
    def __init__(self, domain_name=None):
        self.domain_name = domain_name  # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        return self


class DescribeLiveDomainRealtimeLogDeliveryResponse(TeaModel):
    def __init__(self, request_id=None, project=None, region=None, logstore=None, status=None):
        self.request_id = request_id    # type: str
        self.project = project          # type: str
        self.region = region            # type: str
        self.logstore = logstore        # type: str
        self.status = status            # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.project, 'project')
        self.validate_required(self.region, 'region')
        self.validate_required(self.logstore, 'logstore')
        self.validate_required(self.status, 'status')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Project'] = self.project
        result['Region'] = self.region
        result['Logstore'] = self.logstore
        result['Status'] = self.status
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.project = map.get('Project')
        self.region = map.get('Region')
        self.logstore = map.get('Logstore')
        self.status = map.get('Status')
        return self


class DeleteLiveRealtimeLogDeliveryRequest(TeaModel):
    def __init__(self, domain_name=None, project=None, logstore=None, region=None):
        self.domain_name = domain_name  # type: str
        self.project = project          # type: str
        self.logstore = logstore        # type: str
        self.region = region            # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.project, 'project')
        self.validate_required(self.logstore, 'logstore')
        self.validate_required(self.region, 'region')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['Project'] = self.project
        result['Logstore'] = self.logstore
        result['Region'] = self.region
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.project = map.get('Project')
        self.logstore = map.get('Logstore')
        self.region = map.get('Region')
        return self


class DeleteLiveRealtimeLogDeliveryResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class CreateLiveRealTimeLogDeliveryRequest(TeaModel):
    def __init__(self, project=None, logstore=None, region=None, domain_name=None):
        self.project = project          # type: str
        self.logstore = logstore        # type: str
        self.region = region            # type: str
        self.domain_name = domain_name  # type: str

    def validate(self):
        self.validate_required(self.project, 'project')
        self.validate_required(self.logstore, 'logstore')
        self.validate_required(self.region, 'region')
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = {}
        result['Project'] = self.project
        result['Logstore'] = self.logstore
        result['Region'] = self.region
        result['DomainName'] = self.domain_name
        return result

    def from_map(self, map={}):
        self.project = map.get('Project')
        self.logstore = map.get('Logstore')
        self.region = map.get('Region')
        self.domain_name = map.get('DomainName')
        return self


class CreateLiveRealTimeLogDeliveryResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeLiveDomainLimitRequest(TeaModel):
    def __init__(self, domain_name=None, liveapi_request_from=None):
        self.domain_name = domain_name  # type: str
        self.liveapi_request_from = liveapi_request_from  # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['LiveapiRequestFrom'] = self.liveapi_request_from
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.liveapi_request_from = map.get('LiveapiRequestFrom')
        return self


class DescribeLiveDomainLimitResponse(TeaModel):
    def __init__(self, request_id=None, live_domain_limit_list=None):
        self.request_id = request_id    # type: str
        self.live_domain_limit_list = live_domain_limit_list  # type: DescribeLiveDomainLimitResponseLiveDomainLimitList

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.live_domain_limit_list, 'live_domain_limit_list')
        if self.live_domain_limit_list:
            self.live_domain_limit_list.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.live_domain_limit_list is not None:
            result['LiveDomainLimitList'] = self.live_domain_limit_list.to_map()
        else:
            result['LiveDomainLimitList'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('LiveDomainLimitList') is not None:
            temp_model = DescribeLiveDomainLimitResponseLiveDomainLimitList()
            self.live_domain_limit_list = temp_model.from_map(map['LiveDomainLimitList'])
        else:
            self.live_domain_limit_list = None
        return self


class DescribeLiveDomainLimitResponseLiveDomainLimitListLiveDomainLimit(TeaModel):
    def __init__(self, domain_name=None, limit_num=None, limit_transcode_num=None):
        self.domain_name = domain_name  # type: str
        self.limit_num = limit_num      # type: int
        self.limit_transcode_num = limit_transcode_num  # type: int

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.limit_num, 'limit_num')
        self.validate_required(self.limit_transcode_num, 'limit_transcode_num')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['LimitNum'] = self.limit_num
        result['LimitTranscodeNum'] = self.limit_transcode_num
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.limit_num = map.get('LimitNum')
        self.limit_transcode_num = map.get('LimitTranscodeNum')
        return self


class DescribeLiveDomainLimitResponseLiveDomainLimitList(TeaModel):
    def __init__(self, live_domain_limit=None):
        self.live_domain_limit = live_domain_limit  # type: List[DescribeLiveDomainLimitResponseLiveDomainLimitListLiveDomainLimit]

    def validate(self):
        self.validate_required(self.live_domain_limit, 'live_domain_limit')
        if self.live_domain_limit:
            for k in self.live_domain_limit:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['LiveDomainLimit'] = []
        if self.live_domain_limit is not None:
            for k in self.live_domain_limit:
                result['LiveDomainLimit'].append(k.to_map() if k else None)
        else:
            result['LiveDomainLimit'] = None
        return result

    def from_map(self, map={}):
        self.live_domain_limit = []
        if map.get('LiveDomainLimit') is not None:
            for k in map.get('LiveDomainLimit'):
                temp_model = DescribeLiveDomainLimitResponseLiveDomainLimitListLiveDomainLimit()
                self.live_domain_limit.append(temp_model.from_map(k))
        else:
            self.live_domain_limit = None
        return self


class DescribeLiveDomainBpsDataByTimeStampRequest(TeaModel):
    def __init__(self, domain_name=None, time_point=None, isp_names=None, location_names=None):
        self.domain_name = domain_name  # type: str
        self.time_point = time_point    # type: str
        self.isp_names = isp_names      # type: str
        self.location_names = location_names  # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.time_point, 'time_point')
        self.validate_required(self.isp_names, 'isp_names')
        self.validate_required(self.location_names, 'location_names')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['TimePoint'] = self.time_point
        result['IspNames'] = self.isp_names
        result['LocationNames'] = self.location_names
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.time_point = map.get('TimePoint')
        self.isp_names = map.get('IspNames')
        self.location_names = map.get('LocationNames')
        return self


class DescribeLiveDomainBpsDataByTimeStampResponse(TeaModel):
    def __init__(self, request_id=None, domain_name=None, time_stamp=None, bps_data_list=None):
        self.request_id = request_id    # type: str
        self.domain_name = domain_name  # type: str
        self.time_stamp = time_stamp    # type: str
        self.bps_data_list = bps_data_list  # type: DescribeLiveDomainBpsDataByTimeStampResponseBpsDataList

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.time_stamp, 'time_stamp')
        self.validate_required(self.bps_data_list, 'bps_data_list')
        if self.bps_data_list:
            self.bps_data_list.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DomainName'] = self.domain_name
        result['TimeStamp'] = self.time_stamp
        if self.bps_data_list is not None:
            result['BpsDataList'] = self.bps_data_list.to_map()
        else:
            result['BpsDataList'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.domain_name = map.get('DomainName')
        self.time_stamp = map.get('TimeStamp')
        if map.get('BpsDataList') is not None:
            temp_model = DescribeLiveDomainBpsDataByTimeStampResponseBpsDataList()
            self.bps_data_list = temp_model.from_map(map['BpsDataList'])
        else:
            self.bps_data_list = None
        return self


class DescribeLiveDomainBpsDataByTimeStampResponseBpsDataListBpsDataModel(TeaModel):
    def __init__(self, time_stamp=None, location_name=None, isp_name=None, bps=None):
        self.time_stamp = time_stamp    # type: str
        self.location_name = location_name  # type: str
        self.isp_name = isp_name        # type: str
        self.bps = bps                  # type: int

    def validate(self):
        self.validate_required(self.time_stamp, 'time_stamp')
        self.validate_required(self.location_name, 'location_name')
        self.validate_required(self.isp_name, 'isp_name')
        self.validate_required(self.bps, 'bps')

    def to_map(self):
        result = {}
        result['TimeStamp'] = self.time_stamp
        result['LocationName'] = self.location_name
        result['IspName'] = self.isp_name
        result['Bps'] = self.bps
        return result

    def from_map(self, map={}):
        self.time_stamp = map.get('TimeStamp')
        self.location_name = map.get('LocationName')
        self.isp_name = map.get('IspName')
        self.bps = map.get('Bps')
        return self


class DescribeLiveDomainBpsDataByTimeStampResponseBpsDataList(TeaModel):
    def __init__(self, bps_data_model=None):
        self.bps_data_model = bps_data_model  # type: List[DescribeLiveDomainBpsDataByTimeStampResponseBpsDataListBpsDataModel]

    def validate(self):
        self.validate_required(self.bps_data_model, 'bps_data_model')
        if self.bps_data_model:
            for k in self.bps_data_model:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['BpsDataModel'] = []
        if self.bps_data_model is not None:
            for k in self.bps_data_model:
                result['BpsDataModel'].append(k.to_map() if k else None)
        else:
            result['BpsDataModel'] = None
        return result

    def from_map(self, map={}):
        self.bps_data_model = []
        if map.get('BpsDataModel') is not None:
            for k in map.get('BpsDataModel'):
                temp_model = DescribeLiveDomainBpsDataByTimeStampResponseBpsDataListBpsDataModel()
                self.bps_data_model.append(temp_model.from_map(k))
        else:
            self.bps_data_model = None
        return self


class DescribeLiveStreamTranscodeStreamNumRequest(TeaModel):
    def __init__(self, domain_name=None):
        self.domain_name = domain_name  # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        return self


class DescribeLiveStreamTranscodeStreamNumResponse(TeaModel):
    def __init__(self, request_id=None, total=None, transcoded_number=None, untranscode_number=None,
                 lazy_transcoded_number=None):
        self.request_id = request_id    # type: str
        self.total = total              # type: int
        self.transcoded_number = transcoded_number  # type: int
        self.untranscode_number = untranscode_number  # type: int
        self.lazy_transcoded_number = lazy_transcoded_number  # type: int

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total, 'total')
        self.validate_required(self.transcoded_number, 'transcoded_number')
        self.validate_required(self.untranscode_number, 'untranscode_number')
        self.validate_required(self.lazy_transcoded_number, 'lazy_transcoded_number')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Total'] = self.total
        result['TranscodedNumber'] = self.transcoded_number
        result['UntranscodeNumber'] = self.untranscode_number
        result['LazyTranscodedNumber'] = self.lazy_transcoded_number
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total = map.get('Total')
        self.transcoded_number = map.get('TranscodedNumber')
        self.untranscode_number = map.get('UntranscodeNumber')
        self.lazy_transcoded_number = map.get('LazyTranscodedNumber')
        return self


class UpdateLiveTopLevelDomainRequest(TeaModel):
    def __init__(self, security_token=None, domain_name=None, top_level_domain=None):
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str
        self.top_level_domain = top_level_domain  # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.top_level_domain, 'top_level_domain')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['DomainName'] = self.domain_name
        result['TopLevelDomain'] = self.top_level_domain
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.domain_name = map.get('DomainName')
        self.top_level_domain = map.get('TopLevelDomain')
        return self


class UpdateLiveTopLevelDomainResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeLiveDomainCertificateInfoRequest(TeaModel):
    def __init__(self, domain_name=None):
        self.domain_name = domain_name  # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        return self


class DescribeLiveDomainCertificateInfoResponse(TeaModel):
    def __init__(self, request_id=None, cert_infos=None):
        self.request_id = request_id    # type: str
        self.cert_infos = cert_infos    # type: DescribeLiveDomainCertificateInfoResponseCertInfos

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.cert_infos, 'cert_infos')
        if self.cert_infos:
            self.cert_infos.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.cert_infos is not None:
            result['CertInfos'] = self.cert_infos.to_map()
        else:
            result['CertInfos'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('CertInfos') is not None:
            temp_model = DescribeLiveDomainCertificateInfoResponseCertInfos()
            self.cert_infos = temp_model.from_map(map['CertInfos'])
        else:
            self.cert_infos = None
        return self


class DescribeLiveDomainCertificateInfoResponseCertInfosCertInfo(TeaModel):
    def __init__(self, domain_name=None, cert_name=None, cert_domain_name=None, cert_expire_time=None,
                 cert_life=None, cert_org=None, cert_type=None, sslprotocol=None, status=None, sslpub=None):
        self.domain_name = domain_name  # type: str
        self.cert_name = cert_name      # type: str
        self.cert_domain_name = cert_domain_name  # type: str
        self.cert_expire_time = cert_expire_time  # type: str
        self.cert_life = cert_life      # type: str
        self.cert_org = cert_org        # type: str
        self.cert_type = cert_type      # type: str
        self.sslprotocol = sslprotocol  # type: str
        self.status = status            # type: str
        self.sslpub = sslpub            # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.cert_name, 'cert_name')
        self.validate_required(self.cert_domain_name, 'cert_domain_name')
        self.validate_required(self.cert_expire_time, 'cert_expire_time')
        self.validate_required(self.cert_life, 'cert_life')
        self.validate_required(self.cert_org, 'cert_org')
        self.validate_required(self.cert_type, 'cert_type')
        self.validate_required(self.sslprotocol, 'sslprotocol')
        self.validate_required(self.status, 'status')
        self.validate_required(self.sslpub, 'sslpub')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['CertName'] = self.cert_name
        result['CertDomainName'] = self.cert_domain_name
        result['CertExpireTime'] = self.cert_expire_time
        result['CertLife'] = self.cert_life
        result['CertOrg'] = self.cert_org
        result['CertType'] = self.cert_type
        result['SSLProtocol'] = self.sslprotocol
        result['Status'] = self.status
        result['SSLPub'] = self.sslpub
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.cert_name = map.get('CertName')
        self.cert_domain_name = map.get('CertDomainName')
        self.cert_expire_time = map.get('CertExpireTime')
        self.cert_life = map.get('CertLife')
        self.cert_org = map.get('CertOrg')
        self.cert_type = map.get('CertType')
        self.sslprotocol = map.get('SSLProtocol')
        self.status = map.get('Status')
        self.sslpub = map.get('SSLPub')
        return self


class DescribeLiveDomainCertificateInfoResponseCertInfos(TeaModel):
    def __init__(self, cert_info=None):
        self.cert_info = cert_info      # type: List[DescribeLiveDomainCertificateInfoResponseCertInfosCertInfo]

    def validate(self):
        self.validate_required(self.cert_info, 'cert_info')
        if self.cert_info:
            for k in self.cert_info:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['CertInfo'] = []
        if self.cert_info is not None:
            for k in self.cert_info:
                result['CertInfo'].append(k.to_map() if k else None)
        else:
            result['CertInfo'] = None
        return result

    def from_map(self, map={}):
        self.cert_info = []
        if map.get('CertInfo') is not None:
            for k in map.get('CertInfo'):
                temp_model = DescribeLiveDomainCertificateInfoResponseCertInfosCertInfo()
                self.cert_info.append(temp_model.from_map(k))
        else:
            self.cert_info = None
        return self


class ModifyLiveDomainSchdmByPropertyRequest(TeaModel):
    def __init__(self, domain_name=None, property=None):
        self.domain_name = domain_name  # type: str
        self.property = property        # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.property, 'property')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['Property'] = self.property
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.property = map.get('Property')
        return self


class ModifyLiveDomainSchdmByPropertyResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class SetLiveStreamOptimizedFeatureConfigRequest(TeaModel):
    def __init__(self, domain_name=None, config_name=None, config_status=None, config_value=None):
        self.domain_name = domain_name  # type: str
        self.config_name = config_name  # type: str
        self.config_status = config_status  # type: str
        self.config_value = config_value  # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.config_name, 'config_name')
        self.validate_required(self.config_status, 'config_status')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['ConfigName'] = self.config_name
        result['ConfigStatus'] = self.config_status
        result['ConfigValue'] = self.config_value
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.config_name = map.get('ConfigName')
        self.config_status = map.get('ConfigStatus')
        self.config_value = map.get('ConfigValue')
        return self


class SetLiveStreamOptimizedFeatureConfigResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeLiveStreamOptimizedFeatureConfigRequest(TeaModel):
    def __init__(self, domain_name=None, config_name=None):
        self.domain_name = domain_name  # type: str
        self.config_name = config_name  # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.config_name, 'config_name')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['ConfigName'] = self.config_name
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.config_name = map.get('ConfigName')
        return self


class DescribeLiveStreamOptimizedFeatureConfigResponse(TeaModel):
    def __init__(self, request_id=None, live_stream_optimized_feature_config_list=None):
        self.request_id = request_id    # type: str
        self.live_stream_optimized_feature_config_list = live_stream_optimized_feature_config_list  # type: DescribeLiveStreamOptimizedFeatureConfigResponseLiveStreamOptimizedFeatureConfigList

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.live_stream_optimized_feature_config_list, 'live_stream_optimized_feature_config_list')
        if self.live_stream_optimized_feature_config_list:
            self.live_stream_optimized_feature_config_list.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.live_stream_optimized_feature_config_list is not None:
            result['LiveStreamOptimizedFeatureConfigList'] = self.live_stream_optimized_feature_config_list.to_map()
        else:
            result['LiveStreamOptimizedFeatureConfigList'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('LiveStreamOptimizedFeatureConfigList') is not None:
            temp_model = DescribeLiveStreamOptimizedFeatureConfigResponseLiveStreamOptimizedFeatureConfigList()
            self.live_stream_optimized_feature_config_list = temp_model.from_map(map['LiveStreamOptimizedFeatureConfigList'])
        else:
            self.live_stream_optimized_feature_config_list = None
        return self


class DescribeLiveStreamOptimizedFeatureConfigResponseLiveStreamOptimizedFeatureConfigListLiveStreamOptimizedFeatureConfig(TeaModel):
    def __init__(self, domain_name=None, config_name=None, config_status=None, config_value=None):
        self.domain_name = domain_name  # type: str
        self.config_name = config_name  # type: str
        self.config_status = config_status  # type: str
        self.config_value = config_value  # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.config_name, 'config_name')
        self.validate_required(self.config_status, 'config_status')
        self.validate_required(self.config_value, 'config_value')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['ConfigName'] = self.config_name
        result['ConfigStatus'] = self.config_status
        result['ConfigValue'] = self.config_value
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.config_name = map.get('ConfigName')
        self.config_status = map.get('ConfigStatus')
        self.config_value = map.get('ConfigValue')
        return self


class DescribeLiveStreamOptimizedFeatureConfigResponseLiveStreamOptimizedFeatureConfigList(TeaModel):
    def __init__(self, live_stream_optimized_feature_config=None):
        self.live_stream_optimized_feature_config = live_stream_optimized_feature_config  # type: List[DescribeLiveStreamOptimizedFeatureConfigResponseLiveStreamOptimizedFeatureConfigListLiveStreamOptimizedFeatureConfig]

    def validate(self):
        self.validate_required(self.live_stream_optimized_feature_config, 'live_stream_optimized_feature_config')
        if self.live_stream_optimized_feature_config:
            for k in self.live_stream_optimized_feature_config:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['LiveStreamOptimizedFeatureConfig'] = []
        if self.live_stream_optimized_feature_config is not None:
            for k in self.live_stream_optimized_feature_config:
                result['LiveStreamOptimizedFeatureConfig'].append(k.to_map() if k else None)
        else:
            result['LiveStreamOptimizedFeatureConfig'] = None
        return result

    def from_map(self, map={}):
        self.live_stream_optimized_feature_config = []
        if map.get('LiveStreamOptimizedFeatureConfig') is not None:
            for k in map.get('LiveStreamOptimizedFeatureConfig'):
                temp_model = DescribeLiveStreamOptimizedFeatureConfigResponseLiveStreamOptimizedFeatureConfigListLiveStreamOptimizedFeatureConfig()
                self.live_stream_optimized_feature_config.append(temp_model.from_map(k))
        else:
            self.live_stream_optimized_feature_config = None
        return self


class SetLiveStreamDelayConfigRequest(TeaModel):
    def __init__(self, domain_name=None, hls_delay=None, hls_level=None, flv_delay=None, flv_level=None,
                 rtmp_delay=None, rtmp_level=None):
        self.domain_name = domain_name  # type: str
        self.hls_delay = hls_delay      # type: int
        self.hls_level = hls_level      # type: str
        self.flv_delay = flv_delay      # type: int
        self.flv_level = flv_level      # type: str
        self.rtmp_delay = rtmp_delay    # type: int
        self.rtmp_level = rtmp_level    # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['HlsDelay'] = self.hls_delay
        result['HlsLevel'] = self.hls_level
        result['FlvDelay'] = self.flv_delay
        result['FlvLevel'] = self.flv_level
        result['RtmpDelay'] = self.rtmp_delay
        result['RtmpLevel'] = self.rtmp_level
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.hls_delay = map.get('HlsDelay')
        self.hls_level = map.get('HlsLevel')
        self.flv_delay = map.get('FlvDelay')
        self.flv_level = map.get('FlvLevel')
        self.rtmp_delay = map.get('RtmpDelay')
        self.rtmp_level = map.get('RtmpLevel')
        return self


class SetLiveStreamDelayConfigResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeLiveStreamDelayConfigRequest(TeaModel):
    def __init__(self, domain_name=None):
        self.domain_name = domain_name  # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        return self


class DescribeLiveStreamDelayConfigResponse(TeaModel):
    def __init__(self, request_id=None, live_stream_hls_delay_config=None, live_stream_flv_delay_config=None,
                 live_stream_rtmp_delay_config=None):
        self.request_id = request_id    # type: str
        self.live_stream_hls_delay_config = live_stream_hls_delay_config  # type: DescribeLiveStreamDelayConfigResponseLiveStreamHlsDelayConfig
        self.live_stream_flv_delay_config = live_stream_flv_delay_config  # type: DescribeLiveStreamDelayConfigResponseLiveStreamFlvDelayConfig
        self.live_stream_rtmp_delay_config = live_stream_rtmp_delay_config  # type: DescribeLiveStreamDelayConfigResponseLiveStreamRtmpDelayConfig

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.live_stream_hls_delay_config, 'live_stream_hls_delay_config')
        if self.live_stream_hls_delay_config:
            self.live_stream_hls_delay_config.validate()
        self.validate_required(self.live_stream_flv_delay_config, 'live_stream_flv_delay_config')
        if self.live_stream_flv_delay_config:
            self.live_stream_flv_delay_config.validate()
        self.validate_required(self.live_stream_rtmp_delay_config, 'live_stream_rtmp_delay_config')
        if self.live_stream_rtmp_delay_config:
            self.live_stream_rtmp_delay_config.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.live_stream_hls_delay_config is not None:
            result['LiveStreamHlsDelayConfig'] = self.live_stream_hls_delay_config.to_map()
        else:
            result['LiveStreamHlsDelayConfig'] = None
        if self.live_stream_flv_delay_config is not None:
            result['LiveStreamFlvDelayConfig'] = self.live_stream_flv_delay_config.to_map()
        else:
            result['LiveStreamFlvDelayConfig'] = None
        if self.live_stream_rtmp_delay_config is not None:
            result['LiveStreamRtmpDelayConfig'] = self.live_stream_rtmp_delay_config.to_map()
        else:
            result['LiveStreamRtmpDelayConfig'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('LiveStreamHlsDelayConfig') is not None:
            temp_model = DescribeLiveStreamDelayConfigResponseLiveStreamHlsDelayConfig()
            self.live_stream_hls_delay_config = temp_model.from_map(map['LiveStreamHlsDelayConfig'])
        else:
            self.live_stream_hls_delay_config = None
        if map.get('LiveStreamFlvDelayConfig') is not None:
            temp_model = DescribeLiveStreamDelayConfigResponseLiveStreamFlvDelayConfig()
            self.live_stream_flv_delay_config = temp_model.from_map(map['LiveStreamFlvDelayConfig'])
        else:
            self.live_stream_flv_delay_config = None
        if map.get('LiveStreamRtmpDelayConfig') is not None:
            temp_model = DescribeLiveStreamDelayConfigResponseLiveStreamRtmpDelayConfig()
            self.live_stream_rtmp_delay_config = temp_model.from_map(map['LiveStreamRtmpDelayConfig'])
        else:
            self.live_stream_rtmp_delay_config = None
        return self


class DescribeLiveStreamDelayConfigResponseLiveStreamHlsDelayConfig(TeaModel):
    def __init__(self, level=None, delay=None):
        self.level = level              # type: str
        self.delay = delay              # type: int

    def validate(self):
        self.validate_required(self.level, 'level')
        self.validate_required(self.delay, 'delay')

    def to_map(self):
        result = {}
        result['Level'] = self.level
        result['Delay'] = self.delay
        return result

    def from_map(self, map={}):
        self.level = map.get('Level')
        self.delay = map.get('Delay')
        return self


class DescribeLiveStreamDelayConfigResponseLiveStreamFlvDelayConfig(TeaModel):
    def __init__(self, level=None, delay=None):
        self.level = level              # type: str
        self.delay = delay              # type: int

    def validate(self):
        self.validate_required(self.level, 'level')
        self.validate_required(self.delay, 'delay')

    def to_map(self):
        result = {}
        result['Level'] = self.level
        result['Delay'] = self.delay
        return result

    def from_map(self, map={}):
        self.level = map.get('Level')
        self.delay = map.get('Delay')
        return self


class DescribeLiveStreamDelayConfigResponseLiveStreamRtmpDelayConfig(TeaModel):
    def __init__(self, level=None, delay=None):
        self.level = level              # type: str
        self.delay = delay              # type: int

    def validate(self):
        self.validate_required(self.level, 'level')
        self.validate_required(self.delay, 'delay')

    def to_map(self):
        result = {}
        result['Level'] = self.level
        result['Delay'] = self.delay
        return result

    def from_map(self, map={}):
        self.level = map.get('Level')
        self.delay = map.get('Delay')
        return self


class DescribeLiveDomainOnlineUserNumRequest(TeaModel):
    def __init__(self, domain_name=None, query_time=None):
        self.domain_name = domain_name  # type: str
        self.query_time = query_time    # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['QueryTime'] = self.query_time
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.query_time = map.get('QueryTime')
        return self


class DescribeLiveDomainOnlineUserNumResponse(TeaModel):
    def __init__(self, request_id=None, stream_count=None, user_count=None, online_user_info=None):
        self.request_id = request_id    # type: str
        self.stream_count = stream_count  # type: int
        self.user_count = user_count    # type: int
        self.online_user_info = online_user_info  # type: DescribeLiveDomainOnlineUserNumResponseOnlineUserInfo

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.stream_count, 'stream_count')
        self.validate_required(self.user_count, 'user_count')
        self.validate_required(self.online_user_info, 'online_user_info')
        if self.online_user_info:
            self.online_user_info.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['StreamCount'] = self.stream_count
        result['UserCount'] = self.user_count
        if self.online_user_info is not None:
            result['OnlineUserInfo'] = self.online_user_info.to_map()
        else:
            result['OnlineUserInfo'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.stream_count = map.get('StreamCount')
        self.user_count = map.get('UserCount')
        if map.get('OnlineUserInfo') is not None:
            temp_model = DescribeLiveDomainOnlineUserNumResponseOnlineUserInfo()
            self.online_user_info = temp_model.from_map(map['OnlineUserInfo'])
        else:
            self.online_user_info = None
        return self


class DescribeLiveDomainOnlineUserNumResponseOnlineUserInfoLiveStreamOnlineUserNumInfoInfosInfo(TeaModel):
    def __init__(self, transcode_template=None, user_number=None):
        self.transcode_template = transcode_template  # type: str
        self.user_number = user_number  # type: int

    def validate(self):
        self.validate_required(self.transcode_template, 'transcode_template')
        self.validate_required(self.user_number, 'user_number')

    def to_map(self):
        result = {}
        result['TranscodeTemplate'] = self.transcode_template
        result['UserNumber'] = self.user_number
        return result

    def from_map(self, map={}):
        self.transcode_template = map.get('TranscodeTemplate')
        self.user_number = map.get('UserNumber')
        return self


class DescribeLiveDomainOnlineUserNumResponseOnlineUserInfoLiveStreamOnlineUserNumInfoInfos(TeaModel):
    def __init__(self, info=None):
        self.info = info                # type: List[DescribeLiveDomainOnlineUserNumResponseOnlineUserInfoLiveStreamOnlineUserNumInfoInfosInfo]

    def validate(self):
        self.validate_required(self.info, 'info')
        if self.info:
            for k in self.info:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Info'] = []
        if self.info is not None:
            for k in self.info:
                result['Info'].append(k.to_map() if k else None)
        else:
            result['Info'] = None
        return result

    def from_map(self, map={}):
        self.info = []
        if map.get('Info') is not None:
            for k in map.get('Info'):
                temp_model = DescribeLiveDomainOnlineUserNumResponseOnlineUserInfoLiveStreamOnlineUserNumInfoInfosInfo()
                self.info.append(temp_model.from_map(k))
        else:
            self.info = None
        return self


class DescribeLiveDomainOnlineUserNumResponseOnlineUserInfoLiveStreamOnlineUserNumInfo(TeaModel):
    def __init__(self, stream_name=None, infos=None):
        self.stream_name = stream_name  # type: str
        self.infos = infos              # type: DescribeLiveDomainOnlineUserNumResponseOnlineUserInfoLiveStreamOnlineUserNumInfoInfos

    def validate(self):
        self.validate_required(self.stream_name, 'stream_name')
        self.validate_required(self.infos, 'infos')
        if self.infos:
            self.infos.validate()

    def to_map(self):
        result = {}
        result['StreamName'] = self.stream_name
        if self.infos is not None:
            result['Infos'] = self.infos.to_map()
        else:
            result['Infos'] = None
        return result

    def from_map(self, map={}):
        self.stream_name = map.get('StreamName')
        if map.get('Infos') is not None:
            temp_model = DescribeLiveDomainOnlineUserNumResponseOnlineUserInfoLiveStreamOnlineUserNumInfoInfos()
            self.infos = temp_model.from_map(map['Infos'])
        else:
            self.infos = None
        return self


class DescribeLiveDomainOnlineUserNumResponseOnlineUserInfo(TeaModel):
    def __init__(self, live_stream_online_user_num_info=None):
        self.live_stream_online_user_num_info = live_stream_online_user_num_info  # type: List[DescribeLiveDomainOnlineUserNumResponseOnlineUserInfoLiveStreamOnlineUserNumInfo]

    def validate(self):
        self.validate_required(self.live_stream_online_user_num_info, 'live_stream_online_user_num_info')
        if self.live_stream_online_user_num_info:
            for k in self.live_stream_online_user_num_info:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['LiveStreamOnlineUserNumInfo'] = []
        if self.live_stream_online_user_num_info is not None:
            for k in self.live_stream_online_user_num_info:
                result['LiveStreamOnlineUserNumInfo'].append(k.to_map() if k else None)
        else:
            result['LiveStreamOnlineUserNumInfo'] = None
        return result

    def from_map(self, map={}):
        self.live_stream_online_user_num_info = []
        if map.get('LiveStreamOnlineUserNumInfo') is not None:
            for k in map.get('LiveStreamOnlineUserNumInfo'):
                temp_model = DescribeLiveDomainOnlineUserNumResponseOnlineUserInfoLiveStreamOnlineUserNumInfo()
                self.live_stream_online_user_num_info.append(temp_model.from_map(k))
        else:
            self.live_stream_online_user_num_info = None
        return self


class DescribeLiveDomainFrameRateAndBitRateDataRequest(TeaModel):
    def __init__(self, domain_name=None, query_time=None):
        self.domain_name = domain_name  # type: str
        self.query_time = query_time    # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.query_time, 'query_time')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['QueryTime'] = self.query_time
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.query_time = map.get('QueryTime')
        return self


class DescribeLiveDomainFrameRateAndBitRateDataResponse(TeaModel):
    def __init__(self, request_id=None, frame_rate_and_bit_rate_infos=None):
        self.request_id = request_id    # type: str
        self.frame_rate_and_bit_rate_infos = frame_rate_and_bit_rate_infos  # type: DescribeLiveDomainFrameRateAndBitRateDataResponseFrameRateAndBitRateInfos

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.frame_rate_and_bit_rate_infos, 'frame_rate_and_bit_rate_infos')
        if self.frame_rate_and_bit_rate_infos:
            self.frame_rate_and_bit_rate_infos.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.frame_rate_and_bit_rate_infos is not None:
            result['FrameRateAndBitRateInfos'] = self.frame_rate_and_bit_rate_infos.to_map()
        else:
            result['FrameRateAndBitRateInfos'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('FrameRateAndBitRateInfos') is not None:
            temp_model = DescribeLiveDomainFrameRateAndBitRateDataResponseFrameRateAndBitRateInfos()
            self.frame_rate_and_bit_rate_infos = temp_model.from_map(map['FrameRateAndBitRateInfos'])
        else:
            self.frame_rate_and_bit_rate_infos = None
        return self


class DescribeLiveDomainFrameRateAndBitRateDataResponseFrameRateAndBitRateInfosFrameRateAndBitRateInfo(TeaModel):
    def __init__(self, audio_frame_rate=None, bit_rate=None, video_frame_rate=None, stream_url=None):
        self.audio_frame_rate = audio_frame_rate  # type: float
        self.bit_rate = bit_rate        # type: float
        self.video_frame_rate = video_frame_rate  # type: float
        self.stream_url = stream_url    # type: str

    def validate(self):
        self.validate_required(self.audio_frame_rate, 'audio_frame_rate')
        self.validate_required(self.bit_rate, 'bit_rate')
        self.validate_required(self.video_frame_rate, 'video_frame_rate')
        self.validate_required(self.stream_url, 'stream_url')

    def to_map(self):
        result = {}
        result['AudioFrameRate'] = self.audio_frame_rate
        result['BitRate'] = self.bit_rate
        result['VideoFrameRate'] = self.video_frame_rate
        result['StreamUrl'] = self.stream_url
        return result

    def from_map(self, map={}):
        self.audio_frame_rate = map.get('AudioFrameRate')
        self.bit_rate = map.get('BitRate')
        self.video_frame_rate = map.get('VideoFrameRate')
        self.stream_url = map.get('StreamUrl')
        return self


class DescribeLiveDomainFrameRateAndBitRateDataResponseFrameRateAndBitRateInfos(TeaModel):
    def __init__(self, frame_rate_and_bit_rate_info=None):
        self.frame_rate_and_bit_rate_info = frame_rate_and_bit_rate_info  # type: List[DescribeLiveDomainFrameRateAndBitRateDataResponseFrameRateAndBitRateInfosFrameRateAndBitRateInfo]

    def validate(self):
        self.validate_required(self.frame_rate_and_bit_rate_info, 'frame_rate_and_bit_rate_info')
        if self.frame_rate_and_bit_rate_info:
            for k in self.frame_rate_and_bit_rate_info:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['FrameRateAndBitRateInfo'] = []
        if self.frame_rate_and_bit_rate_info is not None:
            for k in self.frame_rate_and_bit_rate_info:
                result['FrameRateAndBitRateInfo'].append(k.to_map() if k else None)
        else:
            result['FrameRateAndBitRateInfo'] = None
        return result

    def from_map(self, map={}):
        self.frame_rate_and_bit_rate_info = []
        if map.get('FrameRateAndBitRateInfo') is not None:
            for k in map.get('FrameRateAndBitRateInfo'):
                temp_model = DescribeLiveDomainFrameRateAndBitRateDataResponseFrameRateAndBitRateInfosFrameRateAndBitRateInfo()
                self.frame_rate_and_bit_rate_info.append(temp_model.from_map(k))
        else:
            self.frame_rate_and_bit_rate_info = None
        return self


class SetBoardCallbackRequest(TeaModel):
    def __init__(self, app_id=None, auth_key=None, auth_switch=None, callback_enable=None, callback_uri=None,
                 callback_events=None):
        self.app_id = app_id            # type: str
        self.auth_key = auth_key        # type: str
        self.auth_switch = auth_switch  # type: str
        self.callback_enable = callback_enable  # type: int
        self.callback_uri = callback_uri  # type: str
        self.callback_events = callback_events  # type: str

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.callback_enable, 'callback_enable')

    def to_map(self):
        result = {}
        result['AppId'] = self.app_id
        result['AuthKey'] = self.auth_key
        result['AuthSwitch'] = self.auth_switch
        result['CallbackEnable'] = self.callback_enable
        result['CallbackUri'] = self.callback_uri
        result['CallbackEvents'] = self.callback_events
        return result

    def from_map(self, map={}):
        self.app_id = map.get('AppId')
        self.auth_key = map.get('AuthKey')
        self.auth_switch = map.get('AuthSwitch')
        self.callback_enable = map.get('CallbackEnable')
        self.callback_uri = map.get('CallbackUri')
        self.callback_events = map.get('CallbackEvents')
        return self


class SetBoardCallbackResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeRecordsRequest(TeaModel):
    def __init__(self, app_id=None, page_num=None, page_size=None, record_state=None):
        self.app_id = app_id            # type: str
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int
        self.record_state = record_state  # type: str

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.page_num, 'page_num')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        result = {}
        result['AppId'] = self.app_id
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        result['RecordState'] = self.record_state
        return result

    def from_map(self, map={}):
        self.app_id = map.get('AppId')
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        self.record_state = map.get('RecordState')
        return self


class DescribeRecordsResponse(TeaModel):
    def __init__(self, request_id=None, records=None):
        self.request_id = request_id    # type: str
        self.records = records          # type: List[DescribeRecordsResponseRecords]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.records, 'records')
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        else:
            result['Records'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.records = []
        if map.get('Records') is not None:
            for k in map.get('Records'):
                temp_model = DescribeRecordsResponseRecords()
                self.records.append(temp_model.from_map(k))
        else:
            self.records = None
        return self


class DescribeRecordsResponseRecords(TeaModel):
    def __init__(self, record_id=None, app_id=None, board_id=None, record_start_time=None, start_time=None,
                 end_time=None, state=None, oss_path=None, oss_bucket=None, oss_endpoint=None):
        self.record_id = record_id      # type: str
        self.app_id = app_id            # type: str
        self.board_id = board_id        # type: int
        self.record_start_time = record_start_time  # type: int
        self.start_time = start_time    # type: int
        self.end_time = end_time        # type: int
        self.state = state              # type: int
        self.oss_path = oss_path        # type: str
        self.oss_bucket = oss_bucket    # type: str
        self.oss_endpoint = oss_endpoint  # type: str

    def validate(self):
        self.validate_required(self.record_id, 'record_id')
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.board_id, 'board_id')
        self.validate_required(self.record_start_time, 'record_start_time')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.state, 'state')
        self.validate_required(self.oss_path, 'oss_path')
        self.validate_required(self.oss_bucket, 'oss_bucket')
        self.validate_required(self.oss_endpoint, 'oss_endpoint')

    def to_map(self):
        result = {}
        result['RecordId'] = self.record_id
        result['AppId'] = self.app_id
        result['BoardId'] = self.board_id
        result['RecordStartTime'] = self.record_start_time
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['State'] = self.state
        result['OssPath'] = self.oss_path
        result['OssBucket'] = self.oss_bucket
        result['OssEndpoint'] = self.oss_endpoint
        return result

    def from_map(self, map={}):
        self.record_id = map.get('RecordId')
        self.app_id = map.get('AppId')
        self.board_id = map.get('BoardId')
        self.record_start_time = map.get('RecordStartTime')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.state = map.get('State')
        self.oss_path = map.get('OssPath')
        self.oss_bucket = map.get('OssBucket')
        self.oss_endpoint = map.get('OssEndpoint')
        return self


class DescribeRecordRequest(TeaModel):
    def __init__(self, app_id=None, record_id=None):
        self.app_id = app_id            # type: str
        self.record_id = record_id      # type: str

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.record_id, 'record_id')

    def to_map(self):
        result = {}
        result['AppId'] = self.app_id
        result['RecordId'] = self.record_id
        return result

    def from_map(self, map={}):
        self.app_id = map.get('AppId')
        self.record_id = map.get('RecordId')
        return self


class DescribeRecordResponse(TeaModel):
    def __init__(self, request_id=None, record_id=None, app_id=None, board_id=None, record_start_time=None,
                 start_time=None, end_time=None, state=None, oss_path=None, oss_bucket=None, oss_endpoint=None):
        self.request_id = request_id    # type: str
        self.record_id = record_id      # type: str
        self.app_id = app_id            # type: str
        self.board_id = board_id        # type: int
        self.record_start_time = record_start_time  # type: int
        self.start_time = start_time    # type: int
        self.end_time = end_time        # type: int
        self.state = state              # type: int
        self.oss_path = oss_path        # type: str
        self.oss_bucket = oss_bucket    # type: str
        self.oss_endpoint = oss_endpoint  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.record_id, 'record_id')
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.board_id, 'board_id')
        self.validate_required(self.record_start_time, 'record_start_time')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.state, 'state')
        self.validate_required(self.oss_path, 'oss_path')
        self.validate_required(self.oss_bucket, 'oss_bucket')
        self.validate_required(self.oss_endpoint, 'oss_endpoint')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['RecordId'] = self.record_id
        result['AppId'] = self.app_id
        result['BoardId'] = self.board_id
        result['RecordStartTime'] = self.record_start_time
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['State'] = self.state
        result['OssPath'] = self.oss_path
        result['OssBucket'] = self.oss_bucket
        result['OssEndpoint'] = self.oss_endpoint
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.record_id = map.get('RecordId')
        self.app_id = map.get('AppId')
        self.board_id = map.get('BoardId')
        self.record_start_time = map.get('RecordStartTime')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.state = map.get('State')
        self.oss_path = map.get('OssPath')
        self.oss_bucket = map.get('OssBucket')
        self.oss_endpoint = map.get('OssEndpoint')
        return self


class CompleteBoardRecordRequest(TeaModel):
    def __init__(self, app_id=None, record_id=None, end_time=None):
        self.app_id = app_id            # type: str
        self.record_id = record_id      # type: str
        self.end_time = end_time        # type: str

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.record_id, 'record_id')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        result = {}
        result['AppId'] = self.app_id
        result['RecordId'] = self.record_id
        result['EndTime'] = self.end_time
        return result

    def from_map(self, map={}):
        self.app_id = map.get('AppId')
        self.record_id = map.get('RecordId')
        self.end_time = map.get('EndTime')
        return self


class CompleteBoardRecordResponse(TeaModel):
    def __init__(self, request_id=None, oss_path=None):
        self.request_id = request_id    # type: str
        self.oss_path = oss_path        # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.oss_path, 'oss_path')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['OssPath'] = self.oss_path
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.oss_path = map.get('OssPath')
        return self


class StartBoardRecordRequest(TeaModel):
    def __init__(self, app_id=None, board_id=None, start_time=None):
        self.app_id = app_id            # type: str
        self.board_id = board_id        # type: str
        self.start_time = start_time    # type: str

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.board_id, 'board_id')
        self.validate_required(self.start_time, 'start_time')

    def to_map(self):
        result = {}
        result['AppId'] = self.app_id
        result['BoardId'] = self.board_id
        result['StartTime'] = self.start_time
        return result

    def from_map(self, map={}):
        self.app_id = map.get('AppId')
        self.board_id = map.get('BoardId')
        self.start_time = map.get('StartTime')
        return self


class StartBoardRecordResponse(TeaModel):
    def __init__(self, request_id=None, record_id=None):
        self.request_id = request_id    # type: str
        self.record_id = record_id      # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.record_id, 'record_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['RecordId'] = self.record_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.record_id = map.get('RecordId')
        return self


class ApplyRecordTokenRequest(TeaModel):
    def __init__(self, app_id=None):
        self.app_id = app_id            # type: str

    def validate(self):
        self.validate_required(self.app_id, 'app_id')

    def to_map(self):
        result = {}
        result['AppId'] = self.app_id
        return result

    def from_map(self, map={}):
        self.app_id = map.get('AppId')
        return self


class ApplyRecordTokenResponse(TeaModel):
    def __init__(self, request_id=None, security_token=None, access_key_secret=None, access_key_id=None,
                 expiration=None):
        self.request_id = request_id    # type: str
        self.security_token = security_token  # type: str
        self.access_key_secret = access_key_secret  # type: str
        self.access_key_id = access_key_id  # type: str
        self.expiration = expiration    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.security_token, 'security_token')
        self.validate_required(self.access_key_secret, 'access_key_secret')
        self.validate_required(self.access_key_id, 'access_key_id')
        self.validate_required(self.expiration, 'expiration')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['SecurityToken'] = self.security_token
        result['AccessKeySecret'] = self.access_key_secret
        result['AccessKeyId'] = self.access_key_id
        result['Expiration'] = self.expiration
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.security_token = map.get('SecurityToken')
        self.access_key_secret = map.get('AccessKeySecret')
        self.access_key_id = map.get('AccessKeyId')
        self.expiration = map.get('Expiration')
        return self


class UpdateBoardCallbackRequest(TeaModel):
    def __init__(self, app_id=None, auth_key=None, auth_switch=None, callback_enable=None, callback_uri=None,
                 callback_events=None):
        self.app_id = app_id            # type: str
        self.auth_key = auth_key        # type: str
        self.auth_switch = auth_switch  # type: str
        self.callback_enable = callback_enable  # type: int
        self.callback_uri = callback_uri  # type: str
        self.callback_events = callback_events  # type: str

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.callback_enable, 'callback_enable')

    def to_map(self):
        result = {}
        result['AppId'] = self.app_id
        result['AuthKey'] = self.auth_key
        result['AuthSwitch'] = self.auth_switch
        result['CallbackEnable'] = self.callback_enable
        result['CallbackUri'] = self.callback_uri
        result['CallbackEvents'] = self.callback_events
        return result

    def from_map(self, map={}):
        self.app_id = map.get('AppId')
        self.auth_key = map.get('AuthKey')
        self.auth_switch = map.get('AuthSwitch')
        self.callback_enable = map.get('CallbackEnable')
        self.callback_uri = map.get('CallbackUri')
        self.callback_events = map.get('CallbackEvents')
        return self


class UpdateBoardCallbackResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeLiveDomainMappingRequest(TeaModel):
    def __init__(self, domain_name=None):
        self.domain_name = domain_name  # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        return self


class DescribeLiveDomainMappingResponse(TeaModel):
    def __init__(self, request_id=None, live_domain_models=None):
        self.request_id = request_id    # type: str
        self.live_domain_models = live_domain_models  # type: DescribeLiveDomainMappingResponseLiveDomainModels

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.live_domain_models, 'live_domain_models')
        if self.live_domain_models:
            self.live_domain_models.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.live_domain_models is not None:
            result['LiveDomainModels'] = self.live_domain_models.to_map()
        else:
            result['LiveDomainModels'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('LiveDomainModels') is not None:
            temp_model = DescribeLiveDomainMappingResponseLiveDomainModels()
            self.live_domain_models = temp_model.from_map(map['LiveDomainModels'])
        else:
            self.live_domain_models = None
        return self


class DescribeLiveDomainMappingResponseLiveDomainModelsLiveDomainModel(TeaModel):
    def __init__(self, domain_name=None, type=None):
        self.domain_name = domain_name  # type: str
        self.type = type                # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.type, 'type')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['Type'] = self.type
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.type = map.get('Type')
        return self


class DescribeLiveDomainMappingResponseLiveDomainModels(TeaModel):
    def __init__(self, live_domain_model=None):
        self.live_domain_model = live_domain_model  # type: List[DescribeLiveDomainMappingResponseLiveDomainModelsLiveDomainModel]

    def validate(self):
        self.validate_required(self.live_domain_model, 'live_domain_model')
        if self.live_domain_model:
            for k in self.live_domain_model:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['LiveDomainModel'] = []
        if self.live_domain_model is not None:
            for k in self.live_domain_model:
                result['LiveDomainModel'].append(k.to_map() if k else None)
        else:
            result['LiveDomainModel'] = None
        return result

    def from_map(self, map={}):
        self.live_domain_model = []
        if map.get('LiveDomainModel') is not None:
            for k in map.get('LiveDomainModel'):
                temp_model = DescribeLiveDomainMappingResponseLiveDomainModelsLiveDomainModel()
                self.live_domain_model.append(temp_model.from_map(k))
        else:
            self.live_domain_model = None
        return self


class StopLiveIndexRequest(TeaModel):
    def __init__(self, domain_name=None, app_name=None, stream_name=None, task_id=None):
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str
        self.stream_name = stream_name  # type: str
        self.task_id = task_id          # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.app_name, 'app_name')
        self.validate_required(self.stream_name, 'stream_name')
        self.validate_required(self.task_id, 'task_id')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        result['StreamName'] = self.stream_name
        result['TaskId'] = self.task_id
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        self.stream_name = map.get('StreamName')
        self.task_id = map.get('TaskId')
        return self


class StopLiveIndexResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class StartLiveIndexRequest(TeaModel):
    def __init__(self, domain_name=None, app_name=None, stream_name=None, token_id=None, input_url=None,
                 interval=None, oss_bucket=None, oss_endpoint=None, oss_user_id=None, oss_ram_role=None):
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str
        self.stream_name = stream_name  # type: str
        self.token_id = token_id        # type: str
        self.input_url = input_url      # type: str
        self.interval = interval        # type: int
        self.oss_bucket = oss_bucket    # type: str
        self.oss_endpoint = oss_endpoint  # type: str
        self.oss_user_id = oss_user_id  # type: str
        self.oss_ram_role = oss_ram_role  # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.app_name, 'app_name')
        self.validate_required(self.stream_name, 'stream_name')
        self.validate_required(self.token_id, 'token_id')
        self.validate_required(self.input_url, 'input_url')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        result['StreamName'] = self.stream_name
        result['TokenId'] = self.token_id
        result['InputUrl'] = self.input_url
        result['Interval'] = self.interval
        result['OssBucket'] = self.oss_bucket
        result['OssEndpoint'] = self.oss_endpoint
        result['OssUserId'] = self.oss_user_id
        result['OssRamRole'] = self.oss_ram_role
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        self.stream_name = map.get('StreamName')
        self.token_id = map.get('TokenId')
        self.input_url = map.get('InputUrl')
        self.interval = map.get('Interval')
        self.oss_bucket = map.get('OssBucket')
        self.oss_endpoint = map.get('OssEndpoint')
        self.oss_user_id = map.get('OssUserId')
        self.oss_ram_role = map.get('OssRamRole')
        return self


class StartLiveIndexResponse(TeaModel):
    def __init__(self, request_id=None, task_id=None):
        self.request_id = request_id    # type: str
        self.task_id = task_id          # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.task_id, 'task_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TaskId'] = self.task_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.task_id = map.get('TaskId')
        return self


class RealTimeSnapshotCommandRequest(TeaModel):
    def __init__(self, command=None, domain_name=None, app_name=None, stream_name=None, mode=None, interval=None):
        self.command = command          # type: str
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str
        self.stream_name = stream_name  # type: str
        self.mode = mode                # type: int
        self.interval = interval        # type: int

    def validate(self):
        self.validate_required(self.command, 'command')
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.app_name, 'app_name')
        self.validate_required(self.stream_name, 'stream_name')

    def to_map(self):
        result = {}
        result['Command'] = self.command
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        result['StreamName'] = self.stream_name
        result['Mode'] = self.mode
        result['Interval'] = self.interval
        return result

    def from_map(self, map={}):
        self.command = map.get('Command')
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        self.stream_name = map.get('StreamName')
        self.mode = map.get('Mode')
        self.interval = map.get('Interval')
        return self


class RealTimeSnapshotCommandResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeLiveTopDomainsByFlowRequest(TeaModel):
    def __init__(self, start_time=None, end_time=None, limit=None):
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.limit = limit              # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['Limit'] = self.limit
        return result

    def from_map(self, map={}):
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.limit = map.get('Limit')
        return self


class DescribeLiveTopDomainsByFlowResponse(TeaModel):
    def __init__(self, request_id=None, start_time=None, end_time=None, domain_count=None, domain_online_count=None,
                 top_domains=None):
        self.request_id = request_id    # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.domain_count = domain_count  # type: int
        self.domain_online_count = domain_online_count  # type: int
        self.top_domains = top_domains  # type: DescribeLiveTopDomainsByFlowResponseTopDomains

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.domain_count, 'domain_count')
        self.validate_required(self.domain_online_count, 'domain_online_count')
        self.validate_required(self.top_domains, 'top_domains')
        if self.top_domains:
            self.top_domains.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['DomainCount'] = self.domain_count
        result['DomainOnlineCount'] = self.domain_online_count
        if self.top_domains is not None:
            result['TopDomains'] = self.top_domains.to_map()
        else:
            result['TopDomains'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.domain_count = map.get('DomainCount')
        self.domain_online_count = map.get('DomainOnlineCount')
        if map.get('TopDomains') is not None:
            temp_model = DescribeLiveTopDomainsByFlowResponseTopDomains()
            self.top_domains = temp_model.from_map(map['TopDomains'])
        else:
            self.top_domains = None
        return self


class DescribeLiveTopDomainsByFlowResponseTopDomainsTopDomain(TeaModel):
    def __init__(self, domain_name=None, rank=None, total_traffic=None, traffic_percent=None, max_bps=None,
                 max_bps_time=None, total_access=None):
        self.domain_name = domain_name  # type: str
        self.rank = rank                # type: int
        self.total_traffic = total_traffic  # type: str
        self.traffic_percent = traffic_percent  # type: str
        self.max_bps = max_bps          # type: int
        self.max_bps_time = max_bps_time  # type: str
        self.total_access = total_access  # type: int

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.rank, 'rank')
        self.validate_required(self.total_traffic, 'total_traffic')
        self.validate_required(self.traffic_percent, 'traffic_percent')
        self.validate_required(self.max_bps, 'max_bps')
        self.validate_required(self.max_bps_time, 'max_bps_time')
        self.validate_required(self.total_access, 'total_access')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['Rank'] = self.rank
        result['TotalTraffic'] = self.total_traffic
        result['TrafficPercent'] = self.traffic_percent
        result['MaxBps'] = self.max_bps
        result['MaxBpsTime'] = self.max_bps_time
        result['TotalAccess'] = self.total_access
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.rank = map.get('Rank')
        self.total_traffic = map.get('TotalTraffic')
        self.traffic_percent = map.get('TrafficPercent')
        self.max_bps = map.get('MaxBps')
        self.max_bps_time = map.get('MaxBpsTime')
        self.total_access = map.get('TotalAccess')
        return self


class DescribeLiveTopDomainsByFlowResponseTopDomains(TeaModel):
    def __init__(self, top_domain=None):
        self.top_domain = top_domain    # type: List[DescribeLiveTopDomainsByFlowResponseTopDomainsTopDomain]

    def validate(self):
        self.validate_required(self.top_domain, 'top_domain')
        if self.top_domain:
            for k in self.top_domain:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['TopDomain'] = []
        if self.top_domain is not None:
            for k in self.top_domain:
                result['TopDomain'].append(k.to_map() if k else None)
        else:
            result['TopDomain'] = None
        return result

    def from_map(self, map={}):
        self.top_domain = []
        if map.get('TopDomain') is not None:
            for k in map.get('TopDomain'):
                temp_model = DescribeLiveTopDomainsByFlowResponseTopDomainsTopDomain()
                self.top_domain.append(temp_model.from_map(k))
        else:
            self.top_domain = None
        return self


class DescribeLiveDomainRealTimeBpsDataRequest(TeaModel):
    def __init__(self, domain_name=None, isp_name_en=None, location_name_en=None, start_time=None, end_time=None):
        self.domain_name = domain_name  # type: str
        self.isp_name_en = isp_name_en  # type: str
        self.location_name_en = location_name_en  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['IspNameEn'] = self.isp_name_en
        result['LocationNameEn'] = self.location_name_en
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.isp_name_en = map.get('IspNameEn')
        self.location_name_en = map.get('LocationNameEn')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        return self


class DescribeLiveDomainRealTimeBpsDataResponse(TeaModel):
    def __init__(self, request_id=None, domain_name=None, start_time=None, end_time=None, data_interval=None,
                 real_time_bps_data_per_interval=None):
        self.request_id = request_id    # type: str
        self.domain_name = domain_name  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.data_interval = data_interval  # type: str
        self.real_time_bps_data_per_interval = real_time_bps_data_per_interval  # type: DescribeLiveDomainRealTimeBpsDataResponseRealTimeBpsDataPerInterval

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.data_interval, 'data_interval')
        self.validate_required(self.real_time_bps_data_per_interval, 'real_time_bps_data_per_interval')
        if self.real_time_bps_data_per_interval:
            self.real_time_bps_data_per_interval.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DomainName'] = self.domain_name
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['DataInterval'] = self.data_interval
        if self.real_time_bps_data_per_interval is not None:
            result['RealTimeBpsDataPerInterval'] = self.real_time_bps_data_per_interval.to_map()
        else:
            result['RealTimeBpsDataPerInterval'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.domain_name = map.get('DomainName')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.data_interval = map.get('DataInterval')
        if map.get('RealTimeBpsDataPerInterval') is not None:
            temp_model = DescribeLiveDomainRealTimeBpsDataResponseRealTimeBpsDataPerInterval()
            self.real_time_bps_data_per_interval = temp_model.from_map(map['RealTimeBpsDataPerInterval'])
        else:
            self.real_time_bps_data_per_interval = None
        return self


class DescribeLiveDomainRealTimeBpsDataResponseRealTimeBpsDataPerIntervalDataModule(TeaModel):
    def __init__(self, time_stamp=None, value=None):
        self.time_stamp = time_stamp    # type: str
        self.value = value              # type: str

    def validate(self):
        self.validate_required(self.time_stamp, 'time_stamp')
        self.validate_required(self.value, 'value')

    def to_map(self):
        result = {}
        result['TimeStamp'] = self.time_stamp
        result['Value'] = self.value
        return result

    def from_map(self, map={}):
        self.time_stamp = map.get('TimeStamp')
        self.value = map.get('Value')
        return self


class DescribeLiveDomainRealTimeBpsDataResponseRealTimeBpsDataPerInterval(TeaModel):
    def __init__(self, data_module=None):
        self.data_module = data_module  # type: List[DescribeLiveDomainRealTimeBpsDataResponseRealTimeBpsDataPerIntervalDataModule]

    def validate(self):
        self.validate_required(self.data_module, 'data_module')
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        else:
            result['DataModule'] = None
        return result

    def from_map(self, map={}):
        self.data_module = []
        if map.get('DataModule') is not None:
            for k in map.get('DataModule'):
                temp_model = DescribeLiveDomainRealTimeBpsDataResponseRealTimeBpsDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        else:
            self.data_module = None
        return self


class DescribeLiveDomainRealTimeHttpCodeDataRequest(TeaModel):
    def __init__(self, domain_name=None, start_time=None, end_time=None, isp_name_en=None, location_name_en=None):
        self.domain_name = domain_name  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.isp_name_en = isp_name_en  # type: str
        self.location_name_en = location_name_en  # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['IspNameEn'] = self.isp_name_en
        result['LocationNameEn'] = self.location_name_en
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.isp_name_en = map.get('IspNameEn')
        self.location_name_en = map.get('LocationNameEn')
        return self


class DescribeLiveDomainRealTimeHttpCodeDataResponse(TeaModel):
    def __init__(self, request_id=None, domain_name=None, start_time=None, end_time=None, data_interval=None,
                 real_time_http_code_data=None):
        self.request_id = request_id    # type: str
        self.domain_name = domain_name  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.data_interval = data_interval  # type: str
        self.real_time_http_code_data = real_time_http_code_data  # type: DescribeLiveDomainRealTimeHttpCodeDataResponseRealTimeHttpCodeData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.data_interval, 'data_interval')
        self.validate_required(self.real_time_http_code_data, 'real_time_http_code_data')
        if self.real_time_http_code_data:
            self.real_time_http_code_data.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DomainName'] = self.domain_name
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['DataInterval'] = self.data_interval
        if self.real_time_http_code_data is not None:
            result['RealTimeHttpCodeData'] = self.real_time_http_code_data.to_map()
        else:
            result['RealTimeHttpCodeData'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.domain_name = map.get('DomainName')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.data_interval = map.get('DataInterval')
        if map.get('RealTimeHttpCodeData') is not None:
            temp_model = DescribeLiveDomainRealTimeHttpCodeDataResponseRealTimeHttpCodeData()
            self.real_time_http_code_data = temp_model.from_map(map['RealTimeHttpCodeData'])
        else:
            self.real_time_http_code_data = None
        return self


class DescribeLiveDomainRealTimeHttpCodeDataResponseRealTimeHttpCodeDataUsageDataValueRealTimeCodeProportionData(TeaModel):
    def __init__(self, code=None, proportion=None, count=None):
        self.code = code                # type: str
        self.proportion = proportion    # type: str
        self.count = count              # type: str

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.proportion, 'proportion')
        self.validate_required(self.count, 'count')

    def to_map(self):
        result = {}
        result['Code'] = self.code
        result['Proportion'] = self.proportion
        result['Count'] = self.count
        return result

    def from_map(self, map={}):
        self.code = map.get('Code')
        self.proportion = map.get('Proportion')
        self.count = map.get('Count')
        return self


class DescribeLiveDomainRealTimeHttpCodeDataResponseRealTimeHttpCodeDataUsageDataValue(TeaModel):
    def __init__(self, real_time_code_proportion_data=None):
        self.real_time_code_proportion_data = real_time_code_proportion_data  # type: List[DescribeLiveDomainRealTimeHttpCodeDataResponseRealTimeHttpCodeDataUsageDataValueRealTimeCodeProportionData]

    def validate(self):
        self.validate_required(self.real_time_code_proportion_data, 'real_time_code_proportion_data')
        if self.real_time_code_proportion_data:
            for k in self.real_time_code_proportion_data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RealTimeCodeProportionData'] = []
        if self.real_time_code_proportion_data is not None:
            for k in self.real_time_code_proportion_data:
                result['RealTimeCodeProportionData'].append(k.to_map() if k else None)
        else:
            result['RealTimeCodeProportionData'] = None
        return result

    def from_map(self, map={}):
        self.real_time_code_proportion_data = []
        if map.get('RealTimeCodeProportionData') is not None:
            for k in map.get('RealTimeCodeProportionData'):
                temp_model = DescribeLiveDomainRealTimeHttpCodeDataResponseRealTimeHttpCodeDataUsageDataValueRealTimeCodeProportionData()
                self.real_time_code_proportion_data.append(temp_model.from_map(k))
        else:
            self.real_time_code_proportion_data = None
        return self


class DescribeLiveDomainRealTimeHttpCodeDataResponseRealTimeHttpCodeDataUsageData(TeaModel):
    def __init__(self, time_stamp=None, value=None):
        self.time_stamp = time_stamp    # type: str
        self.value = value              # type: DescribeLiveDomainRealTimeHttpCodeDataResponseRealTimeHttpCodeDataUsageDataValue

    def validate(self):
        self.validate_required(self.time_stamp, 'time_stamp')
        self.validate_required(self.value, 'value')
        if self.value:
            self.value.validate()

    def to_map(self):
        result = {}
        result['TimeStamp'] = self.time_stamp
        if self.value is not None:
            result['Value'] = self.value.to_map()
        else:
            result['Value'] = None
        return result

    def from_map(self, map={}):
        self.time_stamp = map.get('TimeStamp')
        if map.get('Value') is not None:
            temp_model = DescribeLiveDomainRealTimeHttpCodeDataResponseRealTimeHttpCodeDataUsageDataValue()
            self.value = temp_model.from_map(map['Value'])
        else:
            self.value = None
        return self


class DescribeLiveDomainRealTimeHttpCodeDataResponseRealTimeHttpCodeData(TeaModel):
    def __init__(self, usage_data=None):
        self.usage_data = usage_data    # type: List[DescribeLiveDomainRealTimeHttpCodeDataResponseRealTimeHttpCodeDataUsageData]

    def validate(self):
        self.validate_required(self.usage_data, 'usage_data')
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['UsageData'] = []
        if self.usage_data is not None:
            for k in self.usage_data:
                result['UsageData'].append(k.to_map() if k else None)
        else:
            result['UsageData'] = None
        return result

    def from_map(self, map={}):
        self.usage_data = []
        if map.get('UsageData') is not None:
            for k in map.get('UsageData'):
                temp_model = DescribeLiveDomainRealTimeHttpCodeDataResponseRealTimeHttpCodeDataUsageData()
                self.usage_data.append(temp_model.from_map(k))
        else:
            self.usage_data = None
        return self


class DescribeLiveDomainRealTimeTrafficDataRequest(TeaModel):
    def __init__(self, domain_name=None, start_time=None, isp_name_en=None, location_name_en=None, end_time=None):
        self.domain_name = domain_name  # type: str
        self.start_time = start_time    # type: str
        self.isp_name_en = isp_name_en  # type: str
        self.location_name_en = location_name_en  # type: str
        self.end_time = end_time        # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['StartTime'] = self.start_time
        result['IspNameEn'] = self.isp_name_en
        result['LocationNameEn'] = self.location_name_en
        result['EndTime'] = self.end_time
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.start_time = map.get('StartTime')
        self.isp_name_en = map.get('IspNameEn')
        self.location_name_en = map.get('LocationNameEn')
        self.end_time = map.get('EndTime')
        return self


class DescribeLiveDomainRealTimeTrafficDataResponse(TeaModel):
    def __init__(self, request_id=None, domain_name=None, start_time=None, end_time=None, data_interval=None,
                 real_time_traffic_data_per_interval=None):
        self.request_id = request_id    # type: str
        self.domain_name = domain_name  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.data_interval = data_interval  # type: str
        self.real_time_traffic_data_per_interval = real_time_traffic_data_per_interval  # type: DescribeLiveDomainRealTimeTrafficDataResponseRealTimeTrafficDataPerInterval

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.data_interval, 'data_interval')
        self.validate_required(self.real_time_traffic_data_per_interval, 'real_time_traffic_data_per_interval')
        if self.real_time_traffic_data_per_interval:
            self.real_time_traffic_data_per_interval.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DomainName'] = self.domain_name
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['DataInterval'] = self.data_interval
        if self.real_time_traffic_data_per_interval is not None:
            result['RealTimeTrafficDataPerInterval'] = self.real_time_traffic_data_per_interval.to_map()
        else:
            result['RealTimeTrafficDataPerInterval'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.domain_name = map.get('DomainName')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.data_interval = map.get('DataInterval')
        if map.get('RealTimeTrafficDataPerInterval') is not None:
            temp_model = DescribeLiveDomainRealTimeTrafficDataResponseRealTimeTrafficDataPerInterval()
            self.real_time_traffic_data_per_interval = temp_model.from_map(map['RealTimeTrafficDataPerInterval'])
        else:
            self.real_time_traffic_data_per_interval = None
        return self


class DescribeLiveDomainRealTimeTrafficDataResponseRealTimeTrafficDataPerIntervalDataModule(TeaModel):
    def __init__(self, time_stamp=None, value=None):
        self.time_stamp = time_stamp    # type: str
        self.value = value              # type: str

    def validate(self):
        self.validate_required(self.time_stamp, 'time_stamp')
        self.validate_required(self.value, 'value')

    def to_map(self):
        result = {}
        result['TimeStamp'] = self.time_stamp
        result['Value'] = self.value
        return result

    def from_map(self, map={}):
        self.time_stamp = map.get('TimeStamp')
        self.value = map.get('Value')
        return self


class DescribeLiveDomainRealTimeTrafficDataResponseRealTimeTrafficDataPerInterval(TeaModel):
    def __init__(self, data_module=None):
        self.data_module = data_module  # type: List[DescribeLiveDomainRealTimeTrafficDataResponseRealTimeTrafficDataPerIntervalDataModule]

    def validate(self):
        self.validate_required(self.data_module, 'data_module')
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        else:
            result['DataModule'] = None
        return result

    def from_map(self, map={}):
        self.data_module = []
        if map.get('DataModule') is not None:
            for k in map.get('DataModule'):
                temp_model = DescribeLiveDomainRealTimeTrafficDataResponseRealTimeTrafficDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        else:
            self.data_module = None
        return self


class AddLiveDomainPlayMappingRequest(TeaModel):
    def __init__(self, play_domain=None, pull_domain=None):
        self.play_domain = play_domain  # type: str
        self.pull_domain = pull_domain  # type: str

    def validate(self):
        self.validate_required(self.play_domain, 'play_domain')
        self.validate_required(self.pull_domain, 'pull_domain')

    def to_map(self):
        result = {}
        result['PlayDomain'] = self.play_domain
        result['PullDomain'] = self.pull_domain
        return result

    def from_map(self, map={}):
        self.play_domain = map.get('PlayDomain')
        self.pull_domain = map.get('PullDomain')
        return self


class AddLiveDomainPlayMappingResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DeleteLiveLazyPullStreamInfoConfigRequest(TeaModel):
    def __init__(self, domain_name=None, app_name=None):
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.app_name, 'app_name')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        return self


class DeleteLiveLazyPullStreamInfoConfigResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeLiveLazyPullStreamConfigRequest(TeaModel):
    def __init__(self, domain_name=None, app_name=None, liveapi_request_from=None):
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str
        self.liveapi_request_from = liveapi_request_from  # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        result['LiveapiRequestFrom'] = self.liveapi_request_from
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        self.liveapi_request_from = map.get('LiveapiRequestFrom')
        return self


class DescribeLiveLazyPullStreamConfigResponse(TeaModel):
    def __init__(self, request_id=None, live_lazy_pull_config_list=None):
        self.request_id = request_id    # type: str
        self.live_lazy_pull_config_list = live_lazy_pull_config_list  # type: DescribeLiveLazyPullStreamConfigResponseLiveLazyPullConfigList

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.live_lazy_pull_config_list, 'live_lazy_pull_config_list')
        if self.live_lazy_pull_config_list:
            self.live_lazy_pull_config_list.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.live_lazy_pull_config_list is not None:
            result['LiveLazyPullConfigList'] = self.live_lazy_pull_config_list.to_map()
        else:
            result['LiveLazyPullConfigList'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('LiveLazyPullConfigList') is not None:
            temp_model = DescribeLiveLazyPullStreamConfigResponseLiveLazyPullConfigList()
            self.live_lazy_pull_config_list = temp_model.from_map(map['LiveLazyPullConfigList'])
        else:
            self.live_lazy_pull_config_list = None
        return self


class DescribeLiveLazyPullStreamConfigResponseLiveLazyPullConfigListLiveLazyPullConfig(TeaModel):
    def __init__(self, domain_name=None, app_name=None, pull_domain_name=None, pull_app_name=None,
                 pull_protocol=None, pull_auth_type=None, pull_auth_key=None, pull_args=None):
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str
        self.pull_domain_name = pull_domain_name  # type: str
        self.pull_app_name = pull_app_name  # type: str
        self.pull_protocol = pull_protocol  # type: str
        self.pull_auth_type = pull_auth_type  # type: str
        self.pull_auth_key = pull_auth_key  # type: str
        self.pull_args = pull_args      # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.app_name, 'app_name')
        self.validate_required(self.pull_domain_name, 'pull_domain_name')
        self.validate_required(self.pull_app_name, 'pull_app_name')
        self.validate_required(self.pull_protocol, 'pull_protocol')
        self.validate_required(self.pull_auth_type, 'pull_auth_type')
        self.validate_required(self.pull_auth_key, 'pull_auth_key')
        self.validate_required(self.pull_args, 'pull_args')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        result['PullDomainName'] = self.pull_domain_name
        result['PullAppName'] = self.pull_app_name
        result['PullProtocol'] = self.pull_protocol
        result['PullAuthType'] = self.pull_auth_type
        result['PullAuthKey'] = self.pull_auth_key
        result['PullArgs'] = self.pull_args
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        self.pull_domain_name = map.get('PullDomainName')
        self.pull_app_name = map.get('PullAppName')
        self.pull_protocol = map.get('PullProtocol')
        self.pull_auth_type = map.get('PullAuthType')
        self.pull_auth_key = map.get('PullAuthKey')
        self.pull_args = map.get('PullArgs')
        return self


class DescribeLiveLazyPullStreamConfigResponseLiveLazyPullConfigList(TeaModel):
    def __init__(self, live_lazy_pull_config=None):
        self.live_lazy_pull_config = live_lazy_pull_config  # type: List[DescribeLiveLazyPullStreamConfigResponseLiveLazyPullConfigListLiveLazyPullConfig]

    def validate(self):
        self.validate_required(self.live_lazy_pull_config, 'live_lazy_pull_config')
        if self.live_lazy_pull_config:
            for k in self.live_lazy_pull_config:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['LiveLazyPullConfig'] = []
        if self.live_lazy_pull_config is not None:
            for k in self.live_lazy_pull_config:
                result['LiveLazyPullConfig'].append(k.to_map() if k else None)
        else:
            result['LiveLazyPullConfig'] = None
        return result

    def from_map(self, map={}):
        self.live_lazy_pull_config = []
        if map.get('LiveLazyPullConfig') is not None:
            for k in map.get('LiveLazyPullConfig'):
                temp_model = DescribeLiveLazyPullStreamConfigResponseLiveLazyPullConfigListLiveLazyPullConfig()
                self.live_lazy_pull_config.append(temp_model.from_map(k))
        else:
            self.live_lazy_pull_config = None
        return self


class SetLiveLazyPullStreamInfoConfigRequest(TeaModel):
    def __init__(self, domain_name=None, app_name=None, pull_domain_name=None, pull_app_name=None,
                 pull_protocol=None, pull_auth_type=None, pull_auth_key=None, pull_args=None, liveapi_request_from=None):
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str
        self.pull_domain_name = pull_domain_name  # type: str
        self.pull_app_name = pull_app_name  # type: str
        self.pull_protocol = pull_protocol  # type: str
        self.pull_auth_type = pull_auth_type  # type: str
        self.pull_auth_key = pull_auth_key  # type: str
        self.pull_args = pull_args      # type: str
        self.liveapi_request_from = liveapi_request_from  # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.app_name, 'app_name')
        self.validate_required(self.pull_domain_name, 'pull_domain_name')
        self.validate_required(self.pull_protocol, 'pull_protocol')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        result['PullDomainName'] = self.pull_domain_name
        result['PullAppName'] = self.pull_app_name
        result['PullProtocol'] = self.pull_protocol
        result['PullAuthType'] = self.pull_auth_type
        result['PullAuthKey'] = self.pull_auth_key
        result['PullArgs'] = self.pull_args
        result['LiveapiRequestFrom'] = self.liveapi_request_from
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        self.pull_domain_name = map.get('PullDomainName')
        self.pull_app_name = map.get('PullAppName')
        self.pull_protocol = map.get('PullProtocol')
        self.pull_auth_type = map.get('PullAuthType')
        self.pull_auth_key = map.get('PullAuthKey')
        self.pull_args = map.get('PullArgs')
        self.liveapi_request_from = map.get('LiveapiRequestFrom')
        return self


class SetLiveLazyPullStreamInfoConfigResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class UpdateCasterSceneAudioRequest(TeaModel):
    def __init__(self, caster_id=None, scene_id=None, follow_enable=None, audio_layer=None, mix_list=None):
        self.caster_id = caster_id      # type: str
        self.scene_id = scene_id        # type: str
        self.follow_enable = follow_enable  # type: int
        self.audio_layer = audio_layer  # type: List[UpdateCasterSceneAudioRequestAudioLayer]
        self.mix_list = mix_list        # type: List[str]

    def validate(self):
        self.validate_required(self.caster_id, 'caster_id')
        self.validate_required(self.scene_id, 'scene_id')
        if self.audio_layer:
            for k in self.audio_layer:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['CasterId'] = self.caster_id
        result['SceneId'] = self.scene_id
        result['FollowEnable'] = self.follow_enable
        result['AudioLayer'] = []
        if self.audio_layer is not None:
            for k in self.audio_layer:
                result['AudioLayer'].append(k.to_map() if k else None)
        else:
            result['AudioLayer'] = None
        result['MixList'] = self.mix_list
        return result

    def from_map(self, map={}):
        self.caster_id = map.get('CasterId')
        self.scene_id = map.get('SceneId')
        self.follow_enable = map.get('FollowEnable')
        self.audio_layer = []
        if map.get('AudioLayer') is not None:
            for k in map.get('AudioLayer'):
                temp_model = UpdateCasterSceneAudioRequestAudioLayer()
                self.audio_layer.append(temp_model.from_map(k))
        else:
            self.audio_layer = None
        self.mix_list = map.get('MixList')
        return self


class UpdateCasterSceneAudioRequestAudioLayer(TeaModel):
    def __init__(self, volume_rate=None, valid_channel=None, fixed_delay_duration=None):
        self.volume_rate = volume_rate  # type: float
        self.valid_channel = valid_channel  # type: str
        self.fixed_delay_duration = fixed_delay_duration  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['VolumeRate'] = self.volume_rate
        result['ValidChannel'] = self.valid_channel
        result['FixedDelayDuration'] = self.fixed_delay_duration
        return result

    def from_map(self, map={}):
        self.volume_rate = map.get('VolumeRate')
        self.valid_channel = map.get('ValidChannel')
        self.fixed_delay_duration = map.get('FixedDelayDuration')
        return self


class UpdateCasterSceneAudioResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class SetCasterChannelRequest(TeaModel):
    def __init__(self, caster_id=None, channel_id=None, resource_id=None, seek_offset=None, play_status=None,
                 reload_flag=None):
        self.caster_id = caster_id      # type: str
        self.channel_id = channel_id    # type: str
        self.resource_id = resource_id  # type: str
        self.seek_offset = seek_offset  # type: int
        self.play_status = play_status  # type: int
        self.reload_flag = reload_flag  # type: int

    def validate(self):
        self.validate_required(self.caster_id, 'caster_id')
        self.validate_required(self.channel_id, 'channel_id')

    def to_map(self):
        result = {}
        result['CasterId'] = self.caster_id
        result['ChannelId'] = self.channel_id
        result['ResourceId'] = self.resource_id
        result['SeekOffset'] = self.seek_offset
        result['PlayStatus'] = self.play_status
        result['ReloadFlag'] = self.reload_flag
        return result

    def from_map(self, map={}):
        self.caster_id = map.get('CasterId')
        self.channel_id = map.get('ChannelId')
        self.resource_id = map.get('ResourceId')
        self.seek_offset = map.get('SeekOffset')
        self.play_status = map.get('PlayStatus')
        self.reload_flag = map.get('ReloadFlag')
        return self


class SetCasterChannelResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeCasterSceneAudioRequest(TeaModel):
    def __init__(self, caster_id=None, scene_id=None):
        self.caster_id = caster_id      # type: str
        self.scene_id = scene_id        # type: str

    def validate(self):
        self.validate_required(self.caster_id, 'caster_id')
        self.validate_required(self.scene_id, 'scene_id')

    def to_map(self):
        result = {}
        result['CasterId'] = self.caster_id
        result['SceneId'] = self.scene_id
        return result

    def from_map(self, map={}):
        self.caster_id = map.get('CasterId')
        self.scene_id = map.get('SceneId')
        return self


class DescribeCasterSceneAudioResponse(TeaModel):
    def __init__(self, request_id=None, caster_id=None, follow_enable=None, audio_layers=None, mix_list=None):
        self.request_id = request_id    # type: str
        self.caster_id = caster_id      # type: str
        self.follow_enable = follow_enable  # type: int
        self.audio_layers = audio_layers  # type: DescribeCasterSceneAudioResponseAudioLayers
        self.mix_list = mix_list        # type: DescribeCasterSceneAudioResponseMixList

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.caster_id, 'caster_id')
        self.validate_required(self.follow_enable, 'follow_enable')
        self.validate_required(self.audio_layers, 'audio_layers')
        if self.audio_layers:
            self.audio_layers.validate()
        self.validate_required(self.mix_list, 'mix_list')
        if self.mix_list:
            self.mix_list.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['CasterId'] = self.caster_id
        result['FollowEnable'] = self.follow_enable
        if self.audio_layers is not None:
            result['AudioLayers'] = self.audio_layers.to_map()
        else:
            result['AudioLayers'] = None
        if self.mix_list is not None:
            result['MixList'] = self.mix_list.to_map()
        else:
            result['MixList'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.caster_id = map.get('CasterId')
        self.follow_enable = map.get('FollowEnable')
        if map.get('AudioLayers') is not None:
            temp_model = DescribeCasterSceneAudioResponseAudioLayers()
            self.audio_layers = temp_model.from_map(map['AudioLayers'])
        else:
            self.audio_layers = None
        if map.get('MixList') is not None:
            temp_model = DescribeCasterSceneAudioResponseMixList()
            self.mix_list = temp_model.from_map(map['MixList'])
        else:
            self.mix_list = None
        return self


class DescribeCasterSceneAudioResponseAudioLayersAudioLayer(TeaModel):
    def __init__(self, volume_rate=None, valid_channel=None, fixed_delay_duration=None):
        self.volume_rate = volume_rate  # type: float
        self.valid_channel = valid_channel  # type: str
        self.fixed_delay_duration = fixed_delay_duration  # type: int

    def validate(self):
        self.validate_required(self.volume_rate, 'volume_rate')
        self.validate_required(self.valid_channel, 'valid_channel')
        self.validate_required(self.fixed_delay_duration, 'fixed_delay_duration')

    def to_map(self):
        result = {}
        result['VolumeRate'] = self.volume_rate
        result['ValidChannel'] = self.valid_channel
        result['FixedDelayDuration'] = self.fixed_delay_duration
        return result

    def from_map(self, map={}):
        self.volume_rate = map.get('VolumeRate')
        self.valid_channel = map.get('ValidChannel')
        self.fixed_delay_duration = map.get('FixedDelayDuration')
        return self


class DescribeCasterSceneAudioResponseAudioLayers(TeaModel):
    def __init__(self, audio_layer=None):
        self.audio_layer = audio_layer  # type: List[DescribeCasterSceneAudioResponseAudioLayersAudioLayer]

    def validate(self):
        self.validate_required(self.audio_layer, 'audio_layer')
        if self.audio_layer:
            for k in self.audio_layer:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['AudioLayer'] = []
        if self.audio_layer is not None:
            for k in self.audio_layer:
                result['AudioLayer'].append(k.to_map() if k else None)
        else:
            result['AudioLayer'] = None
        return result

    def from_map(self, map={}):
        self.audio_layer = []
        if map.get('AudioLayer') is not None:
            for k in map.get('AudioLayer'):
                temp_model = DescribeCasterSceneAudioResponseAudioLayersAudioLayer()
                self.audio_layer.append(temp_model.from_map(k))
        else:
            self.audio_layer = None
        return self


class DescribeCasterSceneAudioResponseMixList(TeaModel):
    def __init__(self, location_id=None):
        self.location_id = location_id  # type: List[str]

    def validate(self):
        self.validate_required(self.location_id, 'location_id')

    def to_map(self):
        result = {}
        result['LocationId'] = self.location_id
        return result

    def from_map(self, map={}):
        self.location_id = map.get('LocationId')
        return self


class DescribeCasterChannelsRequest(TeaModel):
    def __init__(self, caster_id=None):
        self.caster_id = caster_id      # type: str

    def validate(self):
        self.validate_required(self.caster_id, 'caster_id')

    def to_map(self):
        result = {}
        result['CasterId'] = self.caster_id
        return result

    def from_map(self, map={}):
        self.caster_id = map.get('CasterId')
        return self


class DescribeCasterChannelsResponse(TeaModel):
    def __init__(self, request_id=None, total=None, channels=None):
        self.request_id = request_id    # type: str
        self.total = total              # type: int
        self.channels = channels        # type: DescribeCasterChannelsResponseChannels

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total, 'total')
        self.validate_required(self.channels, 'channels')
        if self.channels:
            self.channels.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Total'] = self.total
        if self.channels is not None:
            result['Channels'] = self.channels.to_map()
        else:
            result['Channels'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total = map.get('Total')
        if map.get('Channels') is not None:
            temp_model = DescribeCasterChannelsResponseChannels()
            self.channels = temp_model.from_map(map['Channels'])
        else:
            self.channels = None
        return self


class DescribeCasterChannelsResponseChannelsChannel(TeaModel):
    def __init__(self, channel_id=None, resource_id=None, stream_url=None, rtmp_url=None):
        self.channel_id = channel_id    # type: str
        self.resource_id = resource_id  # type: str
        self.stream_url = stream_url    # type: str
        self.rtmp_url = rtmp_url        # type: str

    def validate(self):
        self.validate_required(self.channel_id, 'channel_id')
        self.validate_required(self.resource_id, 'resource_id')
        self.validate_required(self.stream_url, 'stream_url')
        self.validate_required(self.rtmp_url, 'rtmp_url')

    def to_map(self):
        result = {}
        result['ChannelId'] = self.channel_id
        result['ResourceId'] = self.resource_id
        result['StreamUrl'] = self.stream_url
        result['RtmpUrl'] = self.rtmp_url
        return result

    def from_map(self, map={}):
        self.channel_id = map.get('ChannelId')
        self.resource_id = map.get('ResourceId')
        self.stream_url = map.get('StreamUrl')
        self.rtmp_url = map.get('RtmpUrl')
        return self


class DescribeCasterChannelsResponseChannels(TeaModel):
    def __init__(self, channel=None):
        self.channel = channel          # type: List[DescribeCasterChannelsResponseChannelsChannel]

    def validate(self):
        self.validate_required(self.channel, 'channel')
        if self.channel:
            for k in self.channel:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Channel'] = []
        if self.channel is not None:
            for k in self.channel:
                result['Channel'].append(k.to_map() if k else None)
        else:
            result['Channel'] = None
        return result

    def from_map(self, map={}):
        self.channel = []
        if map.get('Channel') is not None:
            for k in map.get('Channel'):
                temp_model = DescribeCasterChannelsResponseChannelsChannel()
                self.channel.append(temp_model.from_map(k))
        else:
            self.channel = None
        return self


class UpdateBoardRequest(TeaModel):
    def __init__(self, app_id=None, board_data=None):
        self.app_id = app_id            # type: str
        self.board_data = board_data    # type: str

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.board_data, 'board_data')

    def to_map(self):
        result = {}
        result['AppId'] = self.app_id
        result['BoardData'] = self.board_data
        return result

    def from_map(self, map={}):
        self.app_id = map.get('AppId')
        self.board_data = map.get('BoardData')
        return self


class UpdateBoardResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class JoinBoardRequest(TeaModel):
    def __init__(self, app_id=None, app_uid=None, board_id=None):
        self.app_id = app_id            # type: str
        self.app_uid = app_uid          # type: str
        self.board_id = board_id        # type: str

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.app_uid, 'app_uid')
        self.validate_required(self.board_id, 'board_id')

    def to_map(self):
        result = {}
        result['AppId'] = self.app_id
        result['AppUid'] = self.app_uid
        result['BoardId'] = self.board_id
        return result

    def from_map(self, map={}):
        self.app_id = map.get('AppId')
        self.app_uid = map.get('AppUid')
        self.board_id = map.get('BoardId')
        return self


class JoinBoardResponse(TeaModel):
    def __init__(self, request_id=None, token=None, board_id=None, topic_id=None, keepalive_topic=None,
                 keepalive_interval=None):
        self.request_id = request_id    # type: str
        self.token = token              # type: str
        self.board_id = board_id        # type: str
        self.topic_id = topic_id        # type: str
        self.keepalive_topic = keepalive_topic  # type: str
        self.keepalive_interval = keepalive_interval  # type: int

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.token, 'token')
        self.validate_required(self.board_id, 'board_id')
        self.validate_required(self.topic_id, 'topic_id')
        self.validate_required(self.keepalive_topic, 'keepalive_topic')
        self.validate_required(self.keepalive_interval, 'keepalive_interval')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Token'] = self.token
        result['BoardId'] = self.board_id
        result['TopicId'] = self.topic_id
        result['KeepaliveTopic'] = self.keepalive_topic
        result['KeepaliveInterval'] = self.keepalive_interval
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.token = map.get('Token')
        self.board_id = map.get('BoardId')
        self.topic_id = map.get('TopicId')
        self.keepalive_topic = map.get('KeepaliveTopic')
        self.keepalive_interval = map.get('KeepaliveInterval')
        return self


class DescribeBoardSnapshotRequest(TeaModel):
    def __init__(self, app_id=None, board_id=None):
        self.app_id = app_id            # type: str
        self.board_id = board_id        # type: str

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.board_id, 'board_id')

    def to_map(self):
        result = {}
        result['AppId'] = self.app_id
        result['BoardId'] = self.board_id
        return result

    def from_map(self, map={}):
        self.app_id = map.get('AppId')
        self.board_id = map.get('BoardId')
        return self


class DescribeBoardSnapshotResponse(TeaModel):
    def __init__(self, request_id=None, snapshot=None):
        self.request_id = request_id    # type: str
        self.snapshot = snapshot        # type: DescribeBoardSnapshotResponseSnapshot

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.snapshot, 'snapshot')
        if self.snapshot:
            self.snapshot.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.snapshot is not None:
            result['Snapshot'] = self.snapshot.to_map()
        else:
            result['Snapshot'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('Snapshot') is not None:
            temp_model = DescribeBoardSnapshotResponseSnapshot()
            self.snapshot = temp_model.from_map(map['Snapshot'])
        else:
            self.snapshot = None
        return self


class DescribeBoardSnapshotResponseSnapshotBoardPagesElements(TeaModel):
    def __init__(self, element_index=None, owner_id=None, element_type=None, update_timestamp=None, data=None):
        self.element_index = element_index  # type: str
        self.owner_id = owner_id        # type: str
        self.element_type = element_type  # type: int
        self.update_timestamp = update_timestamp  # type: int
        self.data = data                # type: str

    def validate(self):
        self.validate_required(self.element_index, 'element_index')
        self.validate_required(self.owner_id, 'owner_id')
        self.validate_required(self.element_type, 'element_type')
        self.validate_required(self.update_timestamp, 'update_timestamp')
        self.validate_required(self.data, 'data')

    def to_map(self):
        result = {}
        result['ElementIndex'] = self.element_index
        result['OwnerId'] = self.owner_id
        result['ElementType'] = self.element_type
        result['UpdateTimestamp'] = self.update_timestamp
        result['Data'] = self.data
        return result

    def from_map(self, map={}):
        self.element_index = map.get('ElementIndex')
        self.owner_id = map.get('OwnerId')
        self.element_type = map.get('ElementType')
        self.update_timestamp = map.get('UpdateTimestamp')
        self.data = map.get('Data')
        return self


class DescribeBoardSnapshotResponseSnapshotBoardPages(TeaModel):
    def __init__(self, page_index=None, elements=None):
        self.page_index = page_index    # type: int
        self.elements = elements        # type: List[DescribeBoardSnapshotResponseSnapshotBoardPagesElements]

    def validate(self):
        self.validate_required(self.page_index, 'page_index')
        self.validate_required(self.elements, 'elements')
        if self.elements:
            for k in self.elements:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PageIndex'] = self.page_index
        result['Elements'] = []
        if self.elements is not None:
            for k in self.elements:
                result['Elements'].append(k.to_map() if k else None)
        else:
            result['Elements'] = None
        return result

    def from_map(self, map={}):
        self.page_index = map.get('PageIndex')
        self.elements = []
        if map.get('Elements') is not None:
            for k in map.get('Elements'):
                temp_model = DescribeBoardSnapshotResponseSnapshotBoardPagesElements()
                self.elements.append(temp_model.from_map(k))
        else:
            self.elements = None
        return self


class DescribeBoardSnapshotResponseSnapshotBoardConfigs(TeaModel):
    def __init__(self, app_uid=None, data=None):
        self.app_uid = app_uid          # type: str
        self.data = data                # type: str

    def validate(self):
        self.validate_required(self.app_uid, 'app_uid')
        self.validate_required(self.data, 'data')

    def to_map(self):
        result = {}
        result['AppUid'] = self.app_uid
        result['Data'] = self.data
        return result

    def from_map(self, map={}):
        self.app_uid = map.get('AppUid')
        self.data = map.get('Data')
        return self


class DescribeBoardSnapshotResponseSnapshotBoard(TeaModel):
    def __init__(self, board_id=None, app_uid=None, event_timestamp=None, create_timestamp=None,
                 update_timestamp=None, pages=None, configs=None):
        self.board_id = board_id        # type: str
        self.app_uid = app_uid          # type: str
        self.event_timestamp = event_timestamp  # type: int
        self.create_timestamp = create_timestamp  # type: int
        self.update_timestamp = update_timestamp  # type: int
        self.pages = pages              # type: List[DescribeBoardSnapshotResponseSnapshotBoardPages]
        self.configs = configs          # type: List[DescribeBoardSnapshotResponseSnapshotBoardConfigs]

    def validate(self):
        self.validate_required(self.board_id, 'board_id')
        self.validate_required(self.app_uid, 'app_uid')
        self.validate_required(self.event_timestamp, 'event_timestamp')
        self.validate_required(self.create_timestamp, 'create_timestamp')
        self.validate_required(self.update_timestamp, 'update_timestamp')
        self.validate_required(self.pages, 'pages')
        if self.pages:
            for k in self.pages:
                if k:
                    k.validate()
        self.validate_required(self.configs, 'configs')
        if self.configs:
            for k in self.configs:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['BoardId'] = self.board_id
        result['AppUid'] = self.app_uid
        result['EventTimestamp'] = self.event_timestamp
        result['CreateTimestamp'] = self.create_timestamp
        result['UpdateTimestamp'] = self.update_timestamp
        result['Pages'] = []
        if self.pages is not None:
            for k in self.pages:
                result['Pages'].append(k.to_map() if k else None)
        else:
            result['Pages'] = None
        result['Configs'] = []
        if self.configs is not None:
            for k in self.configs:
                result['Configs'].append(k.to_map() if k else None)
        else:
            result['Configs'] = None
        return result

    def from_map(self, map={}):
        self.board_id = map.get('BoardId')
        self.app_uid = map.get('AppUid')
        self.event_timestamp = map.get('EventTimestamp')
        self.create_timestamp = map.get('CreateTimestamp')
        self.update_timestamp = map.get('UpdateTimestamp')
        self.pages = []
        if map.get('Pages') is not None:
            for k in map.get('Pages'):
                temp_model = DescribeBoardSnapshotResponseSnapshotBoardPages()
                self.pages.append(temp_model.from_map(k))
        else:
            self.pages = None
        self.configs = []
        if map.get('Configs') is not None:
            for k in map.get('Configs'):
                temp_model = DescribeBoardSnapshotResponseSnapshotBoardConfigs()
                self.configs.append(temp_model.from_map(k))
        else:
            self.configs = None
        return self


class DescribeBoardSnapshotResponseSnapshot(TeaModel):
    def __init__(self, board=None):
        self.board = board              # type: DescribeBoardSnapshotResponseSnapshotBoard

    def validate(self):
        self.validate_required(self.board, 'board')
        if self.board:
            self.board.validate()

    def to_map(self):
        result = {}
        if self.board is not None:
            result['Board'] = self.board.to_map()
        else:
            result['Board'] = None
        return result

    def from_map(self, map={}):
        if map.get('Board') is not None:
            temp_model = DescribeBoardSnapshotResponseSnapshotBoard()
            self.board = temp_model.from_map(map['Board'])
        else:
            self.board = None
        return self


class DescribeBoardsRequest(TeaModel):
    def __init__(self, app_id=None, page_num=None, page_size=None):
        self.app_id = app_id            # type: str
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.page_num, 'page_num')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        result = {}
        result['AppId'] = self.app_id
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.app_id = map.get('AppId')
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        return self


class DescribeBoardsResponse(TeaModel):
    def __init__(self, request_id=None, boards=None):
        self.request_id = request_id    # type: str
        self.boards = boards            # type: List[DescribeBoardsResponseBoards]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.boards, 'boards')
        if self.boards:
            for k in self.boards:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Boards'] = []
        if self.boards is not None:
            for k in self.boards:
                result['Boards'].append(k.to_map() if k else None)
        else:
            result['Boards'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.boards = []
        if map.get('Boards') is not None:
            for k in map.get('Boards'):
                temp_model = DescribeBoardsResponseBoards()
                self.boards.append(temp_model.from_map(k))
        else:
            self.boards = None
        return self


class DescribeBoardsResponseBoards(TeaModel):
    def __init__(self, board_id=None, topic=None, state=None, user_id=None):
        self.board_id = board_id        # type: str
        self.topic = topic              # type: str
        self.state = state              # type: int
        self.user_id = user_id          # type: str

    def validate(self):
        self.validate_required(self.board_id, 'board_id')
        self.validate_required(self.topic, 'topic')
        self.validate_required(self.state, 'state')
        self.validate_required(self.user_id, 'user_id')

    def to_map(self):
        result = {}
        result['BoardId'] = self.board_id
        result['Topic'] = self.topic
        result['State'] = self.state
        result['UserId'] = self.user_id
        return result

    def from_map(self, map={}):
        self.board_id = map.get('BoardId')
        self.topic = map.get('Topic')
        self.state = map.get('State')
        self.user_id = map.get('UserId')
        return self


class DescribeBoardEventsRequest(TeaModel):
    def __init__(self, app_id=None, start_time=None, end_time=None, board_id=None):
        self.app_id = app_id            # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.board_id = board_id        # type: str

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.board_id, 'board_id')

    def to_map(self):
        result = {}
        result['AppId'] = self.app_id
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['BoardId'] = self.board_id
        return result

    def from_map(self, map={}):
        self.app_id = map.get('AppId')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.board_id = map.get('BoardId')
        return self


class DescribeBoardEventsResponse(TeaModel):
    def __init__(self, request_id=None, events=None):
        self.request_id = request_id    # type: str
        self.events = events            # type: List[DescribeBoardEventsResponseEvents]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.events, 'events')
        if self.events:
            for k in self.events:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Events'] = []
        if self.events is not None:
            for k in self.events:
                result['Events'].append(k.to_map() if k else None)
        else:
            result['Events'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.events = []
        if map.get('Events') is not None:
            for k in map.get('Events'):
                temp_model = DescribeBoardEventsResponseEvents()
                self.events.append(temp_model.from_map(k))
        else:
            self.events = None
        return self


class DescribeBoardEventsResponseEvents(TeaModel):
    def __init__(self, event_id=None, event_type=None, user_id=None, data=None, timestamp=None):
        self.event_id = event_id        # type: int
        self.event_type = event_type    # type: int
        self.user_id = user_id          # type: int
        self.data = data                # type: str
        self.timestamp = timestamp      # type: int

    def validate(self):
        self.validate_required(self.event_id, 'event_id')
        self.validate_required(self.event_type, 'event_type')
        self.validate_required(self.user_id, 'user_id')
        self.validate_required(self.data, 'data')
        self.validate_required(self.timestamp, 'timestamp')

    def to_map(self):
        result = {}
        result['EventId'] = self.event_id
        result['EventType'] = self.event_type
        result['UserId'] = self.user_id
        result['Data'] = self.data
        result['Timestamp'] = self.timestamp
        return result

    def from_map(self, map={}):
        self.event_id = map.get('EventId')
        self.event_type = map.get('EventType')
        self.user_id = map.get('UserId')
        self.data = map.get('Data')
        self.timestamp = map.get('Timestamp')
        return self


class DeleteBoardRequest(TeaModel):
    def __init__(self, app_id=None, board_id=None):
        self.app_id = app_id            # type: str
        self.board_id = board_id        # type: str

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.board_id, 'board_id')

    def to_map(self):
        result = {}
        result['AppId'] = self.app_id
        result['BoardId'] = self.board_id
        return result

    def from_map(self, map={}):
        self.app_id = map.get('AppId')
        self.board_id = map.get('BoardId')
        return self


class DeleteBoardResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class CreateBoardRequest(TeaModel):
    def __init__(self, app_id=None, app_uid=None):
        self.app_id = app_id            # type: str
        self.app_uid = app_uid          # type: str

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.app_uid, 'app_uid')

    def to_map(self):
        result = {}
        result['AppId'] = self.app_id
        result['AppUid'] = self.app_uid
        return result

    def from_map(self, map={}):
        self.app_id = map.get('AppId')
        self.app_uid = map.get('AppUid')
        return self


class CreateBoardResponse(TeaModel):
    def __init__(self, request_id=None, board_id=None):
        self.request_id = request_id    # type: str
        self.board_id = board_id        # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.board_id, 'board_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['BoardId'] = self.board_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.board_id = map.get('BoardId')
        return self


class CompleteBoardRequest(TeaModel):
    def __init__(self, app_id=None, board_id=None):
        self.app_id = app_id            # type: str
        self.board_id = board_id        # type: str

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.board_id, 'board_id')

    def to_map(self):
        result = {}
        result['AppId'] = self.app_id
        result['BoardId'] = self.board_id
        return result

    def from_map(self, map={}):
        self.app_id = map.get('AppId')
        self.board_id = map.get('BoardId')
        return self


class CompleteBoardResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ApplyBoardTokenRequest(TeaModel):
    def __init__(self, app_id=None, app_uid=None, board_id=None):
        self.app_id = app_id            # type: str
        self.app_uid = app_uid          # type: str
        self.board_id = board_id        # type: str

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.app_uid, 'app_uid')
        self.validate_required(self.board_id, 'board_id')

    def to_map(self):
        result = {}
        result['AppId'] = self.app_id
        result['AppUid'] = self.app_uid
        result['BoardId'] = self.board_id
        return result

    def from_map(self, map={}):
        self.app_id = map.get('AppId')
        self.app_uid = map.get('AppUid')
        self.board_id = map.get('BoardId')
        return self


class ApplyBoardTokenResponse(TeaModel):
    def __init__(self, request_id=None, token=None, expired=None):
        self.request_id = request_id    # type: str
        self.token = token              # type: str
        self.expired = expired          # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.token, 'token')
        self.validate_required(self.expired, 'expired')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Token'] = self.token
        result['Expired'] = self.expired
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.token = map.get('Token')
        self.expired = map.get('Expired')
        return self


class DescribeLiveStreamCountRequest(TeaModel):
    def __init__(self, domain_name=None):
        self.domain_name = domain_name  # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        return self


class DescribeLiveStreamCountResponse(TeaModel):
    def __init__(self, request_id=None, stream_count_infos=None):
        self.request_id = request_id    # type: str
        self.stream_count_infos = stream_count_infos  # type: DescribeLiveStreamCountResponseStreamCountInfos

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.stream_count_infos, 'stream_count_infos')
        if self.stream_count_infos:
            self.stream_count_infos.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.stream_count_infos is not None:
            result['StreamCountInfos'] = self.stream_count_infos.to_map()
        else:
            result['StreamCountInfos'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('StreamCountInfos') is not None:
            temp_model = DescribeLiveStreamCountResponseStreamCountInfos()
            self.stream_count_infos = temp_model.from_map(map['StreamCountInfos'])
        else:
            self.stream_count_infos = None
        return self


class DescribeLiveStreamCountResponseStreamCountInfosStreamCountInfoStreamCountDetailsStreamCountDetail(TeaModel):
    def __init__(self, format=None, video_data_rate=None, count=None):
        self.format = format            # type: str
        self.video_data_rate = video_data_rate  # type: int
        self.count = count              # type: int

    def validate(self):
        self.validate_required(self.format, 'format')
        self.validate_required(self.video_data_rate, 'video_data_rate')
        self.validate_required(self.count, 'count')

    def to_map(self):
        result = {}
        result['Format'] = self.format
        result['VideoDataRate'] = self.video_data_rate
        result['Count'] = self.count
        return result

    def from_map(self, map={}):
        self.format = map.get('Format')
        self.video_data_rate = map.get('VideoDataRate')
        self.count = map.get('Count')
        return self


class DescribeLiveStreamCountResponseStreamCountInfosStreamCountInfoStreamCountDetails(TeaModel):
    def __init__(self, stream_count_detail=None):
        self.stream_count_detail = stream_count_detail  # type: List[DescribeLiveStreamCountResponseStreamCountInfosStreamCountInfoStreamCountDetailsStreamCountDetail]

    def validate(self):
        self.validate_required(self.stream_count_detail, 'stream_count_detail')
        if self.stream_count_detail:
            for k in self.stream_count_detail:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['StreamCountDetail'] = []
        if self.stream_count_detail is not None:
            for k in self.stream_count_detail:
                result['StreamCountDetail'].append(k.to_map() if k else None)
        else:
            result['StreamCountDetail'] = None
        return result

    def from_map(self, map={}):
        self.stream_count_detail = []
        if map.get('StreamCountDetail') is not None:
            for k in map.get('StreamCountDetail'):
                temp_model = DescribeLiveStreamCountResponseStreamCountInfosStreamCountInfoStreamCountDetailsStreamCountDetail()
                self.stream_count_detail.append(temp_model.from_map(k))
        else:
            self.stream_count_detail = None
        return self


class DescribeLiveStreamCountResponseStreamCountInfosStreamCountInfo(TeaModel):
    def __init__(self, count=None, limit=None, type=None, stream_count_details=None):
        self.count = count              # type: int
        self.limit = limit              # type: int
        self.type = type                # type: str
        self.stream_count_details = stream_count_details  # type: DescribeLiveStreamCountResponseStreamCountInfosStreamCountInfoStreamCountDetails

    def validate(self):
        self.validate_required(self.count, 'count')
        self.validate_required(self.limit, 'limit')
        self.validate_required(self.type, 'type')
        self.validate_required(self.stream_count_details, 'stream_count_details')
        if self.stream_count_details:
            self.stream_count_details.validate()

    def to_map(self):
        result = {}
        result['Count'] = self.count
        result['Limit'] = self.limit
        result['Type'] = self.type
        if self.stream_count_details is not None:
            result['StreamCountDetails'] = self.stream_count_details.to_map()
        else:
            result['StreamCountDetails'] = None
        return result

    def from_map(self, map={}):
        self.count = map.get('Count')
        self.limit = map.get('Limit')
        self.type = map.get('Type')
        if map.get('StreamCountDetails') is not None:
            temp_model = DescribeLiveStreamCountResponseStreamCountInfosStreamCountInfoStreamCountDetails()
            self.stream_count_details = temp_model.from_map(map['StreamCountDetails'])
        else:
            self.stream_count_details = None
        return self


class DescribeLiveStreamCountResponseStreamCountInfos(TeaModel):
    def __init__(self, stream_count_info=None):
        self.stream_count_info = stream_count_info  # type: List[DescribeLiveStreamCountResponseStreamCountInfosStreamCountInfo]

    def validate(self):
        self.validate_required(self.stream_count_info, 'stream_count_info')
        if self.stream_count_info:
            for k in self.stream_count_info:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['StreamCountInfo'] = []
        if self.stream_count_info is not None:
            for k in self.stream_count_info:
                result['StreamCountInfo'].append(k.to_map() if k else None)
        else:
            result['StreamCountInfo'] = None
        return result

    def from_map(self, map={}):
        self.stream_count_info = []
        if map.get('StreamCountInfo') is not None:
            for k in map.get('StreamCountInfo'):
                temp_model = DescribeLiveStreamCountResponseStreamCountInfosStreamCountInfo()
                self.stream_count_info.append(temp_model.from_map(k))
        else:
            self.stream_count_info = None
        return self


class DescribeLiveCertificateDetailRequest(TeaModel):
    def __init__(self, security_token=None, cert_name=None):
        self.security_token = security_token  # type: str
        self.cert_name = cert_name      # type: str

    def validate(self):
        self.validate_required(self.cert_name, 'cert_name')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['CertName'] = self.cert_name
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.cert_name = map.get('CertName')
        return self


class DescribeLiveCertificateDetailResponse(TeaModel):
    def __init__(self, request_id=None, cert=None, key=None, cert_id=None, cert_name=None):
        self.request_id = request_id    # type: str
        self.cert = cert                # type: str
        self.key = key                  # type: str
        self.cert_id = cert_id          # type: int
        self.cert_name = cert_name      # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.cert, 'cert')
        self.validate_required(self.key, 'key')
        self.validate_required(self.cert_id, 'cert_id')
        self.validate_required(self.cert_name, 'cert_name')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Cert'] = self.cert
        result['Key'] = self.key
        result['CertId'] = self.cert_id
        result['CertName'] = self.cert_name
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.cert = map.get('Cert')
        self.key = map.get('Key')
        self.cert_id = map.get('CertId')
        self.cert_name = map.get('CertName')
        return self


class DescribeHlsLiveStreamRealTimeBpsDataRequest(TeaModel):
    def __init__(self, domain_name=None, time=None):
        self.domain_name = domain_name  # type: str
        self.time = time                # type: str

    def validate(self):
        self.validate_required(self.time, 'time')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['Time'] = self.time
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.time = map.get('Time')
        return self


class DescribeHlsLiveStreamRealTimeBpsDataResponse(TeaModel):
    def __init__(self, time=None, request_id=None, usage_data=None):
        self.time = time                # type: str
        self.request_id = request_id    # type: str
        self.usage_data = usage_data    # type: List[DescribeHlsLiveStreamRealTimeBpsDataResponseUsageData]

    def validate(self):
        self.validate_required(self.time, 'time')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.usage_data, 'usage_data')
        if self.usage_data:
            for k in self.usage_data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Time'] = self.time
        result['RequestId'] = self.request_id
        result['UsageData'] = []
        if self.usage_data is not None:
            for k in self.usage_data:
                result['UsageData'].append(k.to_map() if k else None)
        else:
            result['UsageData'] = None
        return result

    def from_map(self, map={}):
        self.time = map.get('Time')
        self.request_id = map.get('RequestId')
        self.usage_data = []
        if map.get('UsageData') is not None:
            for k in map.get('UsageData'):
                temp_model = DescribeHlsLiveStreamRealTimeBpsDataResponseUsageData()
                self.usage_data.append(temp_model.from_map(k))
        else:
            self.usage_data = None
        return self


class DescribeHlsLiveStreamRealTimeBpsDataResponseUsageDataStreamInfosInfos(TeaModel):
    def __init__(self, down_flow=None, rate=None, online=None):
        self.down_flow = down_flow      # type: float
        self.rate = rate                # type: str
        self.online = online            # type: float

    def validate(self):
        self.validate_required(self.down_flow, 'down_flow')
        self.validate_required(self.rate, 'rate')
        self.validate_required(self.online, 'online')

    def to_map(self):
        result = {}
        result['DownFlow'] = self.down_flow
        result['Rate'] = self.rate
        result['Online'] = self.online
        return result

    def from_map(self, map={}):
        self.down_flow = map.get('DownFlow')
        self.rate = map.get('Rate')
        self.online = map.get('Online')
        return self


class DescribeHlsLiveStreamRealTimeBpsDataResponseUsageDataStreamInfos(TeaModel):
    def __init__(self, stream_name=None, infos=None):
        self.stream_name = stream_name  # type: str
        self.infos = infos              # type: List[DescribeHlsLiveStreamRealTimeBpsDataResponseUsageDataStreamInfosInfos]

    def validate(self):
        self.validate_required(self.stream_name, 'stream_name')
        self.validate_required(self.infos, 'infos')
        if self.infos:
            for k in self.infos:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['StreamName'] = self.stream_name
        result['Infos'] = []
        if self.infos is not None:
            for k in self.infos:
                result['Infos'].append(k.to_map() if k else None)
        else:
            result['Infos'] = None
        return result

    def from_map(self, map={}):
        self.stream_name = map.get('StreamName')
        self.infos = []
        if map.get('Infos') is not None:
            for k in map.get('Infos'):
                temp_model = DescribeHlsLiveStreamRealTimeBpsDataResponseUsageDataStreamInfosInfos()
                self.infos.append(temp_model.from_map(k))
        else:
            self.infos = None
        return self


class DescribeHlsLiveStreamRealTimeBpsDataResponseUsageData(TeaModel):
    def __init__(self, domain_name=None, stream_infos=None):
        self.domain_name = domain_name  # type: str
        self.stream_infos = stream_infos  # type: List[DescribeHlsLiveStreamRealTimeBpsDataResponseUsageDataStreamInfos]

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.stream_infos, 'stream_infos')
        if self.stream_infos:
            for k in self.stream_infos:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['StreamInfos'] = []
        if self.stream_infos is not None:
            for k in self.stream_infos:
                result['StreamInfos'].append(k.to_map() if k else None)
        else:
            result['StreamInfos'] = None
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.stream_infos = []
        if map.get('StreamInfos') is not None:
            for k in map.get('StreamInfos'):
                temp_model = DescribeHlsLiveStreamRealTimeBpsDataResponseUsageDataStreamInfos()
                self.stream_infos.append(temp_model.from_map(k))
        else:
            self.stream_infos = None
        return self


class StopLiveDomainRequest(TeaModel):
    def __init__(self, security_token=None, domain_name=None):
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['DomainName'] = self.domain_name
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.domain_name = map.get('DomainName')
        return self


class StopLiveDomainResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class StartLiveDomainRequest(TeaModel):
    def __init__(self, security_token=None, domain_name=None):
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['DomainName'] = self.domain_name
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.domain_name = map.get('DomainName')
        return self


class StartLiveDomainResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class SetLiveDomainCertificateRequest(TeaModel):
    def __init__(self, security_token=None, domain_name=None, cert_name=None, cert_type=None, sslprotocol=None,
                 sslpub=None, sslpri=None, force_set=None):
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str
        self.cert_name = cert_name      # type: str
        self.cert_type = cert_type      # type: str
        self.sslprotocol = sslprotocol  # type: str
        self.sslpub = sslpub            # type: str
        self.sslpri = sslpri            # type: str
        self.force_set = force_set      # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.sslprotocol, 'sslprotocol')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['DomainName'] = self.domain_name
        result['CertName'] = self.cert_name
        result['CertType'] = self.cert_type
        result['SSLProtocol'] = self.sslprotocol
        result['SSLPub'] = self.sslpub
        result['SSLPri'] = self.sslpri
        result['ForceSet'] = self.force_set
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.domain_name = map.get('DomainName')
        self.cert_name = map.get('CertName')
        self.cert_type = map.get('CertType')
        self.sslprotocol = map.get('SSLProtocol')
        self.sslpub = map.get('SSLPub')
        self.sslpri = map.get('SSLPri')
        self.force_set = map.get('ForceSet')
        return self


class SetLiveDomainCertificateResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class BatchSetLiveDomainConfigsRequest(TeaModel):
    def __init__(self, security_token=None, domain_names=None, functions=None):
        self.security_token = security_token  # type: str
        self.domain_names = domain_names  # type: str
        self.functions = functions      # type: str

    def validate(self):
        self.validate_required(self.domain_names, 'domain_names')
        self.validate_required(self.functions, 'functions')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['DomainNames'] = self.domain_names
        result['Functions'] = self.functions
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.domain_names = map.get('DomainNames')
        self.functions = map.get('Functions')
        return self


class BatchSetLiveDomainConfigsResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeLiveCertificateListRequest(TeaModel):
    def __init__(self, security_token=None, domain_name=None):
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['DomainName'] = self.domain_name
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.domain_name = map.get('DomainName')
        return self


class DescribeLiveCertificateListResponse(TeaModel):
    def __init__(self, request_id=None, certificate_list_model=None):
        self.request_id = request_id    # type: str
        self.certificate_list_model = certificate_list_model  # type: DescribeLiveCertificateListResponseCertificateListModel

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.certificate_list_model, 'certificate_list_model')
        if self.certificate_list_model:
            self.certificate_list_model.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.certificate_list_model is not None:
            result['CertificateListModel'] = self.certificate_list_model.to_map()
        else:
            result['CertificateListModel'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('CertificateListModel') is not None:
            temp_model = DescribeLiveCertificateListResponseCertificateListModel()
            self.certificate_list_model = temp_model.from_map(map['CertificateListModel'])
        else:
            self.certificate_list_model = None
        return self


class DescribeLiveCertificateListResponseCertificateListModelCertListCert(TeaModel):
    def __init__(self, cert_name=None, cert_id=None, fingerprint=None, common=None, issuer=None, last_time=None):
        self.cert_name = cert_name      # type: str
        self.cert_id = cert_id          # type: int
        self.fingerprint = fingerprint  # type: str
        self.common = common            # type: str
        self.issuer = issuer            # type: str
        self.last_time = last_time      # type: int

    def validate(self):
        self.validate_required(self.cert_name, 'cert_name')
        self.validate_required(self.cert_id, 'cert_id')
        self.validate_required(self.fingerprint, 'fingerprint')
        self.validate_required(self.common, 'common')
        self.validate_required(self.issuer, 'issuer')
        self.validate_required(self.last_time, 'last_time')

    def to_map(self):
        result = {}
        result['CertName'] = self.cert_name
        result['CertId'] = self.cert_id
        result['Fingerprint'] = self.fingerprint
        result['Common'] = self.common
        result['Issuer'] = self.issuer
        result['LastTime'] = self.last_time
        return result

    def from_map(self, map={}):
        self.cert_name = map.get('CertName')
        self.cert_id = map.get('CertId')
        self.fingerprint = map.get('Fingerprint')
        self.common = map.get('Common')
        self.issuer = map.get('Issuer')
        self.last_time = map.get('LastTime')
        return self


class DescribeLiveCertificateListResponseCertificateListModelCertList(TeaModel):
    def __init__(self, cert=None):
        self.cert = cert                # type: List[DescribeLiveCertificateListResponseCertificateListModelCertListCert]

    def validate(self):
        self.validate_required(self.cert, 'cert')
        if self.cert:
            for k in self.cert:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Cert'] = []
        if self.cert is not None:
            for k in self.cert:
                result['Cert'].append(k.to_map() if k else None)
        else:
            result['Cert'] = None
        return result

    def from_map(self, map={}):
        self.cert = []
        if map.get('Cert') is not None:
            for k in map.get('Cert'):
                temp_model = DescribeLiveCertificateListResponseCertificateListModelCertListCert()
                self.cert.append(temp_model.from_map(k))
        else:
            self.cert = None
        return self


class DescribeLiveCertificateListResponseCertificateListModel(TeaModel):
    def __init__(self, count=None, cert_list=None):
        self.count = count              # type: int
        self.cert_list = cert_list      # type: DescribeLiveCertificateListResponseCertificateListModelCertList

    def validate(self):
        self.validate_required(self.count, 'count')
        self.validate_required(self.cert_list, 'cert_list')
        if self.cert_list:
            self.cert_list.validate()

    def to_map(self):
        result = {}
        result['Count'] = self.count
        if self.cert_list is not None:
            result['CertList'] = self.cert_list.to_map()
        else:
            result['CertList'] = None
        return result

    def from_map(self, map={}):
        self.count = map.get('Count')
        if map.get('CertList') is not None:
            temp_model = DescribeLiveCertificateListResponseCertificateListModelCertList()
            self.cert_list = temp_model.from_map(map['CertList'])
        else:
            self.cert_list = None
        return self


class DeleteLiveDomainRequest(TeaModel):
    def __init__(self, security_token=None, domain_name=None):
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['DomainName'] = self.domain_name
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.domain_name = map.get('DomainName')
        return self


class DeleteLiveDomainResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeLiveDomainConfigsRequest(TeaModel):
    def __init__(self, security_token=None, domain_name=None, function_names=None):
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str
        self.function_names = function_names  # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.function_names, 'function_names')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['DomainName'] = self.domain_name
        result['FunctionNames'] = self.function_names
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.domain_name = map.get('DomainName')
        self.function_names = map.get('FunctionNames')
        return self


class DescribeLiveDomainConfigsResponse(TeaModel):
    def __init__(self, request_id=None, domain_configs=None):
        self.request_id = request_id    # type: str
        self.domain_configs = domain_configs  # type: DescribeLiveDomainConfigsResponseDomainConfigs

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.domain_configs, 'domain_configs')
        if self.domain_configs:
            self.domain_configs.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.domain_configs is not None:
            result['DomainConfigs'] = self.domain_configs.to_map()
        else:
            result['DomainConfigs'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('DomainConfigs') is not None:
            temp_model = DescribeLiveDomainConfigsResponseDomainConfigs()
            self.domain_configs = temp_model.from_map(map['DomainConfigs'])
        else:
            self.domain_configs = None
        return self


class DescribeLiveDomainConfigsResponseDomainConfigsDomainConfigFunctionArgsFunctionArg(TeaModel):
    def __init__(self, arg_name=None, arg_value=None):
        self.arg_name = arg_name        # type: str
        self.arg_value = arg_value      # type: str

    def validate(self):
        self.validate_required(self.arg_name, 'arg_name')
        self.validate_required(self.arg_value, 'arg_value')

    def to_map(self):
        result = {}
        result['ArgName'] = self.arg_name
        result['ArgValue'] = self.arg_value
        return result

    def from_map(self, map={}):
        self.arg_name = map.get('ArgName')
        self.arg_value = map.get('ArgValue')
        return self


class DescribeLiveDomainConfigsResponseDomainConfigsDomainConfigFunctionArgs(TeaModel):
    def __init__(self, function_arg=None):
        self.function_arg = function_arg  # type: List[DescribeLiveDomainConfigsResponseDomainConfigsDomainConfigFunctionArgsFunctionArg]

    def validate(self):
        self.validate_required(self.function_arg, 'function_arg')
        if self.function_arg:
            for k in self.function_arg:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['FunctionArg'] = []
        if self.function_arg is not None:
            for k in self.function_arg:
                result['FunctionArg'].append(k.to_map() if k else None)
        else:
            result['FunctionArg'] = None
        return result

    def from_map(self, map={}):
        self.function_arg = []
        if map.get('FunctionArg') is not None:
            for k in map.get('FunctionArg'):
                temp_model = DescribeLiveDomainConfigsResponseDomainConfigsDomainConfigFunctionArgsFunctionArg()
                self.function_arg.append(temp_model.from_map(k))
        else:
            self.function_arg = None
        return self


class DescribeLiveDomainConfigsResponseDomainConfigsDomainConfig(TeaModel):
    def __init__(self, function_name=None, config_id=None, status=None, function_args=None):
        self.function_name = function_name  # type: str
        self.config_id = config_id      # type: str
        self.status = status            # type: str
        self.function_args = function_args  # type: DescribeLiveDomainConfigsResponseDomainConfigsDomainConfigFunctionArgs

    def validate(self):
        self.validate_required(self.function_name, 'function_name')
        self.validate_required(self.config_id, 'config_id')
        self.validate_required(self.status, 'status')
        self.validate_required(self.function_args, 'function_args')
        if self.function_args:
            self.function_args.validate()

    def to_map(self):
        result = {}
        result['FunctionName'] = self.function_name
        result['ConfigId'] = self.config_id
        result['Status'] = self.status
        if self.function_args is not None:
            result['FunctionArgs'] = self.function_args.to_map()
        else:
            result['FunctionArgs'] = None
        return result

    def from_map(self, map={}):
        self.function_name = map.get('FunctionName')
        self.config_id = map.get('ConfigId')
        self.status = map.get('Status')
        if map.get('FunctionArgs') is not None:
            temp_model = DescribeLiveDomainConfigsResponseDomainConfigsDomainConfigFunctionArgs()
            self.function_args = temp_model.from_map(map['FunctionArgs'])
        else:
            self.function_args = None
        return self


class DescribeLiveDomainConfigsResponseDomainConfigs(TeaModel):
    def __init__(self, domain_config=None):
        self.domain_config = domain_config  # type: List[DescribeLiveDomainConfigsResponseDomainConfigsDomainConfig]

    def validate(self):
        self.validate_required(self.domain_config, 'domain_config')
        if self.domain_config:
            for k in self.domain_config:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['DomainConfig'] = []
        if self.domain_config is not None:
            for k in self.domain_config:
                result['DomainConfig'].append(k.to_map() if k else None)
        else:
            result['DomainConfig'] = None
        return result

    def from_map(self, map={}):
        self.domain_config = []
        if map.get('DomainConfig') is not None:
            for k in map.get('DomainConfig'):
                temp_model = DescribeLiveDomainConfigsResponseDomainConfigsDomainConfig()
                self.domain_config.append(temp_model.from_map(k))
        else:
            self.domain_config = None
        return self


class AddLiveDomainRequest(TeaModel):
    def __init__(self, security_token=None, live_domain_type=None, domain_name=None, region=None, check_url=None,
                 scope=None, top_level_domain=None):
        self.security_token = security_token  # type: str
        self.live_domain_type = live_domain_type  # type: str
        self.domain_name = domain_name  # type: str
        self.region = region            # type: str
        self.check_url = check_url      # type: str
        self.scope = scope              # type: str
        self.top_level_domain = top_level_domain  # type: str

    def validate(self):
        self.validate_required(self.live_domain_type, 'live_domain_type')
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.region, 'region')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['LiveDomainType'] = self.live_domain_type
        result['DomainName'] = self.domain_name
        result['Region'] = self.region
        result['CheckUrl'] = self.check_url
        result['Scope'] = self.scope
        result['TopLevelDomain'] = self.top_level_domain
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.live_domain_type = map.get('LiveDomainType')
        self.domain_name = map.get('DomainName')
        self.region = map.get('Region')
        self.check_url = map.get('CheckUrl')
        self.scope = map.get('Scope')
        self.top_level_domain = map.get('TopLevelDomain')
        return self


class AddLiveDomainResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeLiveDomainDetailRequest(TeaModel):
    def __init__(self, security_token=None, domain_name=None):
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['DomainName'] = self.domain_name
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.domain_name = map.get('DomainName')
        return self


class DescribeLiveDomainDetailResponse(TeaModel):
    def __init__(self, request_id=None, domain_detail=None):
        self.request_id = request_id    # type: str
        self.domain_detail = domain_detail  # type: DescribeLiveDomainDetailResponseDomainDetail

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.domain_detail, 'domain_detail')
        if self.domain_detail:
            self.domain_detail.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.domain_detail is not None:
            result['DomainDetail'] = self.domain_detail.to_map()
        else:
            result['DomainDetail'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('DomainDetail') is not None:
            temp_model = DescribeLiveDomainDetailResponseDomainDetail()
            self.domain_detail = temp_model.from_map(map['DomainDetail'])
        else:
            self.domain_detail = None
        return self


class DescribeLiveDomainDetailResponseDomainDetail(TeaModel):
    def __init__(self, gmt_created=None, gmt_modified=None, domain_status=None, cname=None, domain_name=None,
                 live_domain_type=None, region=None, description=None, sslprotocol=None, sslpub=None, scope=None, cert_name=None):
        self.gmt_created = gmt_created  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.domain_status = domain_status  # type: str
        self.cname = cname              # type: str
        self.domain_name = domain_name  # type: str
        self.live_domain_type = live_domain_type  # type: str
        self.region = region            # type: str
        self.description = description  # type: str
        self.sslprotocol = sslprotocol  # type: str
        self.sslpub = sslpub            # type: str
        self.scope = scope              # type: str
        self.cert_name = cert_name      # type: str

    def validate(self):
        self.validate_required(self.gmt_created, 'gmt_created')
        self.validate_required(self.gmt_modified, 'gmt_modified')
        self.validate_required(self.domain_status, 'domain_status')
        self.validate_required(self.cname, 'cname')
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.live_domain_type, 'live_domain_type')
        self.validate_required(self.region, 'region')
        self.validate_required(self.description, 'description')
        self.validate_required(self.sslprotocol, 'sslprotocol')
        self.validate_required(self.sslpub, 'sslpub')
        self.validate_required(self.scope, 'scope')
        self.validate_required(self.cert_name, 'cert_name')

    def to_map(self):
        result = {}
        result['GmtCreated'] = self.gmt_created
        result['GmtModified'] = self.gmt_modified
        result['DomainStatus'] = self.domain_status
        result['Cname'] = self.cname
        result['DomainName'] = self.domain_name
        result['LiveDomainType'] = self.live_domain_type
        result['Region'] = self.region
        result['Description'] = self.description
        result['SSLProtocol'] = self.sslprotocol
        result['SSLPub'] = self.sslpub
        result['Scope'] = self.scope
        result['CertName'] = self.cert_name
        return result

    def from_map(self, map={}):
        self.gmt_created = map.get('GmtCreated')
        self.gmt_modified = map.get('GmtModified')
        self.domain_status = map.get('DomainStatus')
        self.cname = map.get('Cname')
        self.domain_name = map.get('DomainName')
        self.live_domain_type = map.get('LiveDomainType')
        self.region = map.get('Region')
        self.description = map.get('Description')
        self.sslprotocol = map.get('SSLProtocol')
        self.sslpub = map.get('SSLPub')
        self.scope = map.get('Scope')
        self.cert_name = map.get('CertName')
        return self


class BatchDeleteLiveDomainConfigsRequest(TeaModel):
    def __init__(self, security_token=None, domain_names=None, function_names=None):
        self.security_token = security_token  # type: str
        self.domain_names = domain_names  # type: str
        self.function_names = function_names  # type: str

    def validate(self):
        self.validate_required(self.domain_names, 'domain_names')
        self.validate_required(self.function_names, 'function_names')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['DomainNames'] = self.domain_names
        result['FunctionNames'] = self.function_names
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.domain_names = map.get('DomainNames')
        self.function_names = map.get('FunctionNames')
        return self


class BatchDeleteLiveDomainConfigsResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeRoomStatusRequest(TeaModel):
    def __init__(self, app_id=None, room_id=None):
        self.app_id = app_id            # type: str
        self.room_id = room_id          # type: str

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.room_id, 'room_id')

    def to_map(self):
        result = {}
        result['AppId'] = self.app_id
        result['RoomId'] = self.room_id
        return result

    def from_map(self, map={}):
        self.app_id = map.get('AppId')
        self.room_id = map.get('RoomId')
        return self


class DescribeRoomStatusResponse(TeaModel):
    def __init__(self, request_id=None, room_status=None):
        self.request_id = request_id    # type: str
        self.room_status = room_status  # type: int

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.room_status, 'room_status')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['RoomStatus'] = self.room_status
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.room_status = map.get('RoomStatus')
        return self


class DescribeRoomListRequest(TeaModel):
    def __init__(self, app_id=None, room_id=None, anchor_id=None, room_status=None, start_time=None, end_time=None,
                 order=None, page_num=None, page_size=None):
        self.app_id = app_id            # type: str
        self.room_id = room_id          # type: str
        self.anchor_id = anchor_id      # type: str
        self.room_status = room_status  # type: int
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.order = order              # type: str
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int

    def validate(self):
        self.validate_required(self.app_id, 'app_id')

    def to_map(self):
        result = {}
        result['AppId'] = self.app_id
        result['RoomId'] = self.room_id
        result['AnchorId'] = self.anchor_id
        result['RoomStatus'] = self.room_status
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['Order'] = self.order
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.app_id = map.get('AppId')
        self.room_id = map.get('RoomId')
        self.anchor_id = map.get('AnchorId')
        self.room_status = map.get('RoomStatus')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.order = map.get('Order')
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        return self


class DescribeRoomListResponse(TeaModel):
    def __init__(self, request_id=None, total_num=None, total_page=None, room_list=None):
        self.request_id = request_id    # type: str
        self.total_num = total_num      # type: int
        self.total_page = total_page    # type: int
        self.room_list = room_list      # type: List[DescribeRoomListResponseRoomList]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_num, 'total_num')
        self.validate_required(self.total_page, 'total_page')
        self.validate_required(self.room_list, 'room_list')
        if self.room_list:
            for k in self.room_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalNum'] = self.total_num
        result['TotalPage'] = self.total_page
        result['RoomList'] = []
        if self.room_list is not None:
            for k in self.room_list:
                result['RoomList'].append(k.to_map() if k else None)
        else:
            result['RoomList'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_num = map.get('TotalNum')
        self.total_page = map.get('TotalPage')
        self.room_list = []
        if map.get('RoomList') is not None:
            for k in map.get('RoomList'):
                temp_model = DescribeRoomListResponseRoomList()
                self.room_list.append(temp_model.from_map(k))
        else:
            self.room_list = None
        return self


class DescribeRoomListResponseRoomList(TeaModel):
    def __init__(self, room_id=None, anchor_id=None, room_status=None, forbid_stream=None, create_time=None):
        self.room_id = room_id          # type: str
        self.anchor_id = anchor_id      # type: str
        self.room_status = room_status  # type: int
        self.forbid_stream = forbid_stream  # type: str
        self.create_time = create_time  # type: str

    def validate(self):
        self.validate_required(self.room_id, 'room_id')
        self.validate_required(self.anchor_id, 'anchor_id')
        self.validate_required(self.room_status, 'room_status')
        self.validate_required(self.forbid_stream, 'forbid_stream')
        self.validate_required(self.create_time, 'create_time')

    def to_map(self):
        result = {}
        result['RoomId'] = self.room_id
        result['AnchorId'] = self.anchor_id
        result['RoomStatus'] = self.room_status
        result['ForbidStream'] = self.forbid_stream
        result['CreateTime'] = self.create_time
        return result

    def from_map(self, map={}):
        self.room_id = map.get('RoomId')
        self.anchor_id = map.get('AnchorId')
        self.room_status = map.get('RoomStatus')
        self.forbid_stream = map.get('ForbidStream')
        self.create_time = map.get('CreateTime')
        return self


class DescribeRoomKickoutUserListRequest(TeaModel):
    def __init__(self, app_id=None, room_id=None, order=None, page_num=None, page_size=None):
        self.app_id = app_id            # type: str
        self.room_id = room_id          # type: str
        self.order = order              # type: str
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.room_id, 'room_id')

    def to_map(self):
        result = {}
        result['AppId'] = self.app_id
        result['RoomId'] = self.room_id
        result['Order'] = self.order
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.app_id = map.get('AppId')
        self.room_id = map.get('RoomId')
        self.order = map.get('Order')
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        return self


class DescribeRoomKickoutUserListResponse(TeaModel):
    def __init__(self, request_id=None, total_num=None, total_page=None, user_list=None):
        self.request_id = request_id    # type: str
        self.total_num = total_num      # type: int
        self.total_page = total_page    # type: int
        self.user_list = user_list      # type: List[DescribeRoomKickoutUserListResponseUserList]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_num, 'total_num')
        self.validate_required(self.total_page, 'total_page')
        self.validate_required(self.user_list, 'user_list')
        if self.user_list:
            for k in self.user_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalNum'] = self.total_num
        result['TotalPage'] = self.total_page
        result['UserList'] = []
        if self.user_list is not None:
            for k in self.user_list:
                result['UserList'].append(k.to_map() if k else None)
        else:
            result['UserList'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_num = map.get('TotalNum')
        self.total_page = map.get('TotalPage')
        self.user_list = []
        if map.get('UserList') is not None:
            for k in map.get('UserList'):
                temp_model = DescribeRoomKickoutUserListResponseUserList()
                self.user_list.append(temp_model.from_map(k))
        else:
            self.user_list = None
        return self


class DescribeRoomKickoutUserListResponseUserList(TeaModel):
    def __init__(self, app_uid=None, op_start_time=None, op_end_time=None):
        self.app_uid = app_uid          # type: str
        self.op_start_time = op_start_time  # type: str
        self.op_end_time = op_end_time  # type: str

    def validate(self):
        self.validate_required(self.app_uid, 'app_uid')
        self.validate_required(self.op_start_time, 'op_start_time')
        self.validate_required(self.op_end_time, 'op_end_time')

    def to_map(self):
        result = {}
        result['AppUid'] = self.app_uid
        result['OpStartTime'] = self.op_start_time
        result['OpEndTime'] = self.op_end_time
        return result

    def from_map(self, map={}):
        self.app_uid = map.get('AppUid')
        self.op_start_time = map.get('OpStartTime')
        self.op_end_time = map.get('OpEndTime')
        return self


class SendRoomUserNotificationRequest(TeaModel):
    def __init__(self, app_id=None, room_id=None, app_uid=None, to_app_uid=None, data=None, priority=None):
        self.app_id = app_id            # type: str
        self.room_id = room_id          # type: str
        self.app_uid = app_uid          # type: str
        self.to_app_uid = to_app_uid    # type: str
        self.data = data                # type: str
        self.priority = priority        # type: int

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.room_id, 'room_id')
        self.validate_required(self.app_uid, 'app_uid')
        self.validate_required(self.to_app_uid, 'to_app_uid')
        self.validate_required(self.data, 'data')

    def to_map(self):
        result = {}
        result['AppId'] = self.app_id
        result['RoomId'] = self.room_id
        result['AppUid'] = self.app_uid
        result['ToAppUid'] = self.to_app_uid
        result['Data'] = self.data
        result['Priority'] = self.priority
        return result

    def from_map(self, map={}):
        self.app_id = map.get('AppId')
        self.room_id = map.get('RoomId')
        self.app_uid = map.get('AppUid')
        self.to_app_uid = map.get('ToAppUid')
        self.data = map.get('Data')
        self.priority = map.get('Priority')
        return self


class SendRoomUserNotificationResponse(TeaModel):
    def __init__(self, request_id=None, message_id=None):
        self.request_id = request_id    # type: str
        self.message_id = message_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.message_id, 'message_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['MessageId'] = self.message_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.message_id = map.get('MessageId')
        return self


class DescribeForbidPushStreamRoomListRequest(TeaModel):
    def __init__(self, app_id=None, order=None, page_num=None, page_size=None):
        self.app_id = app_id            # type: str
        self.order = order              # type: str
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int

    def validate(self):
        self.validate_required(self.app_id, 'app_id')

    def to_map(self):
        result = {}
        result['AppId'] = self.app_id
        result['Order'] = self.order
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.app_id = map.get('AppId')
        self.order = map.get('Order')
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        return self


class DescribeForbidPushStreamRoomListResponse(TeaModel):
    def __init__(self, request_id=None, total_num=None, total_page=None, room_list=None):
        self.request_id = request_id    # type: str
        self.total_num = total_num      # type: int
        self.total_page = total_page    # type: int
        self.room_list = room_list      # type: List[DescribeForbidPushStreamRoomListResponseRoomList]

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_num, 'total_num')
        self.validate_required(self.total_page, 'total_page')
        self.validate_required(self.room_list, 'room_list')
        if self.room_list:
            for k in self.room_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalNum'] = self.total_num
        result['TotalPage'] = self.total_page
        result['RoomList'] = []
        if self.room_list is not None:
            for k in self.room_list:
                result['RoomList'].append(k.to_map() if k else None)
        else:
            result['RoomList'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_num = map.get('TotalNum')
        self.total_page = map.get('TotalPage')
        self.room_list = []
        if map.get('RoomList') is not None:
            for k in map.get('RoomList'):
                temp_model = DescribeForbidPushStreamRoomListResponseRoomList()
                self.room_list.append(temp_model.from_map(k))
        else:
            self.room_list = None
        return self


class DescribeForbidPushStreamRoomListResponseRoomList(TeaModel):
    def __init__(self, room_id=None, anchor_id=None, op_start_time=None, op_end_time=None):
        self.room_id = room_id          # type: str
        self.anchor_id = anchor_id      # type: str
        self.op_start_time = op_start_time  # type: str
        self.op_end_time = op_end_time  # type: str

    def validate(self):
        self.validate_required(self.room_id, 'room_id')
        self.validate_required(self.anchor_id, 'anchor_id')
        self.validate_required(self.op_start_time, 'op_start_time')
        self.validate_required(self.op_end_time, 'op_end_time')

    def to_map(self):
        result = {}
        result['RoomId'] = self.room_id
        result['AnchorId'] = self.anchor_id
        result['OpStartTime'] = self.op_start_time
        result['OpEndTime'] = self.op_end_time
        return result

    def from_map(self, map={}):
        self.room_id = map.get('RoomId')
        self.anchor_id = map.get('AnchorId')
        self.op_start_time = map.get('OpStartTime')
        self.op_end_time = map.get('OpEndTime')
        return self


class SendRoomNotificationRequest(TeaModel):
    def __init__(self, app_id=None, room_id=None, app_uid=None, data=None, priority=None):
        self.app_id = app_id            # type: str
        self.room_id = room_id          # type: str
        self.app_uid = app_uid          # type: str
        self.data = data                # type: str
        self.priority = priority        # type: int

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.room_id, 'room_id')
        self.validate_required(self.data, 'data')

    def to_map(self):
        result = {}
        result['AppId'] = self.app_id
        result['RoomId'] = self.room_id
        result['AppUid'] = self.app_uid
        result['Data'] = self.data
        result['Priority'] = self.priority
        return result

    def from_map(self, map={}):
        self.app_id = map.get('AppId')
        self.room_id = map.get('RoomId')
        self.app_uid = map.get('AppUid')
        self.data = map.get('Data')
        self.priority = map.get('Priority')
        return self


class SendRoomNotificationResponse(TeaModel):
    def __init__(self, request_id=None, message_id=None):
        self.request_id = request_id    # type: str
        self.message_id = message_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.message_id, 'message_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['MessageId'] = self.message_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.message_id = map.get('MessageId')
        return self


class ForbidPushStreamRequest(TeaModel):
    def __init__(self, app_id=None, room_id=None, user_data=None, end_time=None):
        self.app_id = app_id            # type: str
        self.room_id = room_id          # type: str
        self.user_data = user_data      # type: str
        self.end_time = end_time        # type: str

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.room_id, 'room_id')

    def to_map(self):
        result = {}
        result['AppId'] = self.app_id
        result['RoomId'] = self.room_id
        result['UserData'] = self.user_data
        result['EndTime'] = self.end_time
        return result

    def from_map(self, map={}):
        self.app_id = map.get('AppId')
        self.room_id = map.get('RoomId')
        self.user_data = map.get('UserData')
        self.end_time = map.get('EndTime')
        return self


class ForbidPushStreamResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DeleteRoomRequest(TeaModel):
    def __init__(self, app_id=None, room_id=None):
        self.app_id = app_id            # type: str
        self.room_id = room_id          # type: str

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.room_id, 'room_id')

    def to_map(self):
        result = {}
        result['AppId'] = self.app_id
        result['RoomId'] = self.room_id
        return result

    def from_map(self, map={}):
        self.app_id = map.get('AppId')
        self.room_id = map.get('RoomId')
        return self


class DeleteRoomResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class CreateRoomRequest(TeaModel):
    def __init__(self, app_id=None, room_id=None, anchor_id=None, template_ids=None, use_app_transcode=None):
        self.app_id = app_id            # type: str
        self.room_id = room_id          # type: str
        self.anchor_id = anchor_id      # type: str
        self.template_ids = template_ids  # type: str
        self.use_app_transcode = use_app_transcode  # type: bool

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.room_id, 'room_id')
        self.validate_required(self.anchor_id, 'anchor_id')

    def to_map(self):
        result = {}
        result['AppId'] = self.app_id
        result['RoomId'] = self.room_id
        result['AnchorId'] = self.anchor_id
        result['TemplateIds'] = self.template_ids
        result['UseAppTranscode'] = self.use_app_transcode
        return result

    def from_map(self, map={}):
        self.app_id = map.get('AppId')
        self.room_id = map.get('RoomId')
        self.anchor_id = map.get('AnchorId')
        self.template_ids = map.get('TemplateIds')
        self.use_app_transcode = map.get('UseAppTranscode')
        return self


class CreateRoomResponse(TeaModel):
    def __init__(self, request_id=None, app_id=None, room_id=None, anchor_id=None):
        self.request_id = request_id    # type: str
        self.app_id = app_id            # type: str
        self.room_id = room_id          # type: str
        self.anchor_id = anchor_id      # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.room_id, 'room_id')
        self.validate_required(self.anchor_id, 'anchor_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['AppId'] = self.app_id
        result['RoomId'] = self.room_id
        result['AnchorId'] = self.anchor_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.app_id = map.get('AppId')
        self.room_id = map.get('RoomId')
        self.anchor_id = map.get('AnchorId')
        return self


class AllowPushStreamRequest(TeaModel):
    def __init__(self, app_id=None, room_id=None):
        self.app_id = app_id            # type: str
        self.room_id = room_id          # type: str

    def validate(self):
        self.validate_required(self.app_id, 'app_id')
        self.validate_required(self.room_id, 'room_id')

    def to_map(self):
        result = {}
        result['AppId'] = self.app_id
        result['RoomId'] = self.room_id
        return result

    def from_map(self, map={}):
        self.app_id = map.get('AppId')
        self.room_id = map.get('RoomId')
        return self


class AllowPushStreamResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeLiveUserDomainsRequest(TeaModel):
    def __init__(self, security_token=None, live_domain_type=None, page_size=None, page_number=None,
                 domain_name=None, region_name=None, domain_search_type=None, domain_status=None, tag=None):
        self.security_token = security_token  # type: str
        self.live_domain_type = live_domain_type  # type: str
        self.page_size = page_size      # type: int
        self.page_number = page_number  # type: int
        self.domain_name = domain_name  # type: str
        self.region_name = region_name  # type: str
        self.domain_search_type = domain_search_type  # type: str
        self.domain_status = domain_status  # type: str
        self.tag = tag                  # type: List[DescribeLiveUserDomainsRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['LiveDomainType'] = self.live_domain_type
        result['PageSize'] = self.page_size
        result['PageNumber'] = self.page_number
        result['DomainName'] = self.domain_name
        result['RegionName'] = self.region_name
        result['DomainSearchType'] = self.domain_search_type
        result['DomainStatus'] = self.domain_status
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        else:
            result['Tag'] = None
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.live_domain_type = map.get('LiveDomainType')
        self.page_size = map.get('PageSize')
        self.page_number = map.get('PageNumber')
        self.domain_name = map.get('DomainName')
        self.region_name = map.get('RegionName')
        self.domain_search_type = map.get('DomainSearchType')
        self.domain_status = map.get('DomainStatus')
        self.tag = []
        if map.get('Tag') is not None:
            for k in map.get('Tag'):
                temp_model = DescribeLiveUserDomainsRequestTag()
                self.tag.append(temp_model.from_map(k))
        else:
            self.tag = None
        return self


class DescribeLiveUserDomainsRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key                  # type: str
        self.value = value              # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['Key'] = self.key
        result['Value'] = self.value
        return result

    def from_map(self, map={}):
        self.key = map.get('Key')
        self.value = map.get('Value')
        return self


class DescribeLiveUserDomainsResponse(TeaModel):
    def __init__(self, request_id=None, page_number=None, page_size=None, total_count=None, domains=None):
        self.request_id = request_id    # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size      # type: int
        self.total_count = total_count  # type: int
        self.domains = domains          # type: DescribeLiveUserDomainsResponseDomains

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.page_number, 'page_number')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_count, 'total_count')
        self.validate_required(self.domains, 'domains')
        if self.domains:
            self.domains.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['PageNumber'] = self.page_number
        result['PageSize'] = self.page_size
        result['TotalCount'] = self.total_count
        if self.domains is not None:
            result['Domains'] = self.domains.to_map()
        else:
            result['Domains'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.page_number = map.get('PageNumber')
        self.page_size = map.get('PageSize')
        self.total_count = map.get('TotalCount')
        if map.get('Domains') is not None:
            temp_model = DescribeLiveUserDomainsResponseDomains()
            self.domains = temp_model.from_map(map['Domains'])
        else:
            self.domains = None
        return self


class DescribeLiveUserDomainsResponseDomainsPageData(TeaModel):
    def __init__(self, domain_name=None, cname=None, live_domain_type=None, gmt_created=None, gmt_modified=None,
                 description=None, live_domain_status=None, region_name=None):
        self.domain_name = domain_name  # type: str
        self.cname = cname              # type: str
        self.live_domain_type = live_domain_type  # type: str
        self.gmt_created = gmt_created  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.description = description  # type: str
        self.live_domain_status = live_domain_status  # type: str
        self.region_name = region_name  # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.cname, 'cname')
        self.validate_required(self.live_domain_type, 'live_domain_type')
        self.validate_required(self.gmt_created, 'gmt_created')
        self.validate_required(self.gmt_modified, 'gmt_modified')
        self.validate_required(self.description, 'description')
        self.validate_required(self.live_domain_status, 'live_domain_status')
        self.validate_required(self.region_name, 'region_name')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['Cname'] = self.cname
        result['LiveDomainType'] = self.live_domain_type
        result['GmtCreated'] = self.gmt_created
        result['GmtModified'] = self.gmt_modified
        result['Description'] = self.description
        result['LiveDomainStatus'] = self.live_domain_status
        result['RegionName'] = self.region_name
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.cname = map.get('Cname')
        self.live_domain_type = map.get('LiveDomainType')
        self.gmt_created = map.get('GmtCreated')
        self.gmt_modified = map.get('GmtModified')
        self.description = map.get('Description')
        self.live_domain_status = map.get('LiveDomainStatus')
        self.region_name = map.get('RegionName')
        return self


class DescribeLiveUserDomainsResponseDomains(TeaModel):
    def __init__(self, page_data=None):
        self.page_data = page_data      # type: List[DescribeLiveUserDomainsResponseDomainsPageData]

    def validate(self):
        self.validate_required(self.page_data, 'page_data')
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['PageData'] = []
        if self.page_data is not None:
            for k in self.page_data:
                result['PageData'].append(k.to_map() if k else None)
        else:
            result['PageData'] = None
        return result

    def from_map(self, map={}):
        self.page_data = []
        if map.get('PageData') is not None:
            for k in map.get('PageData'):
                temp_model = DescribeLiveUserDomainsResponseDomainsPageData()
                self.page_data.append(temp_model.from_map(k))
        else:
            self.page_data = None
        return self


class DescribeCasterRtcInfoRequest(TeaModel):
    def __init__(self, caster_id=None):
        self.caster_id = caster_id      # type: str

    def validate(self):
        self.validate_required(self.caster_id, 'caster_id')

    def to_map(self):
        result = {}
        result['CasterId'] = self.caster_id
        return result

    def from_map(self, map={}):
        self.caster_id = map.get('CasterId')
        return self


class DescribeCasterRtcInfoResponse(TeaModel):
    def __init__(self, request_id=None, caster_id=None, auth_token=None):
        self.request_id = request_id    # type: str
        self.caster_id = caster_id      # type: str
        self.auth_token = auth_token    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.caster_id, 'caster_id')
        self.validate_required(self.auth_token, 'auth_token')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['CasterId'] = self.caster_id
        result['AuthToken'] = self.auth_token
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.caster_id = map.get('CasterId')
        self.auth_token = map.get('AuthToken')
        return self


class DescribeUpBpsPeakDataRequest(TeaModel):
    def __init__(self, start_time=None, end_time=None, domain_switch=None, domain_name=None):
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.domain_switch = domain_switch  # type: str
        self.domain_name = domain_name  # type: str

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        result = {}
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['DomainSwitch'] = self.domain_switch
        result['DomainName'] = self.domain_name
        return result

    def from_map(self, map={}):
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.domain_switch = map.get('DomainSwitch')
        self.domain_name = map.get('DomainName')
        return self


class DescribeUpBpsPeakDataResponse(TeaModel):
    def __init__(self, request_id=None, describe_up_peak_traffics=None):
        self.request_id = request_id    # type: str
        self.describe_up_peak_traffics = describe_up_peak_traffics  # type: DescribeUpBpsPeakDataResponseDescribeUpPeakTraffics

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.describe_up_peak_traffics, 'describe_up_peak_traffics')
        if self.describe_up_peak_traffics:
            self.describe_up_peak_traffics.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.describe_up_peak_traffics is not None:
            result['DescribeUpPeakTraffics'] = self.describe_up_peak_traffics.to_map()
        else:
            result['DescribeUpPeakTraffics'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('DescribeUpPeakTraffics') is not None:
            temp_model = DescribeUpBpsPeakDataResponseDescribeUpPeakTraffics()
            self.describe_up_peak_traffics = temp_model.from_map(map['DescribeUpPeakTraffics'])
        else:
            self.describe_up_peak_traffics = None
        return self


class DescribeUpBpsPeakDataResponseDescribeUpPeakTrafficsDescribeUpPeakTraffic(TeaModel):
    def __init__(self, peak_time=None, query_time=None, stat_name=None, band_width=None):
        self.peak_time = peak_time      # type: str
        self.query_time = query_time    # type: str
        self.stat_name = stat_name      # type: str
        self.band_width = band_width    # type: str

    def validate(self):
        self.validate_required(self.peak_time, 'peak_time')
        self.validate_required(self.query_time, 'query_time')
        self.validate_required(self.stat_name, 'stat_name')
        self.validate_required(self.band_width, 'band_width')

    def to_map(self):
        result = {}
        result['PeakTime'] = self.peak_time
        result['QueryTime'] = self.query_time
        result['StatName'] = self.stat_name
        result['BandWidth'] = self.band_width
        return result

    def from_map(self, map={}):
        self.peak_time = map.get('PeakTime')
        self.query_time = map.get('QueryTime')
        self.stat_name = map.get('StatName')
        self.band_width = map.get('BandWidth')
        return self


class DescribeUpBpsPeakDataResponseDescribeUpPeakTraffics(TeaModel):
    def __init__(self, describe_up_peak_traffic=None):
        self.describe_up_peak_traffic = describe_up_peak_traffic  # type: List[DescribeUpBpsPeakDataResponseDescribeUpPeakTrafficsDescribeUpPeakTraffic]

    def validate(self):
        self.validate_required(self.describe_up_peak_traffic, 'describe_up_peak_traffic')
        if self.describe_up_peak_traffic:
            for k in self.describe_up_peak_traffic:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['DescribeUpPeakTraffic'] = []
        if self.describe_up_peak_traffic is not None:
            for k in self.describe_up_peak_traffic:
                result['DescribeUpPeakTraffic'].append(k.to_map() if k else None)
        else:
            result['DescribeUpPeakTraffic'] = None
        return result

    def from_map(self, map={}):
        self.describe_up_peak_traffic = []
        if map.get('DescribeUpPeakTraffic') is not None:
            for k in map.get('DescribeUpPeakTraffic'):
                temp_model = DescribeUpBpsPeakDataResponseDescribeUpPeakTrafficsDescribeUpPeakTraffic()
                self.describe_up_peak_traffic.append(temp_model.from_map(k))
        else:
            self.describe_up_peak_traffic = None
        return self


class DescribeUpBpsPeakOfLineRequest(TeaModel):
    def __init__(self, start_time=None, end_time=None, line=None, domain_switch=None, domain_name=None):
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.line = line                # type: str
        self.domain_switch = domain_switch  # type: str
        self.domain_name = domain_name  # type: str

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.line, 'line')

    def to_map(self):
        result = {}
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['Line'] = self.line
        result['DomainSwitch'] = self.domain_switch
        result['DomainName'] = self.domain_name
        return result

    def from_map(self, map={}):
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.line = map.get('Line')
        self.domain_switch = map.get('DomainSwitch')
        self.domain_name = map.get('DomainName')
        return self


class DescribeUpBpsPeakOfLineResponse(TeaModel):
    def __init__(self, request_id=None, describe_up_bps_peak_of_lines=None):
        self.request_id = request_id    # type: str
        self.describe_up_bps_peak_of_lines = describe_up_bps_peak_of_lines  # type: DescribeUpBpsPeakOfLineResponseDescribeUpBpsPeakOfLines

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.describe_up_bps_peak_of_lines, 'describe_up_bps_peak_of_lines')
        if self.describe_up_bps_peak_of_lines:
            self.describe_up_bps_peak_of_lines.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.describe_up_bps_peak_of_lines is not None:
            result['DescribeUpBpsPeakOfLines'] = self.describe_up_bps_peak_of_lines.to_map()
        else:
            result['DescribeUpBpsPeakOfLines'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('DescribeUpBpsPeakOfLines') is not None:
            temp_model = DescribeUpBpsPeakOfLineResponseDescribeUpBpsPeakOfLines()
            self.describe_up_bps_peak_of_lines = temp_model.from_map(map['DescribeUpBpsPeakOfLines'])
        else:
            self.describe_up_bps_peak_of_lines = None
        return self


class DescribeUpBpsPeakOfLineResponseDescribeUpBpsPeakOfLinesDescribeUpBpsPeakOfLine(TeaModel):
    def __init__(self, band_width=None, peak_time=None, query_time=None, stat_name=None):
        self.band_width = band_width    # type: float
        self.peak_time = peak_time      # type: str
        self.query_time = query_time    # type: str
        self.stat_name = stat_name      # type: str

    def validate(self):
        self.validate_required(self.band_width, 'band_width')
        self.validate_required(self.peak_time, 'peak_time')
        self.validate_required(self.query_time, 'query_time')
        self.validate_required(self.stat_name, 'stat_name')

    def to_map(self):
        result = {}
        result['BandWidth'] = self.band_width
        result['PeakTime'] = self.peak_time
        result['QueryTime'] = self.query_time
        result['StatName'] = self.stat_name
        return result

    def from_map(self, map={}):
        self.band_width = map.get('BandWidth')
        self.peak_time = map.get('PeakTime')
        self.query_time = map.get('QueryTime')
        self.stat_name = map.get('StatName')
        return self


class DescribeUpBpsPeakOfLineResponseDescribeUpBpsPeakOfLines(TeaModel):
    def __init__(self, describe_up_bps_peak_of_line=None):
        self.describe_up_bps_peak_of_line = describe_up_bps_peak_of_line  # type: List[DescribeUpBpsPeakOfLineResponseDescribeUpBpsPeakOfLinesDescribeUpBpsPeakOfLine]

    def validate(self):
        self.validate_required(self.describe_up_bps_peak_of_line, 'describe_up_bps_peak_of_line')
        if self.describe_up_bps_peak_of_line:
            for k in self.describe_up_bps_peak_of_line:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['DescribeUpBpsPeakOfLine'] = []
        if self.describe_up_bps_peak_of_line is not None:
            for k in self.describe_up_bps_peak_of_line:
                result['DescribeUpBpsPeakOfLine'].append(k.to_map() if k else None)
        else:
            result['DescribeUpBpsPeakOfLine'] = None
        return result

    def from_map(self, map={}):
        self.describe_up_bps_peak_of_line = []
        if map.get('DescribeUpBpsPeakOfLine') is not None:
            for k in map.get('DescribeUpBpsPeakOfLine'):
                temp_model = DescribeUpBpsPeakOfLineResponseDescribeUpBpsPeakOfLinesDescribeUpBpsPeakOfLine()
                self.describe_up_bps_peak_of_line.append(temp_model.from_map(k))
        else:
            self.describe_up_bps_peak_of_line = None
        return self


class DescribeUpPeakPublishStreamDataRequest(TeaModel):
    def __init__(self, start_time=None, end_time=None, domain_switch=None, domain_name=None):
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.domain_switch = domain_switch  # type: str
        self.domain_name = domain_name  # type: str

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        result = {}
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['DomainSwitch'] = self.domain_switch
        result['DomainName'] = self.domain_name
        return result

    def from_map(self, map={}):
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.domain_switch = map.get('DomainSwitch')
        self.domain_name = map.get('DomainName')
        return self


class DescribeUpPeakPublishStreamDataResponse(TeaModel):
    def __init__(self, request_id=None, describe_up_peak_publish_stream_datas=None):
        self.request_id = request_id    # type: str
        self.describe_up_peak_publish_stream_datas = describe_up_peak_publish_stream_datas  # type: DescribeUpPeakPublishStreamDataResponseDescribeUpPeakPublishStreamDatas

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.describe_up_peak_publish_stream_datas, 'describe_up_peak_publish_stream_datas')
        if self.describe_up_peak_publish_stream_datas:
            self.describe_up_peak_publish_stream_datas.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.describe_up_peak_publish_stream_datas is not None:
            result['DescribeUpPeakPublishStreamDatas'] = self.describe_up_peak_publish_stream_datas.to_map()
        else:
            result['DescribeUpPeakPublishStreamDatas'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('DescribeUpPeakPublishStreamDatas') is not None:
            temp_model = DescribeUpPeakPublishStreamDataResponseDescribeUpPeakPublishStreamDatas()
            self.describe_up_peak_publish_stream_datas = temp_model.from_map(map['DescribeUpPeakPublishStreamDatas'])
        else:
            self.describe_up_peak_publish_stream_datas = None
        return self


class DescribeUpPeakPublishStreamDataResponseDescribeUpPeakPublishStreamDatasDescribeUpPeakPublishStreamData(TeaModel):
    def __init__(self, publish_stream_num=None, peak_time=None, query_time=None, stat_name=None, band_width=None):
        self.publish_stream_num = publish_stream_num  # type: int
        self.peak_time = peak_time      # type: str
        self.query_time = query_time    # type: str
        self.stat_name = stat_name      # type: str
        self.band_width = band_width    # type: str

    def validate(self):
        self.validate_required(self.publish_stream_num, 'publish_stream_num')
        self.validate_required(self.peak_time, 'peak_time')
        self.validate_required(self.query_time, 'query_time')
        self.validate_required(self.stat_name, 'stat_name')
        self.validate_required(self.band_width, 'band_width')

    def to_map(self):
        result = {}
        result['PublishStreamNum'] = self.publish_stream_num
        result['PeakTime'] = self.peak_time
        result['QueryTime'] = self.query_time
        result['StatName'] = self.stat_name
        result['BandWidth'] = self.band_width
        return result

    def from_map(self, map={}):
        self.publish_stream_num = map.get('PublishStreamNum')
        self.peak_time = map.get('PeakTime')
        self.query_time = map.get('QueryTime')
        self.stat_name = map.get('StatName')
        self.band_width = map.get('BandWidth')
        return self


class DescribeUpPeakPublishStreamDataResponseDescribeUpPeakPublishStreamDatas(TeaModel):
    def __init__(self, describe_up_peak_publish_stream_data=None):
        self.describe_up_peak_publish_stream_data = describe_up_peak_publish_stream_data  # type: List[DescribeUpPeakPublishStreamDataResponseDescribeUpPeakPublishStreamDatasDescribeUpPeakPublishStreamData]

    def validate(self):
        self.validate_required(self.describe_up_peak_publish_stream_data, 'describe_up_peak_publish_stream_data')
        if self.describe_up_peak_publish_stream_data:
            for k in self.describe_up_peak_publish_stream_data:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['DescribeUpPeakPublishStreamData'] = []
        if self.describe_up_peak_publish_stream_data is not None:
            for k in self.describe_up_peak_publish_stream_data:
                result['DescribeUpPeakPublishStreamData'].append(k.to_map() if k else None)
        else:
            result['DescribeUpPeakPublishStreamData'] = None
        return result

    def from_map(self, map={}):
        self.describe_up_peak_publish_stream_data = []
        if map.get('DescribeUpPeakPublishStreamData') is not None:
            for k in map.get('DescribeUpPeakPublishStreamData'):
                temp_model = DescribeUpPeakPublishStreamDataResponseDescribeUpPeakPublishStreamDatasDescribeUpPeakPublishStreamData()
                self.describe_up_peak_publish_stream_data.append(temp_model.from_map(k))
        else:
            self.describe_up_peak_publish_stream_data = None
        return self


class DeleteLiveDomainMappingRequest(TeaModel):
    def __init__(self, security_token=None, push_domain=None, pull_domain=None):
        self.security_token = security_token  # type: str
        self.push_domain = push_domain  # type: str
        self.pull_domain = pull_domain  # type: str

    def validate(self):
        self.validate_required(self.push_domain, 'push_domain')
        self.validate_required(self.pull_domain, 'pull_domain')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['PushDomain'] = self.push_domain
        result['PullDomain'] = self.pull_domain
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.push_domain = map.get('PushDomain')
        self.pull_domain = map.get('PullDomain')
        return self


class DeleteLiveDomainMappingResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class AddLiveDomainMappingRequest(TeaModel):
    def __init__(self, security_token=None, push_domain=None, pull_domain=None):
        self.security_token = security_token  # type: str
        self.push_domain = push_domain  # type: str
        self.pull_domain = pull_domain  # type: str

    def validate(self):
        self.validate_required(self.push_domain, 'push_domain')
        self.validate_required(self.pull_domain, 'pull_domain')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['PushDomain'] = self.push_domain
        result['PullDomain'] = self.pull_domain
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.push_domain = map.get('PushDomain')
        self.pull_domain = map.get('PullDomain')
        return self


class AddLiveDomainMappingResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class AddCasterEpisodeGroupContentRequest(TeaModel):
    def __init__(self, client_token=None, content=None):
        self.client_token = client_token  # type: str
        self.content = content          # type: str

    def validate(self):
        self.validate_required(self.client_token, 'client_token')
        self.validate_required(self.content, 'content')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['Content'] = self.content
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.content = map.get('Content')
        return self


class AddCasterEpisodeGroupContentResponse(TeaModel):
    def __init__(self, request_id=None, program_id=None, item_ids=None):
        self.request_id = request_id    # type: str
        self.program_id = program_id    # type: str
        self.item_ids = item_ids        # type: AddCasterEpisodeGroupContentResponseItemIds

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.program_id, 'program_id')
        self.validate_required(self.item_ids, 'item_ids')
        if self.item_ids:
            self.item_ids.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['ProgramId'] = self.program_id
        if self.item_ids is not None:
            result['ItemIds'] = self.item_ids.to_map()
        else:
            result['ItemIds'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.program_id = map.get('ProgramId')
        if map.get('ItemIds') is not None:
            temp_model = AddCasterEpisodeGroupContentResponseItemIds()
            self.item_ids = temp_model.from_map(map['ItemIds'])
        else:
            self.item_ids = None
        return self


class AddCasterEpisodeGroupContentResponseItemIds(TeaModel):
    def __init__(self, item_id=None):
        self.item_id = item_id          # type: List[str]

    def validate(self):
        self.validate_required(self.item_id, 'item_id')

    def to_map(self):
        result = {}
        result['ItemId'] = self.item_id
        return result

    def from_map(self, map={}):
        self.item_id = map.get('ItemId')
        return self


class ModifyCasterProgramRequest(TeaModel):
    def __init__(self, caster_id=None, episode=None):
        self.caster_id = caster_id      # type: str
        self.episode = episode          # type: List[ModifyCasterProgramRequestEpisode]

    def validate(self):
        self.validate_required(self.caster_id, 'caster_id')
        self.validate_required(self.episode, 'episode')
        if self.episode:
            for k in self.episode:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['CasterId'] = self.caster_id
        result['Episode'] = []
        if self.episode is not None:
            for k in self.episode:
                result['Episode'].append(k.to_map() if k else None)
        else:
            result['Episode'] = None
        return result

    def from_map(self, map={}):
        self.caster_id = map.get('CasterId')
        self.episode = []
        if map.get('Episode') is not None:
            for k in map.get('Episode'):
                temp_model = ModifyCasterProgramRequestEpisode()
                self.episode.append(temp_model.from_map(k))
        else:
            self.episode = None
        return self


class ModifyCasterProgramRequestEpisode(TeaModel):
    def __init__(self, episode_id=None, episode_type=None, episode_name=None, resource_id=None, component_id=None,
                 start_time=None, end_time=None, switch_type=None):
        self.episode_id = episode_id    # type: str
        self.episode_type = episode_type  # type: str
        self.episode_name = episode_name  # type: str
        self.resource_id = resource_id  # type: str
        self.component_id = component_id  # type: List[str]
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.switch_type = switch_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['EpisodeId'] = self.episode_id
        result['EpisodeType'] = self.episode_type
        result['EpisodeName'] = self.episode_name
        result['ResourceId'] = self.resource_id
        result['ComponentId'] = self.component_id
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['SwitchType'] = self.switch_type
        return result

    def from_map(self, map={}):
        self.episode_id = map.get('EpisodeId')
        self.episode_type = map.get('EpisodeType')
        self.episode_name = map.get('EpisodeName')
        self.resource_id = map.get('ResourceId')
        self.component_id = map.get('ComponentId')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.switch_type = map.get('SwitchType')
        return self


class ModifyCasterProgramResponse(TeaModel):
    def __init__(self, request_id=None, caster_id=None):
        self.request_id = request_id    # type: str
        self.caster_id = caster_id      # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.caster_id, 'caster_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['CasterId'] = self.caster_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.caster_id = map.get('CasterId')
        return self


class ModifyCasterEpisodeRequest(TeaModel):
    def __init__(self, caster_id=None, episode_id=None, episode_name=None, resource_id=None, component_id=None,
                 start_time=None, end_time=None, switch_type=None):
        self.caster_id = caster_id      # type: str
        self.episode_id = episode_id    # type: str
        self.episode_name = episode_name  # type: str
        self.resource_id = resource_id  # type: str
        self.component_id = component_id  # type: List[str]
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.switch_type = switch_type  # type: str

    def validate(self):
        self.validate_required(self.caster_id, 'caster_id')
        self.validate_required(self.episode_id, 'episode_id')

    def to_map(self):
        result = {}
        result['CasterId'] = self.caster_id
        result['EpisodeId'] = self.episode_id
        result['EpisodeName'] = self.episode_name
        result['ResourceId'] = self.resource_id
        result['ComponentId'] = self.component_id
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['SwitchType'] = self.switch_type
        return result

    def from_map(self, map={}):
        self.caster_id = map.get('CasterId')
        self.episode_id = map.get('EpisodeId')
        self.episode_name = map.get('EpisodeName')
        self.resource_id = map.get('ResourceId')
        self.component_id = map.get('ComponentId')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.switch_type = map.get('SwitchType')
        return self


class ModifyCasterEpisodeResponse(TeaModel):
    def __init__(self, request_id=None, caster_id=None, episode_id=None):
        self.request_id = request_id    # type: str
        self.caster_id = caster_id      # type: str
        self.episode_id = episode_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.caster_id, 'caster_id')
        self.validate_required(self.episode_id, 'episode_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['CasterId'] = self.caster_id
        result['EpisodeId'] = self.episode_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.caster_id = map.get('CasterId')
        self.episode_id = map.get('EpisodeId')
        return self


class DescribeCasterProgramRequest(TeaModel):
    def __init__(self, caster_id=None, episode_id=None, episode_type=None, start_time=None, end_time=None,
                 page_num=None, page_size=None, status=None):
        self.caster_id = caster_id      # type: str
        self.episode_id = episode_id    # type: str
        self.episode_type = episode_type  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int
        self.status = status            # type: int

    def validate(self):
        self.validate_required(self.caster_id, 'caster_id')

    def to_map(self):
        result = {}
        result['CasterId'] = self.caster_id
        result['EpisodeId'] = self.episode_id
        result['EpisodeType'] = self.episode_type
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        result['Status'] = self.status
        return result

    def from_map(self, map={}):
        self.caster_id = map.get('CasterId')
        self.episode_id = map.get('EpisodeId')
        self.episode_type = map.get('EpisodeType')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        self.status = map.get('Status')
        return self


class DescribeCasterProgramResponse(TeaModel):
    def __init__(self, request_id=None, caster_id=None, program_name=None, program_effect=None, total=None,
                 episodes=None):
        self.request_id = request_id    # type: str
        self.caster_id = caster_id      # type: str
        self.program_name = program_name  # type: str
        self.program_effect = program_effect  # type: int
        self.total = total              # type: int
        self.episodes = episodes        # type: DescribeCasterProgramResponseEpisodes

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.caster_id, 'caster_id')
        self.validate_required(self.program_name, 'program_name')
        self.validate_required(self.program_effect, 'program_effect')
        self.validate_required(self.total, 'total')
        self.validate_required(self.episodes, 'episodes')
        if self.episodes:
            self.episodes.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['CasterId'] = self.caster_id
        result['ProgramName'] = self.program_name
        result['ProgramEffect'] = self.program_effect
        result['Total'] = self.total
        if self.episodes is not None:
            result['Episodes'] = self.episodes.to_map()
        else:
            result['Episodes'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.caster_id = map.get('CasterId')
        self.program_name = map.get('ProgramName')
        self.program_effect = map.get('ProgramEffect')
        self.total = map.get('Total')
        if map.get('Episodes') is not None:
            temp_model = DescribeCasterProgramResponseEpisodes()
            self.episodes = temp_model.from_map(map['Episodes'])
        else:
            self.episodes = None
        return self


class DescribeCasterProgramResponseEpisodesEpisodeComponentIds(TeaModel):
    def __init__(self, component_id=None):
        # ComponentId
        self.component_id = component_id  # type: List[str]

    def validate(self):
        self.validate_required(self.component_id, 'component_id')

    def to_map(self):
        result = {}
        result['ComponentId'] = self.component_id
        return result

    def from_map(self, map={}):
        self.component_id = map.get('ComponentId')
        return self


class DescribeCasterProgramResponseEpisodesEpisode(TeaModel):
    def __init__(self, episode_id=None, episode_type=None, episode_name=None, resource_id=None, start_time=None,
                 end_time=None, switch_type=None, status=None, component_ids=None):
        self.episode_id = episode_id    # type: str
        self.episode_type = episode_type  # type: str
        self.episode_name = episode_name  # type: str
        self.resource_id = resource_id  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.switch_type = switch_type  # type: str
        self.status = status            # type: int
        self.component_ids = component_ids  # type: DescribeCasterProgramResponseEpisodesEpisodeComponentIds

    def validate(self):
        self.validate_required(self.episode_id, 'episode_id')
        self.validate_required(self.episode_type, 'episode_type')
        self.validate_required(self.episode_name, 'episode_name')
        self.validate_required(self.resource_id, 'resource_id')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.switch_type, 'switch_type')
        self.validate_required(self.status, 'status')
        self.validate_required(self.component_ids, 'component_ids')
        if self.component_ids:
            self.component_ids.validate()

    def to_map(self):
        result = {}
        result['EpisodeId'] = self.episode_id
        result['EpisodeType'] = self.episode_type
        result['EpisodeName'] = self.episode_name
        result['ResourceId'] = self.resource_id
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['SwitchType'] = self.switch_type
        result['Status'] = self.status
        if self.component_ids is not None:
            result['ComponentIds'] = self.component_ids.to_map()
        else:
            result['ComponentIds'] = None
        return result

    def from_map(self, map={}):
        self.episode_id = map.get('EpisodeId')
        self.episode_type = map.get('EpisodeType')
        self.episode_name = map.get('EpisodeName')
        self.resource_id = map.get('ResourceId')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.switch_type = map.get('SwitchType')
        self.status = map.get('Status')
        if map.get('ComponentIds') is not None:
            temp_model = DescribeCasterProgramResponseEpisodesEpisodeComponentIds()
            self.component_ids = temp_model.from_map(map['ComponentIds'])
        else:
            self.component_ids = None
        return self


class DescribeCasterProgramResponseEpisodes(TeaModel):
    def __init__(self, episode=None):
        self.episode = episode          # type: List[DescribeCasterProgramResponseEpisodesEpisode]

    def validate(self):
        self.validate_required(self.episode, 'episode')
        if self.episode:
            for k in self.episode:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Episode'] = []
        if self.episode is not None:
            for k in self.episode:
                result['Episode'].append(k.to_map() if k else None)
        else:
            result['Episode'] = None
        return result

    def from_map(self, map={}):
        self.episode = []
        if map.get('Episode') is not None:
            for k in map.get('Episode'):
                temp_model = DescribeCasterProgramResponseEpisodesEpisode()
                self.episode.append(temp_model.from_map(k))
        else:
            self.episode = None
        return self


class DeleteCasterProgramRequest(TeaModel):
    def __init__(self, caster_id=None):
        self.caster_id = caster_id      # type: str

    def validate(self):
        self.validate_required(self.caster_id, 'caster_id')

    def to_map(self):
        result = {}
        result['CasterId'] = self.caster_id
        return result

    def from_map(self, map={}):
        self.caster_id = map.get('CasterId')
        return self


class DeleteCasterProgramResponse(TeaModel):
    def __init__(self, request_id=None, caster_id=None):
        self.request_id = request_id    # type: str
        self.caster_id = caster_id      # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.caster_id, 'caster_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['CasterId'] = self.caster_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.caster_id = map.get('CasterId')
        return self


class DeleteCasterEpisodeGroupRequest(TeaModel):
    def __init__(self, program_id=None):
        self.program_id = program_id    # type: str

    def validate(self):
        self.validate_required(self.program_id, 'program_id')

    def to_map(self):
        result = {}
        result['ProgramId'] = self.program_id
        return result

    def from_map(self, map={}):
        self.program_id = map.get('ProgramId')
        return self


class DeleteCasterEpisodeGroupResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DeleteCasterEpisodeRequest(TeaModel):
    def __init__(self, caster_id=None, episode_id=None):
        self.caster_id = caster_id      # type: str
        self.episode_id = episode_id    # type: str

    def validate(self):
        self.validate_required(self.caster_id, 'caster_id')
        self.validate_required(self.episode_id, 'episode_id')

    def to_map(self):
        result = {}
        result['CasterId'] = self.caster_id
        result['EpisodeId'] = self.episode_id
        return result

    def from_map(self, map={}):
        self.caster_id = map.get('CasterId')
        self.episode_id = map.get('EpisodeId')
        return self


class DeleteCasterEpisodeResponse(TeaModel):
    def __init__(self, request_id=None, caster_id=None, episode_id=None):
        self.request_id = request_id    # type: str
        self.caster_id = caster_id      # type: str
        self.episode_id = episode_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.caster_id, 'caster_id')
        self.validate_required(self.episode_id, 'episode_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['CasterId'] = self.caster_id
        result['EpisodeId'] = self.episode_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.caster_id = map.get('CasterId')
        self.episode_id = map.get('EpisodeId')
        return self


class AddCasterProgramRequest(TeaModel):
    def __init__(self, caster_id=None, episode=None):
        self.caster_id = caster_id      # type: str
        self.episode = episode          # type: List[AddCasterProgramRequestEpisode]

    def validate(self):
        self.validate_required(self.caster_id, 'caster_id')
        self.validate_required(self.episode, 'episode')
        if self.episode:
            for k in self.episode:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['CasterId'] = self.caster_id
        result['Episode'] = []
        if self.episode is not None:
            for k in self.episode:
                result['Episode'].append(k.to_map() if k else None)
        else:
            result['Episode'] = None
        return result

    def from_map(self, map={}):
        self.caster_id = map.get('CasterId')
        self.episode = []
        if map.get('Episode') is not None:
            for k in map.get('Episode'):
                temp_model = AddCasterProgramRequestEpisode()
                self.episode.append(temp_model.from_map(k))
        else:
            self.episode = None
        return self


class AddCasterProgramRequestEpisode(TeaModel):
    def __init__(self, episode_type=None, episode_name=None, resource_id=None, component_id=None, start_time=None,
                 end_time=None, switch_type=None):
        self.episode_type = episode_type  # type: str
        self.episode_name = episode_name  # type: str
        self.resource_id = resource_id  # type: str
        self.component_id = component_id  # type: List[str]
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.switch_type = switch_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['EpisodeType'] = self.episode_type
        result['EpisodeName'] = self.episode_name
        result['ResourceId'] = self.resource_id
        result['ComponentId'] = self.component_id
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['SwitchType'] = self.switch_type
        return result

    def from_map(self, map={}):
        self.episode_type = map.get('EpisodeType')
        self.episode_name = map.get('EpisodeName')
        self.resource_id = map.get('ResourceId')
        self.component_id = map.get('ComponentId')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.switch_type = map.get('SwitchType')
        return self


class AddCasterProgramResponse(TeaModel):
    def __init__(self, request_id=None, episode_ids=None):
        self.request_id = request_id    # type: str
        self.episode_ids = episode_ids  # type: AddCasterProgramResponseEpisodeIds

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.episode_ids, 'episode_ids')
        if self.episode_ids:
            self.episode_ids.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.episode_ids is not None:
            result['EpisodeIds'] = self.episode_ids.to_map()
        else:
            result['EpisodeIds'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('EpisodeIds') is not None:
            temp_model = AddCasterProgramResponseEpisodeIds()
            self.episode_ids = temp_model.from_map(map['EpisodeIds'])
        else:
            self.episode_ids = None
        return self


class AddCasterProgramResponseEpisodeIdsEpisodeId(TeaModel):
    def __init__(self, episode_id=None):
        self.episode_id = episode_id    # type: str

    def validate(self):
        self.validate_required(self.episode_id, 'episode_id')

    def to_map(self):
        result = {}
        result['EpisodeId'] = self.episode_id
        return result

    def from_map(self, map={}):
        self.episode_id = map.get('EpisodeId')
        return self


class AddCasterProgramResponseEpisodeIds(TeaModel):
    def __init__(self, episode_id=None):
        self.episode_id = episode_id    # type: List[AddCasterProgramResponseEpisodeIdsEpisodeId]

    def validate(self):
        self.validate_required(self.episode_id, 'episode_id')
        if self.episode_id:
            for k in self.episode_id:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['EpisodeId'] = []
        if self.episode_id is not None:
            for k in self.episode_id:
                result['EpisodeId'].append(k.to_map() if k else None)
        else:
            result['EpisodeId'] = None
        return result

    def from_map(self, map={}):
        self.episode_id = []
        if map.get('EpisodeId') is not None:
            for k in map.get('EpisodeId'):
                temp_model = AddCasterProgramResponseEpisodeIdsEpisodeId()
                self.episode_id.append(temp_model.from_map(k))
        else:
            self.episode_id = None
        return self


class AddCasterEpisodeGroupRequest(TeaModel):
    def __init__(self, client_token=None, domain_name=None, item=None, start_time=None, repeat_num=None,
                 side_output_url=None, callback_url=None):
        self.client_token = client_token  # type: str
        self.domain_name = domain_name  # type: str
        self.item = item                # type: List[AddCasterEpisodeGroupRequestItem]
        self.start_time = start_time    # type: str
        self.repeat_num = repeat_num    # type: int
        self.side_output_url = side_output_url  # type: str
        self.callback_url = callback_url  # type: str

    def validate(self):
        self.validate_required(self.client_token, 'client_token')
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.item, 'item')
        if self.item:
            for k in self.item:
                if k:
                    k.validate()
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.repeat_num, 'repeat_num')
        self.validate_required(self.side_output_url, 'side_output_url')
        self.validate_required(self.callback_url, 'callback_url')

    def to_map(self):
        result = {}
        result['ClientToken'] = self.client_token
        result['DomainName'] = self.domain_name
        result['Item'] = []
        if self.item is not None:
            for k in self.item:
                result['Item'].append(k.to_map() if k else None)
        else:
            result['Item'] = None
        result['StartTime'] = self.start_time
        result['RepeatNum'] = self.repeat_num
        result['SideOutputUrl'] = self.side_output_url
        result['CallbackUrl'] = self.callback_url
        return result

    def from_map(self, map={}):
        self.client_token = map.get('ClientToken')
        self.domain_name = map.get('DomainName')
        self.item = []
        if map.get('Item') is not None:
            for k in map.get('Item'):
                temp_model = AddCasterEpisodeGroupRequestItem()
                self.item.append(temp_model.from_map(k))
        else:
            self.item = None
        self.start_time = map.get('StartTime')
        self.repeat_num = map.get('RepeatNum')
        self.side_output_url = map.get('SideOutputUrl')
        self.callback_url = map.get('CallbackUrl')
        return self


class AddCasterEpisodeGroupRequestItem(TeaModel):
    def __init__(self, item_name=None, vod_url=None):
        self.item_name = item_name      # type: str
        self.vod_url = vod_url          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['ItemName'] = self.item_name
        result['VodUrl'] = self.vod_url
        return result

    def from_map(self, map={}):
        self.item_name = map.get('ItemName')
        self.vod_url = map.get('VodUrl')
        return self


class AddCasterEpisodeGroupResponse(TeaModel):
    def __init__(self, request_id=None, program_id=None, item_ids=None):
        self.request_id = request_id    # type: str
        self.program_id = program_id    # type: str
        self.item_ids = item_ids        # type: AddCasterEpisodeGroupResponseItemIds

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.program_id, 'program_id')
        self.validate_required(self.item_ids, 'item_ids')
        if self.item_ids:
            self.item_ids.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['ProgramId'] = self.program_id
        if self.item_ids is not None:
            result['ItemIds'] = self.item_ids.to_map()
        else:
            result['ItemIds'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.program_id = map.get('ProgramId')
        if map.get('ItemIds') is not None:
            temp_model = AddCasterEpisodeGroupResponseItemIds()
            self.item_ids = temp_model.from_map(map['ItemIds'])
        else:
            self.item_ids = None
        return self


class AddCasterEpisodeGroupResponseItemIds(TeaModel):
    def __init__(self, item_id=None):
        self.item_id = item_id          # type: List[str]

    def validate(self):
        self.validate_required(self.item_id, 'item_id')

    def to_map(self):
        result = {}
        result['ItemId'] = self.item_id
        return result

    def from_map(self, map={}):
        self.item_id = map.get('ItemId')
        return self


class AddCasterEpisodeRequest(TeaModel):
    def __init__(self, caster_id=None, episode_type=None, episode_name=None, resource_id=None, component_id=None,
                 start_time=None, end_time=None, switch_type=None):
        self.caster_id = caster_id      # type: str
        self.episode_type = episode_type  # type: str
        self.episode_name = episode_name  # type: str
        self.resource_id = resource_id  # type: str
        self.component_id = component_id  # type: List[str]
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.switch_type = switch_type  # type: str

    def validate(self):
        self.validate_required(self.caster_id, 'caster_id')
        self.validate_required(self.episode_type, 'episode_type')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.switch_type, 'switch_type')

    def to_map(self):
        result = {}
        result['CasterId'] = self.caster_id
        result['EpisodeType'] = self.episode_type
        result['EpisodeName'] = self.episode_name
        result['ResourceId'] = self.resource_id
        result['ComponentId'] = self.component_id
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['SwitchType'] = self.switch_type
        return result

    def from_map(self, map={}):
        self.caster_id = map.get('CasterId')
        self.episode_type = map.get('EpisodeType')
        self.episode_name = map.get('EpisodeName')
        self.resource_id = map.get('ResourceId')
        self.component_id = map.get('ComponentId')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.switch_type = map.get('SwitchType')
        return self


class AddCasterEpisodeResponse(TeaModel):
    def __init__(self, request_id=None, episode_id=None):
        self.request_id = request_id    # type: str
        self.episode_id = episode_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.episode_id, 'episode_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['EpisodeId'] = self.episode_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.episode_id = map.get('EpisodeId')
        return self


class DescribeLiveDomainTranscodeDataRequest(TeaModel):
    def __init__(self, domain_name=None, start_time=None, end_time=None):
        self.domain_name = domain_name  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        return self


class DescribeLiveDomainTranscodeDataResponse(TeaModel):
    def __init__(self, request_id=None, transcode_data_infos=None):
        self.request_id = request_id    # type: str
        self.transcode_data_infos = transcode_data_infos  # type: DescribeLiveDomainTranscodeDataResponseTranscodeDataInfos

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.transcode_data_infos, 'transcode_data_infos')
        if self.transcode_data_infos:
            self.transcode_data_infos.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.transcode_data_infos is not None:
            result['TranscodeDataInfos'] = self.transcode_data_infos.to_map()
        else:
            result['TranscodeDataInfos'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('TranscodeDataInfos') is not None:
            temp_model = DescribeLiveDomainTranscodeDataResponseTranscodeDataInfos()
            self.transcode_data_infos = temp_model.from_map(map['TranscodeDataInfos'])
        else:
            self.transcode_data_infos = None
        return self


class DescribeLiveDomainTranscodeDataResponseTranscodeDataInfosTranscodeDataInfo(TeaModel):
    def __init__(self, date=None, total=None, detail=None):
        self.date = date                # type: str
        self.total = total              # type: int
        self.detail = detail            # type: str

    def validate(self):
        self.validate_required(self.date, 'date')
        self.validate_required(self.total, 'total')
        self.validate_required(self.detail, 'detail')

    def to_map(self):
        result = {}
        result['Date'] = self.date
        result['Total'] = self.total
        result['Detail'] = self.detail
        return result

    def from_map(self, map={}):
        self.date = map.get('Date')
        self.total = map.get('Total')
        self.detail = map.get('Detail')
        return self


class DescribeLiveDomainTranscodeDataResponseTranscodeDataInfos(TeaModel):
    def __init__(self, transcode_data_info=None):
        self.transcode_data_info = transcode_data_info  # type: List[DescribeLiveDomainTranscodeDataResponseTranscodeDataInfosTranscodeDataInfo]

    def validate(self):
        self.validate_required(self.transcode_data_info, 'transcode_data_info')
        if self.transcode_data_info:
            for k in self.transcode_data_info:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['TranscodeDataInfo'] = []
        if self.transcode_data_info is not None:
            for k in self.transcode_data_info:
                result['TranscodeDataInfo'].append(k.to_map() if k else None)
        else:
            result['TranscodeDataInfo'] = None
        return result

    def from_map(self, map={}):
        self.transcode_data_info = []
        if map.get('TranscodeDataInfo') is not None:
            for k in map.get('TranscodeDataInfo'):
                temp_model = DescribeLiveDomainTranscodeDataResponseTranscodeDataInfosTranscodeDataInfo()
                self.transcode_data_info.append(temp_model.from_map(k))
        else:
            self.transcode_data_info = None
        return self


class DescribeLiveDomainSnapshotDataRequest(TeaModel):
    def __init__(self, domain_name=None, start_time=None, end_time=None):
        self.domain_name = domain_name  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        return self


class DescribeLiveDomainSnapshotDataResponse(TeaModel):
    def __init__(self, request_id=None, snapshot_data_infos=None):
        self.request_id = request_id    # type: str
        self.snapshot_data_infos = snapshot_data_infos  # type: DescribeLiveDomainSnapshotDataResponseSnapshotDataInfos

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.snapshot_data_infos, 'snapshot_data_infos')
        if self.snapshot_data_infos:
            self.snapshot_data_infos.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.snapshot_data_infos is not None:
            result['SnapshotDataInfos'] = self.snapshot_data_infos.to_map()
        else:
            result['SnapshotDataInfos'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('SnapshotDataInfos') is not None:
            temp_model = DescribeLiveDomainSnapshotDataResponseSnapshotDataInfos()
            self.snapshot_data_infos = temp_model.from_map(map['SnapshotDataInfos'])
        else:
            self.snapshot_data_infos = None
        return self


class DescribeLiveDomainSnapshotDataResponseSnapshotDataInfosSnapshotDataInfo(TeaModel):
    def __init__(self, date=None, total=None):
        self.date = date                # type: str
        self.total = total              # type: int

    def validate(self):
        self.validate_required(self.date, 'date')
        self.validate_required(self.total, 'total')

    def to_map(self):
        result = {}
        result['Date'] = self.date
        result['Total'] = self.total
        return result

    def from_map(self, map={}):
        self.date = map.get('Date')
        self.total = map.get('Total')
        return self


class DescribeLiveDomainSnapshotDataResponseSnapshotDataInfos(TeaModel):
    def __init__(self, snapshot_data_info=None):
        self.snapshot_data_info = snapshot_data_info  # type: List[DescribeLiveDomainSnapshotDataResponseSnapshotDataInfosSnapshotDataInfo]

    def validate(self):
        self.validate_required(self.snapshot_data_info, 'snapshot_data_info')
        if self.snapshot_data_info:
            for k in self.snapshot_data_info:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['SnapshotDataInfo'] = []
        if self.snapshot_data_info is not None:
            for k in self.snapshot_data_info:
                result['SnapshotDataInfo'].append(k.to_map() if k else None)
        else:
            result['SnapshotDataInfo'] = None
        return result

    def from_map(self, map={}):
        self.snapshot_data_info = []
        if map.get('SnapshotDataInfo') is not None:
            for k in map.get('SnapshotDataInfo'):
                temp_model = DescribeLiveDomainSnapshotDataResponseSnapshotDataInfosSnapshotDataInfo()
                self.snapshot_data_info.append(temp_model.from_map(k))
        else:
            self.snapshot_data_info = None
        return self


class DescribeLiveDomainRecordDataRequest(TeaModel):
    def __init__(self, domain_name=None, start_time=None, end_time=None, record_type=None):
        self.domain_name = domain_name  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.record_type = record_type  # type: str

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['RecordType'] = self.record_type
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.record_type = map.get('RecordType')
        return self


class DescribeLiveDomainRecordDataResponse(TeaModel):
    def __init__(self, request_id=None, record_data_infos=None):
        self.request_id = request_id    # type: str
        self.record_data_infos = record_data_infos  # type: DescribeLiveDomainRecordDataResponseRecordDataInfos

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.record_data_infos, 'record_data_infos')
        if self.record_data_infos:
            self.record_data_infos.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.record_data_infos is not None:
            result['RecordDataInfos'] = self.record_data_infos.to_map()
        else:
            result['RecordDataInfos'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('RecordDataInfos') is not None:
            temp_model = DescribeLiveDomainRecordDataResponseRecordDataInfos()
            self.record_data_infos = temp_model.from_map(map['RecordDataInfos'])
        else:
            self.record_data_infos = None
        return self


class DescribeLiveDomainRecordDataResponseRecordDataInfosRecordDataInfoDetail(TeaModel):
    def __init__(self, mp4=None, flv=None, ts=None):
        self.mp4 = mp4                  # type: int
        self.flv = flv                  # type: int
        self.ts = ts                    # type: int

    def validate(self):
        self.validate_required(self.mp4, 'mp4')
        self.validate_required(self.flv, 'flv')
        self.validate_required(self.ts, 'ts')

    def to_map(self):
        result = {}
        result['MP4'] = self.mp4
        result['FLV'] = self.flv
        result['TS'] = self.ts
        return result

    def from_map(self, map={}):
        self.mp4 = map.get('MP4')
        self.flv = map.get('FLV')
        self.ts = map.get('TS')
        return self


class DescribeLiveDomainRecordDataResponseRecordDataInfosRecordDataInfo(TeaModel):
    def __init__(self, date=None, total=None, detail=None):
        self.date = date                # type: str
        self.total = total              # type: int
        self.detail = detail            # type: DescribeLiveDomainRecordDataResponseRecordDataInfosRecordDataInfoDetail

    def validate(self):
        self.validate_required(self.date, 'date')
        self.validate_required(self.total, 'total')
        self.validate_required(self.detail, 'detail')
        if self.detail:
            self.detail.validate()

    def to_map(self):
        result = {}
        result['Date'] = self.date
        result['Total'] = self.total
        if self.detail is not None:
            result['Detail'] = self.detail.to_map()
        else:
            result['Detail'] = None
        return result

    def from_map(self, map={}):
        self.date = map.get('Date')
        self.total = map.get('Total')
        if map.get('Detail') is not None:
            temp_model = DescribeLiveDomainRecordDataResponseRecordDataInfosRecordDataInfoDetail()
            self.detail = temp_model.from_map(map['Detail'])
        else:
            self.detail = None
        return self


class DescribeLiveDomainRecordDataResponseRecordDataInfos(TeaModel):
    def __init__(self, record_data_info=None):
        self.record_data_info = record_data_info  # type: List[DescribeLiveDomainRecordDataResponseRecordDataInfosRecordDataInfo]

    def validate(self):
        self.validate_required(self.record_data_info, 'record_data_info')
        if self.record_data_info:
            for k in self.record_data_info:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RecordDataInfo'] = []
        if self.record_data_info is not None:
            for k in self.record_data_info:
                result['RecordDataInfo'].append(k.to_map() if k else None)
        else:
            result['RecordDataInfo'] = None
        return result

    def from_map(self, map={}):
        self.record_data_info = []
        if map.get('RecordDataInfo') is not None:
            for k in map.get('RecordDataInfo'):
                temp_model = DescribeLiveDomainRecordDataResponseRecordDataInfosRecordDataInfo()
                self.record_data_info.append(temp_model.from_map(k))
        else:
            self.record_data_info = None
        return self


class RealTimeRecordCommandRequest(TeaModel):
    def __init__(self, command=None, domain_name=None, app_name=None, stream_name=None):
        self.command = command          # type: str
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str
        self.stream_name = stream_name  # type: str

    def validate(self):
        self.validate_required(self.command, 'command')
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.app_name, 'app_name')
        self.validate_required(self.stream_name, 'stream_name')

    def to_map(self):
        result = {}
        result['Command'] = self.command
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        result['StreamName'] = self.stream_name
        return result

    def from_map(self, map={}):
        self.command = map.get('Command')
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        self.stream_name = map.get('StreamName')
        return self


class RealTimeRecordCommandResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeLiveDomainTrafficDataRequest(TeaModel):
    def __init__(self, domain_name=None, start_time=None, end_time=None, interval=None, isp_name_en=None,
                 location_name_en=None):
        self.domain_name = domain_name  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.interval = interval        # type: str
        self.isp_name_en = isp_name_en  # type: str
        self.location_name_en = location_name_en  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['Interval'] = self.interval
        result['IspNameEn'] = self.isp_name_en
        result['LocationNameEn'] = self.location_name_en
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.interval = map.get('Interval')
        self.isp_name_en = map.get('IspNameEn')
        self.location_name_en = map.get('LocationNameEn')
        return self


class DescribeLiveDomainTrafficDataResponse(TeaModel):
    def __init__(self, request_id=None, domain_name=None, start_time=None, end_time=None, data_interval=None,
                 traffic_data_per_interval=None):
        self.request_id = request_id    # type: str
        self.domain_name = domain_name  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.data_interval = data_interval  # type: str
        self.traffic_data_per_interval = traffic_data_per_interval  # type: DescribeLiveDomainTrafficDataResponseTrafficDataPerInterval

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.data_interval, 'data_interval')
        self.validate_required(self.traffic_data_per_interval, 'traffic_data_per_interval')
        if self.traffic_data_per_interval:
            self.traffic_data_per_interval.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DomainName'] = self.domain_name
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['DataInterval'] = self.data_interval
        if self.traffic_data_per_interval is not None:
            result['TrafficDataPerInterval'] = self.traffic_data_per_interval.to_map()
        else:
            result['TrafficDataPerInterval'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.domain_name = map.get('DomainName')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.data_interval = map.get('DataInterval')
        if map.get('TrafficDataPerInterval') is not None:
            temp_model = DescribeLiveDomainTrafficDataResponseTrafficDataPerInterval()
            self.traffic_data_per_interval = temp_model.from_map(map['TrafficDataPerInterval'])
        else:
            self.traffic_data_per_interval = None
        return self


class DescribeLiveDomainTrafficDataResponseTrafficDataPerIntervalDataModule(TeaModel):
    def __init__(self, time_stamp=None, traffic_value=None, http_traffic_value=None, https_traffic_value=None):
        self.time_stamp = time_stamp    # type: str
        self.traffic_value = traffic_value  # type: str
        self.http_traffic_value = http_traffic_value  # type: str
        self.https_traffic_value = https_traffic_value  # type: str

    def validate(self):
        self.validate_required(self.time_stamp, 'time_stamp')
        self.validate_required(self.traffic_value, 'traffic_value')
        self.validate_required(self.http_traffic_value, 'http_traffic_value')
        self.validate_required(self.https_traffic_value, 'https_traffic_value')

    def to_map(self):
        result = {}
        result['TimeStamp'] = self.time_stamp
        result['TrafficValue'] = self.traffic_value
        result['HttpTrafficValue'] = self.http_traffic_value
        result['HttpsTrafficValue'] = self.https_traffic_value
        return result

    def from_map(self, map={}):
        self.time_stamp = map.get('TimeStamp')
        self.traffic_value = map.get('TrafficValue')
        self.http_traffic_value = map.get('HttpTrafficValue')
        self.https_traffic_value = map.get('HttpsTrafficValue')
        return self


class DescribeLiveDomainTrafficDataResponseTrafficDataPerInterval(TeaModel):
    def __init__(self, data_module=None):
        self.data_module = data_module  # type: List[DescribeLiveDomainTrafficDataResponseTrafficDataPerIntervalDataModule]

    def validate(self):
        self.validate_required(self.data_module, 'data_module')
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        else:
            result['DataModule'] = None
        return result

    def from_map(self, map={}):
        self.data_module = []
        if map.get('DataModule') is not None:
            for k in map.get('DataModule'):
                temp_model = DescribeLiveDomainTrafficDataResponseTrafficDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        else:
            self.data_module = None
        return self


class DescribeLiveDomainBpsDataRequest(TeaModel):
    def __init__(self, domain_name=None, start_time=None, end_time=None, interval=None, isp_name_en=None,
                 location_name_en=None):
        self.domain_name = domain_name  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.interval = interval        # type: str
        self.isp_name_en = isp_name_en  # type: str
        self.location_name_en = location_name_en  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['Interval'] = self.interval
        result['IspNameEn'] = self.isp_name_en
        result['LocationNameEn'] = self.location_name_en
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.interval = map.get('Interval')
        self.isp_name_en = map.get('IspNameEn')
        self.location_name_en = map.get('LocationNameEn')
        return self


class DescribeLiveDomainBpsDataResponse(TeaModel):
    def __init__(self, request_id=None, domain_name=None, start_time=None, end_time=None, data_interval=None,
                 bps_data_per_interval=None):
        self.request_id = request_id    # type: str
        self.domain_name = domain_name  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.data_interval = data_interval  # type: str
        self.bps_data_per_interval = bps_data_per_interval  # type: DescribeLiveDomainBpsDataResponseBpsDataPerInterval

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.data_interval, 'data_interval')
        self.validate_required(self.bps_data_per_interval, 'bps_data_per_interval')
        if self.bps_data_per_interval:
            self.bps_data_per_interval.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DomainName'] = self.domain_name
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['DataInterval'] = self.data_interval
        if self.bps_data_per_interval is not None:
            result['BpsDataPerInterval'] = self.bps_data_per_interval.to_map()
        else:
            result['BpsDataPerInterval'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.domain_name = map.get('DomainName')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.data_interval = map.get('DataInterval')
        if map.get('BpsDataPerInterval') is not None:
            temp_model = DescribeLiveDomainBpsDataResponseBpsDataPerInterval()
            self.bps_data_per_interval = temp_model.from_map(map['BpsDataPerInterval'])
        else:
            self.bps_data_per_interval = None
        return self


class DescribeLiveDomainBpsDataResponseBpsDataPerIntervalDataModule(TeaModel):
    def __init__(self, time_stamp=None, bps_value=None, http_bps_value=None, https_bps_value=None):
        self.time_stamp = time_stamp    # type: str
        self.bps_value = bps_value      # type: str
        self.http_bps_value = http_bps_value  # type: str
        self.https_bps_value = https_bps_value  # type: str

    def validate(self):
        self.validate_required(self.time_stamp, 'time_stamp')
        self.validate_required(self.bps_value, 'bps_value')
        self.validate_required(self.http_bps_value, 'http_bps_value')
        self.validate_required(self.https_bps_value, 'https_bps_value')

    def to_map(self):
        result = {}
        result['TimeStamp'] = self.time_stamp
        result['BpsValue'] = self.bps_value
        result['HttpBpsValue'] = self.http_bps_value
        result['HttpsBpsValue'] = self.https_bps_value
        return result

    def from_map(self, map={}):
        self.time_stamp = map.get('TimeStamp')
        self.bps_value = map.get('BpsValue')
        self.http_bps_value = map.get('HttpBpsValue')
        self.https_bps_value = map.get('HttpsBpsValue')
        return self


class DescribeLiveDomainBpsDataResponseBpsDataPerInterval(TeaModel):
    def __init__(self, data_module=None):
        self.data_module = data_module  # type: List[DescribeLiveDomainBpsDataResponseBpsDataPerIntervalDataModule]

    def validate(self):
        self.validate_required(self.data_module, 'data_module')
        if self.data_module:
            for k in self.data_module:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['DataModule'] = []
        if self.data_module is not None:
            for k in self.data_module:
                result['DataModule'].append(k.to_map() if k else None)
        else:
            result['DataModule'] = None
        return result

    def from_map(self, map={}):
        self.data_module = []
        if map.get('DataModule') is not None:
            for k in map.get('DataModule'):
                temp_model = DescribeLiveDomainBpsDataResponseBpsDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k))
        else:
            self.data_module = None
        return self


class AddTrancodeSEIRequest(TeaModel):
    def __init__(self, domain_name=None, app_name=None, stream_name=None, text=None, pattern=None, repeat=None,
                 delay=None):
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str
        self.stream_name = stream_name  # type: str
        self.text = text                # type: str
        self.pattern = pattern          # type: str
        self.repeat = repeat            # type: int
        self.delay = delay              # type: int

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.app_name, 'app_name')
        self.validate_required(self.stream_name, 'stream_name')
        self.validate_required(self.text, 'text')
        self.validate_required(self.pattern, 'pattern')
        self.validate_required(self.repeat, 'repeat')
        self.validate_required(self.delay, 'delay')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        result['StreamName'] = self.stream_name
        result['Text'] = self.text
        result['Pattern'] = self.pattern
        result['Repeat'] = self.repeat
        result['Delay'] = self.delay
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        self.stream_name = map.get('StreamName')
        self.text = map.get('Text')
        self.pattern = map.get('Pattern')
        self.repeat = map.get('Repeat')
        self.delay = map.get('Delay')
        return self


class AddTrancodeSEIResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DeleteCasterSceneConfigRequest(TeaModel):
    def __init__(self, caster_id=None, scene_id=None, type=None):
        self.caster_id = caster_id      # type: str
        self.scene_id = scene_id        # type: str
        self.type = type                # type: str

    def validate(self):
        self.validate_required(self.caster_id, 'caster_id')
        self.validate_required(self.scene_id, 'scene_id')
        self.validate_required(self.type, 'type')

    def to_map(self):
        result = {}
        result['CasterId'] = self.caster_id
        result['SceneId'] = self.scene_id
        result['Type'] = self.type
        return result

    def from_map(self, map={}):
        self.caster_id = map.get('CasterId')
        self.scene_id = map.get('SceneId')
        self.type = map.get('Type')
        return self


class DeleteCasterSceneConfigResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class AddCustomLiveStreamTranscodeRequest(TeaModel):
    def __init__(self, domain=None, app=None, template=None, template_type=None, height=None, width=None, fps=None,
                 video_bitrate=None, audio_bitrate=None, gop=None, profile=None, audio_profile=None, audio_codec=None,
                 audio_rate=None, audio_channel_num=None, lazy=None):
        self.domain = domain            # type: str
        self.app = app                  # type: str
        self.template = template        # type: str
        self.template_type = template_type  # type: str
        self.height = height            # type: int
        self.width = width              # type: int
        self.fps = fps                  # type: int
        self.video_bitrate = video_bitrate  # type: int
        self.audio_bitrate = audio_bitrate  # type: int
        self.gop = gop                  # type: str
        self.profile = profile          # type: int
        self.audio_profile = audio_profile  # type: str
        self.audio_codec = audio_codec  # type: str
        self.audio_rate = audio_rate    # type: int
        self.audio_channel_num = audio_channel_num  # type: int
        self.lazy = lazy                # type: str

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.app, 'app')
        self.validate_required(self.template, 'template')
        self.validate_required(self.template_type, 'template_type')

    def to_map(self):
        result = {}
        result['Domain'] = self.domain
        result['App'] = self.app
        result['Template'] = self.template
        result['TemplateType'] = self.template_type
        result['Height'] = self.height
        result['Width'] = self.width
        result['FPS'] = self.fps
        result['VideoBitrate'] = self.video_bitrate
        result['AudioBitrate'] = self.audio_bitrate
        result['Gop'] = self.gop
        result['Profile'] = self.profile
        result['AudioProfile'] = self.audio_profile
        result['AudioCodec'] = self.audio_codec
        result['AudioRate'] = self.audio_rate
        result['AudioChannelNum'] = self.audio_channel_num
        result['Lazy'] = self.lazy
        return result

    def from_map(self, map={}):
        self.domain = map.get('Domain')
        self.app = map.get('App')
        self.template = map.get('Template')
        self.template_type = map.get('TemplateType')
        self.height = map.get('Height')
        self.width = map.get('Width')
        self.fps = map.get('FPS')
        self.video_bitrate = map.get('VideoBitrate')
        self.audio_bitrate = map.get('AudioBitrate')
        self.gop = map.get('Gop')
        self.profile = map.get('Profile')
        self.audio_profile = map.get('AudioProfile')
        self.audio_codec = map.get('AudioCodec')
        self.audio_rate = map.get('AudioRate')
        self.audio_channel_num = map.get('AudioChannelNum')
        self.lazy = map.get('Lazy')
        return self


class AddCustomLiveStreamTranscodeResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeLiveRecordVodConfigsRequest(TeaModel):
    def __init__(self, domain_name=None, app_name=None, stream_name=None, page_num=None, page_size=None):
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str
        self.stream_name = stream_name  # type: str
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        result['StreamName'] = self.stream_name
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        self.stream_name = map.get('StreamName')
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        return self


class DescribeLiveRecordVodConfigsResponse(TeaModel):
    def __init__(self, request_id=None, page_num=None, page_size=None, total=None, live_record_vod_configs=None):
        self.request_id = request_id    # type: str
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int
        self.total = total              # type: str
        self.live_record_vod_configs = live_record_vod_configs  # type: DescribeLiveRecordVodConfigsResponseLiveRecordVodConfigs

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.page_num, 'page_num')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total, 'total')
        self.validate_required(self.live_record_vod_configs, 'live_record_vod_configs')
        if self.live_record_vod_configs:
            self.live_record_vod_configs.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        result['Total'] = self.total
        if self.live_record_vod_configs is not None:
            result['LiveRecordVodConfigs'] = self.live_record_vod_configs.to_map()
        else:
            result['LiveRecordVodConfigs'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        self.total = map.get('Total')
        if map.get('LiveRecordVodConfigs') is not None:
            temp_model = DescribeLiveRecordVodConfigsResponseLiveRecordVodConfigs()
            self.live_record_vod_configs = temp_model.from_map(map['LiveRecordVodConfigs'])
        else:
            self.live_record_vod_configs = None
        return self


class DescribeLiveRecordVodConfigsResponseLiveRecordVodConfigsLiveRecordVodConfig(TeaModel):
    def __init__(self, create_time=None, domain_name=None, app_name=None, stream_name=None,
                 vod_transcode_group_id=None, cycle_duration=None, auto_compose=None, compose_vod_transcode_group_id=None):
        self.create_time = create_time  # type: str
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str
        self.stream_name = stream_name  # type: str
        self.vod_transcode_group_id = vod_transcode_group_id  # type: str
        self.cycle_duration = cycle_duration  # type: int
        self.auto_compose = auto_compose  # type: str
        self.compose_vod_transcode_group_id = compose_vod_transcode_group_id  # type: str

    def validate(self):
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.app_name, 'app_name')
        self.validate_required(self.stream_name, 'stream_name')
        self.validate_required(self.vod_transcode_group_id, 'vod_transcode_group_id')
        self.validate_required(self.cycle_duration, 'cycle_duration')
        self.validate_required(self.auto_compose, 'auto_compose')
        self.validate_required(self.compose_vod_transcode_group_id, 'compose_vod_transcode_group_id')

    def to_map(self):
        result = {}
        result['CreateTime'] = self.create_time
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        result['StreamName'] = self.stream_name
        result['VodTranscodeGroupId'] = self.vod_transcode_group_id
        result['CycleDuration'] = self.cycle_duration
        result['AutoCompose'] = self.auto_compose
        result['ComposeVodTranscodeGroupId'] = self.compose_vod_transcode_group_id
        return result

    def from_map(self, map={}):
        self.create_time = map.get('CreateTime')
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        self.stream_name = map.get('StreamName')
        self.vod_transcode_group_id = map.get('VodTranscodeGroupId')
        self.cycle_duration = map.get('CycleDuration')
        self.auto_compose = map.get('AutoCompose')
        self.compose_vod_transcode_group_id = map.get('ComposeVodTranscodeGroupId')
        return self


class DescribeLiveRecordVodConfigsResponseLiveRecordVodConfigs(TeaModel):
    def __init__(self, live_record_vod_config=None):
        self.live_record_vod_config = live_record_vod_config  # type: List[DescribeLiveRecordVodConfigsResponseLiveRecordVodConfigsLiveRecordVodConfig]

    def validate(self):
        self.validate_required(self.live_record_vod_config, 'live_record_vod_config')
        if self.live_record_vod_config:
            for k in self.live_record_vod_config:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['LiveRecordVodConfig'] = []
        if self.live_record_vod_config is not None:
            for k in self.live_record_vod_config:
                result['LiveRecordVodConfig'].append(k.to_map() if k else None)
        else:
            result['LiveRecordVodConfig'] = None
        return result

    def from_map(self, map={}):
        self.live_record_vod_config = []
        if map.get('LiveRecordVodConfig') is not None:
            for k in map.get('LiveRecordVodConfig'):
                temp_model = DescribeLiveRecordVodConfigsResponseLiveRecordVodConfigsLiveRecordVodConfig()
                self.live_record_vod_config.append(temp_model.from_map(k))
        else:
            self.live_record_vod_config = None
        return self


class DeleteLiveRecordVodConfigRequest(TeaModel):
    def __init__(self, domain_name=None, app_name=None, stream_name=None):
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str
        self.stream_name = stream_name  # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.app_name, 'app_name')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        result['StreamName'] = self.stream_name
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        self.stream_name = map.get('StreamName')
        return self


class DeleteLiveRecordVodConfigResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class AddLiveRecordVodConfigRequest(TeaModel):
    def __init__(self, domain_name=None, app_name=None, stream_name=None, vod_transcode_group_id=None,
                 cycle_duration=None, auto_compose=None, storage_location=None, compose_vod_transcode_group_id=None):
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str
        self.stream_name = stream_name  # type: str
        self.vod_transcode_group_id = vod_transcode_group_id  # type: str
        self.cycle_duration = cycle_duration  # type: int
        self.auto_compose = auto_compose  # type: str
        self.storage_location = storage_location  # type: str
        self.compose_vod_transcode_group_id = compose_vod_transcode_group_id  # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.app_name, 'app_name')
        self.validate_required(self.vod_transcode_group_id, 'vod_transcode_group_id')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        result['StreamName'] = self.stream_name
        result['VodTranscodeGroupId'] = self.vod_transcode_group_id
        result['CycleDuration'] = self.cycle_duration
        result['AutoCompose'] = self.auto_compose
        result['StorageLocation'] = self.storage_location
        result['ComposeVodTranscodeGroupId'] = self.compose_vod_transcode_group_id
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        self.stream_name = map.get('StreamName')
        self.vod_transcode_group_id = map.get('VodTranscodeGroupId')
        self.cycle_duration = map.get('CycleDuration')
        self.auto_compose = map.get('AutoCompose')
        self.storage_location = map.get('StorageLocation')
        self.compose_vod_transcode_group_id = map.get('ComposeVodTranscodeGroupId')
        return self


class AddLiveRecordVodConfigResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ModifyCasterComponentRequest(TeaModel):
    def __init__(self, caster_id=None, component_id=None, component_name=None, component_type=None, effect=None,
                 component_layer=None, text_layer_content=None, image_layer_content=None, caption_layer_content=None):
        self.caster_id = caster_id      # type: str
        self.component_id = component_id  # type: str
        self.component_name = component_name  # type: str
        self.component_type = component_type  # type: str
        self.effect = effect            # type: str
        self.component_layer = component_layer  # type: str
        self.text_layer_content = text_layer_content  # type: str
        self.image_layer_content = image_layer_content  # type: str
        self.caption_layer_content = caption_layer_content  # type: str

    def validate(self):
        self.validate_required(self.caster_id, 'caster_id')
        self.validate_required(self.component_id, 'component_id')

    def to_map(self):
        result = {}
        result['CasterId'] = self.caster_id
        result['ComponentId'] = self.component_id
        result['ComponentName'] = self.component_name
        result['ComponentType'] = self.component_type
        result['Effect'] = self.effect
        result['ComponentLayer'] = self.component_layer
        result['TextLayerContent'] = self.text_layer_content
        result['ImageLayerContent'] = self.image_layer_content
        result['CaptionLayerContent'] = self.caption_layer_content
        return result

    def from_map(self, map={}):
        self.caster_id = map.get('CasterId')
        self.component_id = map.get('ComponentId')
        self.component_name = map.get('ComponentName')
        self.component_type = map.get('ComponentType')
        self.effect = map.get('Effect')
        self.component_layer = map.get('ComponentLayer')
        self.text_layer_content = map.get('TextLayerContent')
        self.image_layer_content = map.get('ImageLayerContent')
        self.caption_layer_content = map.get('CaptionLayerContent')
        return self


class ModifyCasterComponentResponse(TeaModel):
    def __init__(self, request_id=None, component_id=None):
        self.request_id = request_id    # type: str
        self.component_id = component_id  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.component_id, 'component_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['ComponentId'] = self.component_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.component_id = map.get('ComponentId')
        return self


class DescribeCasterComponentsRequest(TeaModel):
    def __init__(self, caster_id=None, component_id=None):
        self.caster_id = caster_id      # type: str
        self.component_id = component_id  # type: str

    def validate(self):
        self.validate_required(self.caster_id, 'caster_id')

    def to_map(self):
        result = {}
        result['CasterId'] = self.caster_id
        result['ComponentId'] = self.component_id
        return result

    def from_map(self, map={}):
        self.caster_id = map.get('CasterId')
        self.component_id = map.get('ComponentId')
        return self


class DescribeCasterComponentsResponse(TeaModel):
    def __init__(self, request_id=None, total=None, components=None):
        self.request_id = request_id    # type: str
        self.total = total              # type: int
        self.components = components    # type: DescribeCasterComponentsResponseComponents

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total, 'total')
        self.validate_required(self.components, 'components')
        if self.components:
            self.components.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Total'] = self.total
        if self.components is not None:
            result['Components'] = self.components.to_map()
        else:
            result['Components'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total = map.get('Total')
        if map.get('Components') is not None:
            temp_model = DescribeCasterComponentsResponseComponents()
            self.components = temp_model.from_map(map['Components'])
        else:
            self.components = None
        return self


class DescribeCasterComponentsResponseComponentsComponentComponentLayerPositionNormalizeds(TeaModel):
    def __init__(self, position=None):
        # Position
        self.position = position        # type: List[float]

    def validate(self):
        self.validate_required(self.position, 'position')

    def to_map(self):
        result = {}
        result['Position'] = self.position
        return result

    def from_map(self, map={}):
        self.position = map.get('Position')
        return self


class DescribeCasterComponentsResponseComponentsComponentComponentLayer(TeaModel):
    def __init__(self, height_normalized=None, width_normalized=None, position_refer=None, transparency=None,
                 position_normalizeds=None):
        self.height_normalized = height_normalized  # type: float
        self.width_normalized = width_normalized  # type: float
        self.position_refer = position_refer  # type: str
        self.transparency = transparency  # type: int
        self.position_normalizeds = position_normalizeds  # type: DescribeCasterComponentsResponseComponentsComponentComponentLayerPositionNormalizeds

    def validate(self):
        self.validate_required(self.height_normalized, 'height_normalized')
        self.validate_required(self.width_normalized, 'width_normalized')
        self.validate_required(self.position_refer, 'position_refer')
        self.validate_required(self.transparency, 'transparency')
        self.validate_required(self.position_normalizeds, 'position_normalizeds')
        if self.position_normalizeds:
            self.position_normalizeds.validate()

    def to_map(self):
        result = {}
        result['HeightNormalized'] = self.height_normalized
        result['WidthNormalized'] = self.width_normalized
        result['PositionRefer'] = self.position_refer
        result['Transparency'] = self.transparency
        if self.position_normalizeds is not None:
            result['PositionNormalizeds'] = self.position_normalizeds.to_map()
        else:
            result['PositionNormalizeds'] = None
        return result

    def from_map(self, map={}):
        self.height_normalized = map.get('HeightNormalized')
        self.width_normalized = map.get('WidthNormalized')
        self.position_refer = map.get('PositionRefer')
        self.transparency = map.get('Transparency')
        if map.get('PositionNormalizeds') is not None:
            temp_model = DescribeCasterComponentsResponseComponentsComponentComponentLayerPositionNormalizeds()
            self.position_normalizeds = temp_model.from_map(map['PositionNormalizeds'])
        else:
            self.position_normalizeds = None
        return self


class DescribeCasterComponentsResponseComponentsComponentTextLayerContent(TeaModel):
    def __init__(self, text=None, color=None, font_name=None, size_normalized=None, border_width_normalized=None,
                 border_color=None):
        self.text = text                # type: str
        self.color = color              # type: str
        self.font_name = font_name      # type: str
        self.size_normalized = size_normalized  # type: float
        self.border_width_normalized = border_width_normalized  # type: float
        self.border_color = border_color  # type: str

    def validate(self):
        self.validate_required(self.text, 'text')
        self.validate_required(self.color, 'color')
        self.validate_required(self.font_name, 'font_name')
        self.validate_required(self.size_normalized, 'size_normalized')
        self.validate_required(self.border_width_normalized, 'border_width_normalized')
        self.validate_required(self.border_color, 'border_color')

    def to_map(self):
        result = {}
        result['Text'] = self.text
        result['Color'] = self.color
        result['FontName'] = self.font_name
        result['SizeNormalized'] = self.size_normalized
        result['BorderWidthNormalized'] = self.border_width_normalized
        result['BorderColor'] = self.border_color
        return result

    def from_map(self, map={}):
        self.text = map.get('Text')
        self.color = map.get('Color')
        self.font_name = map.get('FontName')
        self.size_normalized = map.get('SizeNormalized')
        self.border_width_normalized = map.get('BorderWidthNormalized')
        self.border_color = map.get('BorderColor')
        return self


class DescribeCasterComponentsResponseComponentsComponentImageLayerContent(TeaModel):
    def __init__(self, material_id=None):
        self.material_id = material_id  # type: str

    def validate(self):
        self.validate_required(self.material_id, 'material_id')

    def to_map(self):
        result = {}
        result['MaterialId'] = self.material_id
        return result

    def from_map(self, map={}):
        self.material_id = map.get('MaterialId')
        return self


class DescribeCasterComponentsResponseComponentsComponentCaptionLayerContent(TeaModel):
    def __init__(self, location_id=None, pts_offset=None, words_count=None, color=None, font_name=None,
                 size_normalized=None, border_width_normalized=None, border_color=None, word_count_per_line=None,
                 word_space_normalized=None, line_space_normalized=None):
        self.location_id = location_id  # type: str
        self.pts_offset = pts_offset    # type: int
        self.words_count = words_count  # type: int
        self.color = color              # type: str
        self.font_name = font_name      # type: str
        self.size_normalized = size_normalized  # type: float
        self.border_width_normalized = border_width_normalized  # type: float
        self.border_color = border_color  # type: str
        self.word_count_per_line = word_count_per_line  # type: int
        self.word_space_normalized = word_space_normalized  # type: float
        self.line_space_normalized = line_space_normalized  # type: float

    def validate(self):
        self.validate_required(self.location_id, 'location_id')
        self.validate_required(self.pts_offset, 'pts_offset')
        self.validate_required(self.words_count, 'words_count')
        self.validate_required(self.color, 'color')
        self.validate_required(self.font_name, 'font_name')
        self.validate_required(self.size_normalized, 'size_normalized')
        self.validate_required(self.border_width_normalized, 'border_width_normalized')
        self.validate_required(self.border_color, 'border_color')
        self.validate_required(self.word_count_per_line, 'word_count_per_line')
        self.validate_required(self.word_space_normalized, 'word_space_normalized')
        self.validate_required(self.line_space_normalized, 'line_space_normalized')

    def to_map(self):
        result = {}
        result['LocationId'] = self.location_id
        result['PtsOffset'] = self.pts_offset
        result['WordsCount'] = self.words_count
        result['Color'] = self.color
        result['FontName'] = self.font_name
        result['SizeNormalized'] = self.size_normalized
        result['BorderWidthNormalized'] = self.border_width_normalized
        result['BorderColor'] = self.border_color
        result['WordCountPerLine'] = self.word_count_per_line
        result['WordSpaceNormalized'] = self.word_space_normalized
        result['LineSpaceNormalized'] = self.line_space_normalized
        return result

    def from_map(self, map={}):
        self.location_id = map.get('LocationId')
        self.pts_offset = map.get('PtsOffset')
        self.words_count = map.get('WordsCount')
        self.color = map.get('Color')
        self.font_name = map.get('FontName')
        self.size_normalized = map.get('SizeNormalized')
        self.border_width_normalized = map.get('BorderWidthNormalized')
        self.border_color = map.get('BorderColor')
        self.word_count_per_line = map.get('WordCountPerLine')
        self.word_space_normalized = map.get('WordSpaceNormalized')
        self.line_space_normalized = map.get('LineSpaceNormalized')
        return self


class DescribeCasterComponentsResponseComponentsComponent(TeaModel):
    def __init__(self, component_id=None, component_name=None, location_id=None, component_type=None, effect=None,
                 component_layer=None, text_layer_content=None, image_layer_content=None, caption_layer_content=None):
        self.component_id = component_id  # type: str
        self.component_name = component_name  # type: str
        self.location_id = location_id  # type: str
        self.component_type = component_type  # type: str
        self.effect = effect            # type: str
        self.component_layer = component_layer  # type: DescribeCasterComponentsResponseComponentsComponentComponentLayer
        self.text_layer_content = text_layer_content  # type: DescribeCasterComponentsResponseComponentsComponentTextLayerContent
        self.image_layer_content = image_layer_content  # type: DescribeCasterComponentsResponseComponentsComponentImageLayerContent
        self.caption_layer_content = caption_layer_content  # type: DescribeCasterComponentsResponseComponentsComponentCaptionLayerContent

    def validate(self):
        self.validate_required(self.component_id, 'component_id')
        self.validate_required(self.component_name, 'component_name')
        self.validate_required(self.location_id, 'location_id')
        self.validate_required(self.component_type, 'component_type')
        self.validate_required(self.effect, 'effect')
        self.validate_required(self.component_layer, 'component_layer')
        if self.component_layer:
            self.component_layer.validate()
        self.validate_required(self.text_layer_content, 'text_layer_content')
        if self.text_layer_content:
            self.text_layer_content.validate()
        self.validate_required(self.image_layer_content, 'image_layer_content')
        if self.image_layer_content:
            self.image_layer_content.validate()
        self.validate_required(self.caption_layer_content, 'caption_layer_content')
        if self.caption_layer_content:
            self.caption_layer_content.validate()

    def to_map(self):
        result = {}
        result['ComponentId'] = self.component_id
        result['ComponentName'] = self.component_name
        result['LocationId'] = self.location_id
        result['ComponentType'] = self.component_type
        result['Effect'] = self.effect
        if self.component_layer is not None:
            result['ComponentLayer'] = self.component_layer.to_map()
        else:
            result['ComponentLayer'] = None
        if self.text_layer_content is not None:
            result['TextLayerContent'] = self.text_layer_content.to_map()
        else:
            result['TextLayerContent'] = None
        if self.image_layer_content is not None:
            result['ImageLayerContent'] = self.image_layer_content.to_map()
        else:
            result['ImageLayerContent'] = None
        if self.caption_layer_content is not None:
            result['CaptionLayerContent'] = self.caption_layer_content.to_map()
        else:
            result['CaptionLayerContent'] = None
        return result

    def from_map(self, map={}):
        self.component_id = map.get('ComponentId')
        self.component_name = map.get('ComponentName')
        self.location_id = map.get('LocationId')
        self.component_type = map.get('ComponentType')
        self.effect = map.get('Effect')
        if map.get('ComponentLayer') is not None:
            temp_model = DescribeCasterComponentsResponseComponentsComponentComponentLayer()
            self.component_layer = temp_model.from_map(map['ComponentLayer'])
        else:
            self.component_layer = None
        if map.get('TextLayerContent') is not None:
            temp_model = DescribeCasterComponentsResponseComponentsComponentTextLayerContent()
            self.text_layer_content = temp_model.from_map(map['TextLayerContent'])
        else:
            self.text_layer_content = None
        if map.get('ImageLayerContent') is not None:
            temp_model = DescribeCasterComponentsResponseComponentsComponentImageLayerContent()
            self.image_layer_content = temp_model.from_map(map['ImageLayerContent'])
        else:
            self.image_layer_content = None
        if map.get('CaptionLayerContent') is not None:
            temp_model = DescribeCasterComponentsResponseComponentsComponentCaptionLayerContent()
            self.caption_layer_content = temp_model.from_map(map['CaptionLayerContent'])
        else:
            self.caption_layer_content = None
        return self


class DescribeCasterComponentsResponseComponents(TeaModel):
    def __init__(self, component=None):
        self.component = component      # type: List[DescribeCasterComponentsResponseComponentsComponent]

    def validate(self):
        self.validate_required(self.component, 'component')
        if self.component:
            for k in self.component:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Component'] = []
        if self.component is not None:
            for k in self.component:
                result['Component'].append(k.to_map() if k else None)
        else:
            result['Component'] = None
        return result

    def from_map(self, map={}):
        self.component = []
        if map.get('Component') is not None:
            for k in map.get('Component'):
                temp_model = DescribeCasterComponentsResponseComponentsComponent()
                self.component.append(temp_model.from_map(k))
        else:
            self.component = None
        return self


class DeleteCasterComponentRequest(TeaModel):
    def __init__(self, caster_id=None, component_id=None):
        self.caster_id = caster_id      # type: str
        self.component_id = component_id  # type: str

    def validate(self):
        self.validate_required(self.caster_id, 'caster_id')
        self.validate_required(self.component_id, 'component_id')

    def to_map(self):
        result = {}
        result['CasterId'] = self.caster_id
        result['ComponentId'] = self.component_id
        return result

    def from_map(self, map={}):
        self.caster_id = map.get('CasterId')
        self.component_id = map.get('ComponentId')
        return self


class DeleteCasterComponentResponse(TeaModel):
    def __init__(self, request_id=None, caster_id=None, component_id=None):
        self.request_id = request_id    # type: str
        self.caster_id = caster_id      # type: str
        self.component_id = component_id  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.caster_id, 'caster_id')
        self.validate_required(self.component_id, 'component_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['CasterId'] = self.caster_id
        result['ComponentId'] = self.component_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.caster_id = map.get('CasterId')
        self.component_id = map.get('ComponentId')
        return self


class AddCasterComponentRequest(TeaModel):
    def __init__(self, caster_id=None, component_name=None, location_id=None, component_type=None, effect=None,
                 component_layer=None, layer_order=None, text_layer_content=None, image_layer_content=None,
                 caption_layer_content=None, html_layer_content=None):
        self.caster_id = caster_id      # type: str
        self.component_name = component_name  # type: str
        self.location_id = location_id  # type: str
        self.component_type = component_type  # type: str
        self.effect = effect            # type: str
        self.component_layer = component_layer  # type: str
        self.layer_order = layer_order  # type: str
        self.text_layer_content = text_layer_content  # type: str
        self.image_layer_content = image_layer_content  # type: str
        self.caption_layer_content = caption_layer_content  # type: str
        self.html_layer_content = html_layer_content  # type: str

    def validate(self):
        self.validate_required(self.caster_id, 'caster_id')
        self.validate_required(self.location_id, 'location_id')
        self.validate_required(self.component_type, 'component_type')
        self.validate_required(self.component_layer, 'component_layer')

    def to_map(self):
        result = {}
        result['CasterId'] = self.caster_id
        result['ComponentName'] = self.component_name
        result['LocationId'] = self.location_id
        result['ComponentType'] = self.component_type
        result['Effect'] = self.effect
        result['ComponentLayer'] = self.component_layer
        result['LayerOrder'] = self.layer_order
        result['TextLayerContent'] = self.text_layer_content
        result['ImageLayerContent'] = self.image_layer_content
        result['CaptionLayerContent'] = self.caption_layer_content
        result['HtmlLayerContent'] = self.html_layer_content
        return result

    def from_map(self, map={}):
        self.caster_id = map.get('CasterId')
        self.component_name = map.get('ComponentName')
        self.location_id = map.get('LocationId')
        self.component_type = map.get('ComponentType')
        self.effect = map.get('Effect')
        self.component_layer = map.get('ComponentLayer')
        self.layer_order = map.get('LayerOrder')
        self.text_layer_content = map.get('TextLayerContent')
        self.image_layer_content = map.get('ImageLayerContent')
        self.caption_layer_content = map.get('CaptionLayerContent')
        self.html_layer_content = map.get('HtmlLayerContent')
        return self


class AddCasterComponentResponse(TeaModel):
    def __init__(self, request_id=None, component_id=None):
        self.request_id = request_id    # type: str
        self.component_id = component_id  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.component_id, 'component_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['ComponentId'] = self.component_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.component_id = map.get('ComponentId')
        return self


class StopCasterRequest(TeaModel):
    def __init__(self, caster_id=None):
        self.caster_id = caster_id      # type: str

    def validate(self):
        self.validate_required(self.caster_id, 'caster_id')

    def to_map(self):
        result = {}
        result['CasterId'] = self.caster_id
        return result

    def from_map(self, map={}):
        self.caster_id = map.get('CasterId')
        return self


class StopCasterResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class StartCasterRequest(TeaModel):
    def __init__(self, caster_id=None):
        self.caster_id = caster_id      # type: str

    def validate(self):
        self.validate_required(self.caster_id, 'caster_id')

    def to_map(self):
        result = {}
        result['CasterId'] = self.caster_id
        return result

    def from_map(self, map={}):
        self.caster_id = map.get('CasterId')
        return self


class StartCasterResponse(TeaModel):
    def __init__(self, request_id=None, pvw_scene_infos=None, pgm_scene_infos=None):
        self.request_id = request_id    # type: str
        self.pvw_scene_infos = pvw_scene_infos  # type: StartCasterResponsePvwSceneInfos
        self.pgm_scene_infos = pgm_scene_infos  # type: StartCasterResponsePgmSceneInfos

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.pvw_scene_infos, 'pvw_scene_infos')
        if self.pvw_scene_infos:
            self.pvw_scene_infos.validate()
        self.validate_required(self.pgm_scene_infos, 'pgm_scene_infos')
        if self.pgm_scene_infos:
            self.pgm_scene_infos.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.pvw_scene_infos is not None:
            result['PvwSceneInfos'] = self.pvw_scene_infos.to_map()
        else:
            result['PvwSceneInfos'] = None
        if self.pgm_scene_infos is not None:
            result['PgmSceneInfos'] = self.pgm_scene_infos.to_map()
        else:
            result['PgmSceneInfos'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('PvwSceneInfos') is not None:
            temp_model = StartCasterResponsePvwSceneInfos()
            self.pvw_scene_infos = temp_model.from_map(map['PvwSceneInfos'])
        else:
            self.pvw_scene_infos = None
        if map.get('PgmSceneInfos') is not None:
            temp_model = StartCasterResponsePgmSceneInfos()
            self.pgm_scene_infos = temp_model.from_map(map['PgmSceneInfos'])
        else:
            self.pgm_scene_infos = None
        return self


class StartCasterResponsePvwSceneInfosSceneInfo(TeaModel):
    def __init__(self, scene_id=None, stream_url=None):
        self.scene_id = scene_id        # type: str
        self.stream_url = stream_url    # type: str

    def validate(self):
        self.validate_required(self.scene_id, 'scene_id')
        self.validate_required(self.stream_url, 'stream_url')

    def to_map(self):
        result = {}
        result['SceneId'] = self.scene_id
        result['StreamUrl'] = self.stream_url
        return result

    def from_map(self, map={}):
        self.scene_id = map.get('SceneId')
        self.stream_url = map.get('StreamUrl')
        return self


class StartCasterResponsePvwSceneInfos(TeaModel):
    def __init__(self, scene_info=None):
        self.scene_info = scene_info    # type: List[StartCasterResponsePvwSceneInfosSceneInfo]

    def validate(self):
        self.validate_required(self.scene_info, 'scene_info')
        if self.scene_info:
            for k in self.scene_info:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['SceneInfo'] = []
        if self.scene_info is not None:
            for k in self.scene_info:
                result['SceneInfo'].append(k.to_map() if k else None)
        else:
            result['SceneInfo'] = None
        return result

    def from_map(self, map={}):
        self.scene_info = []
        if map.get('SceneInfo') is not None:
            for k in map.get('SceneInfo'):
                temp_model = StartCasterResponsePvwSceneInfosSceneInfo()
                self.scene_info.append(temp_model.from_map(k))
        else:
            self.scene_info = None
        return self


class StartCasterResponsePgmSceneInfosSceneInfoStreamInfosStreamInfo(TeaModel):
    def __init__(self, transcode_config=None, video_format=None, output_stream_url=None):
        self.transcode_config = transcode_config  # type: str
        self.video_format = video_format  # type: str
        self.output_stream_url = output_stream_url  # type: str

    def validate(self):
        self.validate_required(self.transcode_config, 'transcode_config')
        self.validate_required(self.video_format, 'video_format')
        self.validate_required(self.output_stream_url, 'output_stream_url')

    def to_map(self):
        result = {}
        result['TranscodeConfig'] = self.transcode_config
        result['VideoFormat'] = self.video_format
        result['OutputStreamUrl'] = self.output_stream_url
        return result

    def from_map(self, map={}):
        self.transcode_config = map.get('TranscodeConfig')
        self.video_format = map.get('VideoFormat')
        self.output_stream_url = map.get('OutputStreamUrl')
        return self


class StartCasterResponsePgmSceneInfosSceneInfoStreamInfos(TeaModel):
    def __init__(self, stream_info=None):
        self.stream_info = stream_info  # type: List[StartCasterResponsePgmSceneInfosSceneInfoStreamInfosStreamInfo]

    def validate(self):
        self.validate_required(self.stream_info, 'stream_info')
        if self.stream_info:
            for k in self.stream_info:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['StreamInfo'] = []
        if self.stream_info is not None:
            for k in self.stream_info:
                result['StreamInfo'].append(k.to_map() if k else None)
        else:
            result['StreamInfo'] = None
        return result

    def from_map(self, map={}):
        self.stream_info = []
        if map.get('StreamInfo') is not None:
            for k in map.get('StreamInfo'):
                temp_model = StartCasterResponsePgmSceneInfosSceneInfoStreamInfosStreamInfo()
                self.stream_info.append(temp_model.from_map(k))
        else:
            self.stream_info = None
        return self


class StartCasterResponsePgmSceneInfosSceneInfo(TeaModel):
    def __init__(self, scene_id=None, stream_url=None, stream_infos=None):
        self.scene_id = scene_id        # type: str
        self.stream_url = stream_url    # type: str
        self.stream_infos = stream_infos  # type: StartCasterResponsePgmSceneInfosSceneInfoStreamInfos

    def validate(self):
        self.validate_required(self.scene_id, 'scene_id')
        self.validate_required(self.stream_url, 'stream_url')
        self.validate_required(self.stream_infos, 'stream_infos')
        if self.stream_infos:
            self.stream_infos.validate()

    def to_map(self):
        result = {}
        result['SceneId'] = self.scene_id
        result['StreamUrl'] = self.stream_url
        if self.stream_infos is not None:
            result['StreamInfos'] = self.stream_infos.to_map()
        else:
            result['StreamInfos'] = None
        return result

    def from_map(self, map={}):
        self.scene_id = map.get('SceneId')
        self.stream_url = map.get('StreamUrl')
        if map.get('StreamInfos') is not None:
            temp_model = StartCasterResponsePgmSceneInfosSceneInfoStreamInfos()
            self.stream_infos = temp_model.from_map(map['StreamInfos'])
        else:
            self.stream_infos = None
        return self


class StartCasterResponsePgmSceneInfos(TeaModel):
    def __init__(self, scene_info=None):
        self.scene_info = scene_info    # type: List[StartCasterResponsePgmSceneInfosSceneInfo]

    def validate(self):
        self.validate_required(self.scene_info, 'scene_info')
        if self.scene_info:
            for k in self.scene_info:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['SceneInfo'] = []
        if self.scene_info is not None:
            for k in self.scene_info:
                result['SceneInfo'].append(k.to_map() if k else None)
        else:
            result['SceneInfo'] = None
        return result

    def from_map(self, map={}):
        self.scene_info = []
        if map.get('SceneInfo') is not None:
            for k in map.get('SceneInfo'):
                temp_model = StartCasterResponsePgmSceneInfosSceneInfo()
                self.scene_info.append(temp_model.from_map(k))
        else:
            self.scene_info = None
        return self


class DescribeLiveStreamHistoryUserNumRequest(TeaModel):
    def __init__(self, security_token=None, domain_name=None, app_name=None, stream_name=None, start_time=None,
                 end_time=None):
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str
        self.stream_name = stream_name  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.app_name, 'app_name')
        self.validate_required(self.stream_name, 'stream_name')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        result['StreamName'] = self.stream_name
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        self.stream_name = map.get('StreamName')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        return self


class DescribeLiveStreamHistoryUserNumResponse(TeaModel):
    def __init__(self, request_id=None, live_stream_user_num_infos=None):
        self.request_id = request_id    # type: str
        self.live_stream_user_num_infos = live_stream_user_num_infos  # type: DescribeLiveStreamHistoryUserNumResponseLiveStreamUserNumInfos

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.live_stream_user_num_infos, 'live_stream_user_num_infos')
        if self.live_stream_user_num_infos:
            self.live_stream_user_num_infos.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.live_stream_user_num_infos is not None:
            result['LiveStreamUserNumInfos'] = self.live_stream_user_num_infos.to_map()
        else:
            result['LiveStreamUserNumInfos'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('LiveStreamUserNumInfos') is not None:
            temp_model = DescribeLiveStreamHistoryUserNumResponseLiveStreamUserNumInfos()
            self.live_stream_user_num_infos = temp_model.from_map(map['LiveStreamUserNumInfos'])
        else:
            self.live_stream_user_num_infos = None
        return self


class DescribeLiveStreamHistoryUserNumResponseLiveStreamUserNumInfosLiveStreamUserNumInfo(TeaModel):
    def __init__(self, stream_time=None, user_num=None):
        self.stream_time = stream_time  # type: str
        self.user_num = user_num        # type: str

    def validate(self):
        self.validate_required(self.stream_time, 'stream_time')
        self.validate_required(self.user_num, 'user_num')

    def to_map(self):
        result = {}
        result['StreamTime'] = self.stream_time
        result['UserNum'] = self.user_num
        return result

    def from_map(self, map={}):
        self.stream_time = map.get('StreamTime')
        self.user_num = map.get('UserNum')
        return self


class DescribeLiveStreamHistoryUserNumResponseLiveStreamUserNumInfos(TeaModel):
    def __init__(self, live_stream_user_num_info=None):
        self.live_stream_user_num_info = live_stream_user_num_info  # type: List[DescribeLiveStreamHistoryUserNumResponseLiveStreamUserNumInfosLiveStreamUserNumInfo]

    def validate(self):
        self.validate_required(self.live_stream_user_num_info, 'live_stream_user_num_info')
        if self.live_stream_user_num_info:
            for k in self.live_stream_user_num_info:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['LiveStreamUserNumInfo'] = []
        if self.live_stream_user_num_info is not None:
            for k in self.live_stream_user_num_info:
                result['LiveStreamUserNumInfo'].append(k.to_map() if k else None)
        else:
            result['LiveStreamUserNumInfo'] = None
        return result

    def from_map(self, map={}):
        self.live_stream_user_num_info = []
        if map.get('LiveStreamUserNumInfo') is not None:
            for k in map.get('LiveStreamUserNumInfo'):
                temp_model = DescribeLiveStreamHistoryUserNumResponseLiveStreamUserNumInfosLiveStreamUserNumInfo()
                self.live_stream_user_num_info.append(temp_model.from_map(k))
        else:
            self.live_stream_user_num_info = None
        return self


class UpdateCasterSceneConfigRequest(TeaModel):
    def __init__(self, caster_id=None, scene_id=None, layout_id=None, component_id=None):
        self.caster_id = caster_id      # type: str
        self.scene_id = scene_id        # type: str
        self.layout_id = layout_id      # type: str
        self.component_id = component_id  # type: List[str]

    def validate(self):
        self.validate_required(self.caster_id, 'caster_id')
        self.validate_required(self.scene_id, 'scene_id')
        self.validate_required(self.layout_id, 'layout_id')

    def to_map(self):
        result = {}
        result['CasterId'] = self.caster_id
        result['SceneId'] = self.scene_id
        result['LayoutId'] = self.layout_id
        result['ComponentId'] = self.component_id
        return result

    def from_map(self, map={}):
        self.caster_id = map.get('CasterId')
        self.scene_id = map.get('SceneId')
        self.layout_id = map.get('LayoutId')
        self.component_id = map.get('ComponentId')
        return self


class UpdateCasterSceneConfigResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class StopCasterSceneRequest(TeaModel):
    def __init__(self, caster_id=None, scene_id=None):
        self.caster_id = caster_id      # type: str
        self.scene_id = scene_id        # type: str

    def validate(self):
        self.validate_required(self.caster_id, 'caster_id')
        self.validate_required(self.scene_id, 'scene_id')

    def to_map(self):
        result = {}
        result['CasterId'] = self.caster_id
        result['SceneId'] = self.scene_id
        return result

    def from_map(self, map={}):
        self.caster_id = map.get('CasterId')
        self.scene_id = map.get('SceneId')
        return self


class StopCasterSceneResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class StartCasterSceneRequest(TeaModel):
    def __init__(self, caster_id=None, scene_id=None):
        self.caster_id = caster_id      # type: str
        self.scene_id = scene_id        # type: str

    def validate(self):
        self.validate_required(self.caster_id, 'caster_id')
        self.validate_required(self.scene_id, 'scene_id')

    def to_map(self):
        result = {}
        result['CasterId'] = self.caster_id
        result['SceneId'] = self.scene_id
        return result

    def from_map(self, map={}):
        self.caster_id = map.get('CasterId')
        self.scene_id = map.get('SceneId')
        return self


class StartCasterSceneResponse(TeaModel):
    def __init__(self, request_id=None, stream_url=None):
        self.request_id = request_id    # type: str
        self.stream_url = stream_url    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.stream_url, 'stream_url')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['StreamUrl'] = self.stream_url
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.stream_url = map.get('StreamUrl')
        return self


class SetCasterSceneConfigRequest(TeaModel):
    def __init__(self, caster_id=None, scene_id=None, layout_id=None, component_id=None):
        self.caster_id = caster_id      # type: str
        self.scene_id = scene_id        # type: str
        self.layout_id = layout_id      # type: str
        self.component_id = component_id  # type: List[str]

    def validate(self):
        self.validate_required(self.caster_id, 'caster_id')
        self.validate_required(self.scene_id, 'scene_id')

    def to_map(self):
        result = {}
        result['CasterId'] = self.caster_id
        result['SceneId'] = self.scene_id
        result['LayoutId'] = self.layout_id
        result['ComponentId'] = self.component_id
        return result

    def from_map(self, map={}):
        self.caster_id = map.get('CasterId')
        self.scene_id = map.get('SceneId')
        self.layout_id = map.get('LayoutId')
        self.component_id = map.get('ComponentId')
        return self


class SetCasterSceneConfigResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class SetCasterConfigRequest(TeaModel):
    def __init__(self, caster_id=None, caster_name=None, domain_name=None, transcode_config=None,
                 record_config=None, delay=None, urgent_material_id=None, side_output_url=None, callback_url=None,
                 program_effect=None, program_name=None, channel_enable=None):
        self.caster_id = caster_id      # type: str
        self.caster_name = caster_name  # type: str
        self.domain_name = domain_name  # type: str
        self.transcode_config = transcode_config  # type: str
        self.record_config = record_config  # type: str
        self.delay = delay              # type: float
        self.urgent_material_id = urgent_material_id  # type: str
        self.side_output_url = side_output_url  # type: str
        self.callback_url = callback_url  # type: str
        self.program_effect = program_effect  # type: int
        self.program_name = program_name  # type: str
        self.channel_enable = channel_enable  # type: int

    def validate(self):
        self.validate_required(self.caster_id, 'caster_id')

    def to_map(self):
        result = {}
        result['CasterId'] = self.caster_id
        result['CasterName'] = self.caster_name
        result['DomainName'] = self.domain_name
        result['TranscodeConfig'] = self.transcode_config
        result['RecordConfig'] = self.record_config
        result['Delay'] = self.delay
        result['UrgentMaterialId'] = self.urgent_material_id
        result['SideOutputUrl'] = self.side_output_url
        result['CallbackUrl'] = self.callback_url
        result['ProgramEffect'] = self.program_effect
        result['ProgramName'] = self.program_name
        result['ChannelEnable'] = self.channel_enable
        return result

    def from_map(self, map={}):
        self.caster_id = map.get('CasterId')
        self.caster_name = map.get('CasterName')
        self.domain_name = map.get('DomainName')
        self.transcode_config = map.get('TranscodeConfig')
        self.record_config = map.get('RecordConfig')
        self.delay = map.get('Delay')
        self.urgent_material_id = map.get('UrgentMaterialId')
        self.side_output_url = map.get('SideOutputUrl')
        self.callback_url = map.get('CallbackUrl')
        self.program_effect = map.get('ProgramEffect')
        self.program_name = map.get('ProgramName')
        self.channel_enable = map.get('ChannelEnable')
        return self


class SetCasterConfigResponse(TeaModel):
    def __init__(self, request_id=None, caster_id=None):
        self.request_id = request_id    # type: str
        self.caster_id = caster_id      # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.caster_id, 'caster_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['CasterId'] = self.caster_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.caster_id = map.get('CasterId')
        return self


class ModifyCasterVideoResourceRequest(TeaModel):
    def __init__(self, caster_id=None, resource_id=None, resource_name=None, live_stream_url=None, material_id=None,
                 vod_url=None, begin_offset=None, end_offset=None, repeat_num=None, pts_callback_interval=None):
        self.caster_id = caster_id      # type: str
        self.resource_id = resource_id  # type: str
        self.resource_name = resource_name  # type: str
        self.live_stream_url = live_stream_url  # type: str
        self.material_id = material_id  # type: str
        self.vod_url = vod_url          # type: str
        self.begin_offset = begin_offset  # type: int
        self.end_offset = end_offset    # type: int
        self.repeat_num = repeat_num    # type: int
        self.pts_callback_interval = pts_callback_interval  # type: int

    def validate(self):
        self.validate_required(self.caster_id, 'caster_id')
        self.validate_required(self.resource_id, 'resource_id')

    def to_map(self):
        result = {}
        result['CasterId'] = self.caster_id
        result['ResourceId'] = self.resource_id
        result['ResourceName'] = self.resource_name
        result['LiveStreamUrl'] = self.live_stream_url
        result['MaterialId'] = self.material_id
        result['VodUrl'] = self.vod_url
        result['BeginOffset'] = self.begin_offset
        result['EndOffset'] = self.end_offset
        result['RepeatNum'] = self.repeat_num
        result['PtsCallbackInterval'] = self.pts_callback_interval
        return result

    def from_map(self, map={}):
        self.caster_id = map.get('CasterId')
        self.resource_id = map.get('ResourceId')
        self.resource_name = map.get('ResourceName')
        self.live_stream_url = map.get('LiveStreamUrl')
        self.material_id = map.get('MaterialId')
        self.vod_url = map.get('VodUrl')
        self.begin_offset = map.get('BeginOffset')
        self.end_offset = map.get('EndOffset')
        self.repeat_num = map.get('RepeatNum')
        self.pts_callback_interval = map.get('PtsCallbackInterval')
        return self


class ModifyCasterVideoResourceResponse(TeaModel):
    def __init__(self, request_id=None, caster_id=None, resource_id=None):
        self.request_id = request_id    # type: str
        self.caster_id = caster_id      # type: str
        self.resource_id = resource_id  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.caster_id, 'caster_id')
        self.validate_required(self.resource_id, 'resource_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['CasterId'] = self.caster_id
        result['ResourceId'] = self.resource_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.caster_id = map.get('CasterId')
        self.resource_id = map.get('ResourceId')
        return self


class ModifyCasterLayoutRequest(TeaModel):
    def __init__(self, caster_id=None, layout_id=None, video_layer=None, audio_layer=None, blend_list=None,
                 mix_list=None):
        self.caster_id = caster_id      # type: str
        self.layout_id = layout_id      # type: str
        self.video_layer = video_layer  # type: List[ModifyCasterLayoutRequestVideoLayer]
        self.audio_layer = audio_layer  # type: List[ModifyCasterLayoutRequestAudioLayer]
        self.blend_list = blend_list    # type: List[str]
        self.mix_list = mix_list        # type: List[str]

    def validate(self):
        self.validate_required(self.caster_id, 'caster_id')
        self.validate_required(self.layout_id, 'layout_id')
        self.validate_required(self.video_layer, 'video_layer')
        if self.video_layer:
            for k in self.video_layer:
                if k:
                    k.validate()
        self.validate_required(self.audio_layer, 'audio_layer')
        if self.audio_layer:
            for k in self.audio_layer:
                if k:
                    k.validate()
        self.validate_required(self.blend_list, 'blend_list')
        self.validate_required(self.mix_list, 'mix_list')

    def to_map(self):
        result = {}
        result['CasterId'] = self.caster_id
        result['LayoutId'] = self.layout_id
        result['VideoLayer'] = []
        if self.video_layer is not None:
            for k in self.video_layer:
                result['VideoLayer'].append(k.to_map() if k else None)
        else:
            result['VideoLayer'] = None
        result['AudioLayer'] = []
        if self.audio_layer is not None:
            for k in self.audio_layer:
                result['AudioLayer'].append(k.to_map() if k else None)
        else:
            result['AudioLayer'] = None
        result['BlendList'] = self.blend_list
        result['MixList'] = self.mix_list
        return result

    def from_map(self, map={}):
        self.caster_id = map.get('CasterId')
        self.layout_id = map.get('LayoutId')
        self.video_layer = []
        if map.get('VideoLayer') is not None:
            for k in map.get('VideoLayer'):
                temp_model = ModifyCasterLayoutRequestVideoLayer()
                self.video_layer.append(temp_model.from_map(k))
        else:
            self.video_layer = None
        self.audio_layer = []
        if map.get('AudioLayer') is not None:
            for k in map.get('AudioLayer'):
                temp_model = ModifyCasterLayoutRequestAudioLayer()
                self.audio_layer.append(temp_model.from_map(k))
        else:
            self.audio_layer = None
        self.blend_list = map.get('BlendList')
        self.mix_list = map.get('MixList')
        return self


class ModifyCasterLayoutRequestVideoLayer(TeaModel):
    def __init__(self, fill_mode=None, height_normalized=None, width_normalized=None, position_refer=None,
                 position_normalized=None, fixed_delay_duration=None):
        self.fill_mode = fill_mode      # type: str
        self.height_normalized = height_normalized  # type: float
        self.width_normalized = width_normalized  # type: float
        self.position_refer = position_refer  # type: str
        self.position_normalized = position_normalized  # type: List[float]
        self.fixed_delay_duration = fixed_delay_duration  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['FillMode'] = self.fill_mode
        result['HeightNormalized'] = self.height_normalized
        result['WidthNormalized'] = self.width_normalized
        result['PositionRefer'] = self.position_refer
        result['PositionNormalized'] = self.position_normalized
        result['FixedDelayDuration'] = self.fixed_delay_duration
        return result

    def from_map(self, map={}):
        self.fill_mode = map.get('FillMode')
        self.height_normalized = map.get('HeightNormalized')
        self.width_normalized = map.get('WidthNormalized')
        self.position_refer = map.get('PositionRefer')
        self.position_normalized = map.get('PositionNormalized')
        self.fixed_delay_duration = map.get('FixedDelayDuration')
        return self


class ModifyCasterLayoutRequestAudioLayer(TeaModel):
    def __init__(self, volume_rate=None, valid_channel=None, fixed_delay_duration=None):
        self.volume_rate = volume_rate  # type: float
        self.valid_channel = valid_channel  # type: str
        self.fixed_delay_duration = fixed_delay_duration  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['VolumeRate'] = self.volume_rate
        result['ValidChannel'] = self.valid_channel
        result['FixedDelayDuration'] = self.fixed_delay_duration
        return result

    def from_map(self, map={}):
        self.volume_rate = map.get('VolumeRate')
        self.valid_channel = map.get('ValidChannel')
        self.fixed_delay_duration = map.get('FixedDelayDuration')
        return self


class ModifyCasterLayoutResponse(TeaModel):
    def __init__(self, request_id=None, layout_id=None):
        self.request_id = request_id    # type: str
        self.layout_id = layout_id      # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.layout_id, 'layout_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['LayoutId'] = self.layout_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.layout_id = map.get('LayoutId')
        return self


class EffectCasterVideoResourceRequest(TeaModel):
    def __init__(self, caster_id=None, scene_id=None, resource_id=None):
        self.caster_id = caster_id      # type: str
        self.scene_id = scene_id        # type: str
        self.resource_id = resource_id  # type: str

    def validate(self):
        self.validate_required(self.caster_id, 'caster_id')
        self.validate_required(self.scene_id, 'scene_id')
        self.validate_required(self.resource_id, 'resource_id')

    def to_map(self):
        result = {}
        result['CasterId'] = self.caster_id
        result['SceneId'] = self.scene_id
        result['ResourceId'] = self.resource_id
        return result

    def from_map(self, map={}):
        self.caster_id = map.get('CasterId')
        self.scene_id = map.get('SceneId')
        self.resource_id = map.get('ResourceId')
        return self


class EffectCasterVideoResourceResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class EffectCasterUrgentRequest(TeaModel):
    def __init__(self, caster_id=None, scene_id=None):
        self.caster_id = caster_id      # type: str
        self.scene_id = scene_id        # type: str

    def validate(self):
        self.validate_required(self.caster_id, 'caster_id')
        self.validate_required(self.scene_id, 'scene_id')

    def to_map(self):
        result = {}
        result['CasterId'] = self.caster_id
        result['SceneId'] = self.scene_id
        return result

    def from_map(self, map={}):
        self.caster_id = map.get('CasterId')
        self.scene_id = map.get('SceneId')
        return self


class EffectCasterUrgentResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeCasterVideoResourcesRequest(TeaModel):
    def __init__(self, caster_id=None):
        self.caster_id = caster_id      # type: str

    def validate(self):
        self.validate_required(self.caster_id, 'caster_id')

    def to_map(self):
        result = {}
        result['CasterId'] = self.caster_id
        return result

    def from_map(self, map={}):
        self.caster_id = map.get('CasterId')
        return self


class DescribeCasterVideoResourcesResponse(TeaModel):
    def __init__(self, request_id=None, total=None, video_resources=None):
        self.request_id = request_id    # type: str
        self.total = total              # type: int
        self.video_resources = video_resources  # type: DescribeCasterVideoResourcesResponseVideoResources

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total, 'total')
        self.validate_required(self.video_resources, 'video_resources')
        if self.video_resources:
            self.video_resources.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Total'] = self.total
        if self.video_resources is not None:
            result['VideoResources'] = self.video_resources.to_map()
        else:
            result['VideoResources'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total = map.get('Total')
        if map.get('VideoResources') is not None:
            temp_model = DescribeCasterVideoResourcesResponseVideoResources()
            self.video_resources = temp_model.from_map(map['VideoResources'])
        else:
            self.video_resources = None
        return self


class DescribeCasterVideoResourcesResponseVideoResourcesVideoResource(TeaModel):
    def __init__(self, material_id=None, resource_id=None, resource_name=None, location_id=None,
                 live_stream_url=None, repeat_num=None, vod_url=None, begin_offset=None, end_offset=None,
                 pts_callback_interval=None):
        self.material_id = material_id  # type: str
        self.resource_id = resource_id  # type: str
        self.resource_name = resource_name  # type: str
        self.location_id = location_id  # type: str
        self.live_stream_url = live_stream_url  # type: str
        self.repeat_num = repeat_num    # type: int
        self.vod_url = vod_url          # type: str
        self.begin_offset = begin_offset  # type: int
        self.end_offset = end_offset    # type: int
        self.pts_callback_interval = pts_callback_interval  # type: int

    def validate(self):
        self.validate_required(self.material_id, 'material_id')
        self.validate_required(self.resource_id, 'resource_id')
        self.validate_required(self.resource_name, 'resource_name')
        self.validate_required(self.location_id, 'location_id')
        self.validate_required(self.live_stream_url, 'live_stream_url')
        self.validate_required(self.repeat_num, 'repeat_num')
        self.validate_required(self.vod_url, 'vod_url')
        self.validate_required(self.begin_offset, 'begin_offset')
        self.validate_required(self.end_offset, 'end_offset')
        self.validate_required(self.pts_callback_interval, 'pts_callback_interval')

    def to_map(self):
        result = {}
        result['MaterialId'] = self.material_id
        result['ResourceId'] = self.resource_id
        result['ResourceName'] = self.resource_name
        result['LocationId'] = self.location_id
        result['LiveStreamUrl'] = self.live_stream_url
        result['RepeatNum'] = self.repeat_num
        result['VodUrl'] = self.vod_url
        result['BeginOffset'] = self.begin_offset
        result['EndOffset'] = self.end_offset
        result['PtsCallbackInterval'] = self.pts_callback_interval
        return result

    def from_map(self, map={}):
        self.material_id = map.get('MaterialId')
        self.resource_id = map.get('ResourceId')
        self.resource_name = map.get('ResourceName')
        self.location_id = map.get('LocationId')
        self.live_stream_url = map.get('LiveStreamUrl')
        self.repeat_num = map.get('RepeatNum')
        self.vod_url = map.get('VodUrl')
        self.begin_offset = map.get('BeginOffset')
        self.end_offset = map.get('EndOffset')
        self.pts_callback_interval = map.get('PtsCallbackInterval')
        return self


class DescribeCasterVideoResourcesResponseVideoResources(TeaModel):
    def __init__(self, video_resource=None):
        self.video_resource = video_resource  # type: List[DescribeCasterVideoResourcesResponseVideoResourcesVideoResource]

    def validate(self):
        self.validate_required(self.video_resource, 'video_resource')
        if self.video_resource:
            for k in self.video_resource:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['VideoResource'] = []
        if self.video_resource is not None:
            for k in self.video_resource:
                result['VideoResource'].append(k.to_map() if k else None)
        else:
            result['VideoResource'] = None
        return result

    def from_map(self, map={}):
        self.video_resource = []
        if map.get('VideoResource') is not None:
            for k in map.get('VideoResource'):
                temp_model = DescribeCasterVideoResourcesResponseVideoResourcesVideoResource()
                self.video_resource.append(temp_model.from_map(k))
        else:
            self.video_resource = None
        return self


class DescribeCasterStreamUrlRequest(TeaModel):
    def __init__(self, caster_id=None):
        self.caster_id = caster_id      # type: str

    def validate(self):
        self.validate_required(self.caster_id, 'caster_id')

    def to_map(self):
        result = {}
        result['CasterId'] = self.caster_id
        return result

    def from_map(self, map={}):
        self.caster_id = map.get('CasterId')
        return self


class DescribeCasterStreamUrlResponse(TeaModel):
    def __init__(self, request_id=None, caster_id=None, total=None, caster_streams=None):
        self.request_id = request_id    # type: str
        self.caster_id = caster_id      # type: str
        self.total = total              # type: int
        self.caster_streams = caster_streams  # type: DescribeCasterStreamUrlResponseCasterStreams

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.caster_id, 'caster_id')
        self.validate_required(self.total, 'total')
        self.validate_required(self.caster_streams, 'caster_streams')
        if self.caster_streams:
            self.caster_streams.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['CasterId'] = self.caster_id
        result['Total'] = self.total
        if self.caster_streams is not None:
            result['CasterStreams'] = self.caster_streams.to_map()
        else:
            result['CasterStreams'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.caster_id = map.get('CasterId')
        self.total = map.get('Total')
        if map.get('CasterStreams') is not None:
            temp_model = DescribeCasterStreamUrlResponseCasterStreams()
            self.caster_streams = temp_model.from_map(map['CasterStreams'])
        else:
            self.caster_streams = None
        return self


class DescribeCasterStreamUrlResponseCasterStreamsCasterStreamStreamInfosStreamInfo(TeaModel):
    def __init__(self, transcode_config=None, video_format=None, output_stream_url=None):
        self.transcode_config = transcode_config  # type: str
        self.video_format = video_format  # type: str
        self.output_stream_url = output_stream_url  # type: str

    def validate(self):
        self.validate_required(self.transcode_config, 'transcode_config')
        self.validate_required(self.video_format, 'video_format')
        self.validate_required(self.output_stream_url, 'output_stream_url')

    def to_map(self):
        result = {}
        result['TranscodeConfig'] = self.transcode_config
        result['VideoFormat'] = self.video_format
        result['OutputStreamUrl'] = self.output_stream_url
        return result

    def from_map(self, map={}):
        self.transcode_config = map.get('TranscodeConfig')
        self.video_format = map.get('VideoFormat')
        self.output_stream_url = map.get('OutputStreamUrl')
        return self


class DescribeCasterStreamUrlResponseCasterStreamsCasterStreamStreamInfos(TeaModel):
    def __init__(self, stream_info=None):
        self.stream_info = stream_info  # type: List[DescribeCasterStreamUrlResponseCasterStreamsCasterStreamStreamInfosStreamInfo]

    def validate(self):
        self.validate_required(self.stream_info, 'stream_info')
        if self.stream_info:
            for k in self.stream_info:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['StreamInfo'] = []
        if self.stream_info is not None:
            for k in self.stream_info:
                result['StreamInfo'].append(k.to_map() if k else None)
        else:
            result['StreamInfo'] = None
        return result

    def from_map(self, map={}):
        self.stream_info = []
        if map.get('StreamInfo') is not None:
            for k in map.get('StreamInfo'):
                temp_model = DescribeCasterStreamUrlResponseCasterStreamsCasterStreamStreamInfosStreamInfo()
                self.stream_info.append(temp_model.from_map(k))
        else:
            self.stream_info = None
        return self


class DescribeCasterStreamUrlResponseCasterStreamsCasterStream(TeaModel):
    def __init__(self, scene_id=None, stream_url=None, rtmp_url=None, output_type=None, stream_infos=None):
        self.scene_id = scene_id        # type: str
        self.stream_url = stream_url    # type: str
        self.rtmp_url = rtmp_url        # type: str
        self.output_type = output_type  # type: int
        self.stream_infos = stream_infos  # type: DescribeCasterStreamUrlResponseCasterStreamsCasterStreamStreamInfos

    def validate(self):
        self.validate_required(self.scene_id, 'scene_id')
        self.validate_required(self.stream_url, 'stream_url')
        self.validate_required(self.rtmp_url, 'rtmp_url')
        self.validate_required(self.output_type, 'output_type')
        self.validate_required(self.stream_infos, 'stream_infos')
        if self.stream_infos:
            self.stream_infos.validate()

    def to_map(self):
        result = {}
        result['SceneId'] = self.scene_id
        result['StreamUrl'] = self.stream_url
        result['RtmpUrl'] = self.rtmp_url
        result['OutputType'] = self.output_type
        if self.stream_infos is not None:
            result['StreamInfos'] = self.stream_infos.to_map()
        else:
            result['StreamInfos'] = None
        return result

    def from_map(self, map={}):
        self.scene_id = map.get('SceneId')
        self.stream_url = map.get('StreamUrl')
        self.rtmp_url = map.get('RtmpUrl')
        self.output_type = map.get('OutputType')
        if map.get('StreamInfos') is not None:
            temp_model = DescribeCasterStreamUrlResponseCasterStreamsCasterStreamStreamInfos()
            self.stream_infos = temp_model.from_map(map['StreamInfos'])
        else:
            self.stream_infos = None
        return self


class DescribeCasterStreamUrlResponseCasterStreams(TeaModel):
    def __init__(self, caster_stream=None):
        self.caster_stream = caster_stream  # type: List[DescribeCasterStreamUrlResponseCasterStreamsCasterStream]

    def validate(self):
        self.validate_required(self.caster_stream, 'caster_stream')
        if self.caster_stream:
            for k in self.caster_stream:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['CasterStream'] = []
        if self.caster_stream is not None:
            for k in self.caster_stream:
                result['CasterStream'].append(k.to_map() if k else None)
        else:
            result['CasterStream'] = None
        return result

    def from_map(self, map={}):
        self.caster_stream = []
        if map.get('CasterStream') is not None:
            for k in map.get('CasterStream'):
                temp_model = DescribeCasterStreamUrlResponseCasterStreamsCasterStream()
                self.caster_stream.append(temp_model.from_map(k))
        else:
            self.caster_stream = None
        return self


class DescribeCasterScenesRequest(TeaModel):
    def __init__(self, caster_id=None, scene_id=None):
        self.caster_id = caster_id      # type: str
        self.scene_id = scene_id        # type: str

    def validate(self):
        self.validate_required(self.caster_id, 'caster_id')

    def to_map(self):
        result = {}
        result['CasterId'] = self.caster_id
        result['SceneId'] = self.scene_id
        return result

    def from_map(self, map={}):
        self.caster_id = map.get('CasterId')
        self.scene_id = map.get('SceneId')
        return self


class DescribeCasterScenesResponse(TeaModel):
    def __init__(self, request_id=None, total=None, scene_list=None):
        self.request_id = request_id    # type: str
        self.total = total              # type: int
        self.scene_list = scene_list    # type: DescribeCasterScenesResponseSceneList

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total, 'total')
        self.validate_required(self.scene_list, 'scene_list')
        if self.scene_list:
            self.scene_list.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Total'] = self.total
        if self.scene_list is not None:
            result['SceneList'] = self.scene_list.to_map()
        else:
            result['SceneList'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total = map.get('Total')
        if map.get('SceneList') is not None:
            temp_model = DescribeCasterScenesResponseSceneList()
            self.scene_list = temp_model.from_map(map['SceneList'])
        else:
            self.scene_list = None
        return self


class DescribeCasterScenesResponseSceneListSceneStreamInfosStreamInfo(TeaModel):
    def __init__(self, transcode_config=None, video_format=None, output_stream_url=None):
        self.transcode_config = transcode_config  # type: str
        self.video_format = video_format  # type: str
        self.output_stream_url = output_stream_url  # type: str

    def validate(self):
        self.validate_required(self.transcode_config, 'transcode_config')
        self.validate_required(self.video_format, 'video_format')
        self.validate_required(self.output_stream_url, 'output_stream_url')

    def to_map(self):
        result = {}
        result['TranscodeConfig'] = self.transcode_config
        result['VideoFormat'] = self.video_format
        result['OutputStreamUrl'] = self.output_stream_url
        return result

    def from_map(self, map={}):
        self.transcode_config = map.get('TranscodeConfig')
        self.video_format = map.get('VideoFormat')
        self.output_stream_url = map.get('OutputStreamUrl')
        return self


class DescribeCasterScenesResponseSceneListSceneStreamInfos(TeaModel):
    def __init__(self, stream_info=None):
        self.stream_info = stream_info  # type: List[DescribeCasterScenesResponseSceneListSceneStreamInfosStreamInfo]

    def validate(self):
        self.validate_required(self.stream_info, 'stream_info')
        if self.stream_info:
            for k in self.stream_info:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['StreamInfo'] = []
        if self.stream_info is not None:
            for k in self.stream_info:
                result['StreamInfo'].append(k.to_map() if k else None)
        else:
            result['StreamInfo'] = None
        return result

    def from_map(self, map={}):
        self.stream_info = []
        if map.get('StreamInfo') is not None:
            for k in map.get('StreamInfo'):
                temp_model = DescribeCasterScenesResponseSceneListSceneStreamInfosStreamInfo()
                self.stream_info.append(temp_model.from_map(k))
        else:
            self.stream_info = None
        return self


class DescribeCasterScenesResponseSceneListSceneComponentIds(TeaModel):
    def __init__(self, component_id=None):
        # componentId
        self.component_id = component_id  # type: List[str]

    def validate(self):
        self.validate_required(self.component_id, 'component_id')

    def to_map(self):
        result = {}
        result['componentId'] = self.component_id
        return result

    def from_map(self, map={}):
        self.component_id = map.get('componentId')
        return self


class DescribeCasterScenesResponseSceneListScene(TeaModel):
    def __init__(self, scene_id=None, scene_name=None, output_type=None, layout_id=None, stream_url=None,
                 status=None, stream_infos=None, component_ids=None):
        self.scene_id = scene_id        # type: str
        self.scene_name = scene_name    # type: str
        self.output_type = output_type  # type: str
        self.layout_id = layout_id      # type: str
        self.stream_url = stream_url    # type: str
        self.status = status            # type: int
        self.stream_infos = stream_infos  # type: DescribeCasterScenesResponseSceneListSceneStreamInfos
        self.component_ids = component_ids  # type: DescribeCasterScenesResponseSceneListSceneComponentIds

    def validate(self):
        self.validate_required(self.scene_id, 'scene_id')
        self.validate_required(self.scene_name, 'scene_name')
        self.validate_required(self.output_type, 'output_type')
        self.validate_required(self.layout_id, 'layout_id')
        self.validate_required(self.stream_url, 'stream_url')
        self.validate_required(self.status, 'status')
        self.validate_required(self.stream_infos, 'stream_infos')
        if self.stream_infos:
            self.stream_infos.validate()
        self.validate_required(self.component_ids, 'component_ids')
        if self.component_ids:
            self.component_ids.validate()

    def to_map(self):
        result = {}
        result['SceneId'] = self.scene_id
        result['SceneName'] = self.scene_name
        result['OutputType'] = self.output_type
        result['LayoutId'] = self.layout_id
        result['StreamUrl'] = self.stream_url
        result['Status'] = self.status
        if self.stream_infos is not None:
            result['StreamInfos'] = self.stream_infos.to_map()
        else:
            result['StreamInfos'] = None
        if self.component_ids is not None:
            result['ComponentIds'] = self.component_ids.to_map()
        else:
            result['ComponentIds'] = None
        return result

    def from_map(self, map={}):
        self.scene_id = map.get('SceneId')
        self.scene_name = map.get('SceneName')
        self.output_type = map.get('OutputType')
        self.layout_id = map.get('LayoutId')
        self.stream_url = map.get('StreamUrl')
        self.status = map.get('Status')
        if map.get('StreamInfos') is not None:
            temp_model = DescribeCasterScenesResponseSceneListSceneStreamInfos()
            self.stream_infos = temp_model.from_map(map['StreamInfos'])
        else:
            self.stream_infos = None
        if map.get('ComponentIds') is not None:
            temp_model = DescribeCasterScenesResponseSceneListSceneComponentIds()
            self.component_ids = temp_model.from_map(map['ComponentIds'])
        else:
            self.component_ids = None
        return self


class DescribeCasterScenesResponseSceneList(TeaModel):
    def __init__(self, scene=None):
        self.scene = scene              # type: List[DescribeCasterScenesResponseSceneListScene]

    def validate(self):
        self.validate_required(self.scene, 'scene')
        if self.scene:
            for k in self.scene:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Scene'] = []
        if self.scene is not None:
            for k in self.scene:
                result['Scene'].append(k.to_map() if k else None)
        else:
            result['Scene'] = None
        return result

    def from_map(self, map={}):
        self.scene = []
        if map.get('Scene') is not None:
            for k in map.get('Scene'):
                temp_model = DescribeCasterScenesResponseSceneListScene()
                self.scene.append(temp_model.from_map(k))
        else:
            self.scene = None
        return self


class DescribeCastersRequest(TeaModel):
    def __init__(self, caster_id=None, caster_name=None, start_time=None, end_time=None, page_num=None,
                 page_size=None, status=None):
        self.caster_id = caster_id      # type: str
        self.caster_name = caster_name  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int
        self.status = status            # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['CasterId'] = self.caster_id
        result['CasterName'] = self.caster_name
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        result['Status'] = self.status
        return result

    def from_map(self, map={}):
        self.caster_id = map.get('CasterId')
        self.caster_name = map.get('CasterName')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        self.status = map.get('Status')
        return self


class DescribeCastersResponse(TeaModel):
    def __init__(self, request_id=None, total=None, caster_list=None):
        self.request_id = request_id    # type: str
        self.total = total              # type: int
        self.caster_list = caster_list  # type: DescribeCastersResponseCasterList

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total, 'total')
        self.validate_required(self.caster_list, 'caster_list')
        if self.caster_list:
            self.caster_list.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Total'] = self.total
        if self.caster_list is not None:
            result['CasterList'] = self.caster_list.to_map()
        else:
            result['CasterList'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total = map.get('Total')
        if map.get('CasterList') is not None:
            temp_model = DescribeCastersResponseCasterList()
            self.caster_list = temp_model.from_map(map['CasterList'])
        else:
            self.caster_list = None
        return self


class DescribeCastersResponseCasterListCaster(TeaModel):
    def __init__(self, status=None, norm_type=None, caster_id=None, caster_name=None, create_time=None,
                 start_time=None, purchase_time=None, expire_time=None, charge_type=None, caster_template=None,
                 channel_enable=None):
        self.status = status            # type: int
        self.norm_type = norm_type      # type: int
        self.caster_id = caster_id      # type: str
        self.caster_name = caster_name  # type: str
        self.create_time = create_time  # type: str
        self.start_time = start_time    # type: str
        self.purchase_time = purchase_time  # type: str
        self.expire_time = expire_time  # type: str
        self.charge_type = charge_type  # type: str
        self.caster_template = caster_template  # type: str
        self.channel_enable = channel_enable  # type: int

    def validate(self):
        self.validate_required(self.status, 'status')
        self.validate_required(self.norm_type, 'norm_type')
        self.validate_required(self.caster_id, 'caster_id')
        self.validate_required(self.caster_name, 'caster_name')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.purchase_time, 'purchase_time')
        self.validate_required(self.expire_time, 'expire_time')
        self.validate_required(self.charge_type, 'charge_type')
        self.validate_required(self.caster_template, 'caster_template')
        self.validate_required(self.channel_enable, 'channel_enable')

    def to_map(self):
        result = {}
        result['Status'] = self.status
        result['NormType'] = self.norm_type
        result['CasterId'] = self.caster_id
        result['CasterName'] = self.caster_name
        result['CreateTime'] = self.create_time
        result['StartTime'] = self.start_time
        result['PurchaseTime'] = self.purchase_time
        result['ExpireTime'] = self.expire_time
        result['ChargeType'] = self.charge_type
        result['CasterTemplate'] = self.caster_template
        result['ChannelEnable'] = self.channel_enable
        return result

    def from_map(self, map={}):
        self.status = map.get('Status')
        self.norm_type = map.get('NormType')
        self.caster_id = map.get('CasterId')
        self.caster_name = map.get('CasterName')
        self.create_time = map.get('CreateTime')
        self.start_time = map.get('StartTime')
        self.purchase_time = map.get('PurchaseTime')
        self.expire_time = map.get('ExpireTime')
        self.charge_type = map.get('ChargeType')
        self.caster_template = map.get('CasterTemplate')
        self.channel_enable = map.get('ChannelEnable')
        return self


class DescribeCastersResponseCasterList(TeaModel):
    def __init__(self, caster=None):
        self.caster = caster            # type: List[DescribeCastersResponseCasterListCaster]

    def validate(self):
        self.validate_required(self.caster, 'caster')
        if self.caster:
            for k in self.caster:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Caster'] = []
        if self.caster is not None:
            for k in self.caster:
                result['Caster'].append(k.to_map() if k else None)
        else:
            result['Caster'] = None
        return result

    def from_map(self, map={}):
        self.caster = []
        if map.get('Caster') is not None:
            for k in map.get('Caster'):
                temp_model = DescribeCastersResponseCasterListCaster()
                self.caster.append(temp_model.from_map(k))
        else:
            self.caster = None
        return self


class DescribeCasterLayoutsRequest(TeaModel):
    def __init__(self, caster_id=None, layout_id=None):
        self.caster_id = caster_id      # type: str
        self.layout_id = layout_id      # type: str

    def validate(self):
        self.validate_required(self.caster_id, 'caster_id')

    def to_map(self):
        result = {}
        result['CasterId'] = self.caster_id
        result['LayoutId'] = self.layout_id
        return result

    def from_map(self, map={}):
        self.caster_id = map.get('CasterId')
        self.layout_id = map.get('LayoutId')
        return self


class DescribeCasterLayoutsResponse(TeaModel):
    def __init__(self, request_id=None, total=None, layouts=None):
        self.request_id = request_id    # type: str
        self.total = total              # type: int
        self.layouts = layouts          # type: DescribeCasterLayoutsResponseLayouts

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total, 'total')
        self.validate_required(self.layouts, 'layouts')
        if self.layouts:
            self.layouts.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['Total'] = self.total
        if self.layouts is not None:
            result['Layouts'] = self.layouts.to_map()
        else:
            result['Layouts'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total = map.get('Total')
        if map.get('Layouts') is not None:
            temp_model = DescribeCasterLayoutsResponseLayouts()
            self.layouts = temp_model.from_map(map['Layouts'])
        else:
            self.layouts = None
        return self


class DescribeCasterLayoutsResponseLayoutsLayoutVideoLayersVideoLayerPositionNormalizeds(TeaModel):
    def __init__(self, position=None):
        # Position
        self.position = position        # type: List[float]

    def validate(self):
        self.validate_required(self.position, 'position')

    def to_map(self):
        result = {}
        result['Position'] = self.position
        return result

    def from_map(self, map={}):
        self.position = map.get('Position')
        return self


class DescribeCasterLayoutsResponseLayoutsLayoutVideoLayersVideoLayer(TeaModel):
    def __init__(self, fill_mode=None, height_normalized=None, width_normalized=None, position_refer=None,
                 fixed_delay_duration=None, position_normalizeds=None):
        self.fill_mode = fill_mode      # type: str
        self.height_normalized = height_normalized  # type: float
        self.width_normalized = width_normalized  # type: float
        self.position_refer = position_refer  # type: str
        self.fixed_delay_duration = fixed_delay_duration  # type: int
        self.position_normalizeds = position_normalizeds  # type: DescribeCasterLayoutsResponseLayoutsLayoutVideoLayersVideoLayerPositionNormalizeds

    def validate(self):
        self.validate_required(self.fill_mode, 'fill_mode')
        self.validate_required(self.height_normalized, 'height_normalized')
        self.validate_required(self.width_normalized, 'width_normalized')
        self.validate_required(self.position_refer, 'position_refer')
        self.validate_required(self.fixed_delay_duration, 'fixed_delay_duration')
        self.validate_required(self.position_normalizeds, 'position_normalizeds')
        if self.position_normalizeds:
            self.position_normalizeds.validate()

    def to_map(self):
        result = {}
        result['FillMode'] = self.fill_mode
        result['HeightNormalized'] = self.height_normalized
        result['WidthNormalized'] = self.width_normalized
        result['PositionRefer'] = self.position_refer
        result['FixedDelayDuration'] = self.fixed_delay_duration
        if self.position_normalizeds is not None:
            result['PositionNormalizeds'] = self.position_normalizeds.to_map()
        else:
            result['PositionNormalizeds'] = None
        return result

    def from_map(self, map={}):
        self.fill_mode = map.get('FillMode')
        self.height_normalized = map.get('HeightNormalized')
        self.width_normalized = map.get('WidthNormalized')
        self.position_refer = map.get('PositionRefer')
        self.fixed_delay_duration = map.get('FixedDelayDuration')
        if map.get('PositionNormalizeds') is not None:
            temp_model = DescribeCasterLayoutsResponseLayoutsLayoutVideoLayersVideoLayerPositionNormalizeds()
            self.position_normalizeds = temp_model.from_map(map['PositionNormalizeds'])
        else:
            self.position_normalizeds = None
        return self


class DescribeCasterLayoutsResponseLayoutsLayoutVideoLayers(TeaModel):
    def __init__(self, video_layer=None):
        self.video_layer = video_layer  # type: List[DescribeCasterLayoutsResponseLayoutsLayoutVideoLayersVideoLayer]

    def validate(self):
        self.validate_required(self.video_layer, 'video_layer')
        if self.video_layer:
            for k in self.video_layer:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['VideoLayer'] = []
        if self.video_layer is not None:
            for k in self.video_layer:
                result['VideoLayer'].append(k.to_map() if k else None)
        else:
            result['VideoLayer'] = None
        return result

    def from_map(self, map={}):
        self.video_layer = []
        if map.get('VideoLayer') is not None:
            for k in map.get('VideoLayer'):
                temp_model = DescribeCasterLayoutsResponseLayoutsLayoutVideoLayersVideoLayer()
                self.video_layer.append(temp_model.from_map(k))
        else:
            self.video_layer = None
        return self


class DescribeCasterLayoutsResponseLayoutsLayoutAudioLayersAudioLayer(TeaModel):
    def __init__(self, volume_rate=None, valid_channel=None, fixed_delay_duration=None):
        self.volume_rate = volume_rate  # type: float
        self.valid_channel = valid_channel  # type: str
        self.fixed_delay_duration = fixed_delay_duration  # type: int

    def validate(self):
        self.validate_required(self.volume_rate, 'volume_rate')
        self.validate_required(self.valid_channel, 'valid_channel')
        self.validate_required(self.fixed_delay_duration, 'fixed_delay_duration')

    def to_map(self):
        result = {}
        result['VolumeRate'] = self.volume_rate
        result['ValidChannel'] = self.valid_channel
        result['FixedDelayDuration'] = self.fixed_delay_duration
        return result

    def from_map(self, map={}):
        self.volume_rate = map.get('VolumeRate')
        self.valid_channel = map.get('ValidChannel')
        self.fixed_delay_duration = map.get('FixedDelayDuration')
        return self


class DescribeCasterLayoutsResponseLayoutsLayoutAudioLayers(TeaModel):
    def __init__(self, audio_layer=None):
        self.audio_layer = audio_layer  # type: List[DescribeCasterLayoutsResponseLayoutsLayoutAudioLayersAudioLayer]

    def validate(self):
        self.validate_required(self.audio_layer, 'audio_layer')
        if self.audio_layer:
            for k in self.audio_layer:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['AudioLayer'] = []
        if self.audio_layer is not None:
            for k in self.audio_layer:
                result['AudioLayer'].append(k.to_map() if k else None)
        else:
            result['AudioLayer'] = None
        return result

    def from_map(self, map={}):
        self.audio_layer = []
        if map.get('AudioLayer') is not None:
            for k in map.get('AudioLayer'):
                temp_model = DescribeCasterLayoutsResponseLayoutsLayoutAudioLayersAudioLayer()
                self.audio_layer.append(temp_model.from_map(k))
        else:
            self.audio_layer = None
        return self


class DescribeCasterLayoutsResponseLayoutsLayoutBlendList(TeaModel):
    def __init__(self, location_id=None):
        # LocationId
        self.location_id = location_id  # type: List[str]

    def validate(self):
        self.validate_required(self.location_id, 'location_id')

    def to_map(self):
        result = {}
        result['LocationId'] = self.location_id
        return result

    def from_map(self, map={}):
        self.location_id = map.get('LocationId')
        return self


class DescribeCasterLayoutsResponseLayoutsLayoutMixList(TeaModel):
    def __init__(self, location_id=None):
        # LocationId
        self.location_id = location_id  # type: List[str]

    def validate(self):
        self.validate_required(self.location_id, 'location_id')

    def to_map(self):
        result = {}
        result['LocationId'] = self.location_id
        return result

    def from_map(self, map={}):
        self.location_id = map.get('LocationId')
        return self


class DescribeCasterLayoutsResponseLayoutsLayout(TeaModel):
    def __init__(self, layout_id=None, video_layers=None, audio_layers=None, blend_list=None, mix_list=None):
        self.layout_id = layout_id      # type: str
        self.video_layers = video_layers  # type: DescribeCasterLayoutsResponseLayoutsLayoutVideoLayers
        self.audio_layers = audio_layers  # type: DescribeCasterLayoutsResponseLayoutsLayoutAudioLayers
        self.blend_list = blend_list    # type: DescribeCasterLayoutsResponseLayoutsLayoutBlendList
        self.mix_list = mix_list        # type: DescribeCasterLayoutsResponseLayoutsLayoutMixList

    def validate(self):
        self.validate_required(self.layout_id, 'layout_id')
        self.validate_required(self.video_layers, 'video_layers')
        if self.video_layers:
            self.video_layers.validate()
        self.validate_required(self.audio_layers, 'audio_layers')
        if self.audio_layers:
            self.audio_layers.validate()
        self.validate_required(self.blend_list, 'blend_list')
        if self.blend_list:
            self.blend_list.validate()
        self.validate_required(self.mix_list, 'mix_list')
        if self.mix_list:
            self.mix_list.validate()

    def to_map(self):
        result = {}
        result['LayoutId'] = self.layout_id
        if self.video_layers is not None:
            result['VideoLayers'] = self.video_layers.to_map()
        else:
            result['VideoLayers'] = None
        if self.audio_layers is not None:
            result['AudioLayers'] = self.audio_layers.to_map()
        else:
            result['AudioLayers'] = None
        if self.blend_list is not None:
            result['BlendList'] = self.blend_list.to_map()
        else:
            result['BlendList'] = None
        if self.mix_list is not None:
            result['MixList'] = self.mix_list.to_map()
        else:
            result['MixList'] = None
        return result

    def from_map(self, map={}):
        self.layout_id = map.get('LayoutId')
        if map.get('VideoLayers') is not None:
            temp_model = DescribeCasterLayoutsResponseLayoutsLayoutVideoLayers()
            self.video_layers = temp_model.from_map(map['VideoLayers'])
        else:
            self.video_layers = None
        if map.get('AudioLayers') is not None:
            temp_model = DescribeCasterLayoutsResponseLayoutsLayoutAudioLayers()
            self.audio_layers = temp_model.from_map(map['AudioLayers'])
        else:
            self.audio_layers = None
        if map.get('BlendList') is not None:
            temp_model = DescribeCasterLayoutsResponseLayoutsLayoutBlendList()
            self.blend_list = temp_model.from_map(map['BlendList'])
        else:
            self.blend_list = None
        if map.get('MixList') is not None:
            temp_model = DescribeCasterLayoutsResponseLayoutsLayoutMixList()
            self.mix_list = temp_model.from_map(map['MixList'])
        else:
            self.mix_list = None
        return self


class DescribeCasterLayoutsResponseLayouts(TeaModel):
    def __init__(self, layout=None):
        self.layout = layout            # type: List[DescribeCasterLayoutsResponseLayoutsLayout]

    def validate(self):
        self.validate_required(self.layout, 'layout')
        if self.layout:
            for k in self.layout:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['Layout'] = []
        if self.layout is not None:
            for k in self.layout:
                result['Layout'].append(k.to_map() if k else None)
        else:
            result['Layout'] = None
        return result

    def from_map(self, map={}):
        self.layout = []
        if map.get('Layout') is not None:
            for k in map.get('Layout'):
                temp_model = DescribeCasterLayoutsResponseLayoutsLayout()
                self.layout.append(temp_model.from_map(k))
        else:
            self.layout = None
        return self


class DescribeCasterConfigRequest(TeaModel):
    def __init__(self, caster_id=None):
        self.caster_id = caster_id      # type: str

    def validate(self):
        self.validate_required(self.caster_id, 'caster_id')

    def to_map(self):
        result = {}
        result['CasterId'] = self.caster_id
        return result

    def from_map(self, map={}):
        self.caster_id = map.get('CasterId')
        return self


class DescribeCasterConfigResponse(TeaModel):
    def __init__(self, request_id=None, caster_id=None, caster_name=None, domain_name=None, delay=None,
                 urgent_material_id=None, side_output_url=None, callback_url=None, program_name=None, program_effect=None,
                 channel_enable=None, transcode_config=None, record_config=None):
        self.request_id = request_id    # type: str
        self.caster_id = caster_id      # type: str
        self.caster_name = caster_name  # type: str
        self.domain_name = domain_name  # type: str
        self.delay = delay              # type: float
        self.urgent_material_id = urgent_material_id  # type: str
        self.side_output_url = side_output_url  # type: str
        self.callback_url = callback_url  # type: str
        self.program_name = program_name  # type: str
        self.program_effect = program_effect  # type: int
        self.channel_enable = channel_enable  # type: int
        self.transcode_config = transcode_config  # type: DescribeCasterConfigResponseTranscodeConfig
        self.record_config = record_config  # type: DescribeCasterConfigResponseRecordConfig

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.caster_id, 'caster_id')
        self.validate_required(self.caster_name, 'caster_name')
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.delay, 'delay')
        self.validate_required(self.urgent_material_id, 'urgent_material_id')
        self.validate_required(self.side_output_url, 'side_output_url')
        self.validate_required(self.callback_url, 'callback_url')
        self.validate_required(self.program_name, 'program_name')
        self.validate_required(self.program_effect, 'program_effect')
        self.validate_required(self.channel_enable, 'channel_enable')
        self.validate_required(self.transcode_config, 'transcode_config')
        if self.transcode_config:
            self.transcode_config.validate()
        self.validate_required(self.record_config, 'record_config')
        if self.record_config:
            self.record_config.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['CasterId'] = self.caster_id
        result['CasterName'] = self.caster_name
        result['DomainName'] = self.domain_name
        result['Delay'] = self.delay
        result['UrgentMaterialId'] = self.urgent_material_id
        result['SideOutputUrl'] = self.side_output_url
        result['CallbackUrl'] = self.callback_url
        result['ProgramName'] = self.program_name
        result['ProgramEffect'] = self.program_effect
        result['ChannelEnable'] = self.channel_enable
        if self.transcode_config is not None:
            result['TranscodeConfig'] = self.transcode_config.to_map()
        else:
            result['TranscodeConfig'] = None
        if self.record_config is not None:
            result['RecordConfig'] = self.record_config.to_map()
        else:
            result['RecordConfig'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.caster_id = map.get('CasterId')
        self.caster_name = map.get('CasterName')
        self.domain_name = map.get('DomainName')
        self.delay = map.get('Delay')
        self.urgent_material_id = map.get('UrgentMaterialId')
        self.side_output_url = map.get('SideOutputUrl')
        self.callback_url = map.get('CallbackUrl')
        self.program_name = map.get('ProgramName')
        self.program_effect = map.get('ProgramEffect')
        self.channel_enable = map.get('ChannelEnable')
        if map.get('TranscodeConfig') is not None:
            temp_model = DescribeCasterConfigResponseTranscodeConfig()
            self.transcode_config = temp_model.from_map(map['TranscodeConfig'])
        else:
            self.transcode_config = None
        if map.get('RecordConfig') is not None:
            temp_model = DescribeCasterConfigResponseRecordConfig()
            self.record_config = temp_model.from_map(map['RecordConfig'])
        else:
            self.record_config = None
        return self


class DescribeCasterConfigResponseTranscodeConfigLiveTemplateIds(TeaModel):
    def __init__(self, location_id=None):
        # LocationId
        self.location_id = location_id  # type: List[str]

    def validate(self):
        self.validate_required(self.location_id, 'location_id')

    def to_map(self):
        result = {}
        result['LocationId'] = self.location_id
        return result

    def from_map(self, map={}):
        self.location_id = map.get('LocationId')
        return self


class DescribeCasterConfigResponseTranscodeConfig(TeaModel):
    def __init__(self, caster_template=None, live_template_ids=None):
        self.caster_template = caster_template  # type: str
        self.live_template_ids = live_template_ids  # type: DescribeCasterConfigResponseTranscodeConfigLiveTemplateIds

    def validate(self):
        self.validate_required(self.caster_template, 'caster_template')
        self.validate_required(self.live_template_ids, 'live_template_ids')
        if self.live_template_ids:
            self.live_template_ids.validate()

    def to_map(self):
        result = {}
        result['CasterTemplate'] = self.caster_template
        if self.live_template_ids is not None:
            result['LiveTemplateIds'] = self.live_template_ids.to_map()
        else:
            result['LiveTemplateIds'] = None
        return result

    def from_map(self, map={}):
        self.caster_template = map.get('CasterTemplate')
        if map.get('LiveTemplateIds') is not None:
            temp_model = DescribeCasterConfigResponseTranscodeConfigLiveTemplateIds()
            self.live_template_ids = temp_model.from_map(map['LiveTemplateIds'])
        else:
            self.live_template_ids = None
        return self


class DescribeCasterConfigResponseRecordConfigRecordFormatRecordFormat(TeaModel):
    def __init__(self, format=None, oss_object_prefix=None, slice_oss_object_prefix=None, cycle_duration=None):
        self.format = format            # type: str
        self.oss_object_prefix = oss_object_prefix  # type: str
        self.slice_oss_object_prefix = slice_oss_object_prefix  # type: str
        self.cycle_duration = cycle_duration  # type: int

    def validate(self):
        self.validate_required(self.format, 'format')
        self.validate_required(self.oss_object_prefix, 'oss_object_prefix')
        self.validate_required(self.slice_oss_object_prefix, 'slice_oss_object_prefix')
        self.validate_required(self.cycle_duration, 'cycle_duration')

    def to_map(self):
        result = {}
        result['Format'] = self.format
        result['OssObjectPrefix'] = self.oss_object_prefix
        result['SliceOssObjectPrefix'] = self.slice_oss_object_prefix
        result['CycleDuration'] = self.cycle_duration
        return result

    def from_map(self, map={}):
        self.format = map.get('Format')
        self.oss_object_prefix = map.get('OssObjectPrefix')
        self.slice_oss_object_prefix = map.get('SliceOssObjectPrefix')
        self.cycle_duration = map.get('CycleDuration')
        return self


class DescribeCasterConfigResponseRecordConfigRecordFormat(TeaModel):
    def __init__(self, record_format=None):
        self.record_format = record_format  # type: List[DescribeCasterConfigResponseRecordConfigRecordFormatRecordFormat]

    def validate(self):
        self.validate_required(self.record_format, 'record_format')
        if self.record_format:
            for k in self.record_format:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RecordFormat'] = []
        if self.record_format is not None:
            for k in self.record_format:
                result['RecordFormat'].append(k.to_map() if k else None)
        else:
            result['RecordFormat'] = None
        return result

    def from_map(self, map={}):
        self.record_format = []
        if map.get('RecordFormat') is not None:
            for k in map.get('RecordFormat'):
                temp_model = DescribeCasterConfigResponseRecordConfigRecordFormatRecordFormat()
                self.record_format.append(temp_model.from_map(k))
        else:
            self.record_format = None
        return self


class DescribeCasterConfigResponseRecordConfig(TeaModel):
    def __init__(self, oss_endpoint=None, oss_bucket=None, record_format=None):
        self.oss_endpoint = oss_endpoint  # type: str
        self.oss_bucket = oss_bucket    # type: str
        self.record_format = record_format  # type: DescribeCasterConfigResponseRecordConfigRecordFormat

    def validate(self):
        self.validate_required(self.oss_endpoint, 'oss_endpoint')
        self.validate_required(self.oss_bucket, 'oss_bucket')
        self.validate_required(self.record_format, 'record_format')
        if self.record_format:
            self.record_format.validate()

    def to_map(self):
        result = {}
        result['OssEndpoint'] = self.oss_endpoint
        result['OssBucket'] = self.oss_bucket
        if self.record_format is not None:
            result['RecordFormat'] = self.record_format.to_map()
        else:
            result['RecordFormat'] = None
        return result

    def from_map(self, map={}):
        self.oss_endpoint = map.get('OssEndpoint')
        self.oss_bucket = map.get('OssBucket')
        if map.get('RecordFormat') is not None:
            temp_model = DescribeCasterConfigResponseRecordConfigRecordFormat()
            self.record_format = temp_model.from_map(map['RecordFormat'])
        else:
            self.record_format = None
        return self


class DeleteCasterVideoResourceRequest(TeaModel):
    def __init__(self, caster_id=None, resource_id=None):
        self.caster_id = caster_id      # type: str
        self.resource_id = resource_id  # type: str

    def validate(self):
        self.validate_required(self.caster_id, 'caster_id')
        self.validate_required(self.resource_id, 'resource_id')

    def to_map(self):
        result = {}
        result['CasterId'] = self.caster_id
        result['ResourceId'] = self.resource_id
        return result

    def from_map(self, map={}):
        self.caster_id = map.get('CasterId')
        self.resource_id = map.get('ResourceId')
        return self


class DeleteCasterVideoResourceResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DeleteCasterLayoutRequest(TeaModel):
    def __init__(self, caster_id=None, layout_id=None):
        self.caster_id = caster_id      # type: str
        self.layout_id = layout_id      # type: str

    def validate(self):
        self.validate_required(self.caster_id, 'caster_id')
        self.validate_required(self.layout_id, 'layout_id')

    def to_map(self):
        result = {}
        result['CasterId'] = self.caster_id
        result['LayoutId'] = self.layout_id
        return result

    def from_map(self, map={}):
        self.caster_id = map.get('CasterId')
        self.layout_id = map.get('LayoutId')
        return self


class DeleteCasterLayoutResponse(TeaModel):
    def __init__(self, request_id=None, caster_id=None, layout_id=None):
        self.request_id = request_id    # type: str
        self.caster_id = caster_id      # type: str
        self.layout_id = layout_id      # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.caster_id, 'caster_id')
        self.validate_required(self.layout_id, 'layout_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['CasterId'] = self.caster_id
        result['LayoutId'] = self.layout_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.caster_id = map.get('CasterId')
        self.layout_id = map.get('LayoutId')
        return self


class DeleteCasterRequest(TeaModel):
    def __init__(self, security_token=None, caster_id=None):
        self.security_token = security_token  # type: str
        self.caster_id = caster_id      # type: str

    def validate(self):
        self.validate_required(self.caster_id, 'caster_id')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['CasterId'] = self.caster_id
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.caster_id = map.get('CasterId')
        return self


class DeleteCasterResponse(TeaModel):
    def __init__(self, request_id=None, caster_id=None):
        self.request_id = request_id    # type: str
        self.caster_id = caster_id      # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.caster_id, 'caster_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['CasterId'] = self.caster_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.caster_id = map.get('CasterId')
        return self


class CreateCasterRequest(TeaModel):
    def __init__(self, caster_name=None, client_token=None, norm_type=None, charge_type=None, purchase_time=None,
                 expire_time=None, caster_template=None):
        self.caster_name = caster_name  # type: str
        self.client_token = client_token  # type: str
        self.norm_type = norm_type      # type: int
        self.charge_type = charge_type  # type: str
        self.purchase_time = purchase_time  # type: str
        self.expire_time = expire_time  # type: str
        self.caster_template = caster_template  # type: str

    def validate(self):
        self.validate_required(self.client_token, 'client_token')
        self.validate_required(self.norm_type, 'norm_type')
        self.validate_required(self.charge_type, 'charge_type')

    def to_map(self):
        result = {}
        result['CasterName'] = self.caster_name
        result['ClientToken'] = self.client_token
        result['NormType'] = self.norm_type
        result['ChargeType'] = self.charge_type
        result['PurchaseTime'] = self.purchase_time
        result['ExpireTime'] = self.expire_time
        result['CasterTemplate'] = self.caster_template
        return result

    def from_map(self, map={}):
        self.caster_name = map.get('CasterName')
        self.client_token = map.get('ClientToken')
        self.norm_type = map.get('NormType')
        self.charge_type = map.get('ChargeType')
        self.purchase_time = map.get('PurchaseTime')
        self.expire_time = map.get('ExpireTime')
        self.caster_template = map.get('CasterTemplate')
        return self


class CreateCasterResponse(TeaModel):
    def __init__(self, request_id=None, caster_id=None):
        self.request_id = request_id    # type: str
        self.caster_id = caster_id      # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.caster_id, 'caster_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['CasterId'] = self.caster_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.caster_id = map.get('CasterId')
        return self


class CopyCasterSceneConfigRequest(TeaModel):
    def __init__(self, caster_id=None, from_scene_id=None, to_scene_id=None):
        self.caster_id = caster_id      # type: str
        self.from_scene_id = from_scene_id  # type: str
        self.to_scene_id = to_scene_id  # type: str

    def validate(self):
        self.validate_required(self.caster_id, 'caster_id')
        self.validate_required(self.from_scene_id, 'from_scene_id')
        self.validate_required(self.to_scene_id, 'to_scene_id')

    def to_map(self):
        result = {}
        result['CasterId'] = self.caster_id
        result['FromSceneId'] = self.from_scene_id
        result['ToSceneId'] = self.to_scene_id
        return result

    def from_map(self, map={}):
        self.caster_id = map.get('CasterId')
        self.from_scene_id = map.get('FromSceneId')
        self.to_scene_id = map.get('ToSceneId')
        return self


class CopyCasterSceneConfigResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class CopyCasterRequest(TeaModel):
    def __init__(self, caster_name=None, src_caster_id=None, client_token=None):
        self.caster_name = caster_name  # type: str
        self.src_caster_id = src_caster_id  # type: str
        self.client_token = client_token  # type: str

    def validate(self):
        self.validate_required(self.caster_name, 'caster_name')
        self.validate_required(self.src_caster_id, 'src_caster_id')
        self.validate_required(self.client_token, 'client_token')

    def to_map(self):
        result = {}
        result['CasterName'] = self.caster_name
        result['SrcCasterId'] = self.src_caster_id
        result['ClientToken'] = self.client_token
        return result

    def from_map(self, map={}):
        self.caster_name = map.get('CasterName')
        self.src_caster_id = map.get('SrcCasterId')
        self.client_token = map.get('ClientToken')
        return self


class CopyCasterResponse(TeaModel):
    def __init__(self, request_id=None, caster_id=None):
        self.request_id = request_id    # type: str
        self.caster_id = caster_id      # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.caster_id, 'caster_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['CasterId'] = self.caster_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.caster_id = map.get('CasterId')
        return self


class AddCasterVideoResourceRequest(TeaModel):
    def __init__(self, caster_id=None, resource_name=None, location_id=None, live_stream_url=None, stream_id=None,
                 material_id=None, vod_url=None, begin_offset=None, end_offset=None, repeat_num=None,
                 pts_callback_interval=None):
        self.caster_id = caster_id      # type: str
        self.resource_name = resource_name  # type: str
        self.location_id = location_id  # type: str
        self.live_stream_url = live_stream_url  # type: str
        self.stream_id = stream_id      # type: str
        self.material_id = material_id  # type: str
        self.vod_url = vod_url          # type: str
        self.begin_offset = begin_offset  # type: int
        self.end_offset = end_offset    # type: int
        self.repeat_num = repeat_num    # type: int
        self.pts_callback_interval = pts_callback_interval  # type: int

    def validate(self):
        self.validate_required(self.caster_id, 'caster_id')
        self.validate_required(self.resource_name, 'resource_name')

    def to_map(self):
        result = {}
        result['CasterId'] = self.caster_id
        result['ResourceName'] = self.resource_name
        result['LocationId'] = self.location_id
        result['LiveStreamUrl'] = self.live_stream_url
        result['StreamId'] = self.stream_id
        result['MaterialId'] = self.material_id
        result['VodUrl'] = self.vod_url
        result['BeginOffset'] = self.begin_offset
        result['EndOffset'] = self.end_offset
        result['RepeatNum'] = self.repeat_num
        result['PtsCallbackInterval'] = self.pts_callback_interval
        return result

    def from_map(self, map={}):
        self.caster_id = map.get('CasterId')
        self.resource_name = map.get('ResourceName')
        self.location_id = map.get('LocationId')
        self.live_stream_url = map.get('LiveStreamUrl')
        self.stream_id = map.get('StreamId')
        self.material_id = map.get('MaterialId')
        self.vod_url = map.get('VodUrl')
        self.begin_offset = map.get('BeginOffset')
        self.end_offset = map.get('EndOffset')
        self.repeat_num = map.get('RepeatNum')
        self.pts_callback_interval = map.get('PtsCallbackInterval')
        return self


class AddCasterVideoResourceResponse(TeaModel):
    def __init__(self, request_id=None, resource_id=None):
        self.request_id = request_id    # type: str
        self.resource_id = resource_id  # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.resource_id, 'resource_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['ResourceId'] = self.resource_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.resource_id = map.get('ResourceId')
        return self


class AddCasterLayoutRequest(TeaModel):
    def __init__(self, caster_id=None, video_layer=None, audio_layer=None, blend_list=None, mix_list=None):
        self.caster_id = caster_id      # type: str
        self.video_layer = video_layer  # type: List[AddCasterLayoutRequestVideoLayer]
        self.audio_layer = audio_layer  # type: List[AddCasterLayoutRequestAudioLayer]
        self.blend_list = blend_list    # type: List[str]
        self.mix_list = mix_list        # type: List[str]

    def validate(self):
        self.validate_required(self.caster_id, 'caster_id')
        self.validate_required(self.video_layer, 'video_layer')
        if self.video_layer:
            for k in self.video_layer:
                if k:
                    k.validate()
        self.validate_required(self.audio_layer, 'audio_layer')
        if self.audio_layer:
            for k in self.audio_layer:
                if k:
                    k.validate()
        self.validate_required(self.blend_list, 'blend_list')
        self.validate_required(self.mix_list, 'mix_list')

    def to_map(self):
        result = {}
        result['CasterId'] = self.caster_id
        result['VideoLayer'] = []
        if self.video_layer is not None:
            for k in self.video_layer:
                result['VideoLayer'].append(k.to_map() if k else None)
        else:
            result['VideoLayer'] = None
        result['AudioLayer'] = []
        if self.audio_layer is not None:
            for k in self.audio_layer:
                result['AudioLayer'].append(k.to_map() if k else None)
        else:
            result['AudioLayer'] = None
        result['BlendList'] = self.blend_list
        result['MixList'] = self.mix_list
        return result

    def from_map(self, map={}):
        self.caster_id = map.get('CasterId')
        self.video_layer = []
        if map.get('VideoLayer') is not None:
            for k in map.get('VideoLayer'):
                temp_model = AddCasterLayoutRequestVideoLayer()
                self.video_layer.append(temp_model.from_map(k))
        else:
            self.video_layer = None
        self.audio_layer = []
        if map.get('AudioLayer') is not None:
            for k in map.get('AudioLayer'):
                temp_model = AddCasterLayoutRequestAudioLayer()
                self.audio_layer.append(temp_model.from_map(k))
        else:
            self.audio_layer = None
        self.blend_list = map.get('BlendList')
        self.mix_list = map.get('MixList')
        return self


class AddCasterLayoutRequestVideoLayer(TeaModel):
    def __init__(self, fill_mode=None, height_normalized=None, width_normalized=None, position_refer=None,
                 position_normalized=None, fixed_delay_duration=None):
        self.fill_mode = fill_mode      # type: str
        self.height_normalized = height_normalized  # type: float
        self.width_normalized = width_normalized  # type: float
        self.position_refer = position_refer  # type: str
        self.position_normalized = position_normalized  # type: List[float]
        self.fixed_delay_duration = fixed_delay_duration  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['FillMode'] = self.fill_mode
        result['HeightNormalized'] = self.height_normalized
        result['WidthNormalized'] = self.width_normalized
        result['PositionRefer'] = self.position_refer
        result['PositionNormalized'] = self.position_normalized
        result['FixedDelayDuration'] = self.fixed_delay_duration
        return result

    def from_map(self, map={}):
        self.fill_mode = map.get('FillMode')
        self.height_normalized = map.get('HeightNormalized')
        self.width_normalized = map.get('WidthNormalized')
        self.position_refer = map.get('PositionRefer')
        self.position_normalized = map.get('PositionNormalized')
        self.fixed_delay_duration = map.get('FixedDelayDuration')
        return self


class AddCasterLayoutRequestAudioLayer(TeaModel):
    def __init__(self, volume_rate=None, valid_channel=None, fixed_delay_duration=None):
        self.volume_rate = volume_rate  # type: float
        self.valid_channel = valid_channel  # type: str
        self.fixed_delay_duration = fixed_delay_duration  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['VolumeRate'] = self.volume_rate
        result['ValidChannel'] = self.valid_channel
        result['FixedDelayDuration'] = self.fixed_delay_duration
        return result

    def from_map(self, map={}):
        self.volume_rate = map.get('VolumeRate')
        self.valid_channel = map.get('ValidChannel')
        self.fixed_delay_duration = map.get('FixedDelayDuration')
        return self


class AddCasterLayoutResponse(TeaModel):
    def __init__(self, request_id=None, layout_id=None):
        self.request_id = request_id    # type: str
        self.layout_id = layout_id      # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.layout_id, 'layout_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['LayoutId'] = self.layout_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.layout_id = map.get('LayoutId')
        return self


class DescribeLivePullStreamConfigRequest(TeaModel):
    def __init__(self, domain_name=None):
        self.domain_name = domain_name  # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        return self


class DescribeLivePullStreamConfigResponse(TeaModel):
    def __init__(self, request_id=None, live_app_record_list=None):
        self.request_id = request_id    # type: str
        self.live_app_record_list = live_app_record_list  # type: DescribeLivePullStreamConfigResponseLiveAppRecordList

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.live_app_record_list, 'live_app_record_list')
        if self.live_app_record_list:
            self.live_app_record_list.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.live_app_record_list is not None:
            result['LiveAppRecordList'] = self.live_app_record_list.to_map()
        else:
            result['LiveAppRecordList'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('LiveAppRecordList') is not None:
            temp_model = DescribeLivePullStreamConfigResponseLiveAppRecordList()
            self.live_app_record_list = temp_model.from_map(map['LiveAppRecordList'])
        else:
            self.live_app_record_list = None
        return self


class DescribeLivePullStreamConfigResponseLiveAppRecordListLiveAppRecord(TeaModel):
    def __init__(self, domain_name=None, app_name=None, stream_name=None, source_url=None, start_time=None,
                 end_time=None):
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str
        self.stream_name = stream_name  # type: str
        self.source_url = source_url    # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.app_name, 'app_name')
        self.validate_required(self.stream_name, 'stream_name')
        self.validate_required(self.source_url, 'source_url')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        result['StreamName'] = self.stream_name
        result['SourceUrl'] = self.source_url
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        self.stream_name = map.get('StreamName')
        self.source_url = map.get('SourceUrl')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        return self


class DescribeLivePullStreamConfigResponseLiveAppRecordList(TeaModel):
    def __init__(self, live_app_record=None):
        self.live_app_record = live_app_record  # type: List[DescribeLivePullStreamConfigResponseLiveAppRecordListLiveAppRecord]

    def validate(self):
        self.validate_required(self.live_app_record, 'live_app_record')
        if self.live_app_record:
            for k in self.live_app_record:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['LiveAppRecord'] = []
        if self.live_app_record is not None:
            for k in self.live_app_record:
                result['LiveAppRecord'].append(k.to_map() if k else None)
        else:
            result['LiveAppRecord'] = None
        return result

    def from_map(self, map={}):
        self.live_app_record = []
        if map.get('LiveAppRecord') is not None:
            for k in map.get('LiveAppRecord'):
                temp_model = DescribeLivePullStreamConfigResponseLiveAppRecordListLiveAppRecord()
                self.live_app_record.append(temp_model.from_map(k))
        else:
            self.live_app_record = None
        return self


class DeleteLivePullStreamInfoConfigRequest(TeaModel):
    def __init__(self, security_token=None, domain_name=None, app_name=None, stream_name=None):
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str
        self.stream_name = stream_name  # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.app_name, 'app_name')
        self.validate_required(self.stream_name, 'stream_name')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        result['StreamName'] = self.stream_name
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        self.stream_name = map.get('StreamName')
        return self


class DeleteLivePullStreamInfoConfigResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class AddLivePullStreamInfoConfigRequest(TeaModel):
    def __init__(self, domain_name=None, app_name=None, stream_name=None, source_url=None, start_time=None,
                 end_time=None):
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str
        self.stream_name = stream_name  # type: str
        self.source_url = source_url    # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.app_name, 'app_name')
        self.validate_required(self.stream_name, 'stream_name')
        self.validate_required(self.source_url, 'source_url')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        result['StreamName'] = self.stream_name
        result['SourceUrl'] = self.source_url
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        self.stream_name = map.get('StreamName')
        self.source_url = map.get('SourceUrl')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        return self


class AddLivePullStreamInfoConfigResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeLiveStreamBitRateDataRequest(TeaModel):
    def __init__(self, security_token=None, domain_name=None, app_name=None, stream_name=None, start_time=None,
                 end_time=None):
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str
        self.stream_name = stream_name  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.app_name, 'app_name')
        self.validate_required(self.stream_name, 'stream_name')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        result['StreamName'] = self.stream_name
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        self.stream_name = map.get('StreamName')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        return self


class DescribeLiveStreamBitRateDataResponse(TeaModel):
    def __init__(self, request_id=None, frame_rate_and_bit_rate_infos=None):
        self.request_id = request_id    # type: str
        self.frame_rate_and_bit_rate_infos = frame_rate_and_bit_rate_infos  # type: DescribeLiveStreamBitRateDataResponseFrameRateAndBitRateInfos

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.frame_rate_and_bit_rate_infos, 'frame_rate_and_bit_rate_infos')
        if self.frame_rate_and_bit_rate_infos:
            self.frame_rate_and_bit_rate_infos.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.frame_rate_and_bit_rate_infos is not None:
            result['FrameRateAndBitRateInfos'] = self.frame_rate_and_bit_rate_infos.to_map()
        else:
            result['FrameRateAndBitRateInfos'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('FrameRateAndBitRateInfos') is not None:
            temp_model = DescribeLiveStreamBitRateDataResponseFrameRateAndBitRateInfos()
            self.frame_rate_and_bit_rate_infos = temp_model.from_map(map['FrameRateAndBitRateInfos'])
        else:
            self.frame_rate_and_bit_rate_infos = None
        return self


class DescribeLiveStreamBitRateDataResponseFrameRateAndBitRateInfosFrameRateAndBitRateInfo(TeaModel):
    def __init__(self, stream_url=None, video_frame_rate=None, audio_frame_rate=None, bit_rate=None, time=None):
        self.stream_url = stream_url    # type: str
        self.video_frame_rate = video_frame_rate  # type: float
        self.audio_frame_rate = audio_frame_rate  # type: float
        self.bit_rate = bit_rate        # type: float
        self.time = time                # type: str

    def validate(self):
        self.validate_required(self.stream_url, 'stream_url')
        self.validate_required(self.video_frame_rate, 'video_frame_rate')
        self.validate_required(self.audio_frame_rate, 'audio_frame_rate')
        self.validate_required(self.bit_rate, 'bit_rate')
        self.validate_required(self.time, 'time')

    def to_map(self):
        result = {}
        result['StreamUrl'] = self.stream_url
        result['VideoFrameRate'] = self.video_frame_rate
        result['AudioFrameRate'] = self.audio_frame_rate
        result['BitRate'] = self.bit_rate
        result['Time'] = self.time
        return result

    def from_map(self, map={}):
        self.stream_url = map.get('StreamUrl')
        self.video_frame_rate = map.get('VideoFrameRate')
        self.audio_frame_rate = map.get('AudioFrameRate')
        self.bit_rate = map.get('BitRate')
        self.time = map.get('Time')
        return self


class DescribeLiveStreamBitRateDataResponseFrameRateAndBitRateInfos(TeaModel):
    def __init__(self, frame_rate_and_bit_rate_info=None):
        self.frame_rate_and_bit_rate_info = frame_rate_and_bit_rate_info  # type: List[DescribeLiveStreamBitRateDataResponseFrameRateAndBitRateInfosFrameRateAndBitRateInfo]

    def validate(self):
        self.validate_required(self.frame_rate_and_bit_rate_info, 'frame_rate_and_bit_rate_info')
        if self.frame_rate_and_bit_rate_info:
            for k in self.frame_rate_and_bit_rate_info:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['FrameRateAndBitRateInfo'] = []
        if self.frame_rate_and_bit_rate_info is not None:
            for k in self.frame_rate_and_bit_rate_info:
                result['FrameRateAndBitRateInfo'].append(k.to_map() if k else None)
        else:
            result['FrameRateAndBitRateInfo'] = None
        return result

    def from_map(self, map={}):
        self.frame_rate_and_bit_rate_info = []
        if map.get('FrameRateAndBitRateInfo') is not None:
            for k in map.get('FrameRateAndBitRateInfo'):
                temp_model = DescribeLiveStreamBitRateDataResponseFrameRateAndBitRateInfosFrameRateAndBitRateInfo()
                self.frame_rate_and_bit_rate_info.append(temp_model.from_map(k))
        else:
            self.frame_rate_and_bit_rate_info = None
        return self


class AddLiveDetectNotifyConfigRequest(TeaModel):
    def __init__(self, security_token=None, domain_name=None, notify_url=None):
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str
        self.notify_url = notify_url    # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.notify_url, 'notify_url')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['DomainName'] = self.domain_name
        result['NotifyUrl'] = self.notify_url
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.domain_name = map.get('DomainName')
        self.notify_url = map.get('NotifyUrl')
        return self


class AddLiveDetectNotifyConfigResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class AddLiveSnapshotDetectPornConfigRequest(TeaModel):
    def __init__(self, security_token=None, domain_name=None, app_name=None, oss_endpoint=None, oss_bucket=None,
                 oss_object=None, scene=None, interval=None):
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str
        self.oss_endpoint = oss_endpoint  # type: str
        self.oss_bucket = oss_bucket    # type: str
        self.oss_object = oss_object    # type: str
        self.scene = scene              # type: List[str]
        self.interval = interval        # type: int

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.app_name, 'app_name')
        self.validate_required(self.oss_endpoint, 'oss_endpoint')
        self.validate_required(self.oss_bucket, 'oss_bucket')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        result['OssEndpoint'] = self.oss_endpoint
        result['OssBucket'] = self.oss_bucket
        result['OssObject'] = self.oss_object
        result['Scene'] = self.scene
        result['Interval'] = self.interval
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        self.oss_endpoint = map.get('OssEndpoint')
        self.oss_bucket = map.get('OssBucket')
        self.oss_object = map.get('OssObject')
        self.scene = map.get('Scene')
        self.interval = map.get('Interval')
        return self


class AddLiveSnapshotDetectPornConfigResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DeleteLiveDetectNotifyConfigRequest(TeaModel):
    def __init__(self, security_token=None, domain_name=None):
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['DomainName'] = self.domain_name
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.domain_name = map.get('DomainName')
        return self


class DeleteLiveDetectNotifyConfigResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeLiveDetectNotifyConfigRequest(TeaModel):
    def __init__(self, security_token=None, domain_name=None):
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['DomainName'] = self.domain_name
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.domain_name = map.get('DomainName')
        return self


class DescribeLiveDetectNotifyConfigResponse(TeaModel):
    def __init__(self, request_id=None, live_detect_notify_config=None):
        self.request_id = request_id    # type: str
        self.live_detect_notify_config = live_detect_notify_config  # type: DescribeLiveDetectNotifyConfigResponseLiveDetectNotifyConfig

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.live_detect_notify_config, 'live_detect_notify_config')
        if self.live_detect_notify_config:
            self.live_detect_notify_config.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.live_detect_notify_config is not None:
            result['LiveDetectNotifyConfig'] = self.live_detect_notify_config.to_map()
        else:
            result['LiveDetectNotifyConfig'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('LiveDetectNotifyConfig') is not None:
            temp_model = DescribeLiveDetectNotifyConfigResponseLiveDetectNotifyConfig()
            self.live_detect_notify_config = temp_model.from_map(map['LiveDetectNotifyConfig'])
        else:
            self.live_detect_notify_config = None
        return self


class DescribeLiveDetectNotifyConfigResponseLiveDetectNotifyConfig(TeaModel):
    def __init__(self, domain_name=None, notify_url=None):
        self.domain_name = domain_name  # type: str
        self.notify_url = notify_url    # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.notify_url, 'notify_url')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['NotifyUrl'] = self.notify_url
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.notify_url = map.get('NotifyUrl')
        return self


class DeleteLiveSnapshotDetectPornConfigRequest(TeaModel):
    def __init__(self, security_token=None, domain_name=None, app_name=None):
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.app_name, 'app_name')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        return self


class DeleteLiveSnapshotDetectPornConfigResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeLiveSnapshotDetectPornConfigRequest(TeaModel):
    def __init__(self, security_token=None, domain_name=None, app_name=None, page_num=None, page_size=None,
                 order=None):
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int
        self.order = order              # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        result['Order'] = self.order
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        self.order = map.get('Order')
        return self


class DescribeLiveSnapshotDetectPornConfigResponse(TeaModel):
    def __init__(self, request_id=None, page_num=None, page_size=None, order=None, total_num=None, total_page=None,
                 live_snapshot_detect_porn_config_list=None):
        self.request_id = request_id    # type: str
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int
        self.order = order              # type: str
        self.total_num = total_num      # type: int
        self.total_page = total_page    # type: int
        self.live_snapshot_detect_porn_config_list = live_snapshot_detect_porn_config_list  # type: DescribeLiveSnapshotDetectPornConfigResponseLiveSnapshotDetectPornConfigList

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.page_num, 'page_num')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.order, 'order')
        self.validate_required(self.total_num, 'total_num')
        self.validate_required(self.total_page, 'total_page')
        self.validate_required(self.live_snapshot_detect_porn_config_list, 'live_snapshot_detect_porn_config_list')
        if self.live_snapshot_detect_porn_config_list:
            self.live_snapshot_detect_porn_config_list.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        result['Order'] = self.order
        result['TotalNum'] = self.total_num
        result['TotalPage'] = self.total_page
        if self.live_snapshot_detect_porn_config_list is not None:
            result['LiveSnapshotDetectPornConfigList'] = self.live_snapshot_detect_porn_config_list.to_map()
        else:
            result['LiveSnapshotDetectPornConfigList'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        self.order = map.get('Order')
        self.total_num = map.get('TotalNum')
        self.total_page = map.get('TotalPage')
        if map.get('LiveSnapshotDetectPornConfigList') is not None:
            temp_model = DescribeLiveSnapshotDetectPornConfigResponseLiveSnapshotDetectPornConfigList()
            self.live_snapshot_detect_porn_config_list = temp_model.from_map(map['LiveSnapshotDetectPornConfigList'])
        else:
            self.live_snapshot_detect_porn_config_list = None
        return self


class DescribeLiveSnapshotDetectPornConfigResponseLiveSnapshotDetectPornConfigListLiveSnapshotDetectPornConfigScenes(TeaModel):
    def __init__(self, scene=None):
        # scene
        self.scene = scene              # type: List[str]

    def validate(self):
        self.validate_required(self.scene, 'scene')

    def to_map(self):
        result = {}
        result['scene'] = self.scene
        return result

    def from_map(self, map={}):
        self.scene = map.get('scene')
        return self


class DescribeLiveSnapshotDetectPornConfigResponseLiveSnapshotDetectPornConfigListLiveSnapshotDetectPornConfig(TeaModel):
    def __init__(self, domain_name=None, app_name=None, oss_endpoint=None, oss_bucket=None, oss_object=None,
                 interval=None, scenes=None):
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str
        self.oss_endpoint = oss_endpoint  # type: str
        self.oss_bucket = oss_bucket    # type: str
        self.oss_object = oss_object    # type: str
        self.interval = interval        # type: int
        self.scenes = scenes            # type: DescribeLiveSnapshotDetectPornConfigResponseLiveSnapshotDetectPornConfigListLiveSnapshotDetectPornConfigScenes

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.app_name, 'app_name')
        self.validate_required(self.oss_endpoint, 'oss_endpoint')
        self.validate_required(self.oss_bucket, 'oss_bucket')
        self.validate_required(self.oss_object, 'oss_object')
        self.validate_required(self.interval, 'interval')
        self.validate_required(self.scenes, 'scenes')
        if self.scenes:
            self.scenes.validate()

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        result['OssEndpoint'] = self.oss_endpoint
        result['OssBucket'] = self.oss_bucket
        result['OssObject'] = self.oss_object
        result['Interval'] = self.interval
        if self.scenes is not None:
            result['Scenes'] = self.scenes.to_map()
        else:
            result['Scenes'] = None
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        self.oss_endpoint = map.get('OssEndpoint')
        self.oss_bucket = map.get('OssBucket')
        self.oss_object = map.get('OssObject')
        self.interval = map.get('Interval')
        if map.get('Scenes') is not None:
            temp_model = DescribeLiveSnapshotDetectPornConfigResponseLiveSnapshotDetectPornConfigListLiveSnapshotDetectPornConfigScenes()
            self.scenes = temp_model.from_map(map['Scenes'])
        else:
            self.scenes = None
        return self


class DescribeLiveSnapshotDetectPornConfigResponseLiveSnapshotDetectPornConfigList(TeaModel):
    def __init__(self, live_snapshot_detect_porn_config=None):
        self.live_snapshot_detect_porn_config = live_snapshot_detect_porn_config  # type: List[DescribeLiveSnapshotDetectPornConfigResponseLiveSnapshotDetectPornConfigListLiveSnapshotDetectPornConfig]

    def validate(self):
        self.validate_required(self.live_snapshot_detect_porn_config, 'live_snapshot_detect_porn_config')
        if self.live_snapshot_detect_porn_config:
            for k in self.live_snapshot_detect_porn_config:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['LiveSnapshotDetectPornConfig'] = []
        if self.live_snapshot_detect_porn_config is not None:
            for k in self.live_snapshot_detect_porn_config:
                result['LiveSnapshotDetectPornConfig'].append(k.to_map() if k else None)
        else:
            result['LiveSnapshotDetectPornConfig'] = None
        return result

    def from_map(self, map={}):
        self.live_snapshot_detect_porn_config = []
        if map.get('LiveSnapshotDetectPornConfig') is not None:
            for k in map.get('LiveSnapshotDetectPornConfig'):
                temp_model = DescribeLiveSnapshotDetectPornConfigResponseLiveSnapshotDetectPornConfigListLiveSnapshotDetectPornConfig()
                self.live_snapshot_detect_porn_config.append(temp_model.from_map(k))
        else:
            self.live_snapshot_detect_porn_config = None
        return self


class UpdateLiveDetectNotifyConfigRequest(TeaModel):
    def __init__(self, security_token=None, domain_name=None, notify_url=None):
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str
        self.notify_url = notify_url    # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.notify_url, 'notify_url')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['DomainName'] = self.domain_name
        result['NotifyUrl'] = self.notify_url
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.domain_name = map.get('DomainName')
        self.notify_url = map.get('NotifyUrl')
        return self


class UpdateLiveDetectNotifyConfigResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class UpdateLiveSnapshotDetectPornConfigRequest(TeaModel):
    def __init__(self, security_token=None, domain_name=None, app_name=None, oss_endpoint=None, oss_bucket=None,
                 oss_object=None, interval=None, scene=None):
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str
        self.oss_endpoint = oss_endpoint  # type: str
        self.oss_bucket = oss_bucket    # type: str
        self.oss_object = oss_object    # type: str
        self.interval = interval        # type: int
        self.scene = scene              # type: List[str]

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.app_name, 'app_name')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        result['OssEndpoint'] = self.oss_endpoint
        result['OssBucket'] = self.oss_bucket
        result['OssObject'] = self.oss_object
        result['Interval'] = self.interval
        result['Scene'] = self.scene
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        self.oss_endpoint = map.get('OssEndpoint')
        self.oss_bucket = map.get('OssBucket')
        self.oss_object = map.get('OssObject')
        self.interval = map.get('Interval')
        self.scene = map.get('Scene')
        return self


class UpdateLiveSnapshotDetectPornConfigResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class AddLiveRecordNotifyConfigRequest(TeaModel):
    def __init__(self, security_token=None, domain_name=None, notify_url=None, need_status_notify=None,
                 on_demand_url=None):
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str
        self.notify_url = notify_url    # type: str
        self.need_status_notify = need_status_notify  # type: bool
        self.on_demand_url = on_demand_url  # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.notify_url, 'notify_url')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['DomainName'] = self.domain_name
        result['NotifyUrl'] = self.notify_url
        result['NeedStatusNotify'] = self.need_status_notify
        result['OnDemandUrl'] = self.on_demand_url
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.domain_name = map.get('DomainName')
        self.notify_url = map.get('NotifyUrl')
        self.need_status_notify = map.get('NeedStatusNotify')
        self.on_demand_url = map.get('OnDemandUrl')
        return self


class AddLiveRecordNotifyConfigResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DeleteLiveStreamsNotifyUrlConfigRequest(TeaModel):
    def __init__(self, domain_name=None):
        self.domain_name = domain_name  # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        return self


class DeleteLiveStreamsNotifyUrlConfigResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DeleteLiveRecordNotifyConfigRequest(TeaModel):
    def __init__(self, security_token=None, domain_name=None):
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['DomainName'] = self.domain_name
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.domain_name = map.get('DomainName')
        return self


class DeleteLiveRecordNotifyConfigResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeLiveRecordNotifyConfigRequest(TeaModel):
    def __init__(self, security_token=None, domain_name=None):
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['DomainName'] = self.domain_name
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.domain_name = map.get('DomainName')
        return self


class DescribeLiveRecordNotifyConfigResponse(TeaModel):
    def __init__(self, request_id=None, live_record_notify_config=None):
        self.request_id = request_id    # type: str
        self.live_record_notify_config = live_record_notify_config  # type: DescribeLiveRecordNotifyConfigResponseLiveRecordNotifyConfig

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.live_record_notify_config, 'live_record_notify_config')
        if self.live_record_notify_config:
            self.live_record_notify_config.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.live_record_notify_config is not None:
            result['LiveRecordNotifyConfig'] = self.live_record_notify_config.to_map()
        else:
            result['LiveRecordNotifyConfig'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('LiveRecordNotifyConfig') is not None:
            temp_model = DescribeLiveRecordNotifyConfigResponseLiveRecordNotifyConfig()
            self.live_record_notify_config = temp_model.from_map(map['LiveRecordNotifyConfig'])
        else:
            self.live_record_notify_config = None
        return self


class DescribeLiveRecordNotifyConfigResponseLiveRecordNotifyConfig(TeaModel):
    def __init__(self, domain_name=None, notify_url=None, on_demand_url=None, need_status_notify=None):
        self.domain_name = domain_name  # type: str
        self.notify_url = notify_url    # type: str
        self.on_demand_url = on_demand_url  # type: str
        self.need_status_notify = need_status_notify  # type: bool

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.notify_url, 'notify_url')
        self.validate_required(self.on_demand_url, 'on_demand_url')
        self.validate_required(self.need_status_notify, 'need_status_notify')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['NotifyUrl'] = self.notify_url
        result['OnDemandUrl'] = self.on_demand_url
        result['NeedStatusNotify'] = self.need_status_notify
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.notify_url = map.get('NotifyUrl')
        self.on_demand_url = map.get('OnDemandUrl')
        self.need_status_notify = map.get('NeedStatusNotify')
        return self


class DescribeLiveStreamsNotifyUrlConfigRequest(TeaModel):
    def __init__(self, domain_name=None):
        self.domain_name = domain_name  # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        return self


class DescribeLiveStreamsNotifyUrlConfigResponse(TeaModel):
    def __init__(self, request_id=None, live_streams_notify_config=None):
        self.request_id = request_id    # type: str
        self.live_streams_notify_config = live_streams_notify_config  # type: DescribeLiveStreamsNotifyUrlConfigResponseLiveStreamsNotifyConfig

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.live_streams_notify_config, 'live_streams_notify_config')
        if self.live_streams_notify_config:
            self.live_streams_notify_config.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.live_streams_notify_config is not None:
            result['LiveStreamsNotifyConfig'] = self.live_streams_notify_config.to_map()
        else:
            result['LiveStreamsNotifyConfig'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('LiveStreamsNotifyConfig') is not None:
            temp_model = DescribeLiveStreamsNotifyUrlConfigResponseLiveStreamsNotifyConfig()
            self.live_streams_notify_config = temp_model.from_map(map['LiveStreamsNotifyConfig'])
        else:
            self.live_streams_notify_config = None
        return self


class DescribeLiveStreamsNotifyUrlConfigResponseLiveStreamsNotifyConfig(TeaModel):
    def __init__(self, domain_name=None, notify_url=None, auth_type=None, auth_key=None):
        self.domain_name = domain_name  # type: str
        self.notify_url = notify_url    # type: str
        self.auth_type = auth_type      # type: str
        self.auth_key = auth_key        # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.notify_url, 'notify_url')
        self.validate_required(self.auth_type, 'auth_type')
        self.validate_required(self.auth_key, 'auth_key')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['NotifyUrl'] = self.notify_url
        result['AuthType'] = self.auth_type
        result['AuthKey'] = self.auth_key
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.notify_url = map.get('NotifyUrl')
        self.auth_type = map.get('AuthType')
        self.auth_key = map.get('AuthKey')
        return self


class UpdateLiveRecordNotifyConfigRequest(TeaModel):
    def __init__(self, security_token=None, domain_name=None, notify_url=None, on_demand_url=None,
                 need_status_notify=None):
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str
        self.notify_url = notify_url    # type: str
        self.on_demand_url = on_demand_url  # type: str
        self.need_status_notify = need_status_notify  # type: bool

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['DomainName'] = self.domain_name
        result['NotifyUrl'] = self.notify_url
        result['OnDemandUrl'] = self.on_demand_url
        result['NeedStatusNotify'] = self.need_status_notify
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.domain_name = map.get('DomainName')
        self.notify_url = map.get('NotifyUrl')
        self.on_demand_url = map.get('OnDemandUrl')
        self.need_status_notify = map.get('NeedStatusNotify')
        return self


class UpdateLiveRecordNotifyConfigResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeLiveStreamsBlockListRequest(TeaModel):
    def __init__(self, security_token=None, domain_name=None, page_num=None, page_size=None):
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['DomainName'] = self.domain_name
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.domain_name = map.get('DomainName')
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        return self


class DescribeLiveStreamsBlockListResponse(TeaModel):
    def __init__(self, request_id=None, domain_name=None, page_num=None, page_size=None, total_num=None,
                 total_page=None, stream_urls=None):
        self.request_id = request_id    # type: str
        self.domain_name = domain_name  # type: str
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int
        self.total_num = total_num      # type: int
        self.total_page = total_page    # type: int
        self.stream_urls = stream_urls  # type: DescribeLiveStreamsBlockListResponseStreamUrls

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.page_num, 'page_num')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_num, 'total_num')
        self.validate_required(self.total_page, 'total_page')
        self.validate_required(self.stream_urls, 'stream_urls')
        if self.stream_urls:
            self.stream_urls.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['DomainName'] = self.domain_name
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        result['TotalNum'] = self.total_num
        result['TotalPage'] = self.total_page
        if self.stream_urls is not None:
            result['StreamUrls'] = self.stream_urls.to_map()
        else:
            result['StreamUrls'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.domain_name = map.get('DomainName')
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        self.total_num = map.get('TotalNum')
        self.total_page = map.get('TotalPage')
        if map.get('StreamUrls') is not None:
            temp_model = DescribeLiveStreamsBlockListResponseStreamUrls()
            self.stream_urls = temp_model.from_map(map['StreamUrls'])
        else:
            self.stream_urls = None
        return self


class DescribeLiveStreamsBlockListResponseStreamUrls(TeaModel):
    def __init__(self, stream_url=None):
        self.stream_url = stream_url    # type: List[str]

    def validate(self):
        self.validate_required(self.stream_url, 'stream_url')

    def to_map(self):
        result = {}
        result['StreamUrl'] = self.stream_url
        return result

    def from_map(self, map={}):
        self.stream_url = map.get('StreamUrl')
        return self


class DescribeLiveStreamOnlineUserNumRequest(TeaModel):
    def __init__(self, security_token=None, domain_name=None, app_name=None, stream_name=None, start_time=None,
                 end_time=None):
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str
        self.stream_name = stream_name  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        result['StreamName'] = self.stream_name
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        self.stream_name = map.get('StreamName')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        return self


class DescribeLiveStreamOnlineUserNumResponse(TeaModel):
    def __init__(self, request_id=None, total_user_number=None, online_user_info=None):
        self.request_id = request_id    # type: str
        self.total_user_number = total_user_number  # type: int
        self.online_user_info = online_user_info  # type: DescribeLiveStreamOnlineUserNumResponseOnlineUserInfo

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.total_user_number, 'total_user_number')
        self.validate_required(self.online_user_info, 'online_user_info')
        if self.online_user_info:
            self.online_user_info.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['TotalUserNumber'] = self.total_user_number
        if self.online_user_info is not None:
            result['OnlineUserInfo'] = self.online_user_info.to_map()
        else:
            result['OnlineUserInfo'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.total_user_number = map.get('TotalUserNumber')
        if map.get('OnlineUserInfo') is not None:
            temp_model = DescribeLiveStreamOnlineUserNumResponseOnlineUserInfo()
            self.online_user_info = temp_model.from_map(map['OnlineUserInfo'])
        else:
            self.online_user_info = None
        return self


class DescribeLiveStreamOnlineUserNumResponseOnlineUserInfoLiveStreamOnlineUserNumInfo(TeaModel):
    def __init__(self, stream_url=None, user_number=None, time=None):
        self.stream_url = stream_url    # type: str
        self.user_number = user_number  # type: int
        self.time = time                # type: str

    def validate(self):
        self.validate_required(self.stream_url, 'stream_url')
        self.validate_required(self.user_number, 'user_number')
        self.validate_required(self.time, 'time')

    def to_map(self):
        result = {}
        result['StreamUrl'] = self.stream_url
        result['UserNumber'] = self.user_number
        result['Time'] = self.time
        return result

    def from_map(self, map={}):
        self.stream_url = map.get('StreamUrl')
        self.user_number = map.get('UserNumber')
        self.time = map.get('Time')
        return self


class DescribeLiveStreamOnlineUserNumResponseOnlineUserInfo(TeaModel):
    def __init__(self, live_stream_online_user_num_info=None):
        self.live_stream_online_user_num_info = live_stream_online_user_num_info  # type: List[DescribeLiveStreamOnlineUserNumResponseOnlineUserInfoLiveStreamOnlineUserNumInfo]

    def validate(self):
        self.validate_required(self.live_stream_online_user_num_info, 'live_stream_online_user_num_info')
        if self.live_stream_online_user_num_info:
            for k in self.live_stream_online_user_num_info:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['LiveStreamOnlineUserNumInfo'] = []
        if self.live_stream_online_user_num_info is not None:
            for k in self.live_stream_online_user_num_info:
                result['LiveStreamOnlineUserNumInfo'].append(k.to_map() if k else None)
        else:
            result['LiveStreamOnlineUserNumInfo'] = None
        return result

    def from_map(self, map={}):
        self.live_stream_online_user_num_info = []
        if map.get('LiveStreamOnlineUserNumInfo') is not None:
            for k in map.get('LiveStreamOnlineUserNumInfo'):
                temp_model = DescribeLiveStreamOnlineUserNumResponseOnlineUserInfoLiveStreamOnlineUserNumInfo()
                self.live_stream_online_user_num_info.append(temp_model.from_map(k))
        else:
            self.live_stream_online_user_num_info = None
        return self


class DescribeLiveStreamsPublishListRequest(TeaModel):
    def __init__(self, domain_name=None, app_name=None, stream_name=None, start_time=None, end_time=None,
                 page_size=None, page_number=None, stream_type=None, query_type=None, order_by=None):
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str
        self.stream_name = stream_name  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.page_size = page_size      # type: int
        self.page_number = page_number  # type: int
        self.stream_type = stream_type  # type: str
        self.query_type = query_type    # type: str
        self.order_by = order_by        # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        result['StreamName'] = self.stream_name
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['PageSize'] = self.page_size
        result['PageNumber'] = self.page_number
        result['StreamType'] = self.stream_type
        result['QueryType'] = self.query_type
        result['OrderBy'] = self.order_by
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        self.stream_name = map.get('StreamName')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.page_size = map.get('PageSize')
        self.page_number = map.get('PageNumber')
        self.stream_type = map.get('StreamType')
        self.query_type = map.get('QueryType')
        self.order_by = map.get('OrderBy')
        return self


class DescribeLiveStreamsPublishListResponse(TeaModel):
    def __init__(self, request_id=None, page_num=None, page_size=None, total_num=None, total_page=None,
                 publish_info=None):
        self.request_id = request_id    # type: str
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int
        self.total_num = total_num      # type: int
        self.total_page = total_page    # type: int
        self.publish_info = publish_info  # type: DescribeLiveStreamsPublishListResponsePublishInfo

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.page_num, 'page_num')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_num, 'total_num')
        self.validate_required(self.total_page, 'total_page')
        self.validate_required(self.publish_info, 'publish_info')
        if self.publish_info:
            self.publish_info.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        result['TotalNum'] = self.total_num
        result['TotalPage'] = self.total_page
        if self.publish_info is not None:
            result['PublishInfo'] = self.publish_info.to_map()
        else:
            result['PublishInfo'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        self.total_num = map.get('TotalNum')
        self.total_page = map.get('TotalPage')
        if map.get('PublishInfo') is not None:
            temp_model = DescribeLiveStreamsPublishListResponsePublishInfo()
            self.publish_info = temp_model.from_map(map['PublishInfo'])
        else:
            self.publish_info = None
        return self


class DescribeLiveStreamsPublishListResponsePublishInfoLiveStreamPublishInfo(TeaModel):
    def __init__(self, domain_name=None, app_name=None, stream_name=None, stream_url=None, publish_time=None,
                 stop_time=None, publish_url=None, client_addr=None, edge_node_addr=None, publish_domain=None,
                 publish_type=None, transcoded=None, transcode_id=None):
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str
        self.stream_name = stream_name  # type: str
        self.stream_url = stream_url    # type: str
        self.publish_time = publish_time  # type: str
        self.stop_time = stop_time      # type: str
        self.publish_url = publish_url  # type: str
        self.client_addr = client_addr  # type: str
        self.edge_node_addr = edge_node_addr  # type: str
        self.publish_domain = publish_domain  # type: str
        self.publish_type = publish_type  # type: str
        self.transcoded = transcoded    # type: str
        self.transcode_id = transcode_id  # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.app_name, 'app_name')
        self.validate_required(self.stream_name, 'stream_name')
        self.validate_required(self.stream_url, 'stream_url')
        self.validate_required(self.publish_time, 'publish_time')
        self.validate_required(self.stop_time, 'stop_time')
        self.validate_required(self.publish_url, 'publish_url')
        self.validate_required(self.client_addr, 'client_addr')
        self.validate_required(self.edge_node_addr, 'edge_node_addr')
        self.validate_required(self.publish_domain, 'publish_domain')
        self.validate_required(self.publish_type, 'publish_type')
        self.validate_required(self.transcoded, 'transcoded')
        self.validate_required(self.transcode_id, 'transcode_id')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        result['StreamName'] = self.stream_name
        result['StreamUrl'] = self.stream_url
        result['PublishTime'] = self.publish_time
        result['StopTime'] = self.stop_time
        result['PublishUrl'] = self.publish_url
        result['ClientAddr'] = self.client_addr
        result['EdgeNodeAddr'] = self.edge_node_addr
        result['PublishDomain'] = self.publish_domain
        result['PublishType'] = self.publish_type
        result['Transcoded'] = self.transcoded
        result['TranscodeId'] = self.transcode_id
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        self.stream_name = map.get('StreamName')
        self.stream_url = map.get('StreamUrl')
        self.publish_time = map.get('PublishTime')
        self.stop_time = map.get('StopTime')
        self.publish_url = map.get('PublishUrl')
        self.client_addr = map.get('ClientAddr')
        self.edge_node_addr = map.get('EdgeNodeAddr')
        self.publish_domain = map.get('PublishDomain')
        self.publish_type = map.get('PublishType')
        self.transcoded = map.get('Transcoded')
        self.transcode_id = map.get('TranscodeId')
        return self


class DescribeLiveStreamsPublishListResponsePublishInfo(TeaModel):
    def __init__(self, live_stream_publish_info=None):
        self.live_stream_publish_info = live_stream_publish_info  # type: List[DescribeLiveStreamsPublishListResponsePublishInfoLiveStreamPublishInfo]

    def validate(self):
        self.validate_required(self.live_stream_publish_info, 'live_stream_publish_info')
        if self.live_stream_publish_info:
            for k in self.live_stream_publish_info:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['LiveStreamPublishInfo'] = []
        if self.live_stream_publish_info is not None:
            for k in self.live_stream_publish_info:
                result['LiveStreamPublishInfo'].append(k.to_map() if k else None)
        else:
            result['LiveStreamPublishInfo'] = None
        return result

    def from_map(self, map={}):
        self.live_stream_publish_info = []
        if map.get('LiveStreamPublishInfo') is not None:
            for k in map.get('LiveStreamPublishInfo'):
                temp_model = DescribeLiveStreamsPublishListResponsePublishInfoLiveStreamPublishInfo()
                self.live_stream_publish_info.append(temp_model.from_map(k))
        else:
            self.live_stream_publish_info = None
        return self


class DescribeLiveStreamsOnlineListRequest(TeaModel):
    def __init__(self, domain_name=None, app_name=None, stream_name=None, page_size=None, page_num=None,
                 stream_type=None, query_type=None):
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str
        self.stream_name = stream_name  # type: str
        self.page_size = page_size      # type: int
        self.page_num = page_num        # type: int
        self.stream_type = stream_type  # type: str
        self.query_type = query_type    # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        result['StreamName'] = self.stream_name
        result['PageSize'] = self.page_size
        result['PageNum'] = self.page_num
        result['StreamType'] = self.stream_type
        result['QueryType'] = self.query_type
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        self.stream_name = map.get('StreamName')
        self.page_size = map.get('PageSize')
        self.page_num = map.get('PageNum')
        self.stream_type = map.get('StreamType')
        self.query_type = map.get('QueryType')
        return self


class DescribeLiveStreamsOnlineListResponse(TeaModel):
    def __init__(self, request_id=None, page_num=None, page_size=None, total_num=None, total_page=None,
                 online_info=None):
        self.request_id = request_id    # type: str
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int
        self.total_num = total_num      # type: int
        self.total_page = total_page    # type: int
        self.online_info = online_info  # type: DescribeLiveStreamsOnlineListResponseOnlineInfo

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.page_num, 'page_num')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total_num, 'total_num')
        self.validate_required(self.total_page, 'total_page')
        self.validate_required(self.online_info, 'online_info')
        if self.online_info:
            self.online_info.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        result['TotalNum'] = self.total_num
        result['TotalPage'] = self.total_page
        if self.online_info is not None:
            result['OnlineInfo'] = self.online_info.to_map()
        else:
            result['OnlineInfo'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        self.total_num = map.get('TotalNum')
        self.total_page = map.get('TotalPage')
        if map.get('OnlineInfo') is not None:
            temp_model = DescribeLiveStreamsOnlineListResponseOnlineInfo()
            self.online_info = temp_model.from_map(map['OnlineInfo'])
        else:
            self.online_info = None
        return self


class DescribeLiveStreamsOnlineListResponseOnlineInfoLiveStreamOnlineInfo(TeaModel):
    def __init__(self, domain_name=None, app_name=None, stream_name=None, publish_time=None, publish_url=None,
                 publish_domain=None, publish_type=None, transcoded=None, transcode_id=None, server_ip=None, client_ip=None,
                 video_codec_id=None, video_data_rate=None, frame_rate=None, width=None, height=None, audio_codec_id=None,
                 audio_data_rate=None):
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str
        self.stream_name = stream_name  # type: str
        self.publish_time = publish_time  # type: str
        self.publish_url = publish_url  # type: str
        self.publish_domain = publish_domain  # type: str
        self.publish_type = publish_type  # type: str
        self.transcoded = transcoded    # type: str
        self.transcode_id = transcode_id  # type: str
        self.server_ip = server_ip      # type: str
        self.client_ip = client_ip      # type: str
        self.video_codec_id = video_codec_id  # type: int
        self.video_data_rate = video_data_rate  # type: int
        self.frame_rate = frame_rate    # type: int
        self.width = width              # type: int
        self.height = height            # type: int
        self.audio_codec_id = audio_codec_id  # type: int
        self.audio_data_rate = audio_data_rate  # type: int

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.app_name, 'app_name')
        self.validate_required(self.stream_name, 'stream_name')
        self.validate_required(self.publish_time, 'publish_time')
        self.validate_required(self.publish_url, 'publish_url')
        self.validate_required(self.publish_domain, 'publish_domain')
        self.validate_required(self.publish_type, 'publish_type')
        self.validate_required(self.transcoded, 'transcoded')
        self.validate_required(self.transcode_id, 'transcode_id')
        self.validate_required(self.server_ip, 'server_ip')
        self.validate_required(self.client_ip, 'client_ip')
        self.validate_required(self.video_codec_id, 'video_codec_id')
        self.validate_required(self.video_data_rate, 'video_data_rate')
        self.validate_required(self.frame_rate, 'frame_rate')
        self.validate_required(self.width, 'width')
        self.validate_required(self.height, 'height')
        self.validate_required(self.audio_codec_id, 'audio_codec_id')
        self.validate_required(self.audio_data_rate, 'audio_data_rate')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        result['StreamName'] = self.stream_name
        result['PublishTime'] = self.publish_time
        result['PublishUrl'] = self.publish_url
        result['PublishDomain'] = self.publish_domain
        result['PublishType'] = self.publish_type
        result['Transcoded'] = self.transcoded
        result['TranscodeId'] = self.transcode_id
        result['ServerIp'] = self.server_ip
        result['ClientIp'] = self.client_ip
        result['VideoCodecId'] = self.video_codec_id
        result['VideoDataRate'] = self.video_data_rate
        result['FrameRate'] = self.frame_rate
        result['Width'] = self.width
        result['Height'] = self.height
        result['AudioCodecId'] = self.audio_codec_id
        result['AudioDataRate'] = self.audio_data_rate
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        self.stream_name = map.get('StreamName')
        self.publish_time = map.get('PublishTime')
        self.publish_url = map.get('PublishUrl')
        self.publish_domain = map.get('PublishDomain')
        self.publish_type = map.get('PublishType')
        self.transcoded = map.get('Transcoded')
        self.transcode_id = map.get('TranscodeId')
        self.server_ip = map.get('ServerIp')
        self.client_ip = map.get('ClientIp')
        self.video_codec_id = map.get('VideoCodecId')
        self.video_data_rate = map.get('VideoDataRate')
        self.frame_rate = map.get('FrameRate')
        self.width = map.get('Width')
        self.height = map.get('Height')
        self.audio_codec_id = map.get('AudioCodecId')
        self.audio_data_rate = map.get('AudioDataRate')
        return self


class DescribeLiveStreamsOnlineListResponseOnlineInfo(TeaModel):
    def __init__(self, live_stream_online_info=None):
        self.live_stream_online_info = live_stream_online_info  # type: List[DescribeLiveStreamsOnlineListResponseOnlineInfoLiveStreamOnlineInfo]

    def validate(self):
        self.validate_required(self.live_stream_online_info, 'live_stream_online_info')
        if self.live_stream_online_info:
            for k in self.live_stream_online_info:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['LiveStreamOnlineInfo'] = []
        if self.live_stream_online_info is not None:
            for k in self.live_stream_online_info:
                result['LiveStreamOnlineInfo'].append(k.to_map() if k else None)
        else:
            result['LiveStreamOnlineInfo'] = None
        return result

    def from_map(self, map={}):
        self.live_stream_online_info = []
        if map.get('LiveStreamOnlineInfo') is not None:
            for k in map.get('LiveStreamOnlineInfo'):
                temp_model = DescribeLiveStreamsOnlineListResponseOnlineInfoLiveStreamOnlineInfo()
                self.live_stream_online_info.append(temp_model.from_map(k))
        else:
            self.live_stream_online_info = None
        return self


class DescribeLiveStreamsControlHistoryRequest(TeaModel):
    def __init__(self, security_token=None, domain_name=None, app_name=None, start_time=None, end_time=None):
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        return self


class DescribeLiveStreamsControlHistoryResponse(TeaModel):
    def __init__(self, request_id=None, control_info=None):
        self.request_id = request_id    # type: str
        self.control_info = control_info  # type: DescribeLiveStreamsControlHistoryResponseControlInfo

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.control_info, 'control_info')
        if self.control_info:
            self.control_info.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.control_info is not None:
            result['ControlInfo'] = self.control_info.to_map()
        else:
            result['ControlInfo'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('ControlInfo') is not None:
            temp_model = DescribeLiveStreamsControlHistoryResponseControlInfo()
            self.control_info = temp_model.from_map(map['ControlInfo'])
        else:
            self.control_info = None
        return self


class DescribeLiveStreamsControlHistoryResponseControlInfoLiveStreamControlInfo(TeaModel):
    def __init__(self, stream_name=None, client_ip=None, action=None, time_stamp=None):
        self.stream_name = stream_name  # type: str
        self.client_ip = client_ip      # type: str
        self.action = action            # type: str
        self.time_stamp = time_stamp    # type: str

    def validate(self):
        self.validate_required(self.stream_name, 'stream_name')
        self.validate_required(self.client_ip, 'client_ip')
        self.validate_required(self.action, 'action')
        self.validate_required(self.time_stamp, 'time_stamp')

    def to_map(self):
        result = {}
        result['StreamName'] = self.stream_name
        result['ClientIP'] = self.client_ip
        result['Action'] = self.action
        result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, map={}):
        self.stream_name = map.get('StreamName')
        self.client_ip = map.get('ClientIP')
        self.action = map.get('Action')
        self.time_stamp = map.get('TimeStamp')
        return self


class DescribeLiveStreamsControlHistoryResponseControlInfo(TeaModel):
    def __init__(self, live_stream_control_info=None):
        self.live_stream_control_info = live_stream_control_info  # type: List[DescribeLiveStreamsControlHistoryResponseControlInfoLiveStreamControlInfo]

    def validate(self):
        self.validate_required(self.live_stream_control_info, 'live_stream_control_info')
        if self.live_stream_control_info:
            for k in self.live_stream_control_info:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['LiveStreamControlInfo'] = []
        if self.live_stream_control_info is not None:
            for k in self.live_stream_control_info:
                result['LiveStreamControlInfo'].append(k.to_map() if k else None)
        else:
            result['LiveStreamControlInfo'] = None
        return result

    def from_map(self, map={}):
        self.live_stream_control_info = []
        if map.get('LiveStreamControlInfo') is not None:
            for k in map.get('LiveStreamControlInfo'):
                temp_model = DescribeLiveStreamsControlHistoryResponseControlInfoLiveStreamControlInfo()
                self.live_stream_control_info.append(temp_model.from_map(k))
        else:
            self.live_stream_control_info = None
        return self


class AddLiveStreamTranscodeRequest(TeaModel):
    def __init__(self, domain=None, app=None, template=None, lazy=None, watermark=None, mix=None, only_audio=None,
                 water_pattern=None):
        self.domain = domain            # type: str
        self.app = app                  # type: str
        self.template = template        # type: str
        self.lazy = lazy                # type: str
        self.watermark = watermark      # type: str
        self.mix = mix                  # type: str
        self.only_audio = only_audio    # type: str
        self.water_pattern = water_pattern  # type: str

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.app, 'app')
        self.validate_required(self.template, 'template')

    def to_map(self):
        result = {}
        result['Domain'] = self.domain
        result['App'] = self.app
        result['Template'] = self.template
        result['Lazy'] = self.lazy
        result['Watermark'] = self.watermark
        result['Mix'] = self.mix
        result['OnlyAudio'] = self.only_audio
        result['WaterPattern'] = self.water_pattern
        return result

    def from_map(self, map={}):
        self.domain = map.get('Domain')
        self.app = map.get('App')
        self.template = map.get('Template')
        self.lazy = map.get('Lazy')
        self.watermark = map.get('Watermark')
        self.mix = map.get('Mix')
        self.only_audio = map.get('OnlyAudio')
        self.water_pattern = map.get('WaterPattern')
        return self


class AddLiveStreamTranscodeResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DeleteLiveStreamTranscodeRequest(TeaModel):
    def __init__(self, security_token=None, domain=None, app=None, template=None):
        self.security_token = security_token  # type: str
        self.domain = domain            # type: str
        self.app = app                  # type: str
        self.template = template        # type: str

    def validate(self):
        self.validate_required(self.domain, 'domain')
        self.validate_required(self.app, 'app')
        self.validate_required(self.template, 'template')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['Domain'] = self.domain
        result['App'] = self.app
        result['Template'] = self.template
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.domain = map.get('Domain')
        self.app = map.get('App')
        self.template = map.get('Template')
        return self


class DeleteLiveStreamTranscodeResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeLiveStreamsFrameRateAndBitRateDataRequest(TeaModel):
    def __init__(self, security_token=None, domain_name=None, app_name=None, stream_name=None, start_time=None,
                 end_time=None):
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str
        self.stream_name = stream_name  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.app_name, 'app_name')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        result['StreamName'] = self.stream_name
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        self.stream_name = map.get('StreamName')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        return self


class DescribeLiveStreamsFrameRateAndBitRateDataResponse(TeaModel):
    def __init__(self, request_id=None, frame_rate_and_bit_rate_infos=None):
        self.request_id = request_id    # type: str
        self.frame_rate_and_bit_rate_infos = frame_rate_and_bit_rate_infos  # type: DescribeLiveStreamsFrameRateAndBitRateDataResponseFrameRateAndBitRateInfos

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.frame_rate_and_bit_rate_infos, 'frame_rate_and_bit_rate_infos')
        if self.frame_rate_and_bit_rate_infos:
            self.frame_rate_and_bit_rate_infos.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.frame_rate_and_bit_rate_infos is not None:
            result['FrameRateAndBitRateInfos'] = self.frame_rate_and_bit_rate_infos.to_map()
        else:
            result['FrameRateAndBitRateInfos'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('FrameRateAndBitRateInfos') is not None:
            temp_model = DescribeLiveStreamsFrameRateAndBitRateDataResponseFrameRateAndBitRateInfos()
            self.frame_rate_and_bit_rate_infos = temp_model.from_map(map['FrameRateAndBitRateInfos'])
        else:
            self.frame_rate_and_bit_rate_infos = None
        return self


class DescribeLiveStreamsFrameRateAndBitRateDataResponseFrameRateAndBitRateInfosFrameRateAndBitRateInfo(TeaModel):
    def __init__(self, stream_url=None, video_frame_rate=None, audio_frame_rate=None, bit_rate=None, time=None):
        self.stream_url = stream_url    # type: str
        self.video_frame_rate = video_frame_rate  # type: float
        self.audio_frame_rate = audio_frame_rate  # type: float
        self.bit_rate = bit_rate        # type: float
        self.time = time                # type: str

    def validate(self):
        self.validate_required(self.stream_url, 'stream_url')
        self.validate_required(self.video_frame_rate, 'video_frame_rate')
        self.validate_required(self.audio_frame_rate, 'audio_frame_rate')
        self.validate_required(self.bit_rate, 'bit_rate')
        self.validate_required(self.time, 'time')

    def to_map(self):
        result = {}
        result['StreamUrl'] = self.stream_url
        result['VideoFrameRate'] = self.video_frame_rate
        result['AudioFrameRate'] = self.audio_frame_rate
        result['BitRate'] = self.bit_rate
        result['Time'] = self.time
        return result

    def from_map(self, map={}):
        self.stream_url = map.get('StreamUrl')
        self.video_frame_rate = map.get('VideoFrameRate')
        self.audio_frame_rate = map.get('AudioFrameRate')
        self.bit_rate = map.get('BitRate')
        self.time = map.get('Time')
        return self


class DescribeLiveStreamsFrameRateAndBitRateDataResponseFrameRateAndBitRateInfos(TeaModel):
    def __init__(self, frame_rate_and_bit_rate_info=None):
        self.frame_rate_and_bit_rate_info = frame_rate_and_bit_rate_info  # type: List[DescribeLiveStreamsFrameRateAndBitRateDataResponseFrameRateAndBitRateInfosFrameRateAndBitRateInfo]

    def validate(self):
        self.validate_required(self.frame_rate_and_bit_rate_info, 'frame_rate_and_bit_rate_info')
        if self.frame_rate_and_bit_rate_info:
            for k in self.frame_rate_and_bit_rate_info:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['FrameRateAndBitRateInfo'] = []
        if self.frame_rate_and_bit_rate_info is not None:
            for k in self.frame_rate_and_bit_rate_info:
                result['FrameRateAndBitRateInfo'].append(k.to_map() if k else None)
        else:
            result['FrameRateAndBitRateInfo'] = None
        return result

    def from_map(self, map={}):
        self.frame_rate_and_bit_rate_info = []
        if map.get('FrameRateAndBitRateInfo') is not None:
            for k in map.get('FrameRateAndBitRateInfo'):
                temp_model = DescribeLiveStreamsFrameRateAndBitRateDataResponseFrameRateAndBitRateInfosFrameRateAndBitRateInfo()
                self.frame_rate_and_bit_rate_info.append(temp_model.from_map(k))
        else:
            self.frame_rate_and_bit_rate_info = None
        return self


class ForbidLiveStreamRequest(TeaModel):
    def __init__(self, domain_name=None, app_name=None, stream_name=None, live_stream_type=None, oneshot=None,
                 resume_time=None):
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str
        self.stream_name = stream_name  # type: str
        self.live_stream_type = live_stream_type  # type: str
        self.oneshot = oneshot          # type: str
        self.resume_time = resume_time  # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.app_name, 'app_name')
        self.validate_required(self.stream_name, 'stream_name')
        self.validate_required(self.live_stream_type, 'live_stream_type')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        result['StreamName'] = self.stream_name
        result['LiveStreamType'] = self.live_stream_type
        result['Oneshot'] = self.oneshot
        result['ResumeTime'] = self.resume_time
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        self.stream_name = map.get('StreamName')
        self.live_stream_type = map.get('LiveStreamType')
        self.oneshot = map.get('Oneshot')
        self.resume_time = map.get('ResumeTime')
        return self


class ForbidLiveStreamResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeLiveStreamTranscodeInfoRequest(TeaModel):
    def __init__(self, domain_transcode_name=None):
        self.domain_transcode_name = domain_transcode_name  # type: str

    def validate(self):
        self.validate_required(self.domain_transcode_name, 'domain_transcode_name')

    def to_map(self):
        result = {}
        result['DomainTranscodeName'] = self.domain_transcode_name
        return result

    def from_map(self, map={}):
        self.domain_transcode_name = map.get('DomainTranscodeName')
        return self


class DescribeLiveStreamTranscodeInfoResponse(TeaModel):
    def __init__(self, request_id=None, domain_transcode_list=None):
        self.request_id = request_id    # type: str
        self.domain_transcode_list = domain_transcode_list  # type: DescribeLiveStreamTranscodeInfoResponseDomainTranscodeList

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.domain_transcode_list, 'domain_transcode_list')
        if self.domain_transcode_list:
            self.domain_transcode_list.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.domain_transcode_list is not None:
            result['DomainTranscodeList'] = self.domain_transcode_list.to_map()
        else:
            result['DomainTranscodeList'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('DomainTranscodeList') is not None:
            temp_model = DescribeLiveStreamTranscodeInfoResponseDomainTranscodeList()
            self.domain_transcode_list = temp_model.from_map(map['DomainTranscodeList'])
        else:
            self.domain_transcode_list = None
        return self


class DescribeLiveStreamTranscodeInfoResponseDomainTranscodeListDomainTranscodeInfoCustomTranscodeParameters(TeaModel):
    def __init__(self, rts_flag=None, bframes=None, video_bitrate=None, fps=None, height=None, width=None,
                 template_type=None, video_profile=None, gop=None, audio_bitrate=None, audio_profile=None, audio_codec=None,
                 audio_rate=None, audio_channel_num=None):
        self.rts_flag = rts_flag        # type: str
        self.bframes = bframes          # type: str
        self.video_bitrate = video_bitrate  # type: int
        self.fps = fps                  # type: int
        self.height = height            # type: int
        self.width = width              # type: int
        self.template_type = template_type  # type: str
        self.video_profile = video_profile  # type: str
        self.gop = gop                  # type: str
        self.audio_bitrate = audio_bitrate  # type: int
        self.audio_profile = audio_profile  # type: str
        self.audio_codec = audio_codec  # type: str
        self.audio_rate = audio_rate    # type: int
        self.audio_channel_num = audio_channel_num  # type: int

    def validate(self):
        self.validate_required(self.rts_flag, 'rts_flag')
        self.validate_required(self.bframes, 'bframes')
        self.validate_required(self.video_bitrate, 'video_bitrate')
        self.validate_required(self.fps, 'fps')
        self.validate_required(self.height, 'height')
        self.validate_required(self.width, 'width')
        self.validate_required(self.template_type, 'template_type')
        self.validate_required(self.video_profile, 'video_profile')
        self.validate_required(self.gop, 'gop')
        self.validate_required(self.audio_bitrate, 'audio_bitrate')
        self.validate_required(self.audio_profile, 'audio_profile')
        self.validate_required(self.audio_codec, 'audio_codec')
        self.validate_required(self.audio_rate, 'audio_rate')
        self.validate_required(self.audio_channel_num, 'audio_channel_num')

    def to_map(self):
        result = {}
        result['RtsFlag'] = self.rts_flag
        result['Bframes'] = self.bframes
        result['VideoBitrate'] = self.video_bitrate
        result['FPS'] = self.fps
        result['Height'] = self.height
        result['Width'] = self.width
        result['TemplateType'] = self.template_type
        result['VideoProfile'] = self.video_profile
        result['Gop'] = self.gop
        result['AudioBitrate'] = self.audio_bitrate
        result['AudioProfile'] = self.audio_profile
        result['AudioCodec'] = self.audio_codec
        result['AudioRate'] = self.audio_rate
        result['AudioChannelNum'] = self.audio_channel_num
        return result

    def from_map(self, map={}):
        self.rts_flag = map.get('RtsFlag')
        self.bframes = map.get('Bframes')
        self.video_bitrate = map.get('VideoBitrate')
        self.fps = map.get('FPS')
        self.height = map.get('Height')
        self.width = map.get('Width')
        self.template_type = map.get('TemplateType')
        self.video_profile = map.get('VideoProfile')
        self.gop = map.get('Gop')
        self.audio_bitrate = map.get('AudioBitrate')
        self.audio_profile = map.get('AudioProfile')
        self.audio_codec = map.get('AudioCodec')
        self.audio_rate = map.get('AudioRate')
        self.audio_channel_num = map.get('AudioChannelNum')
        return self


class DescribeLiveStreamTranscodeInfoResponseDomainTranscodeListDomainTranscodeInfo(TeaModel):
    def __init__(self, transcode_app=None, transcode_name=None, transcode_template=None,
                 custom_transcode_parameters=None):
        self.transcode_app = transcode_app  # type: str
        self.transcode_name = transcode_name  # type: str
        self.transcode_template = transcode_template  # type: str
        self.custom_transcode_parameters = custom_transcode_parameters  # type: DescribeLiveStreamTranscodeInfoResponseDomainTranscodeListDomainTranscodeInfoCustomTranscodeParameters

    def validate(self):
        self.validate_required(self.transcode_app, 'transcode_app')
        self.validate_required(self.transcode_name, 'transcode_name')
        self.validate_required(self.transcode_template, 'transcode_template')
        self.validate_required(self.custom_transcode_parameters, 'custom_transcode_parameters')
        if self.custom_transcode_parameters:
            self.custom_transcode_parameters.validate()

    def to_map(self):
        result = {}
        result['TranscodeApp'] = self.transcode_app
        result['TranscodeName'] = self.transcode_name
        result['TranscodeTemplate'] = self.transcode_template
        if self.custom_transcode_parameters is not None:
            result['CustomTranscodeParameters'] = self.custom_transcode_parameters.to_map()
        else:
            result['CustomTranscodeParameters'] = None
        return result

    def from_map(self, map={}):
        self.transcode_app = map.get('TranscodeApp')
        self.transcode_name = map.get('TranscodeName')
        self.transcode_template = map.get('TranscodeTemplate')
        if map.get('CustomTranscodeParameters') is not None:
            temp_model = DescribeLiveStreamTranscodeInfoResponseDomainTranscodeListDomainTranscodeInfoCustomTranscodeParameters()
            self.custom_transcode_parameters = temp_model.from_map(map['CustomTranscodeParameters'])
        else:
            self.custom_transcode_parameters = None
        return self


class DescribeLiveStreamTranscodeInfoResponseDomainTranscodeList(TeaModel):
    def __init__(self, domain_transcode_info=None):
        self.domain_transcode_info = domain_transcode_info  # type: List[DescribeLiveStreamTranscodeInfoResponseDomainTranscodeListDomainTranscodeInfo]

    def validate(self):
        self.validate_required(self.domain_transcode_info, 'domain_transcode_info')
        if self.domain_transcode_info:
            for k in self.domain_transcode_info:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['DomainTranscodeInfo'] = []
        if self.domain_transcode_info is not None:
            for k in self.domain_transcode_info:
                result['DomainTranscodeInfo'].append(k.to_map() if k else None)
        else:
            result['DomainTranscodeInfo'] = None
        return result

    def from_map(self, map={}):
        self.domain_transcode_info = []
        if map.get('DomainTranscodeInfo') is not None:
            for k in map.get('DomainTranscodeInfo'):
                temp_model = DescribeLiveStreamTranscodeInfoResponseDomainTranscodeListDomainTranscodeInfo()
                self.domain_transcode_info.append(temp_model.from_map(k))
        else:
            self.domain_transcode_info = None
        return self


class SetLiveStreamsNotifyUrlConfigRequest(TeaModel):
    def __init__(self, domain_name=None, notify_url=None):
        self.domain_name = domain_name  # type: str
        self.notify_url = notify_url    # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.notify_url, 'notify_url')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['NotifyUrl'] = self.notify_url
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.notify_url = map.get('NotifyUrl')
        return self


class SetLiveStreamsNotifyUrlConfigResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class ResumeLiveStreamRequest(TeaModel):
    def __init__(self, security_token=None, domain_name=None, live_stream_type=None, app_name=None,
                 stream_name=None):
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str
        self.live_stream_type = live_stream_type  # type: str
        self.app_name = app_name        # type: str
        self.stream_name = stream_name  # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.live_stream_type, 'live_stream_type')
        self.validate_required(self.app_name, 'app_name')
        self.validate_required(self.stream_name, 'stream_name')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['DomainName'] = self.domain_name
        result['LiveStreamType'] = self.live_stream_type
        result['AppName'] = self.app_name
        result['StreamName'] = self.stream_name
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.domain_name = map.get('DomainName')
        self.live_stream_type = map.get('LiveStreamType')
        self.app_name = map.get('AppName')
        self.stream_name = map.get('StreamName')
        return self


class ResumeLiveStreamResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class AddLiveAppSnapshotConfigRequest(TeaModel):
    def __init__(self, security_token=None, domain_name=None, app_name=None, time_interval=None, oss_endpoint=None,
                 oss_bucket=None, overwrite_oss_object=None, sequence_oss_object=None, callback=None):
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str
        self.time_interval = time_interval  # type: int
        self.oss_endpoint = oss_endpoint  # type: str
        self.oss_bucket = oss_bucket    # type: str
        self.overwrite_oss_object = overwrite_oss_object  # type: str
        self.sequence_oss_object = sequence_oss_object  # type: str
        self.callback = callback        # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.app_name, 'app_name')
        self.validate_required(self.time_interval, 'time_interval')
        self.validate_required(self.oss_endpoint, 'oss_endpoint')
        self.validate_required(self.oss_bucket, 'oss_bucket')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        result['TimeInterval'] = self.time_interval
        result['OssEndpoint'] = self.oss_endpoint
        result['OssBucket'] = self.oss_bucket
        result['OverwriteOssObject'] = self.overwrite_oss_object
        result['SequenceOssObject'] = self.sequence_oss_object
        result['Callback'] = self.callback
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        self.time_interval = map.get('TimeInterval')
        self.oss_endpoint = map.get('OssEndpoint')
        self.oss_bucket = map.get('OssBucket')
        self.overwrite_oss_object = map.get('OverwriteOssObject')
        self.sequence_oss_object = map.get('SequenceOssObject')
        self.callback = map.get('Callback')
        return self


class AddLiveAppSnapshotConfigResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class AddLiveAppRecordConfigRequest(TeaModel):
    def __init__(self, security_token=None, domain_name=None, app_name=None, oss_endpoint=None, oss_bucket=None,
                 record_format=None, stream_name=None, start_time=None, end_time=None, on_demand=None):
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str
        self.oss_endpoint = oss_endpoint  # type: str
        self.oss_bucket = oss_bucket    # type: str
        self.record_format = record_format  # type: List[AddLiveAppRecordConfigRequestRecordFormat]
        self.stream_name = stream_name  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.on_demand = on_demand      # type: int

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.app_name, 'app_name')
        self.validate_required(self.oss_endpoint, 'oss_endpoint')
        self.validate_required(self.oss_bucket, 'oss_bucket')
        self.validate_required(self.record_format, 'record_format')
        if self.record_format:
            for k in self.record_format:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        result['OssEndpoint'] = self.oss_endpoint
        result['OssBucket'] = self.oss_bucket
        result['RecordFormat'] = []
        if self.record_format is not None:
            for k in self.record_format:
                result['RecordFormat'].append(k.to_map() if k else None)
        else:
            result['RecordFormat'] = None
        result['StreamName'] = self.stream_name
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['OnDemand'] = self.on_demand
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        self.oss_endpoint = map.get('OssEndpoint')
        self.oss_bucket = map.get('OssBucket')
        self.record_format = []
        if map.get('RecordFormat') is not None:
            for k in map.get('RecordFormat'):
                temp_model = AddLiveAppRecordConfigRequestRecordFormat()
                self.record_format.append(temp_model.from_map(k))
        else:
            self.record_format = None
        self.stream_name = map.get('StreamName')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.on_demand = map.get('OnDemand')
        return self


class AddLiveAppRecordConfigRequestRecordFormat(TeaModel):
    def __init__(self, format=None, oss_object_prefix=None, slice_oss_object_prefix=None, cycle_duration=None):
        self.format = format            # type: str
        self.oss_object_prefix = oss_object_prefix  # type: str
        self.slice_oss_object_prefix = slice_oss_object_prefix  # type: str
        self.cycle_duration = cycle_duration  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['Format'] = self.format
        result['OssObjectPrefix'] = self.oss_object_prefix
        result['SliceOssObjectPrefix'] = self.slice_oss_object_prefix
        result['CycleDuration'] = self.cycle_duration
        return result

    def from_map(self, map={}):
        self.format = map.get('Format')
        self.oss_object_prefix = map.get('OssObjectPrefix')
        self.slice_oss_object_prefix = map.get('SliceOssObjectPrefix')
        self.cycle_duration = map.get('CycleDuration')
        return self


class AddLiveAppRecordConfigResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DescribeLiveRecordConfigRequest(TeaModel):
    def __init__(self, security_token=None, domain_name=None, app_name=None, stream_name=None, page_num=None,
                 page_size=None, order=None):
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str
        self.stream_name = stream_name  # type: str
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int
        self.order = order              # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        result['StreamName'] = self.stream_name
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        result['Order'] = self.order
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        self.stream_name = map.get('StreamName')
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        self.order = map.get('Order')
        return self


class DescribeLiveRecordConfigResponse(TeaModel):
    def __init__(self, request_id=None, page_num=None, page_size=None, order=None, total_num=None, total_page=None,
                 live_app_record_list=None):
        self.request_id = request_id    # type: str
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int
        self.order = order              # type: str
        self.total_num = total_num      # type: int
        self.total_page = total_page    # type: int
        self.live_app_record_list = live_app_record_list  # type: DescribeLiveRecordConfigResponseLiveAppRecordList

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.page_num, 'page_num')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.order, 'order')
        self.validate_required(self.total_num, 'total_num')
        self.validate_required(self.total_page, 'total_page')
        self.validate_required(self.live_app_record_list, 'live_app_record_list')
        if self.live_app_record_list:
            self.live_app_record_list.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        result['Order'] = self.order
        result['TotalNum'] = self.total_num
        result['TotalPage'] = self.total_page
        if self.live_app_record_list is not None:
            result['LiveAppRecordList'] = self.live_app_record_list.to_map()
        else:
            result['LiveAppRecordList'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        self.order = map.get('Order')
        self.total_num = map.get('TotalNum')
        self.total_page = map.get('TotalPage')
        if map.get('LiveAppRecordList') is not None:
            temp_model = DescribeLiveRecordConfigResponseLiveAppRecordList()
            self.live_app_record_list = temp_model.from_map(map['LiveAppRecordList'])
        else:
            self.live_app_record_list = None
        return self


class DescribeLiveRecordConfigResponseLiveAppRecordListLiveAppRecordRecordFormatListRecordFormat(TeaModel):
    def __init__(self, format=None, oss_object_prefix=None, slice_oss_object_prefix=None, cycle_duration=None):
        self.format = format            # type: str
        self.oss_object_prefix = oss_object_prefix  # type: str
        self.slice_oss_object_prefix = slice_oss_object_prefix  # type: str
        self.cycle_duration = cycle_duration  # type: int

    def validate(self):
        self.validate_required(self.format, 'format')
        self.validate_required(self.oss_object_prefix, 'oss_object_prefix')
        self.validate_required(self.slice_oss_object_prefix, 'slice_oss_object_prefix')
        self.validate_required(self.cycle_duration, 'cycle_duration')

    def to_map(self):
        result = {}
        result['Format'] = self.format
        result['OssObjectPrefix'] = self.oss_object_prefix
        result['SliceOssObjectPrefix'] = self.slice_oss_object_prefix
        result['CycleDuration'] = self.cycle_duration
        return result

    def from_map(self, map={}):
        self.format = map.get('Format')
        self.oss_object_prefix = map.get('OssObjectPrefix')
        self.slice_oss_object_prefix = map.get('SliceOssObjectPrefix')
        self.cycle_duration = map.get('CycleDuration')
        return self


class DescribeLiveRecordConfigResponseLiveAppRecordListLiveAppRecordRecordFormatList(TeaModel):
    def __init__(self, record_format=None):
        self.record_format = record_format  # type: List[DescribeLiveRecordConfigResponseLiveAppRecordListLiveAppRecordRecordFormatListRecordFormat]

    def validate(self):
        self.validate_required(self.record_format, 'record_format')
        if self.record_format:
            for k in self.record_format:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RecordFormat'] = []
        if self.record_format is not None:
            for k in self.record_format:
                result['RecordFormat'].append(k.to_map() if k else None)
        else:
            result['RecordFormat'] = None
        return result

    def from_map(self, map={}):
        self.record_format = []
        if map.get('RecordFormat') is not None:
            for k in map.get('RecordFormat'):
                temp_model = DescribeLiveRecordConfigResponseLiveAppRecordListLiveAppRecordRecordFormatListRecordFormat()
                self.record_format.append(temp_model.from_map(k))
        else:
            self.record_format = None
        return self


class DescribeLiveRecordConfigResponseLiveAppRecordListLiveAppRecord(TeaModel):
    def __init__(self, domain_name=None, app_name=None, stream_name=None, oss_endpoint=None, oss_bucket=None,
                 create_time=None, start_time=None, end_time=None, on_demond=None, record_format_list=None):
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str
        self.stream_name = stream_name  # type: str
        self.oss_endpoint = oss_endpoint  # type: str
        self.oss_bucket = oss_bucket    # type: str
        self.create_time = create_time  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.on_demond = on_demond      # type: int
        self.record_format_list = record_format_list  # type: DescribeLiveRecordConfigResponseLiveAppRecordListLiveAppRecordRecordFormatList

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.app_name, 'app_name')
        self.validate_required(self.stream_name, 'stream_name')
        self.validate_required(self.oss_endpoint, 'oss_endpoint')
        self.validate_required(self.oss_bucket, 'oss_bucket')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.on_demond, 'on_demond')
        self.validate_required(self.record_format_list, 'record_format_list')
        if self.record_format_list:
            self.record_format_list.validate()

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        result['StreamName'] = self.stream_name
        result['OssEndpoint'] = self.oss_endpoint
        result['OssBucket'] = self.oss_bucket
        result['CreateTime'] = self.create_time
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['OnDemond'] = self.on_demond
        if self.record_format_list is not None:
            result['RecordFormatList'] = self.record_format_list.to_map()
        else:
            result['RecordFormatList'] = None
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        self.stream_name = map.get('StreamName')
        self.oss_endpoint = map.get('OssEndpoint')
        self.oss_bucket = map.get('OssBucket')
        self.create_time = map.get('CreateTime')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.on_demond = map.get('OnDemond')
        if map.get('RecordFormatList') is not None:
            temp_model = DescribeLiveRecordConfigResponseLiveAppRecordListLiveAppRecordRecordFormatList()
            self.record_format_list = temp_model.from_map(map['RecordFormatList'])
        else:
            self.record_format_list = None
        return self


class DescribeLiveRecordConfigResponseLiveAppRecordList(TeaModel):
    def __init__(self, live_app_record=None):
        self.live_app_record = live_app_record  # type: List[DescribeLiveRecordConfigResponseLiveAppRecordListLiveAppRecord]

    def validate(self):
        self.validate_required(self.live_app_record, 'live_app_record')
        if self.live_app_record:
            for k in self.live_app_record:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['LiveAppRecord'] = []
        if self.live_app_record is not None:
            for k in self.live_app_record:
                result['LiveAppRecord'].append(k.to_map() if k else None)
        else:
            result['LiveAppRecord'] = None
        return result

    def from_map(self, map={}):
        self.live_app_record = []
        if map.get('LiveAppRecord') is not None:
            for k in map.get('LiveAppRecord'):
                temp_model = DescribeLiveRecordConfigResponseLiveAppRecordListLiveAppRecord()
                self.live_app_record.append(temp_model.from_map(k))
        else:
            self.live_app_record = None
        return self


class DeleteLiveAppSnapshotConfigRequest(TeaModel):
    def __init__(self, security_token=None, domain_name=None, app_name=None):
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.app_name, 'app_name')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        return self


class DeleteLiveAppSnapshotConfigResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class DeleteLiveAppRecordConfigRequest(TeaModel):
    def __init__(self, security_token=None, domain_name=None, app_name=None, stream_name=None):
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str
        self.stream_name = stream_name  # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.app_name, 'app_name')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        result['StreamName'] = self.stream_name
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        self.stream_name = map.get('StreamName')
        return self


class DeleteLiveAppRecordConfigResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self


class CreateLiveStreamRecordIndexFilesRequest(TeaModel):
    def __init__(self, security_token=None, domain_name=None, app_name=None, stream_name=None, oss_endpoint=None,
                 oss_bucket=None, oss_object=None, start_time=None, end_time=None):
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str
        self.stream_name = stream_name  # type: str
        self.oss_endpoint = oss_endpoint  # type: str
        self.oss_bucket = oss_bucket    # type: str
        self.oss_object = oss_object    # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.app_name, 'app_name')
        self.validate_required(self.stream_name, 'stream_name')
        self.validate_required(self.oss_endpoint, 'oss_endpoint')
        self.validate_required(self.oss_bucket, 'oss_bucket')
        self.validate_required(self.oss_object, 'oss_object')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        result['StreamName'] = self.stream_name
        result['OssEndpoint'] = self.oss_endpoint
        result['OssBucket'] = self.oss_bucket
        result['OssObject'] = self.oss_object
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        self.stream_name = map.get('StreamName')
        self.oss_endpoint = map.get('OssEndpoint')
        self.oss_bucket = map.get('OssBucket')
        self.oss_object = map.get('OssObject')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        return self


class CreateLiveStreamRecordIndexFilesResponse(TeaModel):
    def __init__(self, request_id=None, record_info=None):
        self.request_id = request_id    # type: str
        self.record_info = record_info  # type: CreateLiveStreamRecordIndexFilesResponseRecordInfo

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.record_info, 'record_info')
        if self.record_info:
            self.record_info.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.record_info is not None:
            result['RecordInfo'] = self.record_info.to_map()
        else:
            result['RecordInfo'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('RecordInfo') is not None:
            temp_model = CreateLiveStreamRecordIndexFilesResponseRecordInfo()
            self.record_info = temp_model.from_map(map['RecordInfo'])
        else:
            self.record_info = None
        return self


class CreateLiveStreamRecordIndexFilesResponseRecordInfo(TeaModel):
    def __init__(self, record_id=None, record_url=None, domain_name=None, app_name=None, stream_name=None,
                 oss_bucket=None, oss_endpoint=None, oss_object=None, start_time=None, end_time=None, duration=None,
                 height=None, width=None, create_time=None):
        self.record_id = record_id      # type: str
        self.record_url = record_url    # type: str
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str
        self.stream_name = stream_name  # type: str
        self.oss_bucket = oss_bucket    # type: str
        self.oss_endpoint = oss_endpoint  # type: str
        self.oss_object = oss_object    # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.duration = duration        # type: float
        self.height = height            # type: int
        self.width = width              # type: int
        self.create_time = create_time  # type: str

    def validate(self):
        self.validate_required(self.record_id, 'record_id')
        self.validate_required(self.record_url, 'record_url')
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.app_name, 'app_name')
        self.validate_required(self.stream_name, 'stream_name')
        self.validate_required(self.oss_bucket, 'oss_bucket')
        self.validate_required(self.oss_endpoint, 'oss_endpoint')
        self.validate_required(self.oss_object, 'oss_object')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.duration, 'duration')
        self.validate_required(self.height, 'height')
        self.validate_required(self.width, 'width')
        self.validate_required(self.create_time, 'create_time')

    def to_map(self):
        result = {}
        result['RecordId'] = self.record_id
        result['RecordUrl'] = self.record_url
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        result['StreamName'] = self.stream_name
        result['OssBucket'] = self.oss_bucket
        result['OssEndpoint'] = self.oss_endpoint
        result['OssObject'] = self.oss_object
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['Duration'] = self.duration
        result['Height'] = self.height
        result['Width'] = self.width
        result['CreateTime'] = self.create_time
        return result

    def from_map(self, map={}):
        self.record_id = map.get('RecordId')
        self.record_url = map.get('RecordUrl')
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        self.stream_name = map.get('StreamName')
        self.oss_bucket = map.get('OssBucket')
        self.oss_endpoint = map.get('OssEndpoint')
        self.oss_object = map.get('OssObject')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.duration = map.get('Duration')
        self.height = map.get('Height')
        self.width = map.get('Width')
        self.create_time = map.get('CreateTime')
        return self


class DescribeLiveStreamSnapshotInfoRequest(TeaModel):
    def __init__(self, security_token=None, domain_name=None, app_name=None, stream_name=None, start_time=None,
                 end_time=None, limit=None, order=None):
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str
        self.stream_name = stream_name  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.limit = limit              # type: int
        self.order = order              # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.app_name, 'app_name')
        self.validate_required(self.stream_name, 'stream_name')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        result['StreamName'] = self.stream_name
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['Limit'] = self.limit
        result['Order'] = self.order
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        self.stream_name = map.get('StreamName')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.limit = map.get('Limit')
        self.order = map.get('Order')
        return self


class DescribeLiveStreamSnapshotInfoResponse(TeaModel):
    def __init__(self, request_id=None, next_start_time=None, live_stream_snapshot_info_list=None):
        self.request_id = request_id    # type: str
        self.next_start_time = next_start_time  # type: str
        self.live_stream_snapshot_info_list = live_stream_snapshot_info_list  # type: DescribeLiveStreamSnapshotInfoResponseLiveStreamSnapshotInfoList

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.next_start_time, 'next_start_time')
        self.validate_required(self.live_stream_snapshot_info_list, 'live_stream_snapshot_info_list')
        if self.live_stream_snapshot_info_list:
            self.live_stream_snapshot_info_list.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['NextStartTime'] = self.next_start_time
        if self.live_stream_snapshot_info_list is not None:
            result['LiveStreamSnapshotInfoList'] = self.live_stream_snapshot_info_list.to_map()
        else:
            result['LiveStreamSnapshotInfoList'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.next_start_time = map.get('NextStartTime')
        if map.get('LiveStreamSnapshotInfoList') is not None:
            temp_model = DescribeLiveStreamSnapshotInfoResponseLiveStreamSnapshotInfoList()
            self.live_stream_snapshot_info_list = temp_model.from_map(map['LiveStreamSnapshotInfoList'])
        else:
            self.live_stream_snapshot_info_list = None
        return self


class DescribeLiveStreamSnapshotInfoResponseLiveStreamSnapshotInfoListLiveStreamSnapshotInfo(TeaModel):
    def __init__(self, oss_endpoint=None, oss_bucket=None, oss_object=None, create_time=None):
        self.oss_endpoint = oss_endpoint  # type: str
        self.oss_bucket = oss_bucket    # type: str
        self.oss_object = oss_object    # type: str
        self.create_time = create_time  # type: str

    def validate(self):
        self.validate_required(self.oss_endpoint, 'oss_endpoint')
        self.validate_required(self.oss_bucket, 'oss_bucket')
        self.validate_required(self.oss_object, 'oss_object')
        self.validate_required(self.create_time, 'create_time')

    def to_map(self):
        result = {}
        result['OssEndpoint'] = self.oss_endpoint
        result['OssBucket'] = self.oss_bucket
        result['OssObject'] = self.oss_object
        result['CreateTime'] = self.create_time
        return result

    def from_map(self, map={}):
        self.oss_endpoint = map.get('OssEndpoint')
        self.oss_bucket = map.get('OssBucket')
        self.oss_object = map.get('OssObject')
        self.create_time = map.get('CreateTime')
        return self


class DescribeLiveStreamSnapshotInfoResponseLiveStreamSnapshotInfoList(TeaModel):
    def __init__(self, live_stream_snapshot_info=None):
        self.live_stream_snapshot_info = live_stream_snapshot_info  # type: List[DescribeLiveStreamSnapshotInfoResponseLiveStreamSnapshotInfoListLiveStreamSnapshotInfo]

    def validate(self):
        self.validate_required(self.live_stream_snapshot_info, 'live_stream_snapshot_info')
        if self.live_stream_snapshot_info:
            for k in self.live_stream_snapshot_info:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['LiveStreamSnapshotInfo'] = []
        if self.live_stream_snapshot_info is not None:
            for k in self.live_stream_snapshot_info:
                result['LiveStreamSnapshotInfo'].append(k.to_map() if k else None)
        else:
            result['LiveStreamSnapshotInfo'] = None
        return result

    def from_map(self, map={}):
        self.live_stream_snapshot_info = []
        if map.get('LiveStreamSnapshotInfo') is not None:
            for k in map.get('LiveStreamSnapshotInfo'):
                temp_model = DescribeLiveStreamSnapshotInfoResponseLiveStreamSnapshotInfoListLiveStreamSnapshotInfo()
                self.live_stream_snapshot_info.append(temp_model.from_map(k))
        else:
            self.live_stream_snapshot_info = None
        return self


class DescribeLiveStreamRecordIndexFilesRequest(TeaModel):
    def __init__(self, security_token=None, domain_name=None, app_name=None, stream_name=None, start_time=None,
                 end_time=None, page_num=None, page_size=None, order=None):
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str
        self.stream_name = stream_name  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int
        self.order = order              # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.app_name, 'app_name')
        self.validate_required(self.stream_name, 'stream_name')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        result['StreamName'] = self.stream_name
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        result['Order'] = self.order
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        self.stream_name = map.get('StreamName')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        self.order = map.get('Order')
        return self


class DescribeLiveStreamRecordIndexFilesResponse(TeaModel):
    def __init__(self, request_id=None, page_num=None, page_size=None, order=None, total_num=None, total_page=None,
                 record_index_info_list=None):
        self.request_id = request_id    # type: str
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int
        self.order = order              # type: str
        self.total_num = total_num      # type: int
        self.total_page = total_page    # type: int
        self.record_index_info_list = record_index_info_list  # type: DescribeLiveStreamRecordIndexFilesResponseRecordIndexInfoList

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.page_num, 'page_num')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.order, 'order')
        self.validate_required(self.total_num, 'total_num')
        self.validate_required(self.total_page, 'total_page')
        self.validate_required(self.record_index_info_list, 'record_index_info_list')
        if self.record_index_info_list:
            self.record_index_info_list.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        result['Order'] = self.order
        result['TotalNum'] = self.total_num
        result['TotalPage'] = self.total_page
        if self.record_index_info_list is not None:
            result['RecordIndexInfoList'] = self.record_index_info_list.to_map()
        else:
            result['RecordIndexInfoList'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        self.order = map.get('Order')
        self.total_num = map.get('TotalNum')
        self.total_page = map.get('TotalPage')
        if map.get('RecordIndexInfoList') is not None:
            temp_model = DescribeLiveStreamRecordIndexFilesResponseRecordIndexInfoList()
            self.record_index_info_list = temp_model.from_map(map['RecordIndexInfoList'])
        else:
            self.record_index_info_list = None
        return self


class DescribeLiveStreamRecordIndexFilesResponseRecordIndexInfoListRecordIndexInfo(TeaModel):
    def __init__(self, record_id=None, record_url=None, domain_name=None, app_name=None, stream_name=None,
                 oss_bucket=None, oss_endpoint=None, oss_object=None, start_time=None, end_time=None, duration=None,
                 height=None, width=None, create_time=None):
        self.record_id = record_id      # type: str
        self.record_url = record_url    # type: str
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str
        self.stream_name = stream_name  # type: str
        self.oss_bucket = oss_bucket    # type: str
        self.oss_endpoint = oss_endpoint  # type: str
        self.oss_object = oss_object    # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.duration = duration        # type: float
        self.height = height            # type: int
        self.width = width              # type: int
        self.create_time = create_time  # type: str

    def validate(self):
        self.validate_required(self.record_id, 'record_id')
        self.validate_required(self.record_url, 'record_url')
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.app_name, 'app_name')
        self.validate_required(self.stream_name, 'stream_name')
        self.validate_required(self.oss_bucket, 'oss_bucket')
        self.validate_required(self.oss_endpoint, 'oss_endpoint')
        self.validate_required(self.oss_object, 'oss_object')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.duration, 'duration')
        self.validate_required(self.height, 'height')
        self.validate_required(self.width, 'width')
        self.validate_required(self.create_time, 'create_time')

    def to_map(self):
        result = {}
        result['RecordId'] = self.record_id
        result['RecordUrl'] = self.record_url
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        result['StreamName'] = self.stream_name
        result['OssBucket'] = self.oss_bucket
        result['OssEndpoint'] = self.oss_endpoint
        result['OssObject'] = self.oss_object
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['Duration'] = self.duration
        result['Height'] = self.height
        result['Width'] = self.width
        result['CreateTime'] = self.create_time
        return result

    def from_map(self, map={}):
        self.record_id = map.get('RecordId')
        self.record_url = map.get('RecordUrl')
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        self.stream_name = map.get('StreamName')
        self.oss_bucket = map.get('OssBucket')
        self.oss_endpoint = map.get('OssEndpoint')
        self.oss_object = map.get('OssObject')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.duration = map.get('Duration')
        self.height = map.get('Height')
        self.width = map.get('Width')
        self.create_time = map.get('CreateTime')
        return self


class DescribeLiveStreamRecordIndexFilesResponseRecordIndexInfoList(TeaModel):
    def __init__(self, record_index_info=None):
        self.record_index_info = record_index_info  # type: List[DescribeLiveStreamRecordIndexFilesResponseRecordIndexInfoListRecordIndexInfo]

    def validate(self):
        self.validate_required(self.record_index_info, 'record_index_info')
        if self.record_index_info:
            for k in self.record_index_info:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RecordIndexInfo'] = []
        if self.record_index_info is not None:
            for k in self.record_index_info:
                result['RecordIndexInfo'].append(k.to_map() if k else None)
        else:
            result['RecordIndexInfo'] = None
        return result

    def from_map(self, map={}):
        self.record_index_info = []
        if map.get('RecordIndexInfo') is not None:
            for k in map.get('RecordIndexInfo'):
                temp_model = DescribeLiveStreamRecordIndexFilesResponseRecordIndexInfoListRecordIndexInfo()
                self.record_index_info.append(temp_model.from_map(k))
        else:
            self.record_index_info = None
        return self


class DescribeLiveStreamRecordIndexFileRequest(TeaModel):
    def __init__(self, security_token=None, domain_name=None, app_name=None, stream_name=None, record_id=None):
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str
        self.stream_name = stream_name  # type: str
        self.record_id = record_id      # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.app_name, 'app_name')
        self.validate_required(self.stream_name, 'stream_name')
        self.validate_required(self.record_id, 'record_id')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        result['StreamName'] = self.stream_name
        result['RecordId'] = self.record_id
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        self.stream_name = map.get('StreamName')
        self.record_id = map.get('RecordId')
        return self


class DescribeLiveStreamRecordIndexFileResponse(TeaModel):
    def __init__(self, request_id=None, record_index_info=None):
        self.request_id = request_id    # type: str
        self.record_index_info = record_index_info  # type: DescribeLiveStreamRecordIndexFileResponseRecordIndexInfo

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.record_index_info, 'record_index_info')
        if self.record_index_info:
            self.record_index_info.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.record_index_info is not None:
            result['RecordIndexInfo'] = self.record_index_info.to_map()
        else:
            result['RecordIndexInfo'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('RecordIndexInfo') is not None:
            temp_model = DescribeLiveStreamRecordIndexFileResponseRecordIndexInfo()
            self.record_index_info = temp_model.from_map(map['RecordIndexInfo'])
        else:
            self.record_index_info = None
        return self


class DescribeLiveStreamRecordIndexFileResponseRecordIndexInfo(TeaModel):
    def __init__(self, record_id=None, record_url=None, domain_name=None, app_name=None, stream_name=None,
                 oss_bucket=None, oss_endpoint=None, oss_object=None, start_time=None, end_time=None, duration=None,
                 height=None, width=None, create_time=None):
        self.record_id = record_id      # type: str
        self.record_url = record_url    # type: str
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str
        self.stream_name = stream_name  # type: str
        self.oss_bucket = oss_bucket    # type: str
        self.oss_endpoint = oss_endpoint  # type: str
        self.oss_object = oss_object    # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.duration = duration        # type: float
        self.height = height            # type: int
        self.width = width              # type: int
        self.create_time = create_time  # type: str

    def validate(self):
        self.validate_required(self.record_id, 'record_id')
        self.validate_required(self.record_url, 'record_url')
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.app_name, 'app_name')
        self.validate_required(self.stream_name, 'stream_name')
        self.validate_required(self.oss_bucket, 'oss_bucket')
        self.validate_required(self.oss_endpoint, 'oss_endpoint')
        self.validate_required(self.oss_object, 'oss_object')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.duration, 'duration')
        self.validate_required(self.height, 'height')
        self.validate_required(self.width, 'width')
        self.validate_required(self.create_time, 'create_time')

    def to_map(self):
        result = {}
        result['RecordId'] = self.record_id
        result['RecordUrl'] = self.record_url
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        result['StreamName'] = self.stream_name
        result['OssBucket'] = self.oss_bucket
        result['OssEndpoint'] = self.oss_endpoint
        result['OssObject'] = self.oss_object
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['Duration'] = self.duration
        result['Height'] = self.height
        result['Width'] = self.width
        result['CreateTime'] = self.create_time
        return result

    def from_map(self, map={}):
        self.record_id = map.get('RecordId')
        self.record_url = map.get('RecordUrl')
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        self.stream_name = map.get('StreamName')
        self.oss_bucket = map.get('OssBucket')
        self.oss_endpoint = map.get('OssEndpoint')
        self.oss_object = map.get('OssObject')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.duration = map.get('Duration')
        self.height = map.get('Height')
        self.width = map.get('Width')
        self.create_time = map.get('CreateTime')
        return self


class DescribeLiveStreamRecordContentRequest(TeaModel):
    def __init__(self, security_token=None, domain_name=None, app_name=None, stream_name=None, start_time=None,
                 end_time=None):
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str
        self.stream_name = stream_name  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.app_name, 'app_name')
        self.validate_required(self.stream_name, 'stream_name')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        result['StreamName'] = self.stream_name
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        self.stream_name = map.get('StreamName')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        return self


class DescribeLiveStreamRecordContentResponse(TeaModel):
    def __init__(self, request_id=None, record_content_info_list=None):
        self.request_id = request_id    # type: str
        self.record_content_info_list = record_content_info_list  # type: DescribeLiveStreamRecordContentResponseRecordContentInfoList

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.record_content_info_list, 'record_content_info_list')
        if self.record_content_info_list:
            self.record_content_info_list.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        if self.record_content_info_list is not None:
            result['RecordContentInfoList'] = self.record_content_info_list.to_map()
        else:
            result['RecordContentInfoList'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        if map.get('RecordContentInfoList') is not None:
            temp_model = DescribeLiveStreamRecordContentResponseRecordContentInfoList()
            self.record_content_info_list = temp_model.from_map(map['RecordContentInfoList'])
        else:
            self.record_content_info_list = None
        return self


class DescribeLiveStreamRecordContentResponseRecordContentInfoListRecordContentInfo(TeaModel):
    def __init__(self, oss_endpoint=None, oss_bucket=None, oss_object_prefix=None, start_time=None, end_time=None,
                 duration=None):
        self.oss_endpoint = oss_endpoint  # type: str
        self.oss_bucket = oss_bucket    # type: str
        self.oss_object_prefix = oss_object_prefix  # type: str
        self.start_time = start_time    # type: str
        self.end_time = end_time        # type: str
        self.duration = duration        # type: float

    def validate(self):
        self.validate_required(self.oss_endpoint, 'oss_endpoint')
        self.validate_required(self.oss_bucket, 'oss_bucket')
        self.validate_required(self.oss_object_prefix, 'oss_object_prefix')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.duration, 'duration')

    def to_map(self):
        result = {}
        result['OssEndpoint'] = self.oss_endpoint
        result['OssBucket'] = self.oss_bucket
        result['OssObjectPrefix'] = self.oss_object_prefix
        result['StartTime'] = self.start_time
        result['EndTime'] = self.end_time
        result['Duration'] = self.duration
        return result

    def from_map(self, map={}):
        self.oss_endpoint = map.get('OssEndpoint')
        self.oss_bucket = map.get('OssBucket')
        self.oss_object_prefix = map.get('OssObjectPrefix')
        self.start_time = map.get('StartTime')
        self.end_time = map.get('EndTime')
        self.duration = map.get('Duration')
        return self


class DescribeLiveStreamRecordContentResponseRecordContentInfoList(TeaModel):
    def __init__(self, record_content_info=None):
        self.record_content_info = record_content_info  # type: List[DescribeLiveStreamRecordContentResponseRecordContentInfoListRecordContentInfo]

    def validate(self):
        self.validate_required(self.record_content_info, 'record_content_info')
        if self.record_content_info:
            for k in self.record_content_info:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['RecordContentInfo'] = []
        if self.record_content_info is not None:
            for k in self.record_content_info:
                result['RecordContentInfo'].append(k.to_map() if k else None)
        else:
            result['RecordContentInfo'] = None
        return result

    def from_map(self, map={}):
        self.record_content_info = []
        if map.get('RecordContentInfo') is not None:
            for k in map.get('RecordContentInfo'):
                temp_model = DescribeLiveStreamRecordContentResponseRecordContentInfoListRecordContentInfo()
                self.record_content_info.append(temp_model.from_map(k))
        else:
            self.record_content_info = None
        return self


class DescribeLiveSnapshotConfigRequest(TeaModel):
    def __init__(self, security_token=None, domain_name=None, app_name=None, page_num=None, page_size=None,
                 order=None):
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int
        self.order = order              # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        result['Order'] = self.order
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        self.order = map.get('Order')
        return self


class DescribeLiveSnapshotConfigResponse(TeaModel):
    def __init__(self, request_id=None, page_num=None, page_size=None, order=None, total_num=None, total_page=None,
                 live_stream_snapshot_config_list=None):
        self.request_id = request_id    # type: str
        self.page_num = page_num        # type: int
        self.page_size = page_size      # type: int
        self.order = order              # type: str
        self.total_num = total_num      # type: int
        self.total_page = total_page    # type: int
        self.live_stream_snapshot_config_list = live_stream_snapshot_config_list  # type: DescribeLiveSnapshotConfigResponseLiveStreamSnapshotConfigList

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.page_num, 'page_num')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.order, 'order')
        self.validate_required(self.total_num, 'total_num')
        self.validate_required(self.total_page, 'total_page')
        self.validate_required(self.live_stream_snapshot_config_list, 'live_stream_snapshot_config_list')
        if self.live_stream_snapshot_config_list:
            self.live_stream_snapshot_config_list.validate()

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        result['PageNum'] = self.page_num
        result['PageSize'] = self.page_size
        result['Order'] = self.order
        result['TotalNum'] = self.total_num
        result['TotalPage'] = self.total_page
        if self.live_stream_snapshot_config_list is not None:
            result['LiveStreamSnapshotConfigList'] = self.live_stream_snapshot_config_list.to_map()
        else:
            result['LiveStreamSnapshotConfigList'] = None
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        self.page_num = map.get('PageNum')
        self.page_size = map.get('PageSize')
        self.order = map.get('Order')
        self.total_num = map.get('TotalNum')
        self.total_page = map.get('TotalPage')
        if map.get('LiveStreamSnapshotConfigList') is not None:
            temp_model = DescribeLiveSnapshotConfigResponseLiveStreamSnapshotConfigList()
            self.live_stream_snapshot_config_list = temp_model.from_map(map['LiveStreamSnapshotConfigList'])
        else:
            self.live_stream_snapshot_config_list = None
        return self


class DescribeLiveSnapshotConfigResponseLiveStreamSnapshotConfigListLiveStreamSnapshotConfig(TeaModel):
    def __init__(self, domain_name=None, app_name=None, time_interval=None, oss_endpoint=None, oss_bucket=None,
                 overwrite_oss_object=None, sequence_oss_object=None, create_time=None, callback=None):
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str
        self.time_interval = time_interval  # type: int
        self.oss_endpoint = oss_endpoint  # type: str
        self.oss_bucket = oss_bucket    # type: str
        self.overwrite_oss_object = overwrite_oss_object  # type: str
        self.sequence_oss_object = sequence_oss_object  # type: str
        self.create_time = create_time  # type: str
        self.callback = callback        # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.app_name, 'app_name')
        self.validate_required(self.time_interval, 'time_interval')
        self.validate_required(self.oss_endpoint, 'oss_endpoint')
        self.validate_required(self.oss_bucket, 'oss_bucket')
        self.validate_required(self.overwrite_oss_object, 'overwrite_oss_object')
        self.validate_required(self.sequence_oss_object, 'sequence_oss_object')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.callback, 'callback')

    def to_map(self):
        result = {}
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        result['TimeInterval'] = self.time_interval
        result['OssEndpoint'] = self.oss_endpoint
        result['OssBucket'] = self.oss_bucket
        result['OverwriteOssObject'] = self.overwrite_oss_object
        result['SequenceOssObject'] = self.sequence_oss_object
        result['CreateTime'] = self.create_time
        result['Callback'] = self.callback
        return result

    def from_map(self, map={}):
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        self.time_interval = map.get('TimeInterval')
        self.oss_endpoint = map.get('OssEndpoint')
        self.oss_bucket = map.get('OssBucket')
        self.overwrite_oss_object = map.get('OverwriteOssObject')
        self.sequence_oss_object = map.get('SequenceOssObject')
        self.create_time = map.get('CreateTime')
        self.callback = map.get('Callback')
        return self


class DescribeLiveSnapshotConfigResponseLiveStreamSnapshotConfigList(TeaModel):
    def __init__(self, live_stream_snapshot_config=None):
        self.live_stream_snapshot_config = live_stream_snapshot_config  # type: List[DescribeLiveSnapshotConfigResponseLiveStreamSnapshotConfigListLiveStreamSnapshotConfig]

    def validate(self):
        self.validate_required(self.live_stream_snapshot_config, 'live_stream_snapshot_config')
        if self.live_stream_snapshot_config:
            for k in self.live_stream_snapshot_config:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['LiveStreamSnapshotConfig'] = []
        if self.live_stream_snapshot_config is not None:
            for k in self.live_stream_snapshot_config:
                result['LiveStreamSnapshotConfig'].append(k.to_map() if k else None)
        else:
            result['LiveStreamSnapshotConfig'] = None
        return result

    def from_map(self, map={}):
        self.live_stream_snapshot_config = []
        if map.get('LiveStreamSnapshotConfig') is not None:
            for k in map.get('LiveStreamSnapshotConfig'):
                temp_model = DescribeLiveSnapshotConfigResponseLiveStreamSnapshotConfigListLiveStreamSnapshotConfig()
                self.live_stream_snapshot_config.append(temp_model.from_map(k))
        else:
            self.live_stream_snapshot_config = None
        return self


class UpdateLiveAppSnapshotConfigRequest(TeaModel):
    def __init__(self, security_token=None, domain_name=None, app_name=None, time_interval=None, oss_endpoint=None,
                 oss_bucket=None, overwrite_oss_object=None, sequence_oss_object=None, callback=None):
        self.security_token = security_token  # type: str
        self.domain_name = domain_name  # type: str
        self.app_name = app_name        # type: str
        self.time_interval = time_interval  # type: int
        self.oss_endpoint = oss_endpoint  # type: str
        self.oss_bucket = oss_bucket    # type: str
        self.overwrite_oss_object = overwrite_oss_object  # type: str
        self.sequence_oss_object = sequence_oss_object  # type: str
        self.callback = callback        # type: str

    def validate(self):
        self.validate_required(self.domain_name, 'domain_name')
        self.validate_required(self.app_name, 'app_name')

    def to_map(self):
        result = {}
        result['SecurityToken'] = self.security_token
        result['DomainName'] = self.domain_name
        result['AppName'] = self.app_name
        result['TimeInterval'] = self.time_interval
        result['OssEndpoint'] = self.oss_endpoint
        result['OssBucket'] = self.oss_bucket
        result['OverwriteOssObject'] = self.overwrite_oss_object
        result['SequenceOssObject'] = self.sequence_oss_object
        result['Callback'] = self.callback
        return result

    def from_map(self, map={}):
        self.security_token = map.get('SecurityToken')
        self.domain_name = map.get('DomainName')
        self.app_name = map.get('AppName')
        self.time_interval = map.get('TimeInterval')
        self.oss_endpoint = map.get('OssEndpoint')
        self.oss_bucket = map.get('OssBucket')
        self.overwrite_oss_object = map.get('OverwriteOssObject')
        self.sequence_oss_object = map.get('SequenceOssObject')
        self.callback = map.get('Callback')
        return self


class UpdateLiveAppSnapshotConfigResponse(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        self.request_id = map.get('RequestId')
        return self
