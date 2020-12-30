# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import BinaryIO, Dict, List


class AbstractEcommerceVideoRequest(TeaModel):
    def __init__(
        self,
        video_url: str = None,
        async_: bool = None,
        duration: float = None,
        width: int = None,
        height: int = None,
    ):
        self.video_url = video_url
        self.async_ = async_
        self.duration = duration
        self.width = width
        self.height = height

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        if self.async_ is not None:
            result['Async'] = self.async_
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        if m.get('Async') is not None:
            self.async_ = m.get('Async')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class AbstractEcommerceVideoAdvanceRequest(TeaModel):
    def __init__(
        self,
        video_url_object: BinaryIO = None,
        async_: bool = None,
        duration: float = None,
        width: int = None,
        height: int = None,
    ):
        self.video_url_object = video_url_object
        self.async_ = async_
        self.duration = duration
        self.width = width
        self.height = height

    def validate(self):
        self.validate_required(self.video_url_object, 'video_url_object')

    def to_map(self):
        result = dict()
        if self.video_url_object is not None:
            result['VideoUrlObject'] = self.video_url_object
        if self.async_ is not None:
            result['Async'] = self.async_
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoUrlObject') is not None:
            self.video_url_object = m.get('VideoUrlObject')
        if m.get('Async') is not None:
            self.async_ = m.get('Async')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class AbstractEcommerceVideoResponseBodyData(TeaModel):
    def __init__(
        self,
        video_cover_url: str = None,
        video_url: str = None,
    ):
        self.video_cover_url = video_cover_url
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.video_cover_url is not None:
            result['VideoCoverUrl'] = self.video_cover_url
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoCoverUrl') is not None:
            self.video_cover_url = m.get('VideoCoverUrl')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class AbstractEcommerceVideoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: AbstractEcommerceVideoResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = AbstractEcommerceVideoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class AbstractEcommerceVideoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AbstractEcommerceVideoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AbstractEcommerceVideoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AbstractFilmVideoRequest(TeaModel):
    def __init__(
        self,
        video_url: str = None,
        async_: bool = None,
        length: int = None,
    ):
        self.video_url = video_url
        self.async_ = async_
        self.length = length

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        if self.async_ is not None:
            result['Async'] = self.async_
        if self.length is not None:
            result['Length'] = self.length
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        if m.get('Async') is not None:
            self.async_ = m.get('Async')
        if m.get('Length') is not None:
            self.length = m.get('Length')
        return self


class AbstractFilmVideoAdvanceRequest(TeaModel):
    def __init__(
        self,
        video_url_object: BinaryIO = None,
        async_: bool = None,
        length: int = None,
    ):
        self.video_url_object = video_url_object
        self.async_ = async_
        self.length = length

    def validate(self):
        self.validate_required(self.video_url_object, 'video_url_object')

    def to_map(self):
        result = dict()
        if self.video_url_object is not None:
            result['VideoUrlObject'] = self.video_url_object
        if self.async_ is not None:
            result['Async'] = self.async_
        if self.length is not None:
            result['Length'] = self.length
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoUrlObject') is not None:
            self.video_url_object = m.get('VideoUrlObject')
        if m.get('Async') is not None:
            self.async_ = m.get('Async')
        if m.get('Length') is not None:
            self.length = m.get('Length')
        return self


class AbstractFilmVideoResponseBodyData(TeaModel):
    def __init__(
        self,
        video_url: str = None,
    ):
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class AbstractFilmVideoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: AbstractFilmVideoResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = AbstractFilmVideoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class AbstractFilmVideoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AbstractFilmVideoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AbstractFilmVideoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AdjustVideoColorRequest(TeaModel):
    def __init__(
        self,
        video_url: str = None,
        async_: bool = None,
        video_bitrate: str = None,
        video_codec: str = None,
        video_format: str = None,
        mode: str = None,
    ):
        self.video_url = video_url
        self.async_ = async_
        self.video_bitrate = video_bitrate
        self.video_codec = video_codec
        self.video_format = video_format
        self.mode = mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        if self.async_ is not None:
            result['Async'] = self.async_
        if self.video_bitrate is not None:
            result['VideoBitrate'] = self.video_bitrate
        if self.video_codec is not None:
            result['VideoCodec'] = self.video_codec
        if self.video_format is not None:
            result['VideoFormat'] = self.video_format
        if self.mode is not None:
            result['Mode'] = self.mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        if m.get('Async') is not None:
            self.async_ = m.get('Async')
        if m.get('VideoBitrate') is not None:
            self.video_bitrate = m.get('VideoBitrate')
        if m.get('VideoCodec') is not None:
            self.video_codec = m.get('VideoCodec')
        if m.get('VideoFormat') is not None:
            self.video_format = m.get('VideoFormat')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        return self


class AdjustVideoColorAdvanceRequest(TeaModel):
    def __init__(
        self,
        video_url_object: BinaryIO = None,
        async_: bool = None,
        video_bitrate: str = None,
        video_codec: str = None,
        video_format: str = None,
        mode: str = None,
    ):
        self.video_url_object = video_url_object
        self.async_ = async_
        self.video_bitrate = video_bitrate
        self.video_codec = video_codec
        self.video_format = video_format
        self.mode = mode

    def validate(self):
        self.validate_required(self.video_url_object, 'video_url_object')

    def to_map(self):
        result = dict()
        if self.video_url_object is not None:
            result['VideoUrlObject'] = self.video_url_object
        if self.async_ is not None:
            result['Async'] = self.async_
        if self.video_bitrate is not None:
            result['VideoBitrate'] = self.video_bitrate
        if self.video_codec is not None:
            result['VideoCodec'] = self.video_codec
        if self.video_format is not None:
            result['VideoFormat'] = self.video_format
        if self.mode is not None:
            result['Mode'] = self.mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoUrlObject') is not None:
            self.video_url_object = m.get('VideoUrlObject')
        if m.get('Async') is not None:
            self.async_ = m.get('Async')
        if m.get('VideoBitrate') is not None:
            self.video_bitrate = m.get('VideoBitrate')
        if m.get('VideoCodec') is not None:
            self.video_codec = m.get('VideoCodec')
        if m.get('VideoFormat') is not None:
            self.video_format = m.get('VideoFormat')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        return self


class AdjustVideoColorResponseBodyData(TeaModel):
    def __init__(
        self,
        video_url: str = None,
    ):
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class AdjustVideoColorResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: AdjustVideoColorResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = AdjustVideoColorResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class AdjustVideoColorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AdjustVideoColorResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AdjustVideoColorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeVideoSizeRequest(TeaModel):
    def __init__(
        self,
        video_url: str = None,
        async_: bool = None,
        width: int = None,
        height: int = None,
        crop_type: str = None,
        fill_type: str = None,
        tightness: float = None,
        r: int = None,
        g: int = None,
        b: int = None,
    ):
        self.video_url = video_url
        self.async_ = async_
        self.width = width
        self.height = height
        self.crop_type = crop_type
        self.fill_type = fill_type
        self.tightness = tightness
        self.r = r
        self.g = g
        self.b = b

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        if self.async_ is not None:
            result['Async'] = self.async_
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        if m.get('Async') is not None:
            self.async_ = m.get('Async')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('CropType') is not None:
            self.crop_type = m.get('CropType')
        if m.get('FillType') is not None:
            self.fill_type = m.get('FillType')
        if m.get('Tightness') is not None:
            self.tightness = m.get('Tightness')
        if m.get('R') is not None:
            self.r = m.get('R')
        if m.get('G') is not None:
            self.g = m.get('G')
        if m.get('B') is not None:
            self.b = m.get('B')
        return self


class ChangeVideoSizeAdvanceRequest(TeaModel):
    def __init__(
        self,
        video_url_object: BinaryIO = None,
        async_: bool = None,
        width: int = None,
        height: int = None,
        crop_type: str = None,
        fill_type: str = None,
        tightness: float = None,
        r: int = None,
        g: int = None,
        b: int = None,
    ):
        self.video_url_object = video_url_object
        self.async_ = async_
        self.width = width
        self.height = height
        self.crop_type = crop_type
        self.fill_type = fill_type
        self.tightness = tightness
        self.r = r
        self.g = g
        self.b = b

    def validate(self):
        self.validate_required(self.video_url_object, 'video_url_object')

    def to_map(self):
        result = dict()
        if self.video_url_object is not None:
            result['VideoUrlObject'] = self.video_url_object
        if self.async_ is not None:
            result['Async'] = self.async_
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoUrlObject') is not None:
            self.video_url_object = m.get('VideoUrlObject')
        if m.get('Async') is not None:
            self.async_ = m.get('Async')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('CropType') is not None:
            self.crop_type = m.get('CropType')
        if m.get('FillType') is not None:
            self.fill_type = m.get('FillType')
        if m.get('Tightness') is not None:
            self.tightness = m.get('Tightness')
        if m.get('R') is not None:
            self.r = m.get('R')
        if m.get('G') is not None:
            self.g = m.get('G')
        if m.get('B') is not None:
            self.b = m.get('B')
        return self


class ChangeVideoSizeResponseBodyData(TeaModel):
    def __init__(
        self,
        video_cover_url: str = None,
        video_url: str = None,
    ):
        self.video_cover_url = video_cover_url
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.video_cover_url is not None:
            result['VideoCoverUrl'] = self.video_cover_url
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoCoverUrl') is not None:
            self.video_cover_url = m.get('VideoCoverUrl')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class ChangeVideoSizeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: ChangeVideoSizeResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ChangeVideoSizeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class ChangeVideoSizeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ChangeVideoSizeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ChangeVideoSizeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConvertHdrVideoRequest(TeaModel):
    def __init__(
        self,
        video_url: str = None,
        async_: bool = None,
        hdrformat: str = None,
        max_illuminance: int = None,
        bitrate: int = None,
    ):
        self.video_url = video_url
        self.async_ = async_
        self.hdrformat = hdrformat
        self.max_illuminance = max_illuminance
        self.bitrate = bitrate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.video_url is not None:
            result['VideoURL'] = self.video_url
        if self.async_ is not None:
            result['Async'] = self.async_
        if self.hdrformat is not None:
            result['HDRFormat'] = self.hdrformat
        if self.max_illuminance is not None:
            result['MaxIlluminance'] = self.max_illuminance
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoURL') is not None:
            self.video_url = m.get('VideoURL')
        if m.get('Async') is not None:
            self.async_ = m.get('Async')
        if m.get('HDRFormat') is not None:
            self.hdrformat = m.get('HDRFormat')
        if m.get('MaxIlluminance') is not None:
            self.max_illuminance = m.get('MaxIlluminance')
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        return self


class ConvertHdrVideoAdvanceRequest(TeaModel):
    def __init__(
        self,
        video_urlobject: BinaryIO = None,
        async_: bool = None,
        hdrformat: str = None,
        max_illuminance: int = None,
        bitrate: int = None,
    ):
        self.video_urlobject = video_urlobject
        self.async_ = async_
        self.hdrformat = hdrformat
        self.max_illuminance = max_illuminance
        self.bitrate = bitrate

    def validate(self):
        self.validate_required(self.video_urlobject, 'video_urlobject')

    def to_map(self):
        result = dict()
        if self.video_urlobject is not None:
            result['VideoURLObject'] = self.video_urlobject
        if self.async_ is not None:
            result['Async'] = self.async_
        if self.hdrformat is not None:
            result['HDRFormat'] = self.hdrformat
        if self.max_illuminance is not None:
            result['MaxIlluminance'] = self.max_illuminance
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoURLObject') is not None:
            self.video_urlobject = m.get('VideoURLObject')
        if m.get('Async') is not None:
            self.async_ = m.get('Async')
        if m.get('HDRFormat') is not None:
            self.hdrformat = m.get('HDRFormat')
        if m.get('MaxIlluminance') is not None:
            self.max_illuminance = m.get('MaxIlluminance')
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        return self


class ConvertHdrVideoResponseBodyData(TeaModel):
    def __init__(
        self,
        video_url: str = None,
    ):
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.video_url is not None:
            result['VideoURL'] = self.video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoURL') is not None:
            self.video_url = m.get('VideoURL')
        return self


class ConvertHdrVideoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: ConvertHdrVideoResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ConvertHdrVideoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class ConvertHdrVideoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ConvertHdrVideoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ConvertHdrVideoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnhanceVideoQualityRequest(TeaModel):
    def __init__(
        self,
        video_url: str = None,
        async_: bool = None,
        out_put_width: int = None,
        out_put_height: int = None,
        frame_rate: int = None,
        hdrformat: str = None,
        max_illuminance: int = None,
        bitrate: int = None,
    ):
        self.video_url = video_url
        self.async_ = async_
        self.out_put_width = out_put_width
        self.out_put_height = out_put_height
        self.frame_rate = frame_rate
        self.hdrformat = hdrformat
        self.max_illuminance = max_illuminance
        self.bitrate = bitrate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.video_url is not None:
            result['VideoURL'] = self.video_url
        if self.async_ is not None:
            result['Async'] = self.async_
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoURL') is not None:
            self.video_url = m.get('VideoURL')
        if m.get('Async') is not None:
            self.async_ = m.get('Async')
        if m.get('OutPutWidth') is not None:
            self.out_put_width = m.get('OutPutWidth')
        if m.get('OutPutHeight') is not None:
            self.out_put_height = m.get('OutPutHeight')
        if m.get('FrameRate') is not None:
            self.frame_rate = m.get('FrameRate')
        if m.get('HDRFormat') is not None:
            self.hdrformat = m.get('HDRFormat')
        if m.get('MaxIlluminance') is not None:
            self.max_illuminance = m.get('MaxIlluminance')
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        return self


class EnhanceVideoQualityAdvanceRequest(TeaModel):
    def __init__(
        self,
        video_urlobject: BinaryIO = None,
        async_: bool = None,
        out_put_width: int = None,
        out_put_height: int = None,
        frame_rate: int = None,
        hdrformat: str = None,
        max_illuminance: int = None,
        bitrate: int = None,
    ):
        self.video_urlobject = video_urlobject
        self.async_ = async_
        self.out_put_width = out_put_width
        self.out_put_height = out_put_height
        self.frame_rate = frame_rate
        self.hdrformat = hdrformat
        self.max_illuminance = max_illuminance
        self.bitrate = bitrate

    def validate(self):
        self.validate_required(self.video_urlobject, 'video_urlobject')

    def to_map(self):
        result = dict()
        if self.video_urlobject is not None:
            result['VideoURLObject'] = self.video_urlobject
        if self.async_ is not None:
            result['Async'] = self.async_
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoURLObject') is not None:
            self.video_urlobject = m.get('VideoURLObject')
        if m.get('Async') is not None:
            self.async_ = m.get('Async')
        if m.get('OutPutWidth') is not None:
            self.out_put_width = m.get('OutPutWidth')
        if m.get('OutPutHeight') is not None:
            self.out_put_height = m.get('OutPutHeight')
        if m.get('FrameRate') is not None:
            self.frame_rate = m.get('FrameRate')
        if m.get('HDRFormat') is not None:
            self.hdrformat = m.get('HDRFormat')
        if m.get('MaxIlluminance') is not None:
            self.max_illuminance = m.get('MaxIlluminance')
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        return self


class EnhanceVideoQualityResponseBodyData(TeaModel):
    def __init__(
        self,
        video_url: str = None,
    ):
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.video_url is not None:
            result['VideoURL'] = self.video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoURL') is not None:
            self.video_url = m.get('VideoURL')
        return self


class EnhanceVideoQualityResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: EnhanceVideoQualityResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = EnhanceVideoQualityResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class EnhanceVideoQualityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EnhanceVideoQualityResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = EnhanceVideoQualityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EraseVideoLogoRequestBoxes(TeaModel):
    def __init__(
        self,
        w: float = None,
        h: float = None,
        y: float = None,
        x: float = None,
    ):
        self.w = w
        self.h = h
        self.y = y
        self.x = x

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.w is not None:
            result['W'] = self.w
        if self.h is not None:
            result['H'] = self.h
        if self.y is not None:
            result['Y'] = self.y
        if self.x is not None:
            result['X'] = self.x
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('W') is not None:
            self.w = m.get('W')
        if m.get('H') is not None:
            self.h = m.get('H')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('X') is not None:
            self.x = m.get('X')
        return self


class EraseVideoLogoRequest(TeaModel):
    def __init__(
        self,
        video_url: str = None,
        async_: bool = None,
        boxes: List[EraseVideoLogoRequestBoxes] = None,
    ):
        self.video_url = video_url
        self.async_ = async_
        self.boxes = boxes

    def validate(self):
        if self.boxes:
            for k in self.boxes:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        if self.async_ is not None:
            result['Async'] = self.async_
        result['Boxes'] = []
        if self.boxes is not None:
            for k in self.boxes:
                result['Boxes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        if m.get('Async') is not None:
            self.async_ = m.get('Async')
        self.boxes = []
        if m.get('Boxes') is not None:
            for k in m.get('Boxes'):
                temp_model = EraseVideoLogoRequestBoxes()
                self.boxes.append(temp_model.from_map(k))
        return self


class EraseVideoLogoAdvanceRequestBoxes(TeaModel):
    def __init__(
        self,
        w: float = None,
        h: float = None,
        y: float = None,
        x: float = None,
    ):
        self.w = w
        self.h = h
        self.y = y
        self.x = x

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.w is not None:
            result['W'] = self.w
        if self.h is not None:
            result['H'] = self.h
        if self.y is not None:
            result['Y'] = self.y
        if self.x is not None:
            result['X'] = self.x
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('W') is not None:
            self.w = m.get('W')
        if m.get('H') is not None:
            self.h = m.get('H')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('X') is not None:
            self.x = m.get('X')
        return self


class EraseVideoLogoAdvanceRequest(TeaModel):
    def __init__(
        self,
        video_url_object: BinaryIO = None,
        async_: bool = None,
        boxes: List[EraseVideoLogoAdvanceRequestBoxes] = None,
    ):
        self.video_url_object = video_url_object
        self.async_ = async_
        self.boxes = boxes

    def validate(self):
        self.validate_required(self.video_url_object, 'video_url_object')
        if self.boxes:
            for k in self.boxes:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.video_url_object is not None:
            result['VideoUrlObject'] = self.video_url_object
        if self.async_ is not None:
            result['Async'] = self.async_
        result['Boxes'] = []
        if self.boxes is not None:
            for k in self.boxes:
                result['Boxes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoUrlObject') is not None:
            self.video_url_object = m.get('VideoUrlObject')
        if m.get('Async') is not None:
            self.async_ = m.get('Async')
        self.boxes = []
        if m.get('Boxes') is not None:
            for k in m.get('Boxes'):
                temp_model = EraseVideoLogoAdvanceRequestBoxes()
                self.boxes.append(temp_model.from_map(k))
        return self


class EraseVideoLogoResponseBodyData(TeaModel):
    def __init__(
        self,
        video_url: str = None,
    ):
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class EraseVideoLogoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: EraseVideoLogoResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = EraseVideoLogoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class EraseVideoLogoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EraseVideoLogoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = EraseVideoLogoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EraseVideoSubtitlesRequest(TeaModel):
    def __init__(
        self,
        video_url: str = None,
        async_: bool = None,
        bx: float = None,
        by: float = None,
        bw: float = None,
        bh: float = None,
    ):
        self.video_url = video_url
        self.async_ = async_
        self.bx = bx
        self.by = by
        self.bw = bw
        self.bh = bh

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        if self.async_ is not None:
            result['Async'] = self.async_
        if self.bx is not None:
            result['BX'] = self.bx
        if self.by is not None:
            result['BY'] = self.by
        if self.bw is not None:
            result['BW'] = self.bw
        if self.bh is not None:
            result['BH'] = self.bh
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        if m.get('Async') is not None:
            self.async_ = m.get('Async')
        if m.get('BX') is not None:
            self.bx = m.get('BX')
        if m.get('BY') is not None:
            self.by = m.get('BY')
        if m.get('BW') is not None:
            self.bw = m.get('BW')
        if m.get('BH') is not None:
            self.bh = m.get('BH')
        return self


class EraseVideoSubtitlesAdvanceRequest(TeaModel):
    def __init__(
        self,
        video_url_object: BinaryIO = None,
        async_: bool = None,
        bx: float = None,
        by: float = None,
        bw: float = None,
        bh: float = None,
    ):
        self.video_url_object = video_url_object
        self.async_ = async_
        self.bx = bx
        self.by = by
        self.bw = bw
        self.bh = bh

    def validate(self):
        self.validate_required(self.video_url_object, 'video_url_object')

    def to_map(self):
        result = dict()
        if self.video_url_object is not None:
            result['VideoUrlObject'] = self.video_url_object
        if self.async_ is not None:
            result['Async'] = self.async_
        if self.bx is not None:
            result['BX'] = self.bx
        if self.by is not None:
            result['BY'] = self.by
        if self.bw is not None:
            result['BW'] = self.bw
        if self.bh is not None:
            result['BH'] = self.bh
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoUrlObject') is not None:
            self.video_url_object = m.get('VideoUrlObject')
        if m.get('Async') is not None:
            self.async_ = m.get('Async')
        if m.get('BX') is not None:
            self.bx = m.get('BX')
        if m.get('BY') is not None:
            self.by = m.get('BY')
        if m.get('BW') is not None:
            self.bw = m.get('BW')
        if m.get('BH') is not None:
            self.bh = m.get('BH')
        return self


class EraseVideoSubtitlesResponseBodyData(TeaModel):
    def __init__(
        self,
        video_url: str = None,
    ):
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class EraseVideoSubtitlesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: EraseVideoSubtitlesResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = EraseVideoSubtitlesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class EraseVideoSubtitlesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EraseVideoSubtitlesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = EraseVideoSubtitlesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateVideoRequestFileList(TeaModel):
    def __init__(
        self,
        type: str = None,
        file_url: str = None,
        file_name: str = None,
    ):
        self.type = type
        self.file_url = file_url
        self.file_name = file_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.file_name is not None:
            result['FileName'] = self.file_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        return self


class GenerateVideoRequest(TeaModel):
    def __init__(
        self,
        async_: bool = None,
        scene: str = None,
        width: int = None,
        height: int = None,
        style: str = None,
        duration: float = None,
        duration_adaption: bool = None,
        transition_style: str = None,
        smart_effect: bool = None,
        puzzle_effect: bool = None,
        mute: bool = None,
        file_list: List[GenerateVideoRequestFileList] = None,
    ):
        self.async_ = async_
        self.scene = scene
        self.width = width
        self.height = height
        self.style = style
        self.duration = duration
        self.duration_adaption = duration_adaption
        self.transition_style = transition_style
        self.smart_effect = smart_effect
        self.puzzle_effect = puzzle_effect
        self.mute = mute
        self.file_list = file_list

    def validate(self):
        if self.file_list:
            for k in self.file_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.async_ is not None:
            result['Async'] = self.async_
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
        result['FileList'] = []
        if self.file_list is not None:
            for k in self.file_list:
                result['FileList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Async') is not None:
            self.async_ = m.get('Async')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Style') is not None:
            self.style = m.get('Style')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('DurationAdaption') is not None:
            self.duration_adaption = m.get('DurationAdaption')
        if m.get('TransitionStyle') is not None:
            self.transition_style = m.get('TransitionStyle')
        if m.get('SmartEffect') is not None:
            self.smart_effect = m.get('SmartEffect')
        if m.get('PuzzleEffect') is not None:
            self.puzzle_effect = m.get('PuzzleEffect')
        if m.get('Mute') is not None:
            self.mute = m.get('Mute')
        self.file_list = []
        if m.get('FileList') is not None:
            for k in m.get('FileList'):
                temp_model = GenerateVideoRequestFileList()
                self.file_list.append(temp_model.from_map(k))
        return self


class GenerateVideoResponseBodyData(TeaModel):
    def __init__(
        self,
        video_cover_url: str = None,
        video_url: str = None,
    ):
        self.video_cover_url = video_cover_url
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.video_cover_url is not None:
            result['VideoCoverUrl'] = self.video_cover_url
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoCoverUrl') is not None:
            self.video_cover_url = m.get('VideoCoverUrl')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class GenerateVideoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: GenerateVideoResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GenerateVideoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GenerateVideoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GenerateVideoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GenerateVideoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAsyncJobResultRequest(TeaModel):
    def __init__(
        self,
        async_: bool = None,
        job_id: str = None,
    ):
        self.async_ = async_
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.async_ is not None:
            result['Async'] = self.async_
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Async') is not None:
            self.async_ = m.get('Async')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class GetAsyncJobResultResponseBodyData(TeaModel):
    def __init__(
        self,
        status: str = None,
        error_message: str = None,
        result: str = None,
        error_code: str = None,
        job_id: str = None,
    ):
        self.status = status
        self.error_message = error_message
        self.result = result
        self.error_code = error_code
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.result is not None:
            result['Result'] = self.result
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class GetAsyncJobResultResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: GetAsyncJobResultResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetAsyncJobResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetAsyncJobResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAsyncJobResultResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAsyncJobResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MergeVideoFaceRequest(TeaModel):
    def __init__(
        self,
        video_url: str = None,
        async_: bool = None,
        post_url: str = None,
        reference_url: str = None,
    ):
        self.video_url = video_url
        self.async_ = async_
        self.post_url = post_url
        self.reference_url = reference_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.video_url is not None:
            result['VideoURL'] = self.video_url
        if self.async_ is not None:
            result['Async'] = self.async_
        if self.post_url is not None:
            result['PostURL'] = self.post_url
        if self.reference_url is not None:
            result['ReferenceURL'] = self.reference_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoURL') is not None:
            self.video_url = m.get('VideoURL')
        if m.get('Async') is not None:
            self.async_ = m.get('Async')
        if m.get('PostURL') is not None:
            self.post_url = m.get('PostURL')
        if m.get('ReferenceURL') is not None:
            self.reference_url = m.get('ReferenceURL')
        return self


class MergeVideoFaceAdvanceRequest(TeaModel):
    def __init__(
        self,
        video_urlobject: BinaryIO = None,
        async_: bool = None,
        post_url: str = None,
        reference_url: str = None,
    ):
        self.video_urlobject = video_urlobject
        self.async_ = async_
        self.post_url = post_url
        self.reference_url = reference_url

    def validate(self):
        self.validate_required(self.video_urlobject, 'video_urlobject')

    def to_map(self):
        result = dict()
        if self.video_urlobject is not None:
            result['VideoURLObject'] = self.video_urlobject
        if self.async_ is not None:
            result['Async'] = self.async_
        if self.post_url is not None:
            result['PostURL'] = self.post_url
        if self.reference_url is not None:
            result['ReferenceURL'] = self.reference_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoURLObject') is not None:
            self.video_urlobject = m.get('VideoURLObject')
        if m.get('Async') is not None:
            self.async_ = m.get('Async')
        if m.get('PostURL') is not None:
            self.post_url = m.get('PostURL')
        if m.get('ReferenceURL') is not None:
            self.reference_url = m.get('ReferenceURL')
        return self


class MergeVideoFaceResponseBodyData(TeaModel):
    def __init__(
        self,
        video_url: str = None,
    ):
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.video_url is not None:
            result['VideoURL'] = self.video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoURL') is not None:
            self.video_url = m.get('VideoURL')
        return self


class MergeVideoFaceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: MergeVideoFaceResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = MergeVideoFaceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class MergeVideoFaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: MergeVideoFaceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = MergeVideoFaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SuperResolveVideoRequest(TeaModel):
    def __init__(
        self,
        video_url: str = None,
        async_: bool = None,
        bit_rate: int = None,
    ):
        self.video_url = video_url
        self.async_ = async_
        self.bit_rate = bit_rate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        if self.async_ is not None:
            result['Async'] = self.async_
        if self.bit_rate is not None:
            result['BitRate'] = self.bit_rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        if m.get('Async') is not None:
            self.async_ = m.get('Async')
        if m.get('BitRate') is not None:
            self.bit_rate = m.get('BitRate')
        return self


class SuperResolveVideoAdvanceRequest(TeaModel):
    def __init__(
        self,
        video_url_object: BinaryIO = None,
        async_: bool = None,
        bit_rate: int = None,
    ):
        self.video_url_object = video_url_object
        self.async_ = async_
        self.bit_rate = bit_rate

    def validate(self):
        self.validate_required(self.video_url_object, 'video_url_object')

    def to_map(self):
        result = dict()
        if self.video_url_object is not None:
            result['VideoUrlObject'] = self.video_url_object
        if self.async_ is not None:
            result['Async'] = self.async_
        if self.bit_rate is not None:
            result['BitRate'] = self.bit_rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoUrlObject') is not None:
            self.video_url_object = m.get('VideoUrlObject')
        if m.get('Async') is not None:
            self.async_ = m.get('Async')
        if m.get('BitRate') is not None:
            self.bit_rate = m.get('BitRate')
        return self


class SuperResolveVideoResponseBodyData(TeaModel):
    def __init__(
        self,
        video_url: str = None,
    ):
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class SuperResolveVideoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: SuperResolveVideoResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = SuperResolveVideoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class SuperResolveVideoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SuperResolveVideoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SuperResolveVideoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ToneSdrVideoRequest(TeaModel):
    def __init__(
        self,
        video_url: str = None,
        async_: bool = None,
        bitrate: int = None,
        recolor_model: str = None,
    ):
        self.video_url = video_url
        self.async_ = async_
        self.bitrate = bitrate
        self.recolor_model = recolor_model

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.video_url is not None:
            result['VideoURL'] = self.video_url
        if self.async_ is not None:
            result['Async'] = self.async_
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.recolor_model is not None:
            result['RecolorModel'] = self.recolor_model
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoURL') is not None:
            self.video_url = m.get('VideoURL')
        if m.get('Async') is not None:
            self.async_ = m.get('Async')
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('RecolorModel') is not None:
            self.recolor_model = m.get('RecolorModel')
        return self


class ToneSdrVideoAdvanceRequest(TeaModel):
    def __init__(
        self,
        video_urlobject: BinaryIO = None,
        async_: bool = None,
        bitrate: int = None,
        recolor_model: str = None,
    ):
        self.video_urlobject = video_urlobject
        self.async_ = async_
        self.bitrate = bitrate
        self.recolor_model = recolor_model

    def validate(self):
        self.validate_required(self.video_urlobject, 'video_urlobject')

    def to_map(self):
        result = dict()
        if self.video_urlobject is not None:
            result['VideoURLObject'] = self.video_urlobject
        if self.async_ is not None:
            result['Async'] = self.async_
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.recolor_model is not None:
            result['RecolorModel'] = self.recolor_model
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoURLObject') is not None:
            self.video_urlobject = m.get('VideoURLObject')
        if m.get('Async') is not None:
            self.async_ = m.get('Async')
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('RecolorModel') is not None:
            self.recolor_model = m.get('RecolorModel')
        return self


class ToneSdrVideoResponseBodyData(TeaModel):
    def __init__(
        self,
        video_url: str = None,
    ):
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.video_url is not None:
            result['VideoURL'] = self.video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoURL') is not None:
            self.video_url = m.get('VideoURL')
        return self


class ToneSdrVideoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: ToneSdrVideoResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ToneSdrVideoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class ToneSdrVideoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ToneSdrVideoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ToneSdrVideoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


