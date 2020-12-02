# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
try:
    from typing import BinaryIO, List
except ImportError:
    pass


class EnhanceVideoQualityRequest(TeaModel):
    def __init__(self, video_url=None, out_put_width=None, out_put_height=None, frame_rate=None, hdrformat=None,
                 max_illuminance=None, bitrate=None):
        self.video_url = video_url      # type: str
        self.out_put_width = out_put_width  # type: int
        self.out_put_height = out_put_height  # type: int
        self.frame_rate = frame_rate    # type: int
        self.hdrformat = hdrformat      # type: str
        self.max_illuminance = max_illuminance  # type: int
        self.bitrate = bitrate          # type: int

    def validate(self):
        self.validate_required(self.video_url, 'video_url')

    def to_map(self):
        result = {}
        if self.video_url is not None:
            result['VideoURL'] = self.video_url
        if self.out_put_width is not None:
            result['OutPutWidth'] = self.out_put_width
        if self.out_put_height is not None:
            result['OutPutHeight'] = self.out_put_height
        if self.frame_rate is not None:
            result['FrameRate'] = self.frame_rate
        if self.hdrformat is not None:
            result['HDRFormat'] = self.hdrformat
        if self.max_illuminance is not None:
            result['MaxIlluminance'] = self.max_illuminance
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        return result

    def from_map(self, map={}):
        if map.get('VideoURL') is not None:
            self.video_url = map.get('VideoURL')
        if map.get('OutPutWidth') is not None:
            self.out_put_width = map.get('OutPutWidth')
        if map.get('OutPutHeight') is not None:
            self.out_put_height = map.get('OutPutHeight')
        if map.get('FrameRate') is not None:
            self.frame_rate = map.get('FrameRate')
        if map.get('HDRFormat') is not None:
            self.hdrformat = map.get('HDRFormat')
        if map.get('MaxIlluminance') is not None:
            self.max_illuminance = map.get('MaxIlluminance')
        if map.get('Bitrate') is not None:
            self.bitrate = map.get('Bitrate')
        return self


class EnhanceVideoQualityResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: EnhanceVideoQualityResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = EnhanceVideoQualityResponseData()
            self.data = temp_model.from_map(map['Data'])
        return self


class EnhanceVideoQualityResponseData(TeaModel):
    def __init__(self, video_url=None):
        self.video_url = video_url      # type: str

    def validate(self):
        self.validate_required(self.video_url, 'video_url')

    def to_map(self):
        result = {}
        if self.video_url is not None:
            result['VideoURL'] = self.video_url
        return result

    def from_map(self, map={}):
        if map.get('VideoURL') is not None:
            self.video_url = map.get('VideoURL')
        return self


class EnhanceVideoQualityAdvanceRequest(TeaModel):
    def __init__(self, video_urlobject=None, out_put_width=None, out_put_height=None, frame_rate=None,
                 hdrformat=None, max_illuminance=None, bitrate=None):
        self.video_urlobject = video_urlobject  # type: BinaryIO
        self.out_put_width = out_put_width  # type: int
        self.out_put_height = out_put_height  # type: int
        self.frame_rate = frame_rate    # type: int
        self.hdrformat = hdrformat      # type: str
        self.max_illuminance = max_illuminance  # type: int
        self.bitrate = bitrate          # type: int

    def validate(self):
        self.validate_required(self.video_urlobject, 'video_urlobject')

    def to_map(self):
        result = {}
        if self.video_urlobject is not None:
            result['VideoURLObject'] = self.video_urlobject
        if self.out_put_width is not None:
            result['OutPutWidth'] = self.out_put_width
        if self.out_put_height is not None:
            result['OutPutHeight'] = self.out_put_height
        if self.frame_rate is not None:
            result['FrameRate'] = self.frame_rate
        if self.hdrformat is not None:
            result['HDRFormat'] = self.hdrformat
        if self.max_illuminance is not None:
            result['MaxIlluminance'] = self.max_illuminance
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        return result

    def from_map(self, map={}):
        if map.get('VideoURLObject') is not None:
            self.video_urlobject = map.get('VideoURLObject')
        if map.get('OutPutWidth') is not None:
            self.out_put_width = map.get('OutPutWidth')
        if map.get('OutPutHeight') is not None:
            self.out_put_height = map.get('OutPutHeight')
        if map.get('FrameRate') is not None:
            self.frame_rate = map.get('FrameRate')
        if map.get('HDRFormat') is not None:
            self.hdrformat = map.get('HDRFormat')
        if map.get('MaxIlluminance') is not None:
            self.max_illuminance = map.get('MaxIlluminance')
        if map.get('Bitrate') is not None:
            self.bitrate = map.get('Bitrate')
        return self


class MergeVideoFaceRequest(TeaModel):
    def __init__(self, video_url=None, post_url=None, reference_url=None):
        self.video_url = video_url      # type: str
        self.post_url = post_url        # type: str
        self.reference_url = reference_url  # type: str

    def validate(self):
        self.validate_required(self.video_url, 'video_url')
        self.validate_required(self.post_url, 'post_url')
        self.validate_required(self.reference_url, 'reference_url')

    def to_map(self):
        result = {}
        if self.video_url is not None:
            result['VideoURL'] = self.video_url
        if self.post_url is not None:
            result['PostURL'] = self.post_url
        if self.reference_url is not None:
            result['ReferenceURL'] = self.reference_url
        return result

    def from_map(self, map={}):
        if map.get('VideoURL') is not None:
            self.video_url = map.get('VideoURL')
        if map.get('PostURL') is not None:
            self.post_url = map.get('PostURL')
        if map.get('ReferenceURL') is not None:
            self.reference_url = map.get('ReferenceURL')
        return self


class MergeVideoFaceResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: MergeVideoFaceResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = MergeVideoFaceResponseData()
            self.data = temp_model.from_map(map['Data'])
        return self


class MergeVideoFaceResponseData(TeaModel):
    def __init__(self, video_url=None):
        self.video_url = video_url      # type: str

    def validate(self):
        self.validate_required(self.video_url, 'video_url')

    def to_map(self):
        result = {}
        if self.video_url is not None:
            result['VideoURL'] = self.video_url
        return result

    def from_map(self, map={}):
        if map.get('VideoURL') is not None:
            self.video_url = map.get('VideoURL')
        return self


class MergeVideoFaceAdvanceRequest(TeaModel):
    def __init__(self, video_urlobject=None, post_url=None, reference_url=None):
        self.video_urlobject = video_urlobject  # type: BinaryIO
        self.post_url = post_url        # type: str
        self.reference_url = reference_url  # type: str

    def validate(self):
        self.validate_required(self.video_urlobject, 'video_urlobject')
        self.validate_required(self.post_url, 'post_url')
        self.validate_required(self.reference_url, 'reference_url')

    def to_map(self):
        result = {}
        if self.video_urlobject is not None:
            result['VideoURLObject'] = self.video_urlobject
        if self.post_url is not None:
            result['PostURL'] = self.post_url
        if self.reference_url is not None:
            result['ReferenceURL'] = self.reference_url
        return result

    def from_map(self, map={}):
        if map.get('VideoURLObject') is not None:
            self.video_urlobject = map.get('VideoURLObject')
        if map.get('PostURL') is not None:
            self.post_url = map.get('PostURL')
        if map.get('ReferenceURL') is not None:
            self.reference_url = map.get('ReferenceURL')
        return self


class ChangeVideoSizeRequest(TeaModel):
    def __init__(self, video_url=None, width=None, height=None, crop_type=None, fill_type=None, tightness=None,
                 r=None, g=None, b=None):
        self.video_url = video_url      # type: str
        self.width = width              # type: int
        self.height = height            # type: int
        self.crop_type = crop_type      # type: str
        self.fill_type = fill_type      # type: str
        self.tightness = tightness      # type: float
        self.r = r                      # type: int
        self.g = g                      # type: int
        self.b = b                      # type: int

    def validate(self):
        self.validate_required(self.video_url, 'video_url')
        self.validate_required(self.width, 'width')
        self.validate_required(self.height, 'height')

    def to_map(self):
        result = {}
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.crop_type is not None:
            result['CropType'] = self.crop_type
        if self.fill_type is not None:
            result['FillType'] = self.fill_type
        if self.tightness is not None:
            result['Tightness'] = self.tightness
        if self.r is not None:
            result['R'] = self.r
        if self.g is not None:
            result['G'] = self.g
        if self.b is not None:
            result['B'] = self.b
        return result

    def from_map(self, map={}):
        if map.get('VideoUrl') is not None:
            self.video_url = map.get('VideoUrl')
        if map.get('Width') is not None:
            self.width = map.get('Width')
        if map.get('Height') is not None:
            self.height = map.get('Height')
        if map.get('CropType') is not None:
            self.crop_type = map.get('CropType')
        if map.get('FillType') is not None:
            self.fill_type = map.get('FillType')
        if map.get('Tightness') is not None:
            self.tightness = map.get('Tightness')
        if map.get('R') is not None:
            self.r = map.get('R')
        if map.get('G') is not None:
            self.g = map.get('G')
        if map.get('B') is not None:
            self.b = map.get('B')
        return self


class ChangeVideoSizeResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: ChangeVideoSizeResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = ChangeVideoSizeResponseData()
            self.data = temp_model.from_map(map['Data'])
        return self


class ChangeVideoSizeResponseData(TeaModel):
    def __init__(self, video_url=None, video_cover_url=None):
        self.video_url = video_url      # type: str
        self.video_cover_url = video_cover_url  # type: str

    def validate(self):
        self.validate_required(self.video_url, 'video_url')
        self.validate_required(self.video_cover_url, 'video_cover_url')

    def to_map(self):
        result = {}
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        if self.video_cover_url is not None:
            result['VideoCoverUrl'] = self.video_cover_url
        return result

    def from_map(self, map={}):
        if map.get('VideoUrl') is not None:
            self.video_url = map.get('VideoUrl')
        if map.get('VideoCoverUrl') is not None:
            self.video_cover_url = map.get('VideoCoverUrl')
        return self


class ChangeVideoSizeAdvanceRequest(TeaModel):
    def __init__(self, video_url_object=None, width=None, height=None, crop_type=None, fill_type=None,
                 tightness=None, r=None, g=None, b=None):
        self.video_url_object = video_url_object  # type: BinaryIO
        self.width = width              # type: int
        self.height = height            # type: int
        self.crop_type = crop_type      # type: str
        self.fill_type = fill_type      # type: str
        self.tightness = tightness      # type: float
        self.r = r                      # type: int
        self.g = g                      # type: int
        self.b = b                      # type: int

    def validate(self):
        self.validate_required(self.video_url_object, 'video_url_object')
        self.validate_required(self.width, 'width')
        self.validate_required(self.height, 'height')

    def to_map(self):
        result = {}
        if self.video_url_object is not None:
            result['VideoUrlObject'] = self.video_url_object
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.crop_type is not None:
            result['CropType'] = self.crop_type
        if self.fill_type is not None:
            result['FillType'] = self.fill_type
        if self.tightness is not None:
            result['Tightness'] = self.tightness
        if self.r is not None:
            result['R'] = self.r
        if self.g is not None:
            result['G'] = self.g
        if self.b is not None:
            result['B'] = self.b
        return result

    def from_map(self, map={}):
        if map.get('VideoUrlObject') is not None:
            self.video_url_object = map.get('VideoUrlObject')
        if map.get('Width') is not None:
            self.width = map.get('Width')
        if map.get('Height') is not None:
            self.height = map.get('Height')
        if map.get('CropType') is not None:
            self.crop_type = map.get('CropType')
        if map.get('FillType') is not None:
            self.fill_type = map.get('FillType')
        if map.get('Tightness') is not None:
            self.tightness = map.get('Tightness')
        if map.get('R') is not None:
            self.r = map.get('R')
        if map.get('G') is not None:
            self.g = map.get('G')
        if map.get('B') is not None:
            self.b = map.get('B')
        return self


class GenerateVideoRequest(TeaModel):
    def __init__(self, file_list=None, scene=None, width=None, height=None, style=None, duration=None,
                 duration_adaption=None, transition_style=None, smart_effect=None, puzzle_effect=None, mute=None):
        self.file_list = file_list      # type: List[GenerateVideoRequestFileList]
        self.scene = scene              # type: str
        self.width = width              # type: int
        self.height = height            # type: int
        self.style = style              # type: str
        self.duration = duration        # type: float
        self.duration_adaption = duration_adaption  # type: bool
        self.transition_style = transition_style  # type: str
        self.smart_effect = smart_effect  # type: bool
        self.puzzle_effect = puzzle_effect  # type: bool
        self.mute = mute                # type: bool

    def validate(self):
        self.validate_required(self.file_list, 'file_list')
        if self.file_list:
            for k in self.file_list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['FileList'] = []
        if self.file_list is not None:
            for k in self.file_list:
                result['FileList'].append(k.to_map() if k else None)
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.style is not None:
            result['Style'] = self.style
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.duration_adaption is not None:
            result['DurationAdaption'] = self.duration_adaption
        if self.transition_style is not None:
            result['TransitionStyle'] = self.transition_style
        if self.smart_effect is not None:
            result['SmartEffect'] = self.smart_effect
        if self.puzzle_effect is not None:
            result['PuzzleEffect'] = self.puzzle_effect
        if self.mute is not None:
            result['Mute'] = self.mute
        return result

    def from_map(self, map={}):
        self.file_list = []
        if map.get('FileList') is not None:
            for k in map.get('FileList'):
                temp_model = GenerateVideoRequestFileList()
                self.file_list.append(temp_model.from_map(k))
        if map.get('Scene') is not None:
            self.scene = map.get('Scene')
        if map.get('Width') is not None:
            self.width = map.get('Width')
        if map.get('Height') is not None:
            self.height = map.get('Height')
        if map.get('Style') is not None:
            self.style = map.get('Style')
        if map.get('Duration') is not None:
            self.duration = map.get('Duration')
        if map.get('DurationAdaption') is not None:
            self.duration_adaption = map.get('DurationAdaption')
        if map.get('TransitionStyle') is not None:
            self.transition_style = map.get('TransitionStyle')
        if map.get('SmartEffect') is not None:
            self.smart_effect = map.get('SmartEffect')
        if map.get('PuzzleEffect') is not None:
            self.puzzle_effect = map.get('PuzzleEffect')
        if map.get('Mute') is not None:
            self.mute = map.get('Mute')
        return self


class GenerateVideoRequestFileList(TeaModel):
    def __init__(self, file_url=None, file_name=None, type=None):
        self.file_url = file_url        # type: str
        self.file_name = file_name      # type: str
        self.type = type                # type: str

    def validate(self):
        self.validate_required(self.file_url, 'file_url')
        self.validate_required(self.file_name, 'file_name')
        self.validate_required(self.type, 'type')

    def to_map(self):
        result = {}
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, map={}):
        if map.get('FileUrl') is not None:
            self.file_url = map.get('FileUrl')
        if map.get('FileName') is not None:
            self.file_name = map.get('FileName')
        if map.get('Type') is not None:
            self.type = map.get('Type')
        return self


class GenerateVideoResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: GenerateVideoResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = GenerateVideoResponseData()
            self.data = temp_model.from_map(map['Data'])
        return self


class GenerateVideoResponseData(TeaModel):
    def __init__(self, video_url=None, video_cover_url=None):
        self.video_url = video_url      # type: str
        self.video_cover_url = video_cover_url  # type: str

    def validate(self):
        self.validate_required(self.video_url, 'video_url')
        self.validate_required(self.video_cover_url, 'video_cover_url')

    def to_map(self):
        result = {}
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        if self.video_cover_url is not None:
            result['VideoCoverUrl'] = self.video_cover_url
        return result

    def from_map(self, map={}):
        if map.get('VideoUrl') is not None:
            self.video_url = map.get('VideoUrl')
        if map.get('VideoCoverUrl') is not None:
            self.video_cover_url = map.get('VideoCoverUrl')
        return self


class GetAsyncJobResultRequest(TeaModel):
    def __init__(self, job_id=None):
        self.job_id = job_id            # type: str

    def validate(self):
        self.validate_required(self.job_id, 'job_id')

    def to_map(self):
        result = {}
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, map={}):
        if map.get('JobId') is not None:
            self.job_id = map.get('JobId')
        return self


class GetAsyncJobResultResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: GetAsyncJobResultResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = GetAsyncJobResultResponseData()
            self.data = temp_model.from_map(map['Data'])
        return self


class GetAsyncJobResultResponseData(TeaModel):
    def __init__(self, job_id=None, status=None, result=None, error_code=None, error_message=None):
        self.job_id = job_id            # type: str
        self.status = status            # type: str
        self.result = result            # type: str
        self.error_code = error_code    # type: str
        self.error_message = error_message  # type: str

    def validate(self):
        self.validate_required(self.job_id, 'job_id')
        self.validate_required(self.status, 'status')
        self.validate_required(self.result, 'result')
        self.validate_required(self.error_code, 'error_code')
        self.validate_required(self.error_message, 'error_message')

    def to_map(self):
        result = {}
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.status is not None:
            result['Status'] = self.status
        if self.result is not None:
            result['Result'] = self.result
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        return result

    def from_map(self, map={}):
        if map.get('JobId') is not None:
            self.job_id = map.get('JobId')
        if map.get('Status') is not None:
            self.status = map.get('Status')
        if map.get('Result') is not None:
            self.result = map.get('Result')
        if map.get('ErrorCode') is not None:
            self.error_code = map.get('ErrorCode')
        if map.get('ErrorMessage') is not None:
            self.error_message = map.get('ErrorMessage')
        return self


class SuperResolveVideoRequest(TeaModel):
    def __init__(self, video_url=None, bit_rate=None):
        self.video_url = video_url      # type: str
        self.bit_rate = bit_rate        # type: int

    def validate(self):
        self.validate_required(self.video_url, 'video_url')

    def to_map(self):
        result = {}
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        if self.bit_rate is not None:
            result['BitRate'] = self.bit_rate
        return result

    def from_map(self, map={}):
        if map.get('VideoUrl') is not None:
            self.video_url = map.get('VideoUrl')
        if map.get('BitRate') is not None:
            self.bit_rate = map.get('BitRate')
        return self


class SuperResolveVideoResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: SuperResolveVideoResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = SuperResolveVideoResponseData()
            self.data = temp_model.from_map(map['Data'])
        return self


class SuperResolveVideoResponseData(TeaModel):
    def __init__(self, video_url=None):
        self.video_url = video_url      # type: str

    def validate(self):
        self.validate_required(self.video_url, 'video_url')

    def to_map(self):
        result = {}
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, map={}):
        if map.get('VideoUrl') is not None:
            self.video_url = map.get('VideoUrl')
        return self


class SuperResolveVideoAdvanceRequest(TeaModel):
    def __init__(self, video_url_object=None, bit_rate=None):
        self.video_url_object = video_url_object  # type: BinaryIO
        self.bit_rate = bit_rate        # type: int

    def validate(self):
        self.validate_required(self.video_url_object, 'video_url_object')

    def to_map(self):
        result = {}
        if self.video_url_object is not None:
            result['VideoUrlObject'] = self.video_url_object
        if self.bit_rate is not None:
            result['BitRate'] = self.bit_rate
        return result

    def from_map(self, map={}):
        if map.get('VideoUrlObject') is not None:
            self.video_url_object = map.get('VideoUrlObject')
        if map.get('BitRate') is not None:
            self.bit_rate = map.get('BitRate')
        return self


class EraseVideoLogoRequest(TeaModel):
    def __init__(self, video_url=None, boxes=None):
        self.video_url = video_url      # type: str
        self.boxes = boxes              # type: List[EraseVideoLogoRequestBoxes]

    def validate(self):
        self.validate_required(self.video_url, 'video_url')
        if self.boxes:
            for k in self.boxes:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        result['Boxes'] = []
        if self.boxes is not None:
            for k in self.boxes:
                result['Boxes'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('VideoUrl') is not None:
            self.video_url = map.get('VideoUrl')
        self.boxes = []
        if map.get('Boxes') is not None:
            for k in map.get('Boxes'):
                temp_model = EraseVideoLogoRequestBoxes()
                self.boxes.append(temp_model.from_map(k))
        return self


class EraseVideoLogoRequestBoxes(TeaModel):
    def __init__(self, h=None, w=None, x=None, y=None):
        self.h = h                      # type: float
        self.w = w                      # type: float
        self.x = x                      # type: float
        self.y = y                      # type: float

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.h is not None:
            result['H'] = self.h
        if self.w is not None:
            result['W'] = self.w
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, map={}):
        if map.get('H') is not None:
            self.h = map.get('H')
        if map.get('W') is not None:
            self.w = map.get('W')
        if map.get('X') is not None:
            self.x = map.get('X')
        if map.get('Y') is not None:
            self.y = map.get('Y')
        return self


class EraseVideoLogoResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: EraseVideoLogoResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = EraseVideoLogoResponseData()
            self.data = temp_model.from_map(map['Data'])
        return self


class EraseVideoLogoResponseData(TeaModel):
    def __init__(self, video_url=None):
        self.video_url = video_url      # type: str

    def validate(self):
        self.validate_required(self.video_url, 'video_url')

    def to_map(self):
        result = {}
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, map={}):
        if map.get('VideoUrl') is not None:
            self.video_url = map.get('VideoUrl')
        return self


class EraseVideoLogoAdvanceRequest(TeaModel):
    def __init__(self, video_url_object=None, boxes=None):
        self.video_url_object = video_url_object  # type: BinaryIO
        self.boxes = boxes              # type: List[EraseVideoLogoAdvanceRequestBoxes]

    def validate(self):
        self.validate_required(self.video_url_object, 'video_url_object')
        if self.boxes:
            for k in self.boxes:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.video_url_object is not None:
            result['VideoUrlObject'] = self.video_url_object
        result['Boxes'] = []
        if self.boxes is not None:
            for k in self.boxes:
                result['Boxes'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('VideoUrlObject') is not None:
            self.video_url_object = map.get('VideoUrlObject')
        self.boxes = []
        if map.get('Boxes') is not None:
            for k in map.get('Boxes'):
                temp_model = EraseVideoLogoAdvanceRequestBoxes()
                self.boxes.append(temp_model.from_map(k))
        return self


class EraseVideoLogoAdvanceRequestBoxes(TeaModel):
    def __init__(self, h=None, w=None, x=None, y=None):
        self.h = h                      # type: float
        self.w = w                      # type: float
        self.x = x                      # type: float
        self.y = y                      # type: float

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.h is not None:
            result['H'] = self.h
        if self.w is not None:
            result['W'] = self.w
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, map={}):
        if map.get('H') is not None:
            self.h = map.get('H')
        if map.get('W') is not None:
            self.w = map.get('W')
        if map.get('X') is not None:
            self.x = map.get('X')
        if map.get('Y') is not None:
            self.y = map.get('Y')
        return self


class EraseVideoSubtitlesRequest(TeaModel):
    def __init__(self, video_url=None, bx=None, by=None, bw=None, bh=None):
        self.video_url = video_url      # type: str
        self.bx = bx                    # type: float
        self.by = by                    # type: float
        self.bw = bw                    # type: float
        self.bh = bh                    # type: float

    def validate(self):
        self.validate_required(self.video_url, 'video_url')

    def to_map(self):
        result = {}
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        if self.bx is not None:
            result['BX'] = self.bx
        if self.by is not None:
            result['BY'] = self.by
        if self.bw is not None:
            result['BW'] = self.bw
        if self.bh is not None:
            result['BH'] = self.bh
        return result

    def from_map(self, map={}):
        if map.get('VideoUrl') is not None:
            self.video_url = map.get('VideoUrl')
        if map.get('BX') is not None:
            self.bx = map.get('BX')
        if map.get('BY') is not None:
            self.by = map.get('BY')
        if map.get('BW') is not None:
            self.bw = map.get('BW')
        if map.get('BH') is not None:
            self.bh = map.get('BH')
        return self


class EraseVideoSubtitlesResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: EraseVideoSubtitlesResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = EraseVideoSubtitlesResponseData()
            self.data = temp_model.from_map(map['Data'])
        return self


class EraseVideoSubtitlesResponseData(TeaModel):
    def __init__(self, video_url=None):
        self.video_url = video_url      # type: str

    def validate(self):
        self.validate_required(self.video_url, 'video_url')

    def to_map(self):
        result = {}
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, map={}):
        if map.get('VideoUrl') is not None:
            self.video_url = map.get('VideoUrl')
        return self


class EraseVideoSubtitlesAdvanceRequest(TeaModel):
    def __init__(self, video_url_object=None, bx=None, by=None, bw=None, bh=None):
        self.video_url_object = video_url_object  # type: BinaryIO
        self.bx = bx                    # type: float
        self.by = by                    # type: float
        self.bw = bw                    # type: float
        self.bh = bh                    # type: float

    def validate(self):
        self.validate_required(self.video_url_object, 'video_url_object')

    def to_map(self):
        result = {}
        if self.video_url_object is not None:
            result['VideoUrlObject'] = self.video_url_object
        if self.bx is not None:
            result['BX'] = self.bx
        if self.by is not None:
            result['BY'] = self.by
        if self.bw is not None:
            result['BW'] = self.bw
        if self.bh is not None:
            result['BH'] = self.bh
        return result

    def from_map(self, map={}):
        if map.get('VideoUrlObject') is not None:
            self.video_url_object = map.get('VideoUrlObject')
        if map.get('BX') is not None:
            self.bx = map.get('BX')
        if map.get('BY') is not None:
            self.by = map.get('BY')
        if map.get('BW') is not None:
            self.bw = map.get('BW')
        if map.get('BH') is not None:
            self.bh = map.get('BH')
        return self


class AbstractEcommerceVideoRequest(TeaModel):
    def __init__(self, video_url=None, duration=None, width=None, height=None):
        self.video_url = video_url      # type: str
        self.duration = duration        # type: float
        self.width = width              # type: int
        self.height = height            # type: int

    def validate(self):
        self.validate_required(self.video_url, 'video_url')
        self.validate_required(self.duration, 'duration')

    def to_map(self):
        result = {}
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, map={}):
        if map.get('VideoUrl') is not None:
            self.video_url = map.get('VideoUrl')
        if map.get('Duration') is not None:
            self.duration = map.get('Duration')
        if map.get('Width') is not None:
            self.width = map.get('Width')
        if map.get('Height') is not None:
            self.height = map.get('Height')
        return self


class AbstractEcommerceVideoResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: AbstractEcommerceVideoResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = AbstractEcommerceVideoResponseData()
            self.data = temp_model.from_map(map['Data'])
        return self


class AbstractEcommerceVideoResponseData(TeaModel):
    def __init__(self, video_url=None, video_cover_url=None):
        self.video_url = video_url      # type: str
        self.video_cover_url = video_cover_url  # type: str

    def validate(self):
        self.validate_required(self.video_url, 'video_url')
        self.validate_required(self.video_cover_url, 'video_cover_url')

    def to_map(self):
        result = {}
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        if self.video_cover_url is not None:
            result['VideoCoverUrl'] = self.video_cover_url
        return result

    def from_map(self, map={}):
        if map.get('VideoUrl') is not None:
            self.video_url = map.get('VideoUrl')
        if map.get('VideoCoverUrl') is not None:
            self.video_cover_url = map.get('VideoCoverUrl')
        return self


class AbstractEcommerceVideoAdvanceRequest(TeaModel):
    def __init__(self, video_url_object=None, duration=None, width=None, height=None):
        self.video_url_object = video_url_object  # type: BinaryIO
        self.duration = duration        # type: float
        self.width = width              # type: int
        self.height = height            # type: int

    def validate(self):
        self.validate_required(self.video_url_object, 'video_url_object')
        self.validate_required(self.duration, 'duration')

    def to_map(self):
        result = {}
        if self.video_url_object is not None:
            result['VideoUrlObject'] = self.video_url_object
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, map={}):
        if map.get('VideoUrlObject') is not None:
            self.video_url_object = map.get('VideoUrlObject')
        if map.get('Duration') is not None:
            self.duration = map.get('Duration')
        if map.get('Width') is not None:
            self.width = map.get('Width')
        if map.get('Height') is not None:
            self.height = map.get('Height')
        return self


class AbstractFilmVideoRequest(TeaModel):
    def __init__(self, video_url=None, length=None):
        self.video_url = video_url      # type: str
        self.length = length            # type: int

    def validate(self):
        self.validate_required(self.video_url, 'video_url')
        self.validate_required(self.length, 'length')

    def to_map(self):
        result = {}
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        if self.length is not None:
            result['Length'] = self.length
        return result

    def from_map(self, map={}):
        if map.get('VideoUrl') is not None:
            self.video_url = map.get('VideoUrl')
        if map.get('Length') is not None:
            self.length = map.get('Length')
        return self


class AbstractFilmVideoResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: AbstractFilmVideoResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = AbstractFilmVideoResponseData()
            self.data = temp_model.from_map(map['Data'])
        return self


class AbstractFilmVideoResponseData(TeaModel):
    def __init__(self, video_url=None):
        self.video_url = video_url      # type: str

    def validate(self):
        self.validate_required(self.video_url, 'video_url')

    def to_map(self):
        result = {}
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, map={}):
        if map.get('VideoUrl') is not None:
            self.video_url = map.get('VideoUrl')
        return self


class AbstractFilmVideoAdvanceRequest(TeaModel):
    def __init__(self, video_url_object=None, length=None):
        self.video_url_object = video_url_object  # type: BinaryIO
        self.length = length            # type: int

    def validate(self):
        self.validate_required(self.video_url_object, 'video_url_object')
        self.validate_required(self.length, 'length')

    def to_map(self):
        result = {}
        if self.video_url_object is not None:
            result['VideoUrlObject'] = self.video_url_object
        if self.length is not None:
            result['Length'] = self.length
        return result

    def from_map(self, map={}):
        if map.get('VideoUrlObject') is not None:
            self.video_url_object = map.get('VideoUrlObject')
        if map.get('Length') is not None:
            self.length = map.get('Length')
        return self


class AdjustVideoColorRequest(TeaModel):
    def __init__(self, video_url=None, video_bitrate=None, video_codec=None, video_format=None, mode=None):
        self.video_url = video_url      # type: str
        self.video_bitrate = video_bitrate  # type: str
        self.video_codec = video_codec  # type: str
        self.video_format = video_format  # type: str
        self.mode = mode                # type: str

    def validate(self):
        self.validate_required(self.video_url, 'video_url')
        self.validate_required(self.mode, 'mode')

    def to_map(self):
        result = {}
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        if self.video_bitrate is not None:
            result['VideoBitrate'] = self.video_bitrate
        if self.video_codec is not None:
            result['VideoCodec'] = self.video_codec
        if self.video_format is not None:
            result['VideoFormat'] = self.video_format
        if self.mode is not None:
            result['Mode'] = self.mode
        return result

    def from_map(self, map={}):
        if map.get('VideoUrl') is not None:
            self.video_url = map.get('VideoUrl')
        if map.get('VideoBitrate') is not None:
            self.video_bitrate = map.get('VideoBitrate')
        if map.get('VideoCodec') is not None:
            self.video_codec = map.get('VideoCodec')
        if map.get('VideoFormat') is not None:
            self.video_format = map.get('VideoFormat')
        if map.get('Mode') is not None:
            self.mode = map.get('Mode')
        return self


class AdjustVideoColorResponse(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id    # type: str
        self.data = data                # type: AdjustVideoColorResponseData

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, map={}):
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        if map.get('Data') is not None:
            temp_model = AdjustVideoColorResponseData()
            self.data = temp_model.from_map(map['Data'])
        return self


class AdjustVideoColorResponseData(TeaModel):
    def __init__(self, video_url=None):
        self.video_url = video_url      # type: str

    def validate(self):
        self.validate_required(self.video_url, 'video_url')

    def to_map(self):
        result = {}
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, map={}):
        if map.get('VideoUrl') is not None:
            self.video_url = map.get('VideoUrl')
        return self


class AdjustVideoColorAdvanceRequest(TeaModel):
    def __init__(self, video_url_object=None, video_bitrate=None, video_codec=None, video_format=None, mode=None):
        self.video_url_object = video_url_object  # type: BinaryIO
        self.video_bitrate = video_bitrate  # type: str
        self.video_codec = video_codec  # type: str
        self.video_format = video_format  # type: str
        self.mode = mode                # type: str

    def validate(self):
        self.validate_required(self.video_url_object, 'video_url_object')
        self.validate_required(self.mode, 'mode')

    def to_map(self):
        result = {}
        if self.video_url_object is not None:
            result['VideoUrlObject'] = self.video_url_object
        if self.video_bitrate is not None:
            result['VideoBitrate'] = self.video_bitrate
        if self.video_codec is not None:
            result['VideoCodec'] = self.video_codec
        if self.video_format is not None:
            result['VideoFormat'] = self.video_format
        if self.mode is not None:
            result['Mode'] = self.mode
        return result

    def from_map(self, map={}):
        if map.get('VideoUrlObject') is not None:
            self.video_url_object = map.get('VideoUrlObject')
        if map.get('VideoBitrate') is not None:
            self.video_bitrate = map.get('VideoBitrate')
        if map.get('VideoCodec') is not None:
            self.video_codec = map.get('VideoCodec')
        if map.get('VideoFormat') is not None:
            self.video_format = map.get('VideoFormat')
        if map.get('Mode') is not None:
            self.mode = map.get('Mode')
        return self
