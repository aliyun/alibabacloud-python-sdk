# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class DownloadDataRequest(TeaModel):
    def __init__(
        self,
        band_no: str = None,
        data_id: str = None,
    ):
        self.band_no = band_no
        # 需要下载数据的DataId
        self.data_id = data_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.band_no is not None:
            result['BandNo'] = self.band_no
        if self.data_id is not None:
            result['DataId'] = self.data_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandNo') is not None:
            self.band_no = m.get('BandNo')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        return self


class DownloadDataResponseBody(TeaModel):
    def __init__(
        self,
        data_id: str = None,
        download_url: str = None,
        finished: bool = None,
        request_id: str = None,
        status: str = None,
    ):
        self.data_id = data_id
        self.download_url = download_url
        self.finished = finished
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        if self.finished is not None:
            result['Finished'] = self.finished
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        if m.get('Finished') is not None:
            self.finished = m.get('Finished')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DownloadDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DownloadDataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DownloadDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDatasRequest(TeaModel):
    def __init__(
        self,
        cloudage_max: int = None,
        cloudage_min: int = None,
        date_end: str = None,
        date_start: str = None,
        page_number: int = None,
        page_size: int = None,
        region_wkt: str = None,
        source_type_list: List[str] = None,
    ):
        # 云量上限
        self.cloudage_max = cloudage_max
        # 云量下限
        self.cloudage_min = cloudage_min
        # 结束日期，例如"2020-06-01"
        self.date_end = date_end
        # 开始日期，例如"2020-01-01"
        self.date_start = date_start
        # 页码
        self.page_number = page_number
        # 每页数量
        self.page_size = page_size
        # 区域选择，wkt格式
        self.region_wkt = region_wkt
        # 星源，可多选，枚举值如下：    sentinel1,
        #     sentinel2,
        #     landsat5,
        #     landsat7,
        #     landsat8,
        #     landsat9
        self.source_type_list = source_type_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cloudage_max is not None:
            result['CloudageMax'] = self.cloudage_max
        if self.cloudage_min is not None:
            result['CloudageMin'] = self.cloudage_min
        if self.date_end is not None:
            result['DateEnd'] = self.date_end
        if self.date_start is not None:
            result['DateStart'] = self.date_start
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_wkt is not None:
            result['RegionWkt'] = self.region_wkt
        if self.source_type_list is not None:
            result['SourceTypeList'] = self.source_type_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudageMax') is not None:
            self.cloudage_max = m.get('CloudageMax')
        if m.get('CloudageMin') is not None:
            self.cloudage_min = m.get('CloudageMin')
        if m.get('DateEnd') is not None:
            self.date_end = m.get('DateEnd')
        if m.get('DateStart') is not None:
            self.date_start = m.get('DateStart')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionWkt') is not None:
            self.region_wkt = m.get('RegionWkt')
        if m.get('SourceTypeList') is not None:
            self.source_type_list = m.get('SourceTypeList')
        return self


class ListDatasShrinkRequest(TeaModel):
    def __init__(
        self,
        cloudage_max: int = None,
        cloudage_min: int = None,
        date_end: str = None,
        date_start: str = None,
        page_number: int = None,
        page_size: int = None,
        region_wkt: str = None,
        source_type_list_shrink: str = None,
    ):
        # 云量上限
        self.cloudage_max = cloudage_max
        # 云量下限
        self.cloudage_min = cloudage_min
        # 结束日期，例如"2020-06-01"
        self.date_end = date_end
        # 开始日期，例如"2020-01-01"
        self.date_start = date_start
        # 页码
        self.page_number = page_number
        # 每页数量
        self.page_size = page_size
        # 区域选择，wkt格式
        self.region_wkt = region_wkt
        # 星源，可多选，枚举值如下：    sentinel1,
        #     sentinel2,
        #     landsat5,
        #     landsat7,
        #     landsat8,
        #     landsat9
        self.source_type_list_shrink = source_type_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cloudage_max is not None:
            result['CloudageMax'] = self.cloudage_max
        if self.cloudage_min is not None:
            result['CloudageMin'] = self.cloudage_min
        if self.date_end is not None:
            result['DateEnd'] = self.date_end
        if self.date_start is not None:
            result['DateStart'] = self.date_start
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_wkt is not None:
            result['RegionWkt'] = self.region_wkt
        if self.source_type_list_shrink is not None:
            result['SourceTypeList'] = self.source_type_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudageMax') is not None:
            self.cloudage_max = m.get('CloudageMax')
        if m.get('CloudageMin') is not None:
            self.cloudage_min = m.get('CloudageMin')
        if m.get('DateEnd') is not None:
            self.date_end = m.get('DateEnd')
        if m.get('DateStart') is not None:
            self.date_start = m.get('DateStart')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionWkt') is not None:
            self.region_wkt = m.get('RegionWkt')
        if m.get('SourceTypeList') is not None:
            self.source_type_list_shrink = m.get('SourceTypeList')
        return self


class ListDatasResponseBodyListRasterBands(TeaModel):
    def __init__(
        self,
        band_no: str = None,
        height: int = None,
        resolution: float = None,
        width: int = None,
    ):
        self.band_no = band_no
        self.height = height
        self.resolution = resolution
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.band_no is not None:
            result['BandNo'] = self.band_no
        if self.height is not None:
            result['Height'] = self.height
        if self.resolution is not None:
            result['Resolution'] = self.resolution
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandNo') is not None:
            self.band_no = m.get('BandNo')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class ListDatasResponseBodyListRaster(TeaModel):
    def __init__(
        self,
        acquisition_date_end: str = None,
        acquisition_date_start: str = None,
        bands: List[ListDatasResponseBodyListRasterBands] = None,
        bbox: List[float] = None,
        cloud_coverage: int = None,
        name: str = None,
        source_type: str = None,
        stac_id: str = None,
    ):
        self.acquisition_date_end = acquisition_date_end
        self.acquisition_date_start = acquisition_date_start
        self.bands = bands
        self.bbox = bbox
        self.cloud_coverage = cloud_coverage
        self.name = name
        self.source_type = source_type
        self.stac_id = stac_id

    def validate(self):
        if self.bands:
            for k in self.bands:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acquisition_date_end is not None:
            result['AcquisitionDateEnd'] = self.acquisition_date_end
        if self.acquisition_date_start is not None:
            result['AcquisitionDateStart'] = self.acquisition_date_start
        result['Bands'] = []
        if self.bands is not None:
            for k in self.bands:
                result['Bands'].append(k.to_map() if k else None)
        if self.bbox is not None:
            result['Bbox'] = self.bbox
        if self.cloud_coverage is not None:
            result['CloudCoverage'] = self.cloud_coverage
        if self.name is not None:
            result['Name'] = self.name
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.stac_id is not None:
            result['StacId'] = self.stac_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcquisitionDateEnd') is not None:
            self.acquisition_date_end = m.get('AcquisitionDateEnd')
        if m.get('AcquisitionDateStart') is not None:
            self.acquisition_date_start = m.get('AcquisitionDateStart')
        self.bands = []
        if m.get('Bands') is not None:
            for k in m.get('Bands'):
                temp_model = ListDatasResponseBodyListRasterBands()
                self.bands.append(temp_model.from_map(k))
        if m.get('Bbox') is not None:
            self.bbox = m.get('Bbox')
        if m.get('CloudCoverage') is not None:
            self.cloud_coverage = m.get('CloudCoverage')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('StacId') is not None:
            self.stac_id = m.get('StacId')
        return self


class ListDatasResponseBodyList(TeaModel):
    def __init__(
        self,
        data_id: str = None,
        raster: ListDatasResponseBodyListRaster = None,
    ):
        self.data_id = data_id
        self.raster = raster

    def validate(self):
        if self.raster:
            self.raster.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.raster is not None:
            result['Raster'] = self.raster.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Raster') is not None:
            temp_model = ListDatasResponseBodyListRaster()
            self.raster = temp_model.from_map(m['Raster'])
        return self


class ListDatasResponseBody(TeaModel):
    def __init__(
        self,
        list: List[ListDatasResponseBodyList] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.list = list
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListDatasResponseBodyList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDatasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDatasResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDatasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


