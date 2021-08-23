# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class CompareImageFacesRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        set_id: str = None,
        image_uri_a: str = None,
        image_uri_b: str = None,
        face_id_a: str = None,
        face_id_b: str = None,
    ):
        self.project = project
        self.set_id = set_id
        self.image_uri_a = image_uri_a
        self.image_uri_b = image_uri_b
        self.face_id_a = face_id_a
        self.face_id_b = face_id_b

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.image_uri_a is not None:
            result['ImageUriA'] = self.image_uri_a
        if self.image_uri_b is not None:
            result['ImageUriB'] = self.image_uri_b
        if self.face_id_a is not None:
            result['FaceIdA'] = self.face_id_a
        if self.face_id_b is not None:
            result['FaceIdB'] = self.face_id_b
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('ImageUriA') is not None:
            self.image_uri_a = m.get('ImageUriA')
        if m.get('ImageUriB') is not None:
            self.image_uri_b = m.get('ImageUriB')
        if m.get('FaceIdA') is not None:
            self.face_id_a = m.get('FaceIdA')
        if m.get('FaceIdB') is not None:
            self.face_id_b = m.get('FaceIdB')
        return self


class CompareImageFacesResponseBodyFaceAFaceAttributesFaceBoundary(TeaModel):
    def __init__(
        self,
        left: int = None,
        top: int = None,
        width: int = None,
        height: int = None,
    ):
        self.left = left
        self.top = top
        self.width = width
        self.height = height

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class CompareImageFacesResponseBodyFaceAFaceAttributes(TeaModel):
    def __init__(
        self,
        face_boundary: CompareImageFacesResponseBodyFaceAFaceAttributesFaceBoundary = None,
    ):
        self.face_boundary = face_boundary

    def validate(self):
        if self.face_boundary:
            self.face_boundary.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_boundary is not None:
            result['FaceBoundary'] = self.face_boundary.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceBoundary') is not None:
            temp_model = CompareImageFacesResponseBodyFaceAFaceAttributesFaceBoundary()
            self.face_boundary = temp_model.from_map(m['FaceBoundary'])
        return self


class CompareImageFacesResponseBodyFaceA(TeaModel):
    def __init__(
        self,
        face_id: str = None,
        face_attributes: CompareImageFacesResponseBodyFaceAFaceAttributes = None,
    ):
        self.face_id = face_id
        self.face_attributes = face_attributes

    def validate(self):
        if self.face_attributes:
            self.face_attributes.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_id is not None:
            result['FaceId'] = self.face_id
        if self.face_attributes is not None:
            result['FaceAttributes'] = self.face_attributes.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceId') is not None:
            self.face_id = m.get('FaceId')
        if m.get('FaceAttributes') is not None:
            temp_model = CompareImageFacesResponseBodyFaceAFaceAttributes()
            self.face_attributes = temp_model.from_map(m['FaceAttributes'])
        return self


class CompareImageFacesResponseBodyFaceBFaceAttributesFaceBoundary(TeaModel):
    def __init__(
        self,
        left: int = None,
        top: int = None,
        width: int = None,
        height: int = None,
    ):
        self.left = left
        self.top = top
        self.width = width
        self.height = height

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class CompareImageFacesResponseBodyFaceBFaceAttributes(TeaModel):
    def __init__(
        self,
        face_boundary: CompareImageFacesResponseBodyFaceBFaceAttributesFaceBoundary = None,
    ):
        self.face_boundary = face_boundary

    def validate(self):
        if self.face_boundary:
            self.face_boundary.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_boundary is not None:
            result['FaceBoundary'] = self.face_boundary.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceBoundary') is not None:
            temp_model = CompareImageFacesResponseBodyFaceBFaceAttributesFaceBoundary()
            self.face_boundary = temp_model.from_map(m['FaceBoundary'])
        return self


class CompareImageFacesResponseBodyFaceB(TeaModel):
    def __init__(
        self,
        face_id: str = None,
        face_attributes: CompareImageFacesResponseBodyFaceBFaceAttributes = None,
    ):
        self.face_id = face_id
        self.face_attributes = face_attributes

    def validate(self):
        if self.face_attributes:
            self.face_attributes.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_id is not None:
            result['FaceId'] = self.face_id
        if self.face_attributes is not None:
            result['FaceAttributes'] = self.face_attributes.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceId') is not None:
            self.face_id = m.get('FaceId')
        if m.get('FaceAttributes') is not None:
            temp_model = CompareImageFacesResponseBodyFaceBFaceAttributes()
            self.face_attributes = temp_model.from_map(m['FaceAttributes'])
        return self


class CompareImageFacesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        similarity: float = None,
        set_id: str = None,
        face_a: CompareImageFacesResponseBodyFaceA = None,
        face_b: CompareImageFacesResponseBodyFaceB = None,
    ):
        self.request_id = request_id
        self.similarity = similarity
        self.set_id = set_id
        self.face_a = face_a
        self.face_b = face_b

    def validate(self):
        if self.face_a:
            self.face_a.validate()
        if self.face_b:
            self.face_b.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.similarity is not None:
            result['Similarity'] = self.similarity
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.face_a is not None:
            result['FaceA'] = self.face_a.to_map()
        if self.face_b is not None:
            result['FaceB'] = self.face_b.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Similarity') is not None:
            self.similarity = m.get('Similarity')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('FaceA') is not None:
            temp_model = CompareImageFacesResponseBodyFaceA()
            self.face_a = temp_model.from_map(m['FaceA'])
        if m.get('FaceB') is not None:
            temp_model = CompareImageFacesResponseBodyFaceB()
            self.face_b = temp_model.from_map(m['FaceB'])
        return self


class CompareImageFacesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CompareImageFacesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CompareImageFacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConvertOfficeFormatRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        src_uri: str = None,
        tgt_type: str = None,
        tgt_uri: str = None,
        src_type: str = None,
        start_page: int = None,
        end_page: int = None,
        max_sheet_row: int = None,
        max_sheet_col: int = None,
        max_sheet_count: int = None,
        sheet_one_page: bool = None,
        model_id: str = None,
        password: str = None,
        tgt_file_prefix: str = None,
        tgt_file_suffix: str = None,
        tgt_file_pages: str = None,
        fit_to_pages_tall: bool = None,
        fit_to_pages_wide: bool = None,
        pdf_vector: bool = None,
        hidecomments: bool = None,
    ):
        self.project = project
        self.src_uri = src_uri
        self.tgt_type = tgt_type
        self.tgt_uri = tgt_uri
        self.src_type = src_type
        self.start_page = start_page
        self.end_page = end_page
        self.max_sheet_row = max_sheet_row
        self.max_sheet_col = max_sheet_col
        self.max_sheet_count = max_sheet_count
        self.sheet_one_page = sheet_one_page
        self.model_id = model_id
        self.password = password
        self.tgt_file_prefix = tgt_file_prefix
        self.tgt_file_suffix = tgt_file_suffix
        self.tgt_file_pages = tgt_file_pages
        self.fit_to_pages_tall = fit_to_pages_tall
        self.fit_to_pages_wide = fit_to_pages_wide
        self.pdf_vector = pdf_vector
        self.hidecomments = hidecomments

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.src_uri is not None:
            result['SrcUri'] = self.src_uri
        if self.tgt_type is not None:
            result['TgtType'] = self.tgt_type
        if self.tgt_uri is not None:
            result['TgtUri'] = self.tgt_uri
        if self.src_type is not None:
            result['SrcType'] = self.src_type
        if self.start_page is not None:
            result['StartPage'] = self.start_page
        if self.end_page is not None:
            result['EndPage'] = self.end_page
        if self.max_sheet_row is not None:
            result['MaxSheetRow'] = self.max_sheet_row
        if self.max_sheet_col is not None:
            result['MaxSheetCol'] = self.max_sheet_col
        if self.max_sheet_count is not None:
            result['MaxSheetCount'] = self.max_sheet_count
        if self.sheet_one_page is not None:
            result['SheetOnePage'] = self.sheet_one_page
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.password is not None:
            result['Password'] = self.password
        if self.tgt_file_prefix is not None:
            result['TgtFilePrefix'] = self.tgt_file_prefix
        if self.tgt_file_suffix is not None:
            result['TgtFileSuffix'] = self.tgt_file_suffix
        if self.tgt_file_pages is not None:
            result['TgtFilePages'] = self.tgt_file_pages
        if self.fit_to_pages_tall is not None:
            result['FitToPagesTall'] = self.fit_to_pages_tall
        if self.fit_to_pages_wide is not None:
            result['FitToPagesWide'] = self.fit_to_pages_wide
        if self.pdf_vector is not None:
            result['PdfVector'] = self.pdf_vector
        if self.hidecomments is not None:
            result['Hidecomments'] = self.hidecomments
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SrcUri') is not None:
            self.src_uri = m.get('SrcUri')
        if m.get('TgtType') is not None:
            self.tgt_type = m.get('TgtType')
        if m.get('TgtUri') is not None:
            self.tgt_uri = m.get('TgtUri')
        if m.get('SrcType') is not None:
            self.src_type = m.get('SrcType')
        if m.get('StartPage') is not None:
            self.start_page = m.get('StartPage')
        if m.get('EndPage') is not None:
            self.end_page = m.get('EndPage')
        if m.get('MaxSheetRow') is not None:
            self.max_sheet_row = m.get('MaxSheetRow')
        if m.get('MaxSheetCol') is not None:
            self.max_sheet_col = m.get('MaxSheetCol')
        if m.get('MaxSheetCount') is not None:
            self.max_sheet_count = m.get('MaxSheetCount')
        if m.get('SheetOnePage') is not None:
            self.sheet_one_page = m.get('SheetOnePage')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('TgtFilePrefix') is not None:
            self.tgt_file_prefix = m.get('TgtFilePrefix')
        if m.get('TgtFileSuffix') is not None:
            self.tgt_file_suffix = m.get('TgtFileSuffix')
        if m.get('TgtFilePages') is not None:
            self.tgt_file_pages = m.get('TgtFilePages')
        if m.get('FitToPagesTall') is not None:
            self.fit_to_pages_tall = m.get('FitToPagesTall')
        if m.get('FitToPagesWide') is not None:
            self.fit_to_pages_wide = m.get('FitToPagesWide')
        if m.get('PdfVector') is not None:
            self.pdf_vector = m.get('PdfVector')
        if m.get('Hidecomments') is not None:
            self.hidecomments = m.get('Hidecomments')
        return self


class ConvertOfficeFormatResponseBody(TeaModel):
    def __init__(
        self,
        page_count: int = None,
        request_id: str = None,
    ):
        self.page_count = page_count
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ConvertOfficeFormatResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ConvertOfficeFormatResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ConvertOfficeFormatResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGrabFrameTaskRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        video_uri: str = None,
        notify_topic_name: str = None,
        notify_endpoint: str = None,
        target_list: str = None,
        custom_message: str = None,
    ):
        self.project = project
        self.video_uri = video_uri
        self.notify_topic_name = notify_topic_name
        self.notify_endpoint = notify_endpoint
        self.target_list = target_list
        self.custom_message = custom_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.video_uri is not None:
            result['VideoUri'] = self.video_uri
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        if self.target_list is not None:
            result['TargetList'] = self.target_list
        if self.custom_message is not None:
            result['CustomMessage'] = self.custom_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('VideoUri') is not None:
            self.video_uri = m.get('VideoUri')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        if m.get('TargetList') is not None:
            self.target_list = m.get('TargetList')
        if m.get('CustomMessage') is not None:
            self.custom_message = m.get('CustomMessage')
        return self


class CreateGrabFrameTaskResponseBody(TeaModel):
    def __init__(
        self,
        task_type: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        self.task_type = task_type
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateGrabFrameTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateGrabFrameTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateGrabFrameTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGroupFacesJobRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        set_id: str = None,
        notify_topic_name: str = None,
        notify_endpoint: str = None,
    ):
        self.project = project
        self.set_id = set_id
        self.notify_topic_name = notify_topic_name
        self.notify_endpoint = notify_endpoint

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        return self


class CreateGroupFacesJobResponseBody(TeaModel):
    def __init__(
        self,
        job_type: str = None,
        request_id: str = None,
        set_id: str = None,
        job_id: str = None,
    ):
        self.job_type = job_type
        self.request_id = request_id
        self.set_id = set_id
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class CreateGroupFacesJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateGroupFacesJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateGroupFacesJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateImageProcessTaskRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        image_uri: str = None,
        notify_topic_name: str = None,
        notify_endpoint: str = None,
        target_list: str = None,
    ):
        self.project = project
        self.image_uri = image_uri
        self.notify_topic_name = notify_topic_name
        self.notify_endpoint = notify_endpoint
        self.target_list = target_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        if self.target_list is not None:
            result['TargetList'] = self.target_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        if m.get('TargetList') is not None:
            self.target_list = m.get('TargetList')
        return self


class CreateImageProcessTaskResponseBody(TeaModel):
    def __init__(
        self,
        task_type: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        self.task_type = task_type
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateImageProcessTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateImageProcessTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateImageProcessTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMediaComplexTaskRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        parameters: str = None,
        notify_topic_name: str = None,
        notify_endpoint: str = None,
    ):
        self.project = project
        self.parameters = parameters
        self.notify_topic_name = notify_topic_name
        self.notify_endpoint = notify_endpoint

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        return self


class CreateMediaComplexTaskResponseBody(TeaModel):
    def __init__(
        self,
        task_type: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        self.task_type = task_type
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateMediaComplexTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateMediaComplexTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateMediaComplexTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMergeFaceGroupsJobRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        set_id: str = None,
        notify_topic_name: str = None,
        notify_endpoint: str = None,
        group_id_from: str = None,
        group_id_to: str = None,
        custom_message: str = None,
    ):
        self.project = project
        self.set_id = set_id
        self.notify_topic_name = notify_topic_name
        self.notify_endpoint = notify_endpoint
        self.group_id_from = group_id_from
        self.group_id_to = group_id_to
        self.custom_message = custom_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        if self.group_id_from is not None:
            result['GroupIdFrom'] = self.group_id_from
        if self.group_id_to is not None:
            result['GroupIdTo'] = self.group_id_to
        if self.custom_message is not None:
            result['CustomMessage'] = self.custom_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        if m.get('GroupIdFrom') is not None:
            self.group_id_from = m.get('GroupIdFrom')
        if m.get('GroupIdTo') is not None:
            self.group_id_to = m.get('GroupIdTo')
        if m.get('CustomMessage') is not None:
            self.custom_message = m.get('CustomMessage')
        return self


class CreateMergeFaceGroupsJobResponseBody(TeaModel):
    def __init__(
        self,
        group_id_from: str = None,
        job_type: str = None,
        request_id: str = None,
        set_id: str = None,
        group_id_to: str = None,
        job_id: str = None,
    ):
        self.group_id_from = group_id_from
        self.job_type = job_type
        self.request_id = request_id
        self.set_id = set_id
        self.group_id_to = group_id_to
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id_from is not None:
            result['GroupIdFrom'] = self.group_id_from
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.group_id_to is not None:
            result['GroupIdTo'] = self.group_id_to
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupIdFrom') is not None:
            self.group_id_from = m.get('GroupIdFrom')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('GroupIdTo') is not None:
            self.group_id_to = m.get('GroupIdTo')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class CreateMergeFaceGroupsJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateMergeFaceGroupsJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateMergeFaceGroupsJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOfficeConversionTaskRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        src_uri: str = None,
        tgt_type: str = None,
        tgt_uri: str = None,
        notify_topic_name: str = None,
        notify_endpoint: str = None,
        src_type: str = None,
        start_page: int = None,
        end_page: int = None,
        max_sheet_row: int = None,
        max_sheet_col: int = None,
        max_sheet_count: int = None,
        sheet_one_page: bool = None,
        model_id: str = None,
        password: str = None,
        tgt_file_prefix: str = None,
        tgt_file_suffix: str = None,
        tgt_file_pages: str = None,
        fit_to_pages_tall: bool = None,
        fit_to_pages_wide: bool = None,
        idempotent_token: str = None,
        pdf_vector: bool = None,
        hidecomments: bool = None,
        display_dpi: int = None,
        user_data: str = None,
    ):
        self.project = project
        self.src_uri = src_uri
        self.tgt_type = tgt_type
        self.tgt_uri = tgt_uri
        self.notify_topic_name = notify_topic_name
        self.notify_endpoint = notify_endpoint
        self.src_type = src_type
        self.start_page = start_page
        self.end_page = end_page
        self.max_sheet_row = max_sheet_row
        self.max_sheet_col = max_sheet_col
        self.max_sheet_count = max_sheet_count
        self.sheet_one_page = sheet_one_page
        self.model_id = model_id
        self.password = password
        self.tgt_file_prefix = tgt_file_prefix
        self.tgt_file_suffix = tgt_file_suffix
        self.tgt_file_pages = tgt_file_pages
        self.fit_to_pages_tall = fit_to_pages_tall
        self.fit_to_pages_wide = fit_to_pages_wide
        self.idempotent_token = idempotent_token
        self.pdf_vector = pdf_vector
        self.hidecomments = hidecomments
        self.display_dpi = display_dpi
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.src_uri is not None:
            result['SrcUri'] = self.src_uri
        if self.tgt_type is not None:
            result['TgtType'] = self.tgt_type
        if self.tgt_uri is not None:
            result['TgtUri'] = self.tgt_uri
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        if self.src_type is not None:
            result['SrcType'] = self.src_type
        if self.start_page is not None:
            result['StartPage'] = self.start_page
        if self.end_page is not None:
            result['EndPage'] = self.end_page
        if self.max_sheet_row is not None:
            result['MaxSheetRow'] = self.max_sheet_row
        if self.max_sheet_col is not None:
            result['MaxSheetCol'] = self.max_sheet_col
        if self.max_sheet_count is not None:
            result['MaxSheetCount'] = self.max_sheet_count
        if self.sheet_one_page is not None:
            result['SheetOnePage'] = self.sheet_one_page
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.password is not None:
            result['Password'] = self.password
        if self.tgt_file_prefix is not None:
            result['TgtFilePrefix'] = self.tgt_file_prefix
        if self.tgt_file_suffix is not None:
            result['TgtFileSuffix'] = self.tgt_file_suffix
        if self.tgt_file_pages is not None:
            result['TgtFilePages'] = self.tgt_file_pages
        if self.fit_to_pages_tall is not None:
            result['FitToPagesTall'] = self.fit_to_pages_tall
        if self.fit_to_pages_wide is not None:
            result['FitToPagesWide'] = self.fit_to_pages_wide
        if self.idempotent_token is not None:
            result['IdempotentToken'] = self.idempotent_token
        if self.pdf_vector is not None:
            result['PdfVector'] = self.pdf_vector
        if self.hidecomments is not None:
            result['Hidecomments'] = self.hidecomments
        if self.display_dpi is not None:
            result['DisplayDpi'] = self.display_dpi
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SrcUri') is not None:
            self.src_uri = m.get('SrcUri')
        if m.get('TgtType') is not None:
            self.tgt_type = m.get('TgtType')
        if m.get('TgtUri') is not None:
            self.tgt_uri = m.get('TgtUri')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        if m.get('SrcType') is not None:
            self.src_type = m.get('SrcType')
        if m.get('StartPage') is not None:
            self.start_page = m.get('StartPage')
        if m.get('EndPage') is not None:
            self.end_page = m.get('EndPage')
        if m.get('MaxSheetRow') is not None:
            self.max_sheet_row = m.get('MaxSheetRow')
        if m.get('MaxSheetCol') is not None:
            self.max_sheet_col = m.get('MaxSheetCol')
        if m.get('MaxSheetCount') is not None:
            self.max_sheet_count = m.get('MaxSheetCount')
        if m.get('SheetOnePage') is not None:
            self.sheet_one_page = m.get('SheetOnePage')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('TgtFilePrefix') is not None:
            self.tgt_file_prefix = m.get('TgtFilePrefix')
        if m.get('TgtFileSuffix') is not None:
            self.tgt_file_suffix = m.get('TgtFileSuffix')
        if m.get('TgtFilePages') is not None:
            self.tgt_file_pages = m.get('TgtFilePages')
        if m.get('FitToPagesTall') is not None:
            self.fit_to_pages_tall = m.get('FitToPagesTall')
        if m.get('FitToPagesWide') is not None:
            self.fit_to_pages_wide = m.get('FitToPagesWide')
        if m.get('IdempotentToken') is not None:
            self.idempotent_token = m.get('IdempotentToken')
        if m.get('PdfVector') is not None:
            self.pdf_vector = m.get('PdfVector')
        if m.get('Hidecomments') is not None:
            self.hidecomments = m.get('Hidecomments')
        if m.get('DisplayDpi') is not None:
            self.display_dpi = m.get('DisplayDpi')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateOfficeConversionTaskResponseBody(TeaModel):
    def __init__(
        self,
        status: str = None,
        task_id: str = None,
        request_id: str = None,
        percent: int = None,
        create_time: str = None,
        tgt_loc: str = None,
    ):
        self.status = status
        self.task_id = task_id
        self.request_id = request_id
        self.percent = percent
        self.create_time = create_time
        self.tgt_loc = tgt_loc

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.tgt_loc is not None:
            result['TgtLoc'] = self.tgt_loc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('TgtLoc') is not None:
            self.tgt_loc = m.get('TgtLoc')
        return self


class CreateOfficeConversionTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateOfficeConversionTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateOfficeConversionTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSetRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        set_id: str = None,
        set_name: str = None,
    ):
        self.project = project
        self.set_id = set_id
        self.set_name = set_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.set_name is not None:
            result['SetName'] = self.set_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('SetName') is not None:
            self.set_name = m.get('SetName')
        return self


class CreateSetResponseBody(TeaModel):
    def __init__(
        self,
        video_count: int = None,
        request_id: str = None,
        create_time: str = None,
        video_length: int = None,
        set_id: str = None,
        image_count: int = None,
        face_count: int = None,
        set_name: str = None,
        modify_time: str = None,
    ):
        self.video_count = video_count
        self.request_id = request_id
        self.create_time = create_time
        self.video_length = video_length
        self.set_id = set_id
        self.image_count = image_count
        self.face_count = face_count
        self.set_name = set_name
        self.modify_time = modify_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_count is not None:
            result['VideoCount'] = self.video_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.video_length is not None:
            result['VideoLength'] = self.video_length
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.image_count is not None:
            result['ImageCount'] = self.image_count
        if self.face_count is not None:
            result['FaceCount'] = self.face_count
        if self.set_name is not None:
            result['SetName'] = self.set_name
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoCount') is not None:
            self.video_count = m.get('VideoCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('VideoLength') is not None:
            self.video_length = m.get('VideoLength')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('ImageCount') is not None:
            self.image_count = m.get('ImageCount')
        if m.get('FaceCount') is not None:
            self.face_count = m.get('FaceCount')
        if m.get('SetName') is not None:
            self.set_name = m.get('SetName')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        return self


class CreateSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSetResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVideoAbstractTaskRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        video_uri: str = None,
        notify_topic_name: str = None,
        notify_endpoint: str = None,
        target_video_uri: str = None,
        target_clips_uri: str = None,
        abstract_length: int = None,
    ):
        self.project = project
        self.video_uri = video_uri
        self.notify_topic_name = notify_topic_name
        self.notify_endpoint = notify_endpoint
        self.target_video_uri = target_video_uri
        self.target_clips_uri = target_clips_uri
        self.abstract_length = abstract_length

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.video_uri is not None:
            result['VideoUri'] = self.video_uri
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        if self.target_video_uri is not None:
            result['TargetVideoUri'] = self.target_video_uri
        if self.target_clips_uri is not None:
            result['TargetClipsUri'] = self.target_clips_uri
        if self.abstract_length is not None:
            result['AbstractLength'] = self.abstract_length
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('VideoUri') is not None:
            self.video_uri = m.get('VideoUri')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        if m.get('TargetVideoUri') is not None:
            self.target_video_uri = m.get('TargetVideoUri')
        if m.get('TargetClipsUri') is not None:
            self.target_clips_uri = m.get('TargetClipsUri')
        if m.get('AbstractLength') is not None:
            self.abstract_length = m.get('AbstractLength')
        return self


class CreateVideoAbstractTaskResponseBody(TeaModel):
    def __init__(
        self,
        task_type: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        self.task_type = task_type
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateVideoAbstractTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateVideoAbstractTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateVideoAbstractTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVideoAnalyseTaskRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        video_uri: str = None,
        tgt_uri: str = None,
        notify_topic_name: str = None,
        notify_endpoint: str = None,
    ):
        self.project = project
        self.video_uri = video_uri
        self.tgt_uri = tgt_uri
        self.notify_topic_name = notify_topic_name
        self.notify_endpoint = notify_endpoint

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.video_uri is not None:
            result['VideoUri'] = self.video_uri
        if self.tgt_uri is not None:
            result['TgtUri'] = self.tgt_uri
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('VideoUri') is not None:
            self.video_uri = m.get('VideoUri')
        if m.get('TgtUri') is not None:
            self.tgt_uri = m.get('TgtUri')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        return self


class CreateVideoAnalyseTaskResponseBody(TeaModel):
    def __init__(
        self,
        task_type: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        self.task_type = task_type
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateVideoAnalyseTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateVideoAnalyseTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateVideoAnalyseTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVideoCompressTaskRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        video_uri: str = None,
        notify_topic_name: str = None,
        notify_endpoint: str = None,
        target_list: str = None,
        custom_message: str = None,
        target_container: str = None,
        target_segment: str = None,
    ):
        self.project = project
        self.video_uri = video_uri
        self.notify_topic_name = notify_topic_name
        self.notify_endpoint = notify_endpoint
        self.target_list = target_list
        self.custom_message = custom_message
        self.target_container = target_container
        self.target_segment = target_segment

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.video_uri is not None:
            result['VideoUri'] = self.video_uri
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        if self.target_list is not None:
            result['TargetList'] = self.target_list
        if self.custom_message is not None:
            result['CustomMessage'] = self.custom_message
        if self.target_container is not None:
            result['TargetContainer'] = self.target_container
        if self.target_segment is not None:
            result['TargetSegment'] = self.target_segment
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('VideoUri') is not None:
            self.video_uri = m.get('VideoUri')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        if m.get('TargetList') is not None:
            self.target_list = m.get('TargetList')
        if m.get('CustomMessage') is not None:
            self.custom_message = m.get('CustomMessage')
        if m.get('TargetContainer') is not None:
            self.target_container = m.get('TargetContainer')
        if m.get('TargetSegment') is not None:
            self.target_segment = m.get('TargetSegment')
        return self


class CreateVideoCompressTaskResponseBody(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        request_id: str = None,
        task_type: str = None,
    ):
        self.task_id = task_id
        self.request_id = request_id
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class CreateVideoCompressTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateVideoCompressTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateVideoCompressTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVideoProduceTaskRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        images: str = None,
        notify_topic_name: str = None,
        notify_endpoint: str = None,
        target_uri: str = None,
        custom_message: str = None,
        music: str = None,
        width: int = None,
        height: int = None,
        template_name: str = None,
    ):
        self.project = project
        self.images = images
        self.notify_topic_name = notify_topic_name
        self.notify_endpoint = notify_endpoint
        self.target_uri = target_uri
        self.custom_message = custom_message
        self.music = music
        self.width = width
        self.height = height
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.images is not None:
            result['Images'] = self.images
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        if self.target_uri is not None:
            result['TargetUri'] = self.target_uri
        if self.custom_message is not None:
            result['CustomMessage'] = self.custom_message
        if self.music is not None:
            result['Music'] = self.music
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('Images') is not None:
            self.images = m.get('Images')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        if m.get('TargetUri') is not None:
            self.target_uri = m.get('TargetUri')
        if m.get('CustomMessage') is not None:
            self.custom_message = m.get('CustomMessage')
        if m.get('Music') is not None:
            self.music = m.get('Music')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class CreateVideoProduceTaskResponseBody(TeaModel):
    def __init__(
        self,
        task_type: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        self.task_type = task_type
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateVideoProduceTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateVideoProduceTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateVideoProduceTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DecodeBlindWatermarkRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        image_uri: str = None,
        original_image_uri: str = None,
        target_uri: str = None,
        image_quality: int = None,
        model: str = None,
    ):
        self.project = project
        self.image_uri = image_uri
        self.original_image_uri = original_image_uri
        self.target_uri = target_uri
        self.image_quality = image_quality
        self.model = model

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        if self.original_image_uri is not None:
            result['OriginalImageUri'] = self.original_image_uri
        if self.target_uri is not None:
            result['TargetUri'] = self.target_uri
        if self.image_quality is not None:
            result['ImageQuality'] = self.image_quality
        if self.model is not None:
            result['Model'] = self.model
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        if m.get('OriginalImageUri') is not None:
            self.original_image_uri = m.get('OriginalImageUri')
        if m.get('TargetUri') is not None:
            self.target_uri = m.get('TargetUri')
        if m.get('ImageQuality') is not None:
            self.image_quality = m.get('ImageQuality')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        return self


class DecodeBlindWatermarkResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        target_uri: str = None,
        content: str = None,
    ):
        self.request_id = request_id
        self.target_uri = target_uri
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.target_uri is not None:
            result['TargetUri'] = self.target_uri
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TargetUri') is not None:
            self.target_uri = m.get('TargetUri')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class DecodeBlindWatermarkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DecodeBlindWatermarkResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DecodeBlindWatermarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteImageRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        set_id: str = None,
        image_uri: str = None,
    ):
        self.project = project
        self.set_id = set_id
        self.image_uri = image_uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        return self


class DeleteImageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        set_id: str = None,
        image_uri: str = None,
    ):
        self.request_id = request_id
        self.set_id = set_id
        self.image_uri = image_uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        return self


class DeleteImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteImageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteImageJobRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        job_type: str = None,
        job_id: str = None,
    ):
        self.project = project
        self.job_type = job_type
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class DeleteImageJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteImageJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteImageJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteImageJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteOfficeConversionTaskRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        task_id: str = None,
    ):
        self.project = project
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DeleteOfficeConversionTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteOfficeConversionTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteOfficeConversionTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteOfficeConversionTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProjectRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
    ):
        self.project = project

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        return self


class DeleteProjectResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteProjectResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSetRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        set_id: str = None,
    ):
        self.project = project
        self.set_id = set_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.set_id is not None:
            result['SetId'] = self.set_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        return self


class DeleteSetResponseBody(TeaModel):
    def __init__(
        self,
        set_id: str = None,
        request_id: str = None,
    ):
        self.set_id = set_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteSetResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVideoRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        set_id: str = None,
        video_uri: str = None,
        resources: bool = None,
    ):
        self.project = project
        self.set_id = set_id
        self.video_uri = video_uri
        self.resources = resources

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.video_uri is not None:
            result['VideoUri'] = self.video_uri
        if self.resources is not None:
            result['Resources'] = self.resources
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('VideoUri') is not None:
            self.video_uri = m.get('VideoUri')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        return self


class DeleteVideoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        video_uri: str = None,
        set_id: str = None,
    ):
        self.request_id = request_id
        self.video_uri = video_uri
        self.set_id = set_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.video_uri is not None:
            result['VideoUri'] = self.video_uri
        if self.set_id is not None:
            result['SetId'] = self.set_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VideoUri') is not None:
            self.video_uri = m.get('VideoUri')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        return self


class DeleteVideoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteVideoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteVideoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVideoTaskRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        task_type: str = None,
        task_id: str = None,
    ):
        self.project = project
        self.task_type = task_type
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DeleteVideoTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteVideoTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteVideoTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteVideoTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsResponseBodyRegionsRegion(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        project_types: List[str] = None,
    ):
        self.region_id = region_id
        self.project_types = project_types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.project_types is not None:
            result['ProjectTypes'] = self.project_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ProjectTypes') is not None:
            self.project_types = m.get('ProjectTypes')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        region: List[DescribeRegionsResponseBodyRegionsRegion] = None,
    ):
        self.region = region

    def validate(self):
        if self.region:
            for k in self.region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Region'] = []
        if self.region is not None:
            for k in self.region:
                result['Region'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region = []
        if m.get('Region') is not None:
            for k in m.get('Region'):
                temp_model = DescribeRegionsResponseBodyRegionsRegion()
                self.region.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        regions: DescribeRegionsResponseBodyRegions = None,
    ):
        self.request_id = request_id
        self.regions = regions

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Regions') is not None:
            temp_model = DescribeRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRegionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectImageBodiesRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        image_uri: str = None,
    ):
        self.project = project
        self.image_uri = image_uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        return self


class DetectImageBodiesResponseBodyBodiesBodyBoundary(TeaModel):
    def __init__(
        self,
        left: int = None,
        top: int = None,
        width: int = None,
        height: int = None,
    ):
        self.left = left
        self.top = top
        self.width = width
        self.height = height

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class DetectImageBodiesResponseBodyBodies(TeaModel):
    def __init__(
        self,
        body_confidence: float = None,
        body_boundary: DetectImageBodiesResponseBodyBodiesBodyBoundary = None,
    ):
        self.body_confidence = body_confidence
        self.body_boundary = body_boundary

    def validate(self):
        if self.body_boundary:
            self.body_boundary.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body_confidence is not None:
            result['BodyConfidence'] = self.body_confidence
        if self.body_boundary is not None:
            result['BodyBoundary'] = self.body_boundary.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BodyConfidence') is not None:
            self.body_confidence = m.get('BodyConfidence')
        if m.get('BodyBoundary') is not None:
            temp_model = DetectImageBodiesResponseBodyBodiesBodyBoundary()
            self.body_boundary = temp_model.from_map(m['BodyBoundary'])
        return self


class DetectImageBodiesResponseBody(TeaModel):
    def __init__(
        self,
        image_uri: str = None,
        request_id: str = None,
        bodies: List[DetectImageBodiesResponseBodyBodies] = None,
    ):
        self.image_uri = image_uri
        self.request_id = request_id
        self.bodies = bodies

    def validate(self):
        if self.bodies:
            for k in self.bodies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Bodies'] = []
        if self.bodies is not None:
            for k in self.bodies:
                result['Bodies'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.bodies = []
        if m.get('Bodies') is not None:
            for k in m.get('Bodies'):
                temp_model = DetectImageBodiesResponseBodyBodies()
                self.bodies.append(temp_model.from_map(k))
        return self


class DetectImageBodiesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DetectImageBodiesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DetectImageBodiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectImageFacesRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        image_uri: str = None,
    ):
        self.project = project
        self.image_uri = image_uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        return self


class DetectImageFacesResponseBodyFacesFaceAttributesFaceBoundary(TeaModel):
    def __init__(
        self,
        left: int = None,
        top: int = None,
        width: int = None,
        height: int = None,
    ):
        self.left = left
        self.top = top
        self.width = width
        self.height = height

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class DetectImageFacesResponseBodyFacesFaceAttributesHeadPose(TeaModel):
    def __init__(
        self,
        pitch: float = None,
        roll: float = None,
        yaw: float = None,
    ):
        self.pitch = pitch
        self.roll = roll
        self.yaw = yaw

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pitch is not None:
            result['Pitch'] = self.pitch
        if self.roll is not None:
            result['Roll'] = self.roll
        if self.yaw is not None:
            result['Yaw'] = self.yaw
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pitch') is not None:
            self.pitch = m.get('Pitch')
        if m.get('Roll') is not None:
            self.roll = m.get('Roll')
        if m.get('Yaw') is not None:
            self.yaw = m.get('Yaw')
        return self


class DetectImageFacesResponseBodyFacesFaceAttributes(TeaModel):
    def __init__(
        self,
        glasses_confidence: float = None,
        glasses: str = None,
        mask: str = None,
        beard_confidence: float = None,
        mask_confidence: float = None,
        beard: str = None,
        face_boundary: DetectImageFacesResponseBodyFacesFaceAttributesFaceBoundary = None,
        head_pose: DetectImageFacesResponseBodyFacesFaceAttributesHeadPose = None,
    ):
        self.glasses_confidence = glasses_confidence
        self.glasses = glasses
        self.mask = mask
        self.beard_confidence = beard_confidence
        self.mask_confidence = mask_confidence
        self.beard = beard
        self.face_boundary = face_boundary
        self.head_pose = head_pose

    def validate(self):
        if self.face_boundary:
            self.face_boundary.validate()
        if self.head_pose:
            self.head_pose.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.glasses_confidence is not None:
            result['GlassesConfidence'] = self.glasses_confidence
        if self.glasses is not None:
            result['Glasses'] = self.glasses
        if self.mask is not None:
            result['Mask'] = self.mask
        if self.beard_confidence is not None:
            result['BeardConfidence'] = self.beard_confidence
        if self.mask_confidence is not None:
            result['MaskConfidence'] = self.mask_confidence
        if self.beard is not None:
            result['Beard'] = self.beard
        if self.face_boundary is not None:
            result['FaceBoundary'] = self.face_boundary.to_map()
        if self.head_pose is not None:
            result['HeadPose'] = self.head_pose.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GlassesConfidence') is not None:
            self.glasses_confidence = m.get('GlassesConfidence')
        if m.get('Glasses') is not None:
            self.glasses = m.get('Glasses')
        if m.get('Mask') is not None:
            self.mask = m.get('Mask')
        if m.get('BeardConfidence') is not None:
            self.beard_confidence = m.get('BeardConfidence')
        if m.get('MaskConfidence') is not None:
            self.mask_confidence = m.get('MaskConfidence')
        if m.get('Beard') is not None:
            self.beard = m.get('Beard')
        if m.get('FaceBoundary') is not None:
            temp_model = DetectImageFacesResponseBodyFacesFaceAttributesFaceBoundary()
            self.face_boundary = temp_model.from_map(m['FaceBoundary'])
        if m.get('HeadPose') is not None:
            temp_model = DetectImageFacesResponseBodyFacesFaceAttributesHeadPose()
            self.head_pose = temp_model.from_map(m['HeadPose'])
        return self


class DetectImageFacesResponseBodyFacesEmotionDetails(TeaModel):
    def __init__(
        self,
        happy: float = None,
        calm: float = None,
        surprised: float = None,
        disgusted: float = None,
        angry: float = None,
        sad: float = None,
        scared: float = None,
    ):
        self.happy = happy
        self.calm = calm
        self.surprised = surprised
        self.disgusted = disgusted
        self.angry = angry
        self.sad = sad
        self.scared = scared

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.happy is not None:
            result['HAPPY'] = self.happy
        if self.calm is not None:
            result['CALM'] = self.calm
        if self.surprised is not None:
            result['SURPRISED'] = self.surprised
        if self.disgusted is not None:
            result['DISGUSTED'] = self.disgusted
        if self.angry is not None:
            result['ANGRY'] = self.angry
        if self.sad is not None:
            result['SAD'] = self.sad
        if self.scared is not None:
            result['SCARED'] = self.scared
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HAPPY') is not None:
            self.happy = m.get('HAPPY')
        if m.get('CALM') is not None:
            self.calm = m.get('CALM')
        if m.get('SURPRISED') is not None:
            self.surprised = m.get('SURPRISED')
        if m.get('DISGUSTED') is not None:
            self.disgusted = m.get('DISGUSTED')
        if m.get('ANGRY') is not None:
            self.angry = m.get('ANGRY')
        if m.get('SAD') is not None:
            self.sad = m.get('SAD')
        if m.get('SCARED') is not None:
            self.scared = m.get('SCARED')
        return self


class DetectImageFacesResponseBodyFaces(TeaModel):
    def __init__(
        self,
        emotion_confidence: float = None,
        attractive: float = None,
        attractive_confidence: float = None,
        gender: str = None,
        age_confidence: float = None,
        gender_confidence: float = None,
        face_id: str = None,
        face_quality: float = None,
        emotion: str = None,
        age: int = None,
        face_confidence: float = None,
        face_attributes: DetectImageFacesResponseBodyFacesFaceAttributes = None,
        emotion_details: DetectImageFacesResponseBodyFacesEmotionDetails = None,
    ):
        self.emotion_confidence = emotion_confidence
        self.attractive = attractive
        self.attractive_confidence = attractive_confidence
        self.gender = gender
        self.age_confidence = age_confidence
        self.gender_confidence = gender_confidence
        self.face_id = face_id
        self.face_quality = face_quality
        self.emotion = emotion
        self.age = age
        self.face_confidence = face_confidence
        self.face_attributes = face_attributes
        self.emotion_details = emotion_details

    def validate(self):
        if self.face_attributes:
            self.face_attributes.validate()
        if self.emotion_details:
            self.emotion_details.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.emotion_confidence is not None:
            result['EmotionConfidence'] = self.emotion_confidence
        if self.attractive is not None:
            result['Attractive'] = self.attractive
        if self.attractive_confidence is not None:
            result['AttractiveConfidence'] = self.attractive_confidence
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.age_confidence is not None:
            result['AgeConfidence'] = self.age_confidence
        if self.gender_confidence is not None:
            result['GenderConfidence'] = self.gender_confidence
        if self.face_id is not None:
            result['FaceId'] = self.face_id
        if self.face_quality is not None:
            result['FaceQuality'] = self.face_quality
        if self.emotion is not None:
            result['Emotion'] = self.emotion
        if self.age is not None:
            result['Age'] = self.age
        if self.face_confidence is not None:
            result['FaceConfidence'] = self.face_confidence
        if self.face_attributes is not None:
            result['FaceAttributes'] = self.face_attributes.to_map()
        if self.emotion_details is not None:
            result['EmotionDetails'] = self.emotion_details.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EmotionConfidence') is not None:
            self.emotion_confidence = m.get('EmotionConfidence')
        if m.get('Attractive') is not None:
            self.attractive = m.get('Attractive')
        if m.get('AttractiveConfidence') is not None:
            self.attractive_confidence = m.get('AttractiveConfidence')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('AgeConfidence') is not None:
            self.age_confidence = m.get('AgeConfidence')
        if m.get('GenderConfidence') is not None:
            self.gender_confidence = m.get('GenderConfidence')
        if m.get('FaceId') is not None:
            self.face_id = m.get('FaceId')
        if m.get('FaceQuality') is not None:
            self.face_quality = m.get('FaceQuality')
        if m.get('Emotion') is not None:
            self.emotion = m.get('Emotion')
        if m.get('Age') is not None:
            self.age = m.get('Age')
        if m.get('FaceConfidence') is not None:
            self.face_confidence = m.get('FaceConfidence')
        if m.get('FaceAttributes') is not None:
            temp_model = DetectImageFacesResponseBodyFacesFaceAttributes()
            self.face_attributes = temp_model.from_map(m['FaceAttributes'])
        if m.get('EmotionDetails') is not None:
            temp_model = DetectImageFacesResponseBodyFacesEmotionDetails()
            self.emotion_details = temp_model.from_map(m['EmotionDetails'])
        return self


class DetectImageFacesResponseBody(TeaModel):
    def __init__(
        self,
        image_uri: str = None,
        request_id: str = None,
        faces: List[DetectImageFacesResponseBodyFaces] = None,
    ):
        self.image_uri = image_uri
        self.request_id = request_id
        self.faces = faces

    def validate(self):
        if self.faces:
            for k in self.faces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Faces'] = []
        if self.faces is not None:
            for k in self.faces:
                result['Faces'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.faces = []
        if m.get('Faces') is not None:
            for k in m.get('Faces'):
                temp_model = DetectImageFacesResponseBodyFaces()
                self.faces.append(temp_model.from_map(k))
        return self


class DetectImageFacesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DetectImageFacesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DetectImageFacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectImageLogosRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        image_uri: str = None,
    ):
        self.project = project
        self.image_uri = image_uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        return self


class DetectImageLogosResponseBodyLogosLogoBoundary(TeaModel):
    def __init__(
        self,
        left: int = None,
        top: int = None,
        width: int = None,
        height: int = None,
    ):
        self.left = left
        self.top = top
        self.width = width
        self.height = height

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class DetectImageLogosResponseBodyLogos(TeaModel):
    def __init__(
        self,
        logo_confidence: float = None,
        logo_name: str = None,
        logo_boundary: DetectImageLogosResponseBodyLogosLogoBoundary = None,
    ):
        self.logo_confidence = logo_confidence
        self.logo_name = logo_name
        self.logo_boundary = logo_boundary

    def validate(self):
        if self.logo_boundary:
            self.logo_boundary.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logo_confidence is not None:
            result['LogoConfidence'] = self.logo_confidence
        if self.logo_name is not None:
            result['LogoName'] = self.logo_name
        if self.logo_boundary is not None:
            result['LogoBoundary'] = self.logo_boundary.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogoConfidence') is not None:
            self.logo_confidence = m.get('LogoConfidence')
        if m.get('LogoName') is not None:
            self.logo_name = m.get('LogoName')
        if m.get('LogoBoundary') is not None:
            temp_model = DetectImageLogosResponseBodyLogosLogoBoundary()
            self.logo_boundary = temp_model.from_map(m['LogoBoundary'])
        return self


class DetectImageLogosResponseBody(TeaModel):
    def __init__(
        self,
        image_uri: str = None,
        request_id: str = None,
        logos: List[DetectImageLogosResponseBodyLogos] = None,
    ):
        self.image_uri = image_uri
        self.request_id = request_id
        self.logos = logos

    def validate(self):
        if self.logos:
            for k in self.logos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Logos'] = []
        if self.logos is not None:
            for k in self.logos:
                result['Logos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.logos = []
        if m.get('Logos') is not None:
            for k in m.get('Logos'):
                temp_model = DetectImageLogosResponseBodyLogos()
                self.logos.append(temp_model.from_map(k))
        return self


class DetectImageLogosResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DetectImageLogosResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DetectImageLogosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectImageQRCodesRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        image_uri: str = None,
    ):
        self.project = project
        self.image_uri = image_uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        return self


class DetectImageQRCodesResponseBodyQRCodesQRCodeBoundary(TeaModel):
    def __init__(
        self,
        left: int = None,
        top: int = None,
        width: int = None,
        height: int = None,
    ):
        self.left = left
        self.top = top
        self.width = width
        self.height = height

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class DetectImageQRCodesResponseBodyQRCodes(TeaModel):
    def __init__(
        self,
        content: str = None,
        qrcode_boundary: DetectImageQRCodesResponseBodyQRCodesQRCodeBoundary = None,
    ):
        self.content = content
        self.qrcode_boundary = qrcode_boundary

    def validate(self):
        if self.qrcode_boundary:
            self.qrcode_boundary.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.qrcode_boundary is not None:
            result['QRCodeBoundary'] = self.qrcode_boundary.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('QRCodeBoundary') is not None:
            temp_model = DetectImageQRCodesResponseBodyQRCodesQRCodeBoundary()
            self.qrcode_boundary = temp_model.from_map(m['QRCodeBoundary'])
        return self


class DetectImageQRCodesResponseBody(TeaModel):
    def __init__(
        self,
        image_uri: str = None,
        request_id: str = None,
        qrcodes: List[DetectImageQRCodesResponseBodyQRCodes] = None,
    ):
        self.image_uri = image_uri
        self.request_id = request_id
        self.qrcodes = qrcodes

    def validate(self):
        if self.qrcodes:
            for k in self.qrcodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['QRCodes'] = []
        if self.qrcodes is not None:
            for k in self.qrcodes:
                result['QRCodes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.qrcodes = []
        if m.get('QRCodes') is not None:
            for k in m.get('QRCodes'):
                temp_model = DetectImageQRCodesResponseBodyQRCodes()
                self.qrcodes.append(temp_model.from_map(k))
        return self


class DetectImageQRCodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DetectImageQRCodesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DetectImageQRCodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectImageTagsRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        image_uri: str = None,
    ):
        self.project = project
        self.image_uri = image_uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        return self


class DetectImageTagsResponseBodyTags(TeaModel):
    def __init__(
        self,
        parent_tag_en_name: str = None,
        tag_name: str = None,
        tag_confidence: float = None,
        tag_en_name: str = None,
        tag_level: int = None,
        parent_tag_name: str = None,
    ):
        self.parent_tag_en_name = parent_tag_en_name
        self.tag_name = tag_name
        self.tag_confidence = tag_confidence
        self.tag_en_name = tag_en_name
        self.tag_level = tag_level
        self.parent_tag_name = parent_tag_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parent_tag_en_name is not None:
            result['ParentTagEnName'] = self.parent_tag_en_name
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        if self.tag_confidence is not None:
            result['TagConfidence'] = self.tag_confidence
        if self.tag_en_name is not None:
            result['TagEnName'] = self.tag_en_name
        if self.tag_level is not None:
            result['TagLevel'] = self.tag_level
        if self.parent_tag_name is not None:
            result['ParentTagName'] = self.parent_tag_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParentTagEnName') is not None:
            self.parent_tag_en_name = m.get('ParentTagEnName')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        if m.get('TagConfidence') is not None:
            self.tag_confidence = m.get('TagConfidence')
        if m.get('TagEnName') is not None:
            self.tag_en_name = m.get('TagEnName')
        if m.get('TagLevel') is not None:
            self.tag_level = m.get('TagLevel')
        if m.get('ParentTagName') is not None:
            self.parent_tag_name = m.get('ParentTagName')
        return self


class DetectImageTagsResponseBody(TeaModel):
    def __init__(
        self,
        image_uri: str = None,
        request_id: str = None,
        tags: List[DetectImageTagsResponseBodyTags] = None,
    ):
        self.image_uri = image_uri
        self.request_id = request_id
        self.tags = tags

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DetectImageTagsResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        return self


class DetectImageTagsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DetectImageTagsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DetectImageTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectQRCodesRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        src_uris: str = None,
    ):
        self.project = project
        self.src_uris = src_uris

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.src_uris is not None:
            result['SrcUris'] = self.src_uris
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SrcUris') is not None:
            self.src_uris = m.get('SrcUris')
        return self


class DetectQRCodesResponseBodySuccessDetailsQRCodesQRCodesRectangle(TeaModel):
    def __init__(
        self,
        left: str = None,
        top: str = None,
        width: str = None,
        height: str = None,
    ):
        self.left = left
        self.top = top
        self.width = width
        self.height = height

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class DetectQRCodesResponseBodySuccessDetailsQRCodes(TeaModel):
    def __init__(
        self,
        content: str = None,
        qrcodes_rectangle: DetectQRCodesResponseBodySuccessDetailsQRCodesQRCodesRectangle = None,
    ):
        self.content = content
        self.qrcodes_rectangle = qrcodes_rectangle

    def validate(self):
        if self.qrcodes_rectangle:
            self.qrcodes_rectangle.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.qrcodes_rectangle is not None:
            result['QRCodesRectangle'] = self.qrcodes_rectangle.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('QRCodesRectangle') is not None:
            temp_model = DetectQRCodesResponseBodySuccessDetailsQRCodesQRCodesRectangle()
            self.qrcodes_rectangle = temp_model.from_map(m['QRCodesRectangle'])
        return self


class DetectQRCodesResponseBodySuccessDetails(TeaModel):
    def __init__(
        self,
        src_uri: str = None,
        qrcodes: List[DetectQRCodesResponseBodySuccessDetailsQRCodes] = None,
    ):
        self.src_uri = src_uri
        self.qrcodes = qrcodes

    def validate(self):
        if self.qrcodes:
            for k in self.qrcodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.src_uri is not None:
            result['SrcUri'] = self.src_uri
        result['QRCodes'] = []
        if self.qrcodes is not None:
            for k in self.qrcodes:
                result['QRCodes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SrcUri') is not None:
            self.src_uri = m.get('SrcUri')
        self.qrcodes = []
        if m.get('QRCodes') is not None:
            for k in m.get('QRCodes'):
                temp_model = DetectQRCodesResponseBodySuccessDetailsQRCodes()
                self.qrcodes.append(temp_model.from_map(k))
        return self


class DetectQRCodesResponseBodyFailDetails(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        src_uri: str = None,
        error_code: str = None,
    ):
        self.error_message = error_message
        self.src_uri = src_uri
        self.error_code = error_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.src_uri is not None:
            result['SrcUri'] = self.src_uri
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('SrcUri') is not None:
            self.src_uri = m.get('SrcUri')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        return self


class DetectQRCodesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success_details: List[DetectQRCodesResponseBodySuccessDetails] = None,
        fail_details: List[DetectQRCodesResponseBodyFailDetails] = None,
    ):
        self.request_id = request_id
        self.success_details = success_details
        self.fail_details = fail_details

    def validate(self):
        if self.success_details:
            for k in self.success_details:
                if k:
                    k.validate()
        if self.fail_details:
            for k in self.fail_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SuccessDetails'] = []
        if self.success_details is not None:
            for k in self.success_details:
                result['SuccessDetails'].append(k.to_map() if k else None)
        result['FailDetails'] = []
        if self.fail_details is not None:
            for k in self.fail_details:
                result['FailDetails'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.success_details = []
        if m.get('SuccessDetails') is not None:
            for k in m.get('SuccessDetails'):
                temp_model = DetectQRCodesResponseBodySuccessDetails()
                self.success_details.append(temp_model.from_map(k))
        self.fail_details = []
        if m.get('FailDetails') is not None:
            for k in m.get('FailDetails'):
                temp_model = DetectQRCodesResponseBodyFailDetails()
                self.fail_details.append(temp_model.from_map(k))
        return self


class DetectQRCodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DetectQRCodesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DetectQRCodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EncodeBlindWatermarkRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        image_uri: str = None,
        watermark_uri: str = None,
        target_uri: str = None,
        image_quality: str = None,
        content: str = None,
        target_image_type: str = None,
        model: str = None,
    ):
        self.project = project
        self.image_uri = image_uri
        self.watermark_uri = watermark_uri
        self.target_uri = target_uri
        self.image_quality = image_quality
        self.content = content
        self.target_image_type = target_image_type
        self.model = model

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        if self.watermark_uri is not None:
            result['WatermarkUri'] = self.watermark_uri
        if self.target_uri is not None:
            result['TargetUri'] = self.target_uri
        if self.image_quality is not None:
            result['ImageQuality'] = self.image_quality
        if self.content is not None:
            result['Content'] = self.content
        if self.target_image_type is not None:
            result['TargetImageType'] = self.target_image_type
        if self.model is not None:
            result['Model'] = self.model
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        if m.get('WatermarkUri') is not None:
            self.watermark_uri = m.get('WatermarkUri')
        if m.get('TargetUri') is not None:
            self.target_uri = m.get('TargetUri')
        if m.get('ImageQuality') is not None:
            self.image_quality = m.get('ImageQuality')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('TargetImageType') is not None:
            self.target_image_type = m.get('TargetImageType')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        return self


class EncodeBlindWatermarkResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        target_uri: str = None,
        content: str = None,
    ):
        self.request_id = request_id
        self.target_uri = target_uri
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.target_uri is not None:
            result['TargetUri'] = self.target_uri
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TargetUri') is not None:
            self.target_uri = m.get('TargetUri')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class EncodeBlindWatermarkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EncodeBlindWatermarkResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = EncodeBlindWatermarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FindImagesRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        set_id: str = None,
        image_size_range: str = None,
        image_time_range: str = None,
        create_time_range: str = None,
        modify_time_range: str = None,
        source_type: str = None,
        source_uri_prefix: str = None,
        remarks_aprefix: str = None,
        remarks_bprefix: str = None,
        tag_names: str = None,
        ocrcontents_match: str = None,
        age_range: str = None,
        gender: str = None,
        emotion: str = None,
        order_by: str = None,
        order: str = None,
        marker: str = None,
        location_boundary: str = None,
        remarks_cprefix: str = None,
        remarks_dprefix: str = None,
        external_id: str = None,
        group_id: str = None,
        limit: int = None,
        faces_modify_time_range: str = None,
        tags_modify_time_range: str = None,
        address_line_contents_match: str = None,
        remarks_array_ain: str = None,
        remarks_array_bin: str = None,
    ):
        self.project = project
        self.set_id = set_id
        self.image_size_range = image_size_range
        self.image_time_range = image_time_range
        self.create_time_range = create_time_range
        self.modify_time_range = modify_time_range
        self.source_type = source_type
        self.source_uri_prefix = source_uri_prefix
        self.remarks_aprefix = remarks_aprefix
        self.remarks_bprefix = remarks_bprefix
        self.tag_names = tag_names
        self.ocrcontents_match = ocrcontents_match
        self.age_range = age_range
        self.gender = gender
        self.emotion = emotion
        self.order_by = order_by
        self.order = order
        self.marker = marker
        self.location_boundary = location_boundary
        self.remarks_cprefix = remarks_cprefix
        self.remarks_dprefix = remarks_dprefix
        self.external_id = external_id
        self.group_id = group_id
        self.limit = limit
        self.faces_modify_time_range = faces_modify_time_range
        self.tags_modify_time_range = tags_modify_time_range
        self.address_line_contents_match = address_line_contents_match
        self.remarks_array_ain = remarks_array_ain
        self.remarks_array_bin = remarks_array_bin

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.image_size_range is not None:
            result['ImageSizeRange'] = self.image_size_range
        if self.image_time_range is not None:
            result['ImageTimeRange'] = self.image_time_range
        if self.create_time_range is not None:
            result['CreateTimeRange'] = self.create_time_range
        if self.modify_time_range is not None:
            result['ModifyTimeRange'] = self.modify_time_range
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.source_uri_prefix is not None:
            result['SourceUriPrefix'] = self.source_uri_prefix
        if self.remarks_aprefix is not None:
            result['RemarksAPrefix'] = self.remarks_aprefix
        if self.remarks_bprefix is not None:
            result['RemarksBPrefix'] = self.remarks_bprefix
        if self.tag_names is not None:
            result['TagNames'] = self.tag_names
        if self.ocrcontents_match is not None:
            result['OCRContentsMatch'] = self.ocrcontents_match
        if self.age_range is not None:
            result['AgeRange'] = self.age_range
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.emotion is not None:
            result['Emotion'] = self.emotion
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.order is not None:
            result['Order'] = self.order
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.location_boundary is not None:
            result['LocationBoundary'] = self.location_boundary
        if self.remarks_cprefix is not None:
            result['RemarksCPrefix'] = self.remarks_cprefix
        if self.remarks_dprefix is not None:
            result['RemarksDPrefix'] = self.remarks_dprefix
        if self.external_id is not None:
            result['ExternalId'] = self.external_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.faces_modify_time_range is not None:
            result['FacesModifyTimeRange'] = self.faces_modify_time_range
        if self.tags_modify_time_range is not None:
            result['TagsModifyTimeRange'] = self.tags_modify_time_range
        if self.address_line_contents_match is not None:
            result['AddressLineContentsMatch'] = self.address_line_contents_match
        if self.remarks_array_ain is not None:
            result['RemarksArrayAIn'] = self.remarks_array_ain
        if self.remarks_array_bin is not None:
            result['RemarksArrayBIn'] = self.remarks_array_bin
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('ImageSizeRange') is not None:
            self.image_size_range = m.get('ImageSizeRange')
        if m.get('ImageTimeRange') is not None:
            self.image_time_range = m.get('ImageTimeRange')
        if m.get('CreateTimeRange') is not None:
            self.create_time_range = m.get('CreateTimeRange')
        if m.get('ModifyTimeRange') is not None:
            self.modify_time_range = m.get('ModifyTimeRange')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('SourceUriPrefix') is not None:
            self.source_uri_prefix = m.get('SourceUriPrefix')
        if m.get('RemarksAPrefix') is not None:
            self.remarks_aprefix = m.get('RemarksAPrefix')
        if m.get('RemarksBPrefix') is not None:
            self.remarks_bprefix = m.get('RemarksBPrefix')
        if m.get('TagNames') is not None:
            self.tag_names = m.get('TagNames')
        if m.get('OCRContentsMatch') is not None:
            self.ocrcontents_match = m.get('OCRContentsMatch')
        if m.get('AgeRange') is not None:
            self.age_range = m.get('AgeRange')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('Emotion') is not None:
            self.emotion = m.get('Emotion')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('LocationBoundary') is not None:
            self.location_boundary = m.get('LocationBoundary')
        if m.get('RemarksCPrefix') is not None:
            self.remarks_cprefix = m.get('RemarksCPrefix')
        if m.get('RemarksDPrefix') is not None:
            self.remarks_dprefix = m.get('RemarksDPrefix')
        if m.get('ExternalId') is not None:
            self.external_id = m.get('ExternalId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('FacesModifyTimeRange') is not None:
            self.faces_modify_time_range = m.get('FacesModifyTimeRange')
        if m.get('TagsModifyTimeRange') is not None:
            self.tags_modify_time_range = m.get('TagsModifyTimeRange')
        if m.get('AddressLineContentsMatch') is not None:
            self.address_line_contents_match = m.get('AddressLineContentsMatch')
        if m.get('RemarksArrayAIn') is not None:
            self.remarks_array_ain = m.get('RemarksArrayAIn')
        if m.get('RemarksArrayBIn') is not None:
            self.remarks_array_bin = m.get('RemarksArrayBIn')
        return self


class FindImagesResponseBodyImagesCroppingSuggestionCroppingBoundary(TeaModel):
    def __init__(
        self,
        left: int = None,
        top: int = None,
        width: int = None,
        height: int = None,
    ):
        self.left = left
        self.top = top
        self.width = width
        self.height = height

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class FindImagesResponseBodyImagesCroppingSuggestion(TeaModel):
    def __init__(
        self,
        score: float = None,
        aspect_ratio: str = None,
        cropping_boundary: FindImagesResponseBodyImagesCroppingSuggestionCroppingBoundary = None,
    ):
        self.score = score
        self.aspect_ratio = aspect_ratio
        self.cropping_boundary = cropping_boundary

    def validate(self):
        if self.cropping_boundary:
            self.cropping_boundary.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.score is not None:
            result['Score'] = self.score
        if self.aspect_ratio is not None:
            result['AspectRatio'] = self.aspect_ratio
        if self.cropping_boundary is not None:
            result['CroppingBoundary'] = self.cropping_boundary.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('AspectRatio') is not None:
            self.aspect_ratio = m.get('AspectRatio')
        if m.get('CroppingBoundary') is not None:
            temp_model = FindImagesResponseBodyImagesCroppingSuggestionCroppingBoundary()
            self.cropping_boundary = temp_model.from_map(m['CroppingBoundary'])
        return self


class FindImagesResponseBodyImagesFacesEmotionDetails(TeaModel):
    def __init__(
        self,
        happy: float = None,
        surprised: float = None,
        calm: float = None,
        disgusted: float = None,
        angry: float = None,
        sad: float = None,
        scared: float = None,
    ):
        self.happy = happy
        self.surprised = surprised
        self.calm = calm
        self.disgusted = disgusted
        self.angry = angry
        self.sad = sad
        self.scared = scared

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.happy is not None:
            result['HAPPY'] = self.happy
        if self.surprised is not None:
            result['SURPRISED'] = self.surprised
        if self.calm is not None:
            result['CALM'] = self.calm
        if self.disgusted is not None:
            result['DISGUSTED'] = self.disgusted
        if self.angry is not None:
            result['ANGRY'] = self.angry
        if self.sad is not None:
            result['SAD'] = self.sad
        if self.scared is not None:
            result['SCARED'] = self.scared
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HAPPY') is not None:
            self.happy = m.get('HAPPY')
        if m.get('SURPRISED') is not None:
            self.surprised = m.get('SURPRISED')
        if m.get('CALM') is not None:
            self.calm = m.get('CALM')
        if m.get('DISGUSTED') is not None:
            self.disgusted = m.get('DISGUSTED')
        if m.get('ANGRY') is not None:
            self.angry = m.get('ANGRY')
        if m.get('SAD') is not None:
            self.sad = m.get('SAD')
        if m.get('SCARED') is not None:
            self.scared = m.get('SCARED')
        return self


class FindImagesResponseBodyImagesFacesFaceAttributesFaceBoundary(TeaModel):
    def __init__(
        self,
        left: int = None,
        top: int = None,
        width: int = None,
        height: int = None,
    ):
        self.left = left
        self.top = top
        self.width = width
        self.height = height

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class FindImagesResponseBodyImagesFacesFaceAttributesHeadPose(TeaModel):
    def __init__(
        self,
        pitch: float = None,
        roll: float = None,
        yaw: float = None,
    ):
        self.pitch = pitch
        self.roll = roll
        self.yaw = yaw

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pitch is not None:
            result['Pitch'] = self.pitch
        if self.roll is not None:
            result['Roll'] = self.roll
        if self.yaw is not None:
            result['Yaw'] = self.yaw
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pitch') is not None:
            self.pitch = m.get('Pitch')
        if m.get('Roll') is not None:
            self.roll = m.get('Roll')
        if m.get('Yaw') is not None:
            self.yaw = m.get('Yaw')
        return self


class FindImagesResponseBodyImagesFacesFaceAttributes(TeaModel):
    def __init__(
        self,
        glasses_confidence: float = None,
        glasses: str = None,
        mask: str = None,
        beard_confidence: float = None,
        mask_confidence: float = None,
        beard: str = None,
        face_boundary: FindImagesResponseBodyImagesFacesFaceAttributesFaceBoundary = None,
        head_pose: FindImagesResponseBodyImagesFacesFaceAttributesHeadPose = None,
    ):
        self.glasses_confidence = glasses_confidence
        self.glasses = glasses
        self.mask = mask
        self.beard_confidence = beard_confidence
        self.mask_confidence = mask_confidence
        self.beard = beard
        self.face_boundary = face_boundary
        self.head_pose = head_pose

    def validate(self):
        if self.face_boundary:
            self.face_boundary.validate()
        if self.head_pose:
            self.head_pose.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.glasses_confidence is not None:
            result['GlassesConfidence'] = self.glasses_confidence
        if self.glasses is not None:
            result['Glasses'] = self.glasses
        if self.mask is not None:
            result['Mask'] = self.mask
        if self.beard_confidence is not None:
            result['BeardConfidence'] = self.beard_confidence
        if self.mask_confidence is not None:
            result['MaskConfidence'] = self.mask_confidence
        if self.beard is not None:
            result['Beard'] = self.beard
        if self.face_boundary is not None:
            result['FaceBoundary'] = self.face_boundary.to_map()
        if self.head_pose is not None:
            result['HeadPose'] = self.head_pose.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GlassesConfidence') is not None:
            self.glasses_confidence = m.get('GlassesConfidence')
        if m.get('Glasses') is not None:
            self.glasses = m.get('Glasses')
        if m.get('Mask') is not None:
            self.mask = m.get('Mask')
        if m.get('BeardConfidence') is not None:
            self.beard_confidence = m.get('BeardConfidence')
        if m.get('MaskConfidence') is not None:
            self.mask_confidence = m.get('MaskConfidence')
        if m.get('Beard') is not None:
            self.beard = m.get('Beard')
        if m.get('FaceBoundary') is not None:
            temp_model = FindImagesResponseBodyImagesFacesFaceAttributesFaceBoundary()
            self.face_boundary = temp_model.from_map(m['FaceBoundary'])
        if m.get('HeadPose') is not None:
            temp_model = FindImagesResponseBodyImagesFacesFaceAttributesHeadPose()
            self.head_pose = temp_model.from_map(m['HeadPose'])
        return self


class FindImagesResponseBodyImagesFaces(TeaModel):
    def __init__(
        self,
        emotion_confidence: float = None,
        attractive: float = None,
        group_id: str = None,
        gender: str = None,
        face_id: str = None,
        gender_confidence: float = None,
        face_quality: float = None,
        emotion: str = None,
        age: int = None,
        face_confidence: float = None,
        emotion_details: FindImagesResponseBodyImagesFacesEmotionDetails = None,
        face_attributes: FindImagesResponseBodyImagesFacesFaceAttributes = None,
    ):
        self.emotion_confidence = emotion_confidence
        self.attractive = attractive
        self.group_id = group_id
        self.gender = gender
        self.face_id = face_id
        self.gender_confidence = gender_confidence
        self.face_quality = face_quality
        self.emotion = emotion
        self.age = age
        self.face_confidence = face_confidence
        self.emotion_details = emotion_details
        self.face_attributes = face_attributes

    def validate(self):
        if self.emotion_details:
            self.emotion_details.validate()
        if self.face_attributes:
            self.face_attributes.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.emotion_confidence is not None:
            result['EmotionConfidence'] = self.emotion_confidence
        if self.attractive is not None:
            result['Attractive'] = self.attractive
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.face_id is not None:
            result['FaceId'] = self.face_id
        if self.gender_confidence is not None:
            result['GenderConfidence'] = self.gender_confidence
        if self.face_quality is not None:
            result['FaceQuality'] = self.face_quality
        if self.emotion is not None:
            result['Emotion'] = self.emotion
        if self.age is not None:
            result['Age'] = self.age
        if self.face_confidence is not None:
            result['FaceConfidence'] = self.face_confidence
        if self.emotion_details is not None:
            result['EmotionDetails'] = self.emotion_details.to_map()
        if self.face_attributes is not None:
            result['FaceAttributes'] = self.face_attributes.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EmotionConfidence') is not None:
            self.emotion_confidence = m.get('EmotionConfidence')
        if m.get('Attractive') is not None:
            self.attractive = m.get('Attractive')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('FaceId') is not None:
            self.face_id = m.get('FaceId')
        if m.get('GenderConfidence') is not None:
            self.gender_confidence = m.get('GenderConfidence')
        if m.get('FaceQuality') is not None:
            self.face_quality = m.get('FaceQuality')
        if m.get('Emotion') is not None:
            self.emotion = m.get('Emotion')
        if m.get('Age') is not None:
            self.age = m.get('Age')
        if m.get('FaceConfidence') is not None:
            self.face_confidence = m.get('FaceConfidence')
        if m.get('EmotionDetails') is not None:
            temp_model = FindImagesResponseBodyImagesFacesEmotionDetails()
            self.emotion_details = temp_model.from_map(m['EmotionDetails'])
        if m.get('FaceAttributes') is not None:
            temp_model = FindImagesResponseBodyImagesFacesFaceAttributes()
            self.face_attributes = temp_model.from_map(m['FaceAttributes'])
        return self


class FindImagesResponseBodyImagesTags(TeaModel):
    def __init__(
        self,
        tag_level: int = None,
        parent_tag_name: str = None,
        tag_confidence: float = None,
        tag_name: str = None,
    ):
        self.tag_level = tag_level
        self.parent_tag_name = parent_tag_name
        self.tag_confidence = tag_confidence
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_level is not None:
            result['TagLevel'] = self.tag_level
        if self.parent_tag_name is not None:
            result['ParentTagName'] = self.parent_tag_name
        if self.tag_confidence is not None:
            result['TagConfidence'] = self.tag_confidence
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagLevel') is not None:
            self.tag_level = m.get('TagLevel')
        if m.get('ParentTagName') is not None:
            self.parent_tag_name = m.get('ParentTagName')
        if m.get('TagConfidence') is not None:
            self.tag_confidence = m.get('TagConfidence')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class FindImagesResponseBodyImagesOCROCRBoundary(TeaModel):
    def __init__(
        self,
        left: int = None,
        top: int = None,
        width: int = None,
        height: int = None,
    ):
        self.left = left
        self.top = top
        self.width = width
        self.height = height

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class FindImagesResponseBodyImagesOCR(TeaModel):
    def __init__(
        self,
        ocrconfidence: float = None,
        ocrcontents: str = None,
        ocrboundary: FindImagesResponseBodyImagesOCROCRBoundary = None,
    ):
        self.ocrconfidence = ocrconfidence
        self.ocrcontents = ocrcontents
        self.ocrboundary = ocrboundary

    def validate(self):
        if self.ocrboundary:
            self.ocrboundary.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ocrconfidence is not None:
            result['OCRConfidence'] = self.ocrconfidence
        if self.ocrcontents is not None:
            result['OCRContents'] = self.ocrcontents
        if self.ocrboundary is not None:
            result['OCRBoundary'] = self.ocrboundary.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OCRConfidence') is not None:
            self.ocrconfidence = m.get('OCRConfidence')
        if m.get('OCRContents') is not None:
            self.ocrcontents = m.get('OCRContents')
        if m.get('OCRBoundary') is not None:
            temp_model = FindImagesResponseBodyImagesOCROCRBoundary()
            self.ocrboundary = temp_model.from_map(m['OCRBoundary'])
        return self


class FindImagesResponseBodyImagesImageQuality(TeaModel):
    def __init__(
        self,
        overall_score: float = None,
        color: float = None,
        color_score: float = None,
        contrast_score: float = None,
        contrast: float = None,
        exposure_score: float = None,
        clarity_score: float = None,
        clarity: float = None,
        exposure: float = None,
        composition_score: float = None,
    ):
        self.overall_score = overall_score
        self.color = color
        self.color_score = color_score
        self.contrast_score = contrast_score
        self.contrast = contrast
        self.exposure_score = exposure_score
        self.clarity_score = clarity_score
        self.clarity = clarity
        self.exposure = exposure
        self.composition_score = composition_score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.overall_score is not None:
            result['OverallScore'] = self.overall_score
        if self.color is not None:
            result['Color'] = self.color
        if self.color_score is not None:
            result['ColorScore'] = self.color_score
        if self.contrast_score is not None:
            result['ContrastScore'] = self.contrast_score
        if self.contrast is not None:
            result['Contrast'] = self.contrast
        if self.exposure_score is not None:
            result['ExposureScore'] = self.exposure_score
        if self.clarity_score is not None:
            result['ClarityScore'] = self.clarity_score
        if self.clarity is not None:
            result['Clarity'] = self.clarity
        if self.exposure is not None:
            result['Exposure'] = self.exposure
        if self.composition_score is not None:
            result['CompositionScore'] = self.composition_score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OverallScore') is not None:
            self.overall_score = m.get('OverallScore')
        if m.get('Color') is not None:
            self.color = m.get('Color')
        if m.get('ColorScore') is not None:
            self.color_score = m.get('ColorScore')
        if m.get('ContrastScore') is not None:
            self.contrast_score = m.get('ContrastScore')
        if m.get('Contrast') is not None:
            self.contrast = m.get('Contrast')
        if m.get('ExposureScore') is not None:
            self.exposure_score = m.get('ExposureScore')
        if m.get('ClarityScore') is not None:
            self.clarity_score = m.get('ClarityScore')
        if m.get('Clarity') is not None:
            self.clarity = m.get('Clarity')
        if m.get('Exposure') is not None:
            self.exposure = m.get('Exposure')
        if m.get('CompositionScore') is not None:
            self.composition_score = m.get('CompositionScore')
        return self


class FindImagesResponseBodyImagesAddress(TeaModel):
    def __init__(
        self,
        township: str = None,
        district: str = None,
        address_line: str = None,
        country: str = None,
        city: str = None,
        province: str = None,
    ):
        self.township = township
        self.district = district
        self.address_line = address_line
        self.country = country
        self.city = city
        self.province = province

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.township is not None:
            result['Township'] = self.township
        if self.district is not None:
            result['District'] = self.district
        if self.address_line is not None:
            result['AddressLine'] = self.address_line
        if self.country is not None:
            result['Country'] = self.country
        if self.city is not None:
            result['City'] = self.city
        if self.province is not None:
            result['Province'] = self.province
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Township') is not None:
            self.township = m.get('Township')
        if m.get('District') is not None:
            self.district = m.get('District')
        if m.get('AddressLine') is not None:
            self.address_line = m.get('AddressLine')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        return self


class FindImagesResponseBodyImages(TeaModel):
    def __init__(
        self,
        cropping_suggestion_status: str = None,
        image_quality_modify_time: str = None,
        tags_fail_reason: str = None,
        remarks_c: str = None,
        create_time: str = None,
        source_type: str = None,
        faces_fail_reason: str = None,
        faces_modify_time: str = None,
        image_time: str = None,
        ocrmodify_time: str = None,
        address_modify_time: str = None,
        image_quality_fail_reason: str = None,
        faces_status: str = None,
        remarks_array_a: str = None,
        image_height: int = None,
        external_id: str = None,
        source_uri: str = None,
        file_size: int = None,
        modify_time: str = None,
        source_position: str = None,
        image_quality_status: str = None,
        ocrfail_reason: str = None,
        address_fail_reason: str = None,
        cropping_suggestion_modify_time: str = None,
        image_format: str = None,
        image_width: int = None,
        remarks_array_b: str = None,
        orientation: str = None,
        remarks_d: str = None,
        tags_status: str = None,
        cropping_suggestion_fail_reason: str = None,
        remarks_a: str = None,
        image_uri: str = None,
        tags_modify_time: str = None,
        ocrstatus: str = None,
        address_status: str = None,
        exif: str = None,
        location: str = None,
        remarks_b: str = None,
        cropping_suggestion: List[FindImagesResponseBodyImagesCroppingSuggestion] = None,
        faces: List[FindImagesResponseBodyImagesFaces] = None,
        tags: List[FindImagesResponseBodyImagesTags] = None,
        ocr: List[FindImagesResponseBodyImagesOCR] = None,
        image_quality: FindImagesResponseBodyImagesImageQuality = None,
        address: FindImagesResponseBodyImagesAddress = None,
    ):
        self.cropping_suggestion_status = cropping_suggestion_status
        self.image_quality_modify_time = image_quality_modify_time
        self.tags_fail_reason = tags_fail_reason
        self.remarks_c = remarks_c
        self.create_time = create_time
        self.source_type = source_type
        self.faces_fail_reason = faces_fail_reason
        self.faces_modify_time = faces_modify_time
        self.image_time = image_time
        self.ocrmodify_time = ocrmodify_time
        self.address_modify_time = address_modify_time
        self.image_quality_fail_reason = image_quality_fail_reason
        self.faces_status = faces_status
        self.remarks_array_a = remarks_array_a
        self.image_height = image_height
        self.external_id = external_id
        self.source_uri = source_uri
        self.file_size = file_size
        self.modify_time = modify_time
        self.source_position = source_position
        self.image_quality_status = image_quality_status
        self.ocrfail_reason = ocrfail_reason
        self.address_fail_reason = address_fail_reason
        self.cropping_suggestion_modify_time = cropping_suggestion_modify_time
        self.image_format = image_format
        self.image_width = image_width
        self.remarks_array_b = remarks_array_b
        self.orientation = orientation
        self.remarks_d = remarks_d
        self.tags_status = tags_status
        self.cropping_suggestion_fail_reason = cropping_suggestion_fail_reason
        self.remarks_a = remarks_a
        self.image_uri = image_uri
        self.tags_modify_time = tags_modify_time
        self.ocrstatus = ocrstatus
        self.address_status = address_status
        self.exif = exif
        self.location = location
        self.remarks_b = remarks_b
        self.cropping_suggestion = cropping_suggestion
        self.faces = faces
        self.tags = tags
        self.ocr = ocr
        self.image_quality = image_quality
        self.address = address

    def validate(self):
        if self.cropping_suggestion:
            for k in self.cropping_suggestion:
                if k:
                    k.validate()
        if self.faces:
            for k in self.faces:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.ocr:
            for k in self.ocr:
                if k:
                    k.validate()
        if self.image_quality:
            self.image_quality.validate()
        if self.address:
            self.address.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cropping_suggestion_status is not None:
            result['CroppingSuggestionStatus'] = self.cropping_suggestion_status
        if self.image_quality_modify_time is not None:
            result['ImageQualityModifyTime'] = self.image_quality_modify_time
        if self.tags_fail_reason is not None:
            result['TagsFailReason'] = self.tags_fail_reason
        if self.remarks_c is not None:
            result['RemarksC'] = self.remarks_c
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.faces_fail_reason is not None:
            result['FacesFailReason'] = self.faces_fail_reason
        if self.faces_modify_time is not None:
            result['FacesModifyTime'] = self.faces_modify_time
        if self.image_time is not None:
            result['ImageTime'] = self.image_time
        if self.ocrmodify_time is not None:
            result['OCRModifyTime'] = self.ocrmodify_time
        if self.address_modify_time is not None:
            result['AddressModifyTime'] = self.address_modify_time
        if self.image_quality_fail_reason is not None:
            result['ImageQualityFailReason'] = self.image_quality_fail_reason
        if self.faces_status is not None:
            result['FacesStatus'] = self.faces_status
        if self.remarks_array_a is not None:
            result['RemarksArrayA'] = self.remarks_array_a
        if self.image_height is not None:
            result['ImageHeight'] = self.image_height
        if self.external_id is not None:
            result['ExternalId'] = self.external_id
        if self.source_uri is not None:
            result['SourceUri'] = self.source_uri
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.source_position is not None:
            result['SourcePosition'] = self.source_position
        if self.image_quality_status is not None:
            result['ImageQualityStatus'] = self.image_quality_status
        if self.ocrfail_reason is not None:
            result['OCRFailReason'] = self.ocrfail_reason
        if self.address_fail_reason is not None:
            result['AddressFailReason'] = self.address_fail_reason
        if self.cropping_suggestion_modify_time is not None:
            result['CroppingSuggestionModifyTime'] = self.cropping_suggestion_modify_time
        if self.image_format is not None:
            result['ImageFormat'] = self.image_format
        if self.image_width is not None:
            result['ImageWidth'] = self.image_width
        if self.remarks_array_b is not None:
            result['RemarksArrayB'] = self.remarks_array_b
        if self.orientation is not None:
            result['Orientation'] = self.orientation
        if self.remarks_d is not None:
            result['RemarksD'] = self.remarks_d
        if self.tags_status is not None:
            result['TagsStatus'] = self.tags_status
        if self.cropping_suggestion_fail_reason is not None:
            result['CroppingSuggestionFailReason'] = self.cropping_suggestion_fail_reason
        if self.remarks_a is not None:
            result['RemarksA'] = self.remarks_a
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        if self.tags_modify_time is not None:
            result['TagsModifyTime'] = self.tags_modify_time
        if self.ocrstatus is not None:
            result['OCRStatus'] = self.ocrstatus
        if self.address_status is not None:
            result['AddressStatus'] = self.address_status
        if self.exif is not None:
            result['Exif'] = self.exif
        if self.location is not None:
            result['Location'] = self.location
        if self.remarks_b is not None:
            result['RemarksB'] = self.remarks_b
        result['CroppingSuggestion'] = []
        if self.cropping_suggestion is not None:
            for k in self.cropping_suggestion:
                result['CroppingSuggestion'].append(k.to_map() if k else None)
        result['Faces'] = []
        if self.faces is not None:
            for k in self.faces:
                result['Faces'].append(k.to_map() if k else None)
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        result['OCR'] = []
        if self.ocr is not None:
            for k in self.ocr:
                result['OCR'].append(k.to_map() if k else None)
        if self.image_quality is not None:
            result['ImageQuality'] = self.image_quality.to_map()
        if self.address is not None:
            result['Address'] = self.address.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CroppingSuggestionStatus') is not None:
            self.cropping_suggestion_status = m.get('CroppingSuggestionStatus')
        if m.get('ImageQualityModifyTime') is not None:
            self.image_quality_modify_time = m.get('ImageQualityModifyTime')
        if m.get('TagsFailReason') is not None:
            self.tags_fail_reason = m.get('TagsFailReason')
        if m.get('RemarksC') is not None:
            self.remarks_c = m.get('RemarksC')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('FacesFailReason') is not None:
            self.faces_fail_reason = m.get('FacesFailReason')
        if m.get('FacesModifyTime') is not None:
            self.faces_modify_time = m.get('FacesModifyTime')
        if m.get('ImageTime') is not None:
            self.image_time = m.get('ImageTime')
        if m.get('OCRModifyTime') is not None:
            self.ocrmodify_time = m.get('OCRModifyTime')
        if m.get('AddressModifyTime') is not None:
            self.address_modify_time = m.get('AddressModifyTime')
        if m.get('ImageQualityFailReason') is not None:
            self.image_quality_fail_reason = m.get('ImageQualityFailReason')
        if m.get('FacesStatus') is not None:
            self.faces_status = m.get('FacesStatus')
        if m.get('RemarksArrayA') is not None:
            self.remarks_array_a = m.get('RemarksArrayA')
        if m.get('ImageHeight') is not None:
            self.image_height = m.get('ImageHeight')
        if m.get('ExternalId') is not None:
            self.external_id = m.get('ExternalId')
        if m.get('SourceUri') is not None:
            self.source_uri = m.get('SourceUri')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('SourcePosition') is not None:
            self.source_position = m.get('SourcePosition')
        if m.get('ImageQualityStatus') is not None:
            self.image_quality_status = m.get('ImageQualityStatus')
        if m.get('OCRFailReason') is not None:
            self.ocrfail_reason = m.get('OCRFailReason')
        if m.get('AddressFailReason') is not None:
            self.address_fail_reason = m.get('AddressFailReason')
        if m.get('CroppingSuggestionModifyTime') is not None:
            self.cropping_suggestion_modify_time = m.get('CroppingSuggestionModifyTime')
        if m.get('ImageFormat') is not None:
            self.image_format = m.get('ImageFormat')
        if m.get('ImageWidth') is not None:
            self.image_width = m.get('ImageWidth')
        if m.get('RemarksArrayB') is not None:
            self.remarks_array_b = m.get('RemarksArrayB')
        if m.get('Orientation') is not None:
            self.orientation = m.get('Orientation')
        if m.get('RemarksD') is not None:
            self.remarks_d = m.get('RemarksD')
        if m.get('TagsStatus') is not None:
            self.tags_status = m.get('TagsStatus')
        if m.get('CroppingSuggestionFailReason') is not None:
            self.cropping_suggestion_fail_reason = m.get('CroppingSuggestionFailReason')
        if m.get('RemarksA') is not None:
            self.remarks_a = m.get('RemarksA')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        if m.get('TagsModifyTime') is not None:
            self.tags_modify_time = m.get('TagsModifyTime')
        if m.get('OCRStatus') is not None:
            self.ocrstatus = m.get('OCRStatus')
        if m.get('AddressStatus') is not None:
            self.address_status = m.get('AddressStatus')
        if m.get('Exif') is not None:
            self.exif = m.get('Exif')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('RemarksB') is not None:
            self.remarks_b = m.get('RemarksB')
        self.cropping_suggestion = []
        if m.get('CroppingSuggestion') is not None:
            for k in m.get('CroppingSuggestion'):
                temp_model = FindImagesResponseBodyImagesCroppingSuggestion()
                self.cropping_suggestion.append(temp_model.from_map(k))
        self.faces = []
        if m.get('Faces') is not None:
            for k in m.get('Faces'):
                temp_model = FindImagesResponseBodyImagesFaces()
                self.faces.append(temp_model.from_map(k))
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = FindImagesResponseBodyImagesTags()
                self.tags.append(temp_model.from_map(k))
        self.ocr = []
        if m.get('OCR') is not None:
            for k in m.get('OCR'):
                temp_model = FindImagesResponseBodyImagesOCR()
                self.ocr.append(temp_model.from_map(k))
        if m.get('ImageQuality') is not None:
            temp_model = FindImagesResponseBodyImagesImageQuality()
            self.image_quality = temp_model.from_map(m['ImageQuality'])
        if m.get('Address') is not None:
            temp_model = FindImagesResponseBodyImagesAddress()
            self.address = temp_model.from_map(m['Address'])
        return self


class FindImagesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        next_marker: str = None,
        set_id: str = None,
        images: List[FindImagesResponseBodyImages] = None,
    ):
        self.request_id = request_id
        self.next_marker = next_marker
        self.set_id = set_id
        self.images = images

    def validate(self):
        if self.images:
            for k in self.images:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_marker is not None:
            result['NextMarker'] = self.next_marker
        if self.set_id is not None:
            result['SetId'] = self.set_id
        result['Images'] = []
        if self.images is not None:
            for k in self.images:
                result['Images'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NextMarker') is not None:
            self.next_marker = m.get('NextMarker')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        self.images = []
        if m.get('Images') is not None:
            for k in m.get('Images'):
                temp_model = FindImagesResponseBodyImages()
                self.images.append(temp_model.from_map(k))
        return self


class FindImagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: FindImagesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = FindImagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FindSimilarFacesRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        set_id: str = None,
        image_uri: str = None,
        face_id: str = None,
        limit: int = None,
        min_similarity: float = None,
        response_format: str = None,
    ):
        self.project = project
        self.set_id = set_id
        self.image_uri = image_uri
        self.face_id = face_id
        self.limit = limit
        self.min_similarity = min_similarity
        self.response_format = response_format

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        if self.face_id is not None:
            result['FaceId'] = self.face_id
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.min_similarity is not None:
            result['MinSimilarity'] = self.min_similarity
        if self.response_format is not None:
            result['ResponseFormat'] = self.response_format
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        if m.get('FaceId') is not None:
            self.face_id = m.get('FaceId')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('MinSimilarity') is not None:
            self.min_similarity = m.get('MinSimilarity')
        if m.get('ResponseFormat') is not None:
            self.response_format = m.get('ResponseFormat')
        return self


class FindSimilarFacesResponseBodyFacesSimilarFacesFaceAttributesFaceBoundary(TeaModel):
    def __init__(
        self,
        left: int = None,
        top: int = None,
        width: int = None,
        height: int = None,
    ):
        self.left = left
        self.top = top
        self.width = width
        self.height = height

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class FindSimilarFacesResponseBodyFacesSimilarFacesFaceAttributes(TeaModel):
    def __init__(
        self,
        face_boundary: FindSimilarFacesResponseBodyFacesSimilarFacesFaceAttributesFaceBoundary = None,
    ):
        self.face_boundary = face_boundary

    def validate(self):
        if self.face_boundary:
            self.face_boundary.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_boundary is not None:
            result['FaceBoundary'] = self.face_boundary.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceBoundary') is not None:
            temp_model = FindSimilarFacesResponseBodyFacesSimilarFacesFaceAttributesFaceBoundary()
            self.face_boundary = temp_model.from_map(m['FaceBoundary'])
        return self


class FindSimilarFacesResponseBodyFacesSimilarFaces(TeaModel):
    def __init__(
        self,
        external_id: str = None,
        similarity: float = None,
        face_id: str = None,
        image_uri: str = None,
        face_attributes: FindSimilarFacesResponseBodyFacesSimilarFacesFaceAttributes = None,
    ):
        self.external_id = external_id
        self.similarity = similarity
        self.face_id = face_id
        self.image_uri = image_uri
        self.face_attributes = face_attributes

    def validate(self):
        if self.face_attributes:
            self.face_attributes.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.external_id is not None:
            result['ExternalId'] = self.external_id
        if self.similarity is not None:
            result['Similarity'] = self.similarity
        if self.face_id is not None:
            result['FaceId'] = self.face_id
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        if self.face_attributes is not None:
            result['FaceAttributes'] = self.face_attributes.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternalId') is not None:
            self.external_id = m.get('ExternalId')
        if m.get('Similarity') is not None:
            self.similarity = m.get('Similarity')
        if m.get('FaceId') is not None:
            self.face_id = m.get('FaceId')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        if m.get('FaceAttributes') is not None:
            temp_model = FindSimilarFacesResponseBodyFacesSimilarFacesFaceAttributes()
            self.face_attributes = temp_model.from_map(m['FaceAttributes'])
        return self


class FindSimilarFacesResponseBodyFacesFaceAttributesFaceBoundary(TeaModel):
    def __init__(
        self,
        left: int = None,
        top: int = None,
        width: int = None,
        height: int = None,
    ):
        self.left = left
        self.top = top
        self.width = width
        self.height = height

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class FindSimilarFacesResponseBodyFacesFaceAttributes(TeaModel):
    def __init__(
        self,
        face_boundary: FindSimilarFacesResponseBodyFacesFaceAttributesFaceBoundary = None,
    ):
        self.face_boundary = face_boundary

    def validate(self):
        if self.face_boundary:
            self.face_boundary.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_boundary is not None:
            result['FaceBoundary'] = self.face_boundary.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceBoundary') is not None:
            temp_model = FindSimilarFacesResponseBodyFacesFaceAttributesFaceBoundary()
            self.face_boundary = temp_model.from_map(m['FaceBoundary'])
        return self


class FindSimilarFacesResponseBodyFaces(TeaModel):
    def __init__(
        self,
        external_id: str = None,
        similarity: float = None,
        face_id: str = None,
        image_uri: str = None,
        similar_faces: List[FindSimilarFacesResponseBodyFacesSimilarFaces] = None,
        face_attributes: FindSimilarFacesResponseBodyFacesFaceAttributes = None,
    ):
        self.external_id = external_id
        self.similarity = similarity
        self.face_id = face_id
        self.image_uri = image_uri
        self.similar_faces = similar_faces
        self.face_attributes = face_attributes

    def validate(self):
        if self.similar_faces:
            for k in self.similar_faces:
                if k:
                    k.validate()
        if self.face_attributes:
            self.face_attributes.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.external_id is not None:
            result['ExternalId'] = self.external_id
        if self.similarity is not None:
            result['Similarity'] = self.similarity
        if self.face_id is not None:
            result['FaceId'] = self.face_id
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        result['SimilarFaces'] = []
        if self.similar_faces is not None:
            for k in self.similar_faces:
                result['SimilarFaces'].append(k.to_map() if k else None)
        if self.face_attributes is not None:
            result['FaceAttributes'] = self.face_attributes.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternalId') is not None:
            self.external_id = m.get('ExternalId')
        if m.get('Similarity') is not None:
            self.similarity = m.get('Similarity')
        if m.get('FaceId') is not None:
            self.face_id = m.get('FaceId')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        self.similar_faces = []
        if m.get('SimilarFaces') is not None:
            for k in m.get('SimilarFaces'):
                temp_model = FindSimilarFacesResponseBodyFacesSimilarFaces()
                self.similar_faces.append(temp_model.from_map(k))
        if m.get('FaceAttributes') is not None:
            temp_model = FindSimilarFacesResponseBodyFacesFaceAttributes()
            self.face_attributes = temp_model.from_map(m['FaceAttributes'])
        return self


class FindSimilarFacesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        faces: List[FindSimilarFacesResponseBodyFaces] = None,
    ):
        self.request_id = request_id
        self.faces = faces

    def validate(self):
        if self.faces:
            for k in self.faces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Faces'] = []
        if self.faces is not None:
            for k in self.faces:
                result['Faces'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.faces = []
        if m.get('Faces') is not None:
            for k in m.get('Faces'):
                temp_model = FindSimilarFacesResponseBodyFaces()
                self.faces.append(temp_model.from_map(k))
        return self


class FindSimilarFacesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: FindSimilarFacesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = FindSimilarFacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetContentKeyRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        version_id: str = None,
        drmserver_id: str = None,
        key_ids: str = None,
    ):
        self.project = project
        self.version_id = version_id
        self.drmserver_id = drmserver_id
        self.key_ids = key_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.drmserver_id is not None:
            result['DRMServerId'] = self.drmserver_id
        if self.key_ids is not None:
            result['KeyIds'] = self.key_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('DRMServerId') is not None:
            self.drmserver_id = m.get('DRMServerId')
        if m.get('KeyIds') is not None:
            self.key_ids = m.get('KeyIds')
        return self


class GetContentKeyResponseBody(TeaModel):
    def __init__(
        self,
        version_id: str = None,
        request_id: str = None,
        key_infos: str = None,
    ):
        self.version_id = version_id
        self.request_id = request_id
        self.key_infos = key_infos

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.key_infos is not None:
            result['KeyInfos'] = self.key_infos
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('KeyInfos') is not None:
            self.key_infos = m.get('KeyInfos')
        return self


class GetContentKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetContentKeyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetContentKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDRMLicenseRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        drmtype: str = None,
        drmlicense: str = None,
    ):
        self.project = project
        self.drmtype = drmtype
        self.drmlicense = drmlicense

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.drmtype is not None:
            result['DRMType'] = self.drmtype
        if self.drmlicense is not None:
            result['DRMLicense'] = self.drmlicense
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('DRMType') is not None:
            self.drmtype = m.get('DRMType')
        if m.get('DRMLicense') is not None:
            self.drmlicense = m.get('DRMLicense')
        return self


class GetDRMLicenseResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        device_info: str = None,
        drmdata: str = None,
    ):
        self.request_id = request_id
        self.device_info = device_info
        self.drmdata = drmdata

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info
        if self.drmdata is not None:
            result['DRMData'] = self.drmdata
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DeviceInfo') is not None:
            self.device_info = m.get('DeviceInfo')
        if m.get('DRMData') is not None:
            self.drmdata = m.get('DRMData')
        return self


class GetDRMLicenseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDRMLicenseResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetDRMLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetImageRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        set_id: str = None,
        image_uri: str = None,
    ):
        self.project = project
        self.set_id = set_id
        self.image_uri = image_uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        return self


class GetImageResponseBodyImageQuality(TeaModel):
    def __init__(
        self,
        overall_score: float = None,
        color: float = None,
        color_score: float = None,
        contrast_score: float = None,
        contrast: float = None,
        exposure_score: float = None,
        clarity_score: float = None,
        clarity: float = None,
        exposure: float = None,
        composition_score: float = None,
    ):
        self.overall_score = overall_score
        self.color = color
        self.color_score = color_score
        self.contrast_score = contrast_score
        self.contrast = contrast
        self.exposure_score = exposure_score
        self.clarity_score = clarity_score
        self.clarity = clarity
        self.exposure = exposure
        self.composition_score = composition_score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.overall_score is not None:
            result['OverallScore'] = self.overall_score
        if self.color is not None:
            result['Color'] = self.color
        if self.color_score is not None:
            result['ColorScore'] = self.color_score
        if self.contrast_score is not None:
            result['ContrastScore'] = self.contrast_score
        if self.contrast is not None:
            result['Contrast'] = self.contrast
        if self.exposure_score is not None:
            result['ExposureScore'] = self.exposure_score
        if self.clarity_score is not None:
            result['ClarityScore'] = self.clarity_score
        if self.clarity is not None:
            result['Clarity'] = self.clarity
        if self.exposure is not None:
            result['Exposure'] = self.exposure
        if self.composition_score is not None:
            result['CompositionScore'] = self.composition_score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OverallScore') is not None:
            self.overall_score = m.get('OverallScore')
        if m.get('Color') is not None:
            self.color = m.get('Color')
        if m.get('ColorScore') is not None:
            self.color_score = m.get('ColorScore')
        if m.get('ContrastScore') is not None:
            self.contrast_score = m.get('ContrastScore')
        if m.get('Contrast') is not None:
            self.contrast = m.get('Contrast')
        if m.get('ExposureScore') is not None:
            self.exposure_score = m.get('ExposureScore')
        if m.get('ClarityScore') is not None:
            self.clarity_score = m.get('ClarityScore')
        if m.get('Clarity') is not None:
            self.clarity = m.get('Clarity')
        if m.get('Exposure') is not None:
            self.exposure = m.get('Exposure')
        if m.get('CompositionScore') is not None:
            self.composition_score = m.get('CompositionScore')
        return self


class GetImageResponseBodyAddress(TeaModel):
    def __init__(
        self,
        township: str = None,
        district: str = None,
        address_line: str = None,
        country: str = None,
        city: str = None,
        province: str = None,
    ):
        self.township = township
        self.district = district
        self.address_line = address_line
        self.country = country
        self.city = city
        self.province = province

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.township is not None:
            result['Township'] = self.township
        if self.district is not None:
            result['District'] = self.district
        if self.address_line is not None:
            result['AddressLine'] = self.address_line
        if self.country is not None:
            result['Country'] = self.country
        if self.city is not None:
            result['City'] = self.city
        if self.province is not None:
            result['Province'] = self.province
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Township') is not None:
            self.township = m.get('Township')
        if m.get('District') is not None:
            self.district = m.get('District')
        if m.get('AddressLine') is not None:
            self.address_line = m.get('AddressLine')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        return self


class GetImageResponseBodyTags(TeaModel):
    def __init__(
        self,
        tag_name: str = None,
        tag_confidence: float = None,
        tag_level: int = None,
        parent_tag_name: str = None,
    ):
        self.tag_name = tag_name
        self.tag_confidence = tag_confidence
        self.tag_level = tag_level
        self.parent_tag_name = parent_tag_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        if self.tag_confidence is not None:
            result['TagConfidence'] = self.tag_confidence
        if self.tag_level is not None:
            result['TagLevel'] = self.tag_level
        if self.parent_tag_name is not None:
            result['ParentTagName'] = self.parent_tag_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        if m.get('TagConfidence') is not None:
            self.tag_confidence = m.get('TagConfidence')
        if m.get('TagLevel') is not None:
            self.tag_level = m.get('TagLevel')
        if m.get('ParentTagName') is not None:
            self.parent_tag_name = m.get('ParentTagName')
        return self


class GetImageResponseBodyFacesFaceAttributesFaceBoundary(TeaModel):
    def __init__(
        self,
        top: int = None,
        width: int = None,
        height: int = None,
        left: int = None,
    ):
        self.top = top
        self.width = width
        self.height = height
        self.left = left

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.left is not None:
            result['Left'] = self.left
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Left') is not None:
            self.left = m.get('Left')
        return self


class GetImageResponseBodyFacesFaceAttributesHeadPose(TeaModel):
    def __init__(
        self,
        pitch: float = None,
        roll: float = None,
        yaw: float = None,
    ):
        self.pitch = pitch
        self.roll = roll
        self.yaw = yaw

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pitch is not None:
            result['Pitch'] = self.pitch
        if self.roll is not None:
            result['Roll'] = self.roll
        if self.yaw is not None:
            result['Yaw'] = self.yaw
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pitch') is not None:
            self.pitch = m.get('Pitch')
        if m.get('Roll') is not None:
            self.roll = m.get('Roll')
        if m.get('Yaw') is not None:
            self.yaw = m.get('Yaw')
        return self


class GetImageResponseBodyFacesFaceAttributes(TeaModel):
    def __init__(
        self,
        glasses_confidence: float = None,
        glasses: str = None,
        mask: str = None,
        beard_confidence: float = None,
        mask_confidence: float = None,
        face_boundary: GetImageResponseBodyFacesFaceAttributesFaceBoundary = None,
        head_pose: GetImageResponseBodyFacesFaceAttributesHeadPose = None,
        beard: str = None,
    ):
        self.glasses_confidence = glasses_confidence
        self.glasses = glasses
        self.mask = mask
        self.beard_confidence = beard_confidence
        self.mask_confidence = mask_confidence
        self.face_boundary = face_boundary
        self.head_pose = head_pose
        self.beard = beard

    def validate(self):
        if self.face_boundary:
            self.face_boundary.validate()
        if self.head_pose:
            self.head_pose.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.glasses_confidence is not None:
            result['GlassesConfidence'] = self.glasses_confidence
        if self.glasses is not None:
            result['Glasses'] = self.glasses
        if self.mask is not None:
            result['Mask'] = self.mask
        if self.beard_confidence is not None:
            result['BeardConfidence'] = self.beard_confidence
        if self.mask_confidence is not None:
            result['MaskConfidence'] = self.mask_confidence
        if self.face_boundary is not None:
            result['FaceBoundary'] = self.face_boundary.to_map()
        if self.head_pose is not None:
            result['HeadPose'] = self.head_pose.to_map()
        if self.beard is not None:
            result['Beard'] = self.beard
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GlassesConfidence') is not None:
            self.glasses_confidence = m.get('GlassesConfidence')
        if m.get('Glasses') is not None:
            self.glasses = m.get('Glasses')
        if m.get('Mask') is not None:
            self.mask = m.get('Mask')
        if m.get('BeardConfidence') is not None:
            self.beard_confidence = m.get('BeardConfidence')
        if m.get('MaskConfidence') is not None:
            self.mask_confidence = m.get('MaskConfidence')
        if m.get('FaceBoundary') is not None:
            temp_model = GetImageResponseBodyFacesFaceAttributesFaceBoundary()
            self.face_boundary = temp_model.from_map(m['FaceBoundary'])
        if m.get('HeadPose') is not None:
            temp_model = GetImageResponseBodyFacesFaceAttributesHeadPose()
            self.head_pose = temp_model.from_map(m['HeadPose'])
        if m.get('Beard') is not None:
            self.beard = m.get('Beard')
        return self


class GetImageResponseBodyFacesEmotionDetails(TeaModel):
    def __init__(
        self,
        happy: float = None,
        calm: float = None,
        surprised: float = None,
        disgusted: float = None,
        angry: float = None,
        sad: float = None,
        scared: float = None,
    ):
        self.happy = happy
        self.calm = calm
        self.surprised = surprised
        self.disgusted = disgusted
        self.angry = angry
        self.sad = sad
        self.scared = scared

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.happy is not None:
            result['HAPPY'] = self.happy
        if self.calm is not None:
            result['CALM'] = self.calm
        if self.surprised is not None:
            result['SURPRISED'] = self.surprised
        if self.disgusted is not None:
            result['DISGUSTED'] = self.disgusted
        if self.angry is not None:
            result['ANGRY'] = self.angry
        if self.sad is not None:
            result['SAD'] = self.sad
        if self.scared is not None:
            result['SCARED'] = self.scared
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HAPPY') is not None:
            self.happy = m.get('HAPPY')
        if m.get('CALM') is not None:
            self.calm = m.get('CALM')
        if m.get('SURPRISED') is not None:
            self.surprised = m.get('SURPRISED')
        if m.get('DISGUSTED') is not None:
            self.disgusted = m.get('DISGUSTED')
        if m.get('ANGRY') is not None:
            self.angry = m.get('ANGRY')
        if m.get('SAD') is not None:
            self.sad = m.get('SAD')
        if m.get('SCARED') is not None:
            self.scared = m.get('SCARED')
        return self


class GetImageResponseBodyFaces(TeaModel):
    def __init__(
        self,
        gender: str = None,
        gender_confidence: float = None,
        face_id: str = None,
        face_attributes: GetImageResponseBodyFacesFaceAttributes = None,
        face_quality: float = None,
        emotion: str = None,
        age: str = None,
        face_confidence: float = None,
        emotion_confidence: float = None,
        attractive: float = None,
        group_id: str = None,
        emotion_details: GetImageResponseBodyFacesEmotionDetails = None,
    ):
        self.gender = gender
        self.gender_confidence = gender_confidence
        self.face_id = face_id
        self.face_attributes = face_attributes
        self.face_quality = face_quality
        self.emotion = emotion
        self.age = age
        self.face_confidence = face_confidence
        self.emotion_confidence = emotion_confidence
        self.attractive = attractive
        self.group_id = group_id
        self.emotion_details = emotion_details

    def validate(self):
        if self.face_attributes:
            self.face_attributes.validate()
        if self.emotion_details:
            self.emotion_details.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.gender_confidence is not None:
            result['GenderConfidence'] = self.gender_confidence
        if self.face_id is not None:
            result['FaceId'] = self.face_id
        if self.face_attributes is not None:
            result['FaceAttributes'] = self.face_attributes.to_map()
        if self.face_quality is not None:
            result['FaceQuality'] = self.face_quality
        if self.emotion is not None:
            result['Emotion'] = self.emotion
        if self.age is not None:
            result['Age'] = self.age
        if self.face_confidence is not None:
            result['FaceConfidence'] = self.face_confidence
        if self.emotion_confidence is not None:
            result['EmotionConfidence'] = self.emotion_confidence
        if self.attractive is not None:
            result['Attractive'] = self.attractive
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.emotion_details is not None:
            result['EmotionDetails'] = self.emotion_details.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('GenderConfidence') is not None:
            self.gender_confidence = m.get('GenderConfidence')
        if m.get('FaceId') is not None:
            self.face_id = m.get('FaceId')
        if m.get('FaceAttributes') is not None:
            temp_model = GetImageResponseBodyFacesFaceAttributes()
            self.face_attributes = temp_model.from_map(m['FaceAttributes'])
        if m.get('FaceQuality') is not None:
            self.face_quality = m.get('FaceQuality')
        if m.get('Emotion') is not None:
            self.emotion = m.get('Emotion')
        if m.get('Age') is not None:
            self.age = m.get('Age')
        if m.get('FaceConfidence') is not None:
            self.face_confidence = m.get('FaceConfidence')
        if m.get('EmotionConfidence') is not None:
            self.emotion_confidence = m.get('EmotionConfidence')
        if m.get('Attractive') is not None:
            self.attractive = m.get('Attractive')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('EmotionDetails') is not None:
            temp_model = GetImageResponseBodyFacesEmotionDetails()
            self.emotion_details = temp_model.from_map(m['EmotionDetails'])
        return self


class GetImageResponseBodyCroppingSuggestionCroppingBoundary(TeaModel):
    def __init__(
        self,
        top: int = None,
        width: int = None,
        height: int = None,
        left: int = None,
    ):
        self.top = top
        self.width = width
        self.height = height
        self.left = left

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.left is not None:
            result['Left'] = self.left
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Left') is not None:
            self.left = m.get('Left')
        return self


class GetImageResponseBodyCroppingSuggestion(TeaModel):
    def __init__(
        self,
        score: float = None,
        cropping_boundary: GetImageResponseBodyCroppingSuggestionCroppingBoundary = None,
        aspect_ratio: str = None,
    ):
        self.score = score
        self.cropping_boundary = cropping_boundary
        self.aspect_ratio = aspect_ratio

    def validate(self):
        if self.cropping_boundary:
            self.cropping_boundary.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.score is not None:
            result['Score'] = self.score
        if self.cropping_boundary is not None:
            result['CroppingBoundary'] = self.cropping_boundary.to_map()
        if self.aspect_ratio is not None:
            result['AspectRatio'] = self.aspect_ratio
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('CroppingBoundary') is not None:
            temp_model = GetImageResponseBodyCroppingSuggestionCroppingBoundary()
            self.cropping_boundary = temp_model.from_map(m['CroppingBoundary'])
        if m.get('AspectRatio') is not None:
            self.aspect_ratio = m.get('AspectRatio')
        return self


class GetImageResponseBodyOCROCRBoundary(TeaModel):
    def __init__(
        self,
        top: int = None,
        width: int = None,
        height: int = None,
        left: int = None,
    ):
        self.top = top
        self.width = width
        self.height = height
        self.left = left

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.left is not None:
            result['Left'] = self.left
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Left') is not None:
            self.left = m.get('Left')
        return self


class GetImageResponseBodyOCR(TeaModel):
    def __init__(
        self,
        ocrconfidence: float = None,
        ocrcontents: str = None,
        ocrboundary: GetImageResponseBodyOCROCRBoundary = None,
    ):
        self.ocrconfidence = ocrconfidence
        self.ocrcontents = ocrcontents
        self.ocrboundary = ocrboundary

    def validate(self):
        if self.ocrboundary:
            self.ocrboundary.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ocrconfidence is not None:
            result['OCRConfidence'] = self.ocrconfidence
        if self.ocrcontents is not None:
            result['OCRContents'] = self.ocrcontents
        if self.ocrboundary is not None:
            result['OCRBoundary'] = self.ocrboundary.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OCRConfidence') is not None:
            self.ocrconfidence = m.get('OCRConfidence')
        if m.get('OCRContents') is not None:
            self.ocrcontents = m.get('OCRContents')
        if m.get('OCRBoundary') is not None:
            temp_model = GetImageResponseBodyOCROCRBoundary()
            self.ocrboundary = temp_model.from_map(m['OCRBoundary'])
        return self


class GetImageResponseBody(TeaModel):
    def __init__(
        self,
        image_quality: GetImageResponseBodyImageQuality = None,
        modify_time: str = None,
        address: GetImageResponseBodyAddress = None,
        source_type: str = None,
        source_uri: str = None,
        faces_fail_reason: str = None,
        cropping_suggestion_status: str = None,
        cropping_suggestion_fail_reason: str = None,
        address_fail_reason: str = None,
        remarks_a: str = None,
        address_modify_time: str = None,
        remarks_b: str = None,
        image_format: str = None,
        tags_fail_reason: str = None,
        remarks_array_b: str = None,
        faces_modify_time: str = None,
        exif: str = None,
        remarks_c: str = None,
        remarks_d: str = None,
        image_width: int = None,
        remarks_array_a: str = None,
        source_position: str = None,
        tags: List[GetImageResponseBodyTags] = None,
        faces: List[GetImageResponseBodyFaces] = None,
        address_status: str = None,
        faces_status: str = None,
        image_quality_modify_time: str = None,
        cropping_suggestion: List[GetImageResponseBodyCroppingSuggestion] = None,
        request_id: str = None,
        create_time: str = None,
        external_id: str = None,
        tags_modify_time: str = None,
        image_quality_fail_reason: str = None,
        orientation: str = None,
        image_uri: str = None,
        ocrstatus: str = None,
        ocrmodify_time: str = None,
        image_time: str = None,
        cropping_suggestion_modify_time: str = None,
        image_height: int = None,
        image_quality_status: str = None,
        tags_status: str = None,
        ocrfail_reason: str = None,
        set_id: str = None,
        file_size: int = None,
        location: str = None,
        ocr: List[GetImageResponseBodyOCR] = None,
    ):
        self.image_quality = image_quality
        self.modify_time = modify_time
        self.address = address
        self.source_type = source_type
        self.source_uri = source_uri
        self.faces_fail_reason = faces_fail_reason
        self.cropping_suggestion_status = cropping_suggestion_status
        self.cropping_suggestion_fail_reason = cropping_suggestion_fail_reason
        self.address_fail_reason = address_fail_reason
        self.remarks_a = remarks_a
        self.address_modify_time = address_modify_time
        self.remarks_b = remarks_b
        self.image_format = image_format
        self.tags_fail_reason = tags_fail_reason
        self.remarks_array_b = remarks_array_b
        self.faces_modify_time = faces_modify_time
        self.exif = exif
        self.remarks_c = remarks_c
        self.remarks_d = remarks_d
        self.image_width = image_width
        self.remarks_array_a = remarks_array_a
        self.source_position = source_position
        self.tags = tags
        self.faces = faces
        self.address_status = address_status
        self.faces_status = faces_status
        self.image_quality_modify_time = image_quality_modify_time
        self.cropping_suggestion = cropping_suggestion
        self.request_id = request_id
        self.create_time = create_time
        self.external_id = external_id
        self.tags_modify_time = tags_modify_time
        self.image_quality_fail_reason = image_quality_fail_reason
        self.orientation = orientation
        self.image_uri = image_uri
        self.ocrstatus = ocrstatus
        self.ocrmodify_time = ocrmodify_time
        self.image_time = image_time
        self.cropping_suggestion_modify_time = cropping_suggestion_modify_time
        self.image_height = image_height
        self.image_quality_status = image_quality_status
        self.tags_status = tags_status
        self.ocrfail_reason = ocrfail_reason
        self.set_id = set_id
        self.file_size = file_size
        self.location = location
        self.ocr = ocr

    def validate(self):
        if self.image_quality:
            self.image_quality.validate()
        if self.address:
            self.address.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.faces:
            for k in self.faces:
                if k:
                    k.validate()
        if self.cropping_suggestion:
            for k in self.cropping_suggestion:
                if k:
                    k.validate()
        if self.ocr:
            for k in self.ocr:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_quality is not None:
            result['ImageQuality'] = self.image_quality.to_map()
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.address is not None:
            result['Address'] = self.address.to_map()
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.source_uri is not None:
            result['SourceUri'] = self.source_uri
        if self.faces_fail_reason is not None:
            result['FacesFailReason'] = self.faces_fail_reason
        if self.cropping_suggestion_status is not None:
            result['CroppingSuggestionStatus'] = self.cropping_suggestion_status
        if self.cropping_suggestion_fail_reason is not None:
            result['CroppingSuggestionFailReason'] = self.cropping_suggestion_fail_reason
        if self.address_fail_reason is not None:
            result['AddressFailReason'] = self.address_fail_reason
        if self.remarks_a is not None:
            result['RemarksA'] = self.remarks_a
        if self.address_modify_time is not None:
            result['AddressModifyTime'] = self.address_modify_time
        if self.remarks_b is not None:
            result['RemarksB'] = self.remarks_b
        if self.image_format is not None:
            result['ImageFormat'] = self.image_format
        if self.tags_fail_reason is not None:
            result['TagsFailReason'] = self.tags_fail_reason
        if self.remarks_array_b is not None:
            result['RemarksArrayB'] = self.remarks_array_b
        if self.faces_modify_time is not None:
            result['FacesModifyTime'] = self.faces_modify_time
        if self.exif is not None:
            result['Exif'] = self.exif
        if self.remarks_c is not None:
            result['RemarksC'] = self.remarks_c
        if self.remarks_d is not None:
            result['RemarksD'] = self.remarks_d
        if self.image_width is not None:
            result['ImageWidth'] = self.image_width
        if self.remarks_array_a is not None:
            result['RemarksArrayA'] = self.remarks_array_a
        if self.source_position is not None:
            result['SourcePosition'] = self.source_position
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        result['Faces'] = []
        if self.faces is not None:
            for k in self.faces:
                result['Faces'].append(k.to_map() if k else None)
        if self.address_status is not None:
            result['AddressStatus'] = self.address_status
        if self.faces_status is not None:
            result['FacesStatus'] = self.faces_status
        if self.image_quality_modify_time is not None:
            result['ImageQualityModifyTime'] = self.image_quality_modify_time
        result['CroppingSuggestion'] = []
        if self.cropping_suggestion is not None:
            for k in self.cropping_suggestion:
                result['CroppingSuggestion'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.external_id is not None:
            result['ExternalId'] = self.external_id
        if self.tags_modify_time is not None:
            result['TagsModifyTime'] = self.tags_modify_time
        if self.image_quality_fail_reason is not None:
            result['ImageQualityFailReason'] = self.image_quality_fail_reason
        if self.orientation is not None:
            result['Orientation'] = self.orientation
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        if self.ocrstatus is not None:
            result['OCRStatus'] = self.ocrstatus
        if self.ocrmodify_time is not None:
            result['OCRModifyTime'] = self.ocrmodify_time
        if self.image_time is not None:
            result['ImageTime'] = self.image_time
        if self.cropping_suggestion_modify_time is not None:
            result['CroppingSuggestionModifyTime'] = self.cropping_suggestion_modify_time
        if self.image_height is not None:
            result['ImageHeight'] = self.image_height
        if self.image_quality_status is not None:
            result['ImageQualityStatus'] = self.image_quality_status
        if self.tags_status is not None:
            result['TagsStatus'] = self.tags_status
        if self.ocrfail_reason is not None:
            result['OCRFailReason'] = self.ocrfail_reason
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.location is not None:
            result['Location'] = self.location
        result['OCR'] = []
        if self.ocr is not None:
            for k in self.ocr:
                result['OCR'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageQuality') is not None:
            temp_model = GetImageResponseBodyImageQuality()
            self.image_quality = temp_model.from_map(m['ImageQuality'])
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Address') is not None:
            temp_model = GetImageResponseBodyAddress()
            self.address = temp_model.from_map(m['Address'])
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('SourceUri') is not None:
            self.source_uri = m.get('SourceUri')
        if m.get('FacesFailReason') is not None:
            self.faces_fail_reason = m.get('FacesFailReason')
        if m.get('CroppingSuggestionStatus') is not None:
            self.cropping_suggestion_status = m.get('CroppingSuggestionStatus')
        if m.get('CroppingSuggestionFailReason') is not None:
            self.cropping_suggestion_fail_reason = m.get('CroppingSuggestionFailReason')
        if m.get('AddressFailReason') is not None:
            self.address_fail_reason = m.get('AddressFailReason')
        if m.get('RemarksA') is not None:
            self.remarks_a = m.get('RemarksA')
        if m.get('AddressModifyTime') is not None:
            self.address_modify_time = m.get('AddressModifyTime')
        if m.get('RemarksB') is not None:
            self.remarks_b = m.get('RemarksB')
        if m.get('ImageFormat') is not None:
            self.image_format = m.get('ImageFormat')
        if m.get('TagsFailReason') is not None:
            self.tags_fail_reason = m.get('TagsFailReason')
        if m.get('RemarksArrayB') is not None:
            self.remarks_array_b = m.get('RemarksArrayB')
        if m.get('FacesModifyTime') is not None:
            self.faces_modify_time = m.get('FacesModifyTime')
        if m.get('Exif') is not None:
            self.exif = m.get('Exif')
        if m.get('RemarksC') is not None:
            self.remarks_c = m.get('RemarksC')
        if m.get('RemarksD') is not None:
            self.remarks_d = m.get('RemarksD')
        if m.get('ImageWidth') is not None:
            self.image_width = m.get('ImageWidth')
        if m.get('RemarksArrayA') is not None:
            self.remarks_array_a = m.get('RemarksArrayA')
        if m.get('SourcePosition') is not None:
            self.source_position = m.get('SourcePosition')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = GetImageResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        self.faces = []
        if m.get('Faces') is not None:
            for k in m.get('Faces'):
                temp_model = GetImageResponseBodyFaces()
                self.faces.append(temp_model.from_map(k))
        if m.get('AddressStatus') is not None:
            self.address_status = m.get('AddressStatus')
        if m.get('FacesStatus') is not None:
            self.faces_status = m.get('FacesStatus')
        if m.get('ImageQualityModifyTime') is not None:
            self.image_quality_modify_time = m.get('ImageQualityModifyTime')
        self.cropping_suggestion = []
        if m.get('CroppingSuggestion') is not None:
            for k in m.get('CroppingSuggestion'):
                temp_model = GetImageResponseBodyCroppingSuggestion()
                self.cropping_suggestion.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExternalId') is not None:
            self.external_id = m.get('ExternalId')
        if m.get('TagsModifyTime') is not None:
            self.tags_modify_time = m.get('TagsModifyTime')
        if m.get('ImageQualityFailReason') is not None:
            self.image_quality_fail_reason = m.get('ImageQualityFailReason')
        if m.get('Orientation') is not None:
            self.orientation = m.get('Orientation')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        if m.get('OCRStatus') is not None:
            self.ocrstatus = m.get('OCRStatus')
        if m.get('OCRModifyTime') is not None:
            self.ocrmodify_time = m.get('OCRModifyTime')
        if m.get('ImageTime') is not None:
            self.image_time = m.get('ImageTime')
        if m.get('CroppingSuggestionModifyTime') is not None:
            self.cropping_suggestion_modify_time = m.get('CroppingSuggestionModifyTime')
        if m.get('ImageHeight') is not None:
            self.image_height = m.get('ImageHeight')
        if m.get('ImageQualityStatus') is not None:
            self.image_quality_status = m.get('ImageQualityStatus')
        if m.get('TagsStatus') is not None:
            self.tags_status = m.get('TagsStatus')
        if m.get('OCRFailReason') is not None:
            self.ocrfail_reason = m.get('OCRFailReason')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        self.ocr = []
        if m.get('OCR') is not None:
            for k in m.get('OCR'):
                temp_model = GetImageResponseBodyOCR()
                self.ocr.append(temp_model.from_map(k))
        return self


class GetImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetImageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetImageCroppingSuggestionsRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        image_uri: str = None,
        aspect_ratios: str = None,
    ):
        self.project = project
        self.image_uri = image_uri
        self.aspect_ratios = aspect_ratios

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        if self.aspect_ratios is not None:
            result['AspectRatios'] = self.aspect_ratios
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        if m.get('AspectRatios') is not None:
            self.aspect_ratios = m.get('AspectRatios')
        return self


class GetImageCroppingSuggestionsResponseBodyCroppingSuggestionsCroppingBoundary(TeaModel):
    def __init__(
        self,
        left: int = None,
        top: int = None,
        width: int = None,
        height: int = None,
    ):
        self.left = left
        self.top = top
        self.width = width
        self.height = height

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class GetImageCroppingSuggestionsResponseBodyCroppingSuggestions(TeaModel):
    def __init__(
        self,
        score: float = None,
        aspect_ratio: str = None,
        cropping_boundary: GetImageCroppingSuggestionsResponseBodyCroppingSuggestionsCroppingBoundary = None,
    ):
        self.score = score
        self.aspect_ratio = aspect_ratio
        self.cropping_boundary = cropping_boundary

    def validate(self):
        if self.cropping_boundary:
            self.cropping_boundary.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.score is not None:
            result['Score'] = self.score
        if self.aspect_ratio is not None:
            result['AspectRatio'] = self.aspect_ratio
        if self.cropping_boundary is not None:
            result['CroppingBoundary'] = self.cropping_boundary.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('AspectRatio') is not None:
            self.aspect_ratio = m.get('AspectRatio')
        if m.get('CroppingBoundary') is not None:
            temp_model = GetImageCroppingSuggestionsResponseBodyCroppingSuggestionsCroppingBoundary()
            self.cropping_boundary = temp_model.from_map(m['CroppingBoundary'])
        return self


class GetImageCroppingSuggestionsResponseBody(TeaModel):
    def __init__(
        self,
        image_uri: str = None,
        request_id: str = None,
        cropping_suggestions: List[GetImageCroppingSuggestionsResponseBodyCroppingSuggestions] = None,
    ):
        self.image_uri = image_uri
        self.request_id = request_id
        self.cropping_suggestions = cropping_suggestions

    def validate(self):
        if self.cropping_suggestions:
            for k in self.cropping_suggestions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['CroppingSuggestions'] = []
        if self.cropping_suggestions is not None:
            for k in self.cropping_suggestions:
                result['CroppingSuggestions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.cropping_suggestions = []
        if m.get('CroppingSuggestions') is not None:
            for k in m.get('CroppingSuggestions'):
                temp_model = GetImageCroppingSuggestionsResponseBodyCroppingSuggestions()
                self.cropping_suggestions.append(temp_model.from_map(k))
        return self


class GetImageCroppingSuggestionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetImageCroppingSuggestionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetImageCroppingSuggestionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetImageQualityRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        image_uri: str = None,
    ):
        self.project = project
        self.image_uri = image_uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        return self


class GetImageQualityResponseBodyImageQuality(TeaModel):
    def __init__(
        self,
        overall_score: float = None,
        color: float = None,
        color_score: float = None,
        contrast_score: float = None,
        contrast: float = None,
        exposure_score: float = None,
        clarity_score: float = None,
        clarity: float = None,
        exposure: float = None,
        composition_score: float = None,
    ):
        self.overall_score = overall_score
        self.color = color
        self.color_score = color_score
        self.contrast_score = contrast_score
        self.contrast = contrast
        self.exposure_score = exposure_score
        self.clarity_score = clarity_score
        self.clarity = clarity
        self.exposure = exposure
        self.composition_score = composition_score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.overall_score is not None:
            result['OverallScore'] = self.overall_score
        if self.color is not None:
            result['Color'] = self.color
        if self.color_score is not None:
            result['ColorScore'] = self.color_score
        if self.contrast_score is not None:
            result['ContrastScore'] = self.contrast_score
        if self.contrast is not None:
            result['Contrast'] = self.contrast
        if self.exposure_score is not None:
            result['ExposureScore'] = self.exposure_score
        if self.clarity_score is not None:
            result['ClarityScore'] = self.clarity_score
        if self.clarity is not None:
            result['Clarity'] = self.clarity
        if self.exposure is not None:
            result['Exposure'] = self.exposure
        if self.composition_score is not None:
            result['CompositionScore'] = self.composition_score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OverallScore') is not None:
            self.overall_score = m.get('OverallScore')
        if m.get('Color') is not None:
            self.color = m.get('Color')
        if m.get('ColorScore') is not None:
            self.color_score = m.get('ColorScore')
        if m.get('ContrastScore') is not None:
            self.contrast_score = m.get('ContrastScore')
        if m.get('Contrast') is not None:
            self.contrast = m.get('Contrast')
        if m.get('ExposureScore') is not None:
            self.exposure_score = m.get('ExposureScore')
        if m.get('ClarityScore') is not None:
            self.clarity_score = m.get('ClarityScore')
        if m.get('Clarity') is not None:
            self.clarity = m.get('Clarity')
        if m.get('Exposure') is not None:
            self.exposure = m.get('Exposure')
        if m.get('CompositionScore') is not None:
            self.composition_score = m.get('CompositionScore')
        return self


class GetImageQualityResponseBody(TeaModel):
    def __init__(
        self,
        image_uri: str = None,
        request_id: str = None,
        image_quality: GetImageQualityResponseBodyImageQuality = None,
    ):
        self.image_uri = image_uri
        self.request_id = request_id
        self.image_quality = image_quality

    def validate(self):
        if self.image_quality:
            self.image_quality.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.image_quality is not None:
            result['ImageQuality'] = self.image_quality.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ImageQuality') is not None:
            temp_model = GetImageQualityResponseBodyImageQuality()
            self.image_quality = temp_model.from_map(m['ImageQuality'])
        return self


class GetImageQualityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetImageQualityResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetImageQualityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMediaMetaRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        media_uri: str = None,
    ):
        self.project = project
        self.media_uri = media_uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.media_uri is not None:
            result['MediaUri'] = self.media_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('MediaUri') is not None:
            self.media_uri = m.get('MediaUri')
        return self


class GetMediaMetaResponseBodyMediaMetaMediaFormatTag(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        album: str = None,
        album_artist: str = None,
        performer: str = None,
        composer: str = None,
        artist: str = None,
        title: str = None,
        language: str = None,
    ):
        self.creation_time = creation_time
        self.album = album
        self.album_artist = album_artist
        self.performer = performer
        self.composer = composer
        self.artist = artist
        self.title = title
        self.language = language

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.album is not None:
            result['Album'] = self.album
        if self.album_artist is not None:
            result['AlbumArtist'] = self.album_artist
        if self.performer is not None:
            result['Performer'] = self.performer
        if self.composer is not None:
            result['Composer'] = self.composer
        if self.artist is not None:
            result['Artist'] = self.artist
        if self.title is not None:
            result['Title'] = self.title
        if self.language is not None:
            result['Language'] = self.language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Album') is not None:
            self.album = m.get('Album')
        if m.get('AlbumArtist') is not None:
            self.album_artist = m.get('AlbumArtist')
        if m.get('Performer') is not None:
            self.performer = m.get('Performer')
        if m.get('Composer') is not None:
            self.composer = m.get('Composer')
        if m.get('Artist') is not None:
            self.artist = m.get('Artist')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        return self


class GetMediaMetaResponseBodyMediaMetaMediaFormatAddress(TeaModel):
    def __init__(
        self,
        township: str = None,
        district: str = None,
        address_line: str = None,
        country: str = None,
        city: str = None,
        province: str = None,
    ):
        self.township = township
        self.district = district
        self.address_line = address_line
        self.country = country
        self.city = city
        self.province = province

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.township is not None:
            result['Township'] = self.township
        if self.district is not None:
            result['District'] = self.district
        if self.address_line is not None:
            result['AddressLine'] = self.address_line
        if self.country is not None:
            result['Country'] = self.country
        if self.city is not None:
            result['City'] = self.city
        if self.province is not None:
            result['Province'] = self.province
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Township') is not None:
            self.township = m.get('Township')
        if m.get('District') is not None:
            self.district = m.get('District')
        if m.get('AddressLine') is not None:
            self.address_line = m.get('AddressLine')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        return self


class GetMediaMetaResponseBodyMediaMetaMediaFormat(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        number_programs: int = None,
        number_streams: int = None,
        tag: GetMediaMetaResponseBodyMediaMetaMediaFormatTag = None,
        bitrate: str = None,
        start_time: str = None,
        size: str = None,
        address: GetMediaMetaResponseBodyMediaMetaMediaFormatAddress = None,
        format_long_name: str = None,
        duration: str = None,
        format_name: str = None,
        location: str = None,
    ):
        self.creation_time = creation_time
        self.number_programs = number_programs
        self.number_streams = number_streams
        self.tag = tag
        self.bitrate = bitrate
        self.start_time = start_time
        self.size = size
        self.address = address
        self.format_long_name = format_long_name
        self.duration = duration
        self.format_name = format_name
        self.location = location

    def validate(self):
        if self.tag:
            self.tag.validate()
        if self.address:
            self.address.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.number_programs is not None:
            result['NumberPrograms'] = self.number_programs
        if self.number_streams is not None:
            result['NumberStreams'] = self.number_streams
        if self.tag is not None:
            result['Tag'] = self.tag.to_map()
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.size is not None:
            result['Size'] = self.size
        if self.address is not None:
            result['Address'] = self.address.to_map()
        if self.format_long_name is not None:
            result['FormatLongName'] = self.format_long_name
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.format_name is not None:
            result['FormatName'] = self.format_name
        if self.location is not None:
            result['Location'] = self.location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('NumberPrograms') is not None:
            self.number_programs = m.get('NumberPrograms')
        if m.get('NumberStreams') is not None:
            self.number_streams = m.get('NumberStreams')
        if m.get('Tag') is not None:
            temp_model = GetMediaMetaResponseBodyMediaMetaMediaFormatTag()
            self.tag = temp_model.from_map(m['Tag'])
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Address') is not None:
            temp_model = GetMediaMetaResponseBodyMediaMetaMediaFormatAddress()
            self.address = temp_model.from_map(m['Address'])
        if m.get('FormatLongName') is not None:
            self.format_long_name = m.get('FormatLongName')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('FormatName') is not None:
            self.format_name = m.get('FormatName')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        return self


class GetMediaMetaResponseBodyMediaMetaMediaStreamsVideoStreams(TeaModel):
    def __init__(
        self,
        index: int = None,
        codec_long_name: str = None,
        height: int = None,
        sample_aspect_ratio: str = None,
        average_frame_rate: str = None,
        bitrate: str = None,
        rotate: str = None,
        codec_tag_string: str = None,
        language: str = None,
        has_bframes: int = None,
        frame_rrate: str = None,
        profile: str = None,
        start_time: str = None,
        frames: str = None,
        codec_name: str = None,
        width: int = None,
        duration: str = None,
        display_aspect_ratio: str = None,
        codec_tag: str = None,
        codec_time_base: str = None,
        time_base: str = None,
        level: int = None,
        pixel_format: str = None,
    ):
        self.index = index
        self.codec_long_name = codec_long_name
        self.height = height
        self.sample_aspect_ratio = sample_aspect_ratio
        self.average_frame_rate = average_frame_rate
        self.bitrate = bitrate
        self.rotate = rotate
        self.codec_tag_string = codec_tag_string
        self.language = language
        self.has_bframes = has_bframes
        self.frame_rrate = frame_rrate
        self.profile = profile
        self.start_time = start_time
        self.frames = frames
        self.codec_name = codec_name
        self.width = width
        self.duration = duration
        self.display_aspect_ratio = display_aspect_ratio
        self.codec_tag = codec_tag
        self.codec_time_base = codec_time_base
        self.time_base = time_base
        self.level = level
        self.pixel_format = pixel_format

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.codec_long_name is not None:
            result['CodecLongName'] = self.codec_long_name
        if self.height is not None:
            result['Height'] = self.height
        if self.sample_aspect_ratio is not None:
            result['SampleAspectRatio'] = self.sample_aspect_ratio
        if self.average_frame_rate is not None:
            result['AverageFrameRate'] = self.average_frame_rate
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.rotate is not None:
            result['Rotate'] = self.rotate
        if self.codec_tag_string is not None:
            result['CodecTagString'] = self.codec_tag_string
        if self.language is not None:
            result['Language'] = self.language
        if self.has_bframes is not None:
            result['HasBFrames'] = self.has_bframes
        if self.frame_rrate is not None:
            result['FrameRrate'] = self.frame_rrate
        if self.profile is not None:
            result['Profile'] = self.profile
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.frames is not None:
            result['Frames'] = self.frames
        if self.codec_name is not None:
            result['CodecName'] = self.codec_name
        if self.width is not None:
            result['Width'] = self.width
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.display_aspect_ratio is not None:
            result['DisplayAspectRatio'] = self.display_aspect_ratio
        if self.codec_tag is not None:
            result['CodecTag'] = self.codec_tag
        if self.codec_time_base is not None:
            result['CodecTimeBase'] = self.codec_time_base
        if self.time_base is not None:
            result['TimeBase'] = self.time_base
        if self.level is not None:
            result['Level'] = self.level
        if self.pixel_format is not None:
            result['PixelFormat'] = self.pixel_format
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('CodecLongName') is not None:
            self.codec_long_name = m.get('CodecLongName')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('SampleAspectRatio') is not None:
            self.sample_aspect_ratio = m.get('SampleAspectRatio')
        if m.get('AverageFrameRate') is not None:
            self.average_frame_rate = m.get('AverageFrameRate')
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('Rotate') is not None:
            self.rotate = m.get('Rotate')
        if m.get('CodecTagString') is not None:
            self.codec_tag_string = m.get('CodecTagString')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('HasBFrames') is not None:
            self.has_bframes = m.get('HasBFrames')
        if m.get('FrameRrate') is not None:
            self.frame_rrate = m.get('FrameRrate')
        if m.get('Profile') is not None:
            self.profile = m.get('Profile')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Frames') is not None:
            self.frames = m.get('Frames')
        if m.get('CodecName') is not None:
            self.codec_name = m.get('CodecName')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('DisplayAspectRatio') is not None:
            self.display_aspect_ratio = m.get('DisplayAspectRatio')
        if m.get('CodecTag') is not None:
            self.codec_tag = m.get('CodecTag')
        if m.get('CodecTimeBase') is not None:
            self.codec_time_base = m.get('CodecTimeBase')
        if m.get('TimeBase') is not None:
            self.time_base = m.get('TimeBase')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('PixelFormat') is not None:
            self.pixel_format = m.get('PixelFormat')
        return self


class GetMediaMetaResponseBodyMediaMetaMediaStreamsAudioStreams(TeaModel):
    def __init__(
        self,
        index: int = None,
        sample_rate: str = None,
        channel_layout: str = None,
        codec_long_name: str = None,
        channels: int = None,
        bitrate: str = None,
        codec_tag_string: str = None,
        language: str = None,
        start_time: str = None,
        sample_format: str = None,
        frames: str = None,
        codec_name: str = None,
        duration: str = None,
        codec_tag: str = None,
        codec_time_base: str = None,
        time_base: str = None,
    ):
        self.index = index
        self.sample_rate = sample_rate
        self.channel_layout = channel_layout
        self.codec_long_name = codec_long_name
        self.channels = channels
        self.bitrate = bitrate
        self.codec_tag_string = codec_tag_string
        self.language = language
        self.start_time = start_time
        self.sample_format = sample_format
        self.frames = frames
        self.codec_name = codec_name
        self.duration = duration
        self.codec_tag = codec_tag
        self.codec_time_base = codec_time_base
        self.time_base = time_base

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.sample_rate is not None:
            result['SampleRate'] = self.sample_rate
        if self.channel_layout is not None:
            result['ChannelLayout'] = self.channel_layout
        if self.codec_long_name is not None:
            result['CodecLongName'] = self.codec_long_name
        if self.channels is not None:
            result['Channels'] = self.channels
        if self.bitrate is not None:
            result['Bitrate'] = self.bitrate
        if self.codec_tag_string is not None:
            result['CodecTagString'] = self.codec_tag_string
        if self.language is not None:
            result['Language'] = self.language
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.sample_format is not None:
            result['SampleFormat'] = self.sample_format
        if self.frames is not None:
            result['Frames'] = self.frames
        if self.codec_name is not None:
            result['CodecName'] = self.codec_name
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.codec_tag is not None:
            result['CodecTag'] = self.codec_tag
        if self.codec_time_base is not None:
            result['CodecTimeBase'] = self.codec_time_base
        if self.time_base is not None:
            result['TimeBase'] = self.time_base
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('SampleRate') is not None:
            self.sample_rate = m.get('SampleRate')
        if m.get('ChannelLayout') is not None:
            self.channel_layout = m.get('ChannelLayout')
        if m.get('CodecLongName') is not None:
            self.codec_long_name = m.get('CodecLongName')
        if m.get('Channels') is not None:
            self.channels = m.get('Channels')
        if m.get('Bitrate') is not None:
            self.bitrate = m.get('Bitrate')
        if m.get('CodecTagString') is not None:
            self.codec_tag_string = m.get('CodecTagString')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('SampleFormat') is not None:
            self.sample_format = m.get('SampleFormat')
        if m.get('Frames') is not None:
            self.frames = m.get('Frames')
        if m.get('CodecName') is not None:
            self.codec_name = m.get('CodecName')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('CodecTag') is not None:
            self.codec_tag = m.get('CodecTag')
        if m.get('CodecTimeBase') is not None:
            self.codec_time_base = m.get('CodecTimeBase')
        if m.get('TimeBase') is not None:
            self.time_base = m.get('TimeBase')
        return self


class GetMediaMetaResponseBodyMediaMetaMediaStreamsSubtitleStreams(TeaModel):
    def __init__(
        self,
        index: int = None,
        language: str = None,
    ):
        self.index = index
        self.language = language

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.language is not None:
            result['Language'] = self.language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        return self


class GetMediaMetaResponseBodyMediaMetaMediaStreams(TeaModel):
    def __init__(
        self,
        video_streams: List[GetMediaMetaResponseBodyMediaMetaMediaStreamsVideoStreams] = None,
        audio_streams: List[GetMediaMetaResponseBodyMediaMetaMediaStreamsAudioStreams] = None,
        subtitle_streams: List[GetMediaMetaResponseBodyMediaMetaMediaStreamsSubtitleStreams] = None,
    ):
        self.video_streams = video_streams
        self.audio_streams = audio_streams
        self.subtitle_streams = subtitle_streams

    def validate(self):
        if self.video_streams:
            for k in self.video_streams:
                if k:
                    k.validate()
        if self.audio_streams:
            for k in self.audio_streams:
                if k:
                    k.validate()
        if self.subtitle_streams:
            for k in self.subtitle_streams:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['VideoStreams'] = []
        if self.video_streams is not None:
            for k in self.video_streams:
                result['VideoStreams'].append(k.to_map() if k else None)
        result['AudioStreams'] = []
        if self.audio_streams is not None:
            for k in self.audio_streams:
                result['AudioStreams'].append(k.to_map() if k else None)
        result['SubtitleStreams'] = []
        if self.subtitle_streams is not None:
            for k in self.subtitle_streams:
                result['SubtitleStreams'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.video_streams = []
        if m.get('VideoStreams') is not None:
            for k in m.get('VideoStreams'):
                temp_model = GetMediaMetaResponseBodyMediaMetaMediaStreamsVideoStreams()
                self.video_streams.append(temp_model.from_map(k))
        self.audio_streams = []
        if m.get('AudioStreams') is not None:
            for k in m.get('AudioStreams'):
                temp_model = GetMediaMetaResponseBodyMediaMetaMediaStreamsAudioStreams()
                self.audio_streams.append(temp_model.from_map(k))
        self.subtitle_streams = []
        if m.get('SubtitleStreams') is not None:
            for k in m.get('SubtitleStreams'):
                temp_model = GetMediaMetaResponseBodyMediaMetaMediaStreamsSubtitleStreams()
                self.subtitle_streams.append(temp_model.from_map(k))
        return self


class GetMediaMetaResponseBodyMediaMeta(TeaModel):
    def __init__(
        self,
        media_format: GetMediaMetaResponseBodyMediaMetaMediaFormat = None,
        media_streams: GetMediaMetaResponseBodyMediaMetaMediaStreams = None,
    ):
        self.media_format = media_format
        self.media_streams = media_streams

    def validate(self):
        if self.media_format:
            self.media_format.validate()
        if self.media_streams:
            self.media_streams.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_format is not None:
            result['MediaFormat'] = self.media_format.to_map()
        if self.media_streams is not None:
            result['MediaStreams'] = self.media_streams.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaFormat') is not None:
            temp_model = GetMediaMetaResponseBodyMediaMetaMediaFormat()
            self.media_format = temp_model.from_map(m['MediaFormat'])
        if m.get('MediaStreams') is not None:
            temp_model = GetMediaMetaResponseBodyMediaMetaMediaStreams()
            self.media_streams = temp_model.from_map(m['MediaStreams'])
        return self


class GetMediaMetaResponseBody(TeaModel):
    def __init__(
        self,
        media_uri: str = None,
        request_id: str = None,
        media_meta: GetMediaMetaResponseBodyMediaMeta = None,
    ):
        self.media_uri = media_uri
        self.request_id = request_id
        self.media_meta = media_meta

    def validate(self):
        if self.media_meta:
            self.media_meta.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_uri is not None:
            result['MediaUri'] = self.media_uri
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.media_meta is not None:
            result['MediaMeta'] = self.media_meta.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaUri') is not None:
            self.media_uri = m.get('MediaUri')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MediaMeta') is not None:
            temp_model = GetMediaMetaResponseBodyMediaMeta()
            self.media_meta = temp_model.from_map(m['MediaMeta'])
        return self


class GetMediaMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetMediaMetaResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetMediaMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOfficeConversionTaskRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        task_id: str = None,
    ):
        self.project = project
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetOfficeConversionTaskResponseBodyFailDetail(TeaModel):
    def __init__(
        self,
        code: str = None,
    ):
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class GetOfficeConversionTaskResponseBody(TeaModel):
    def __init__(
        self,
        status: str = None,
        percent: int = None,
        finish_time: str = None,
        create_time: str = None,
        page_count: int = None,
        notify_topic_name: str = None,
        request_id: str = None,
        notify_endpoint: str = None,
        src_uri: str = None,
        tgt_type: str = None,
        tgt_uri: str = None,
        image_spec: str = None,
        external_id: str = None,
        task_id: str = None,
        fail_detail: GetOfficeConversionTaskResponseBodyFailDetail = None,
    ):
        self.status = status
        self.percent = percent
        self.finish_time = finish_time
        self.create_time = create_time
        self.page_count = page_count
        self.notify_topic_name = notify_topic_name
        self.request_id = request_id
        self.notify_endpoint = notify_endpoint
        self.src_uri = src_uri
        self.tgt_type = tgt_type
        self.tgt_uri = tgt_uri
        self.image_spec = image_spec
        self.external_id = external_id
        self.task_id = task_id
        self.fail_detail = fail_detail

    def validate(self):
        if self.fail_detail:
            self.fail_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        if self.src_uri is not None:
            result['SrcUri'] = self.src_uri
        if self.tgt_type is not None:
            result['TgtType'] = self.tgt_type
        if self.tgt_uri is not None:
            result['TgtUri'] = self.tgt_uri
        if self.image_spec is not None:
            result['ImageSpec'] = self.image_spec
        if self.external_id is not None:
            result['ExternalID'] = self.external_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.fail_detail is not None:
            result['FailDetail'] = self.fail_detail.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        if m.get('SrcUri') is not None:
            self.src_uri = m.get('SrcUri')
        if m.get('TgtType') is not None:
            self.tgt_type = m.get('TgtType')
        if m.get('TgtUri') is not None:
            self.tgt_uri = m.get('TgtUri')
        if m.get('ImageSpec') is not None:
            self.image_spec = m.get('ImageSpec')
        if m.get('ExternalID') is not None:
            self.external_id = m.get('ExternalID')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('FailDetail') is not None:
            temp_model = GetOfficeConversionTaskResponseBodyFailDetail()
            self.fail_detail = temp_model.from_map(m['FailDetail'])
        return self


class GetOfficeConversionTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetOfficeConversionTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetOfficeConversionTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOfficeEditURLRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        src_uri: str = None,
        src_type: str = None,
        file_id: str = None,
        tgt_uri: str = None,
        user_id: str = None,
        user_name: str = None,
        notify_endpoint: str = None,
        notify_topic_name: str = None,
        file_name: str = None,
    ):
        self.project = project
        self.src_uri = src_uri
        self.src_type = src_type
        self.file_id = file_id
        self.tgt_uri = tgt_uri
        self.user_id = user_id
        self.user_name = user_name
        self.notify_endpoint = notify_endpoint
        self.notify_topic_name = notify_topic_name
        self.file_name = file_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.src_uri is not None:
            result['SrcUri'] = self.src_uri
        if self.src_type is not None:
            result['SrcType'] = self.src_type
        if self.file_id is not None:
            result['FileID'] = self.file_id
        if self.tgt_uri is not None:
            result['TgtUri'] = self.tgt_uri
        if self.user_id is not None:
            result['UserID'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.file_name is not None:
            result['FileName'] = self.file_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SrcUri') is not None:
            self.src_uri = m.get('SrcUri')
        if m.get('SrcType') is not None:
            self.src_type = m.get('SrcType')
        if m.get('FileID') is not None:
            self.file_id = m.get('FileID')
        if m.get('TgtUri') is not None:
            self.tgt_uri = m.get('TgtUri')
        if m.get('UserID') is not None:
            self.user_id = m.get('UserID')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        return self


class GetOfficeEditURLResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        access_token_expired_time: str = None,
        edit_url: str = None,
        access_token: str = None,
        refresh_token: str = None,
        refresh_token_expired_time: str = None,
    ):
        self.request_id = request_id
        self.access_token_expired_time = access_token_expired_time
        self.edit_url = edit_url
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.refresh_token_expired_time = refresh_token_expired_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.access_token_expired_time is not None:
            result['AccessTokenExpiredTime'] = self.access_token_expired_time
        if self.edit_url is not None:
            result['EditURL'] = self.edit_url
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.refresh_token is not None:
            result['RefreshToken'] = self.refresh_token
        if self.refresh_token_expired_time is not None:
            result['RefreshTokenExpiredTime'] = self.refresh_token_expired_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AccessTokenExpiredTime') is not None:
            self.access_token_expired_time = m.get('AccessTokenExpiredTime')
        if m.get('EditURL') is not None:
            self.edit_url = m.get('EditURL')
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('RefreshToken') is not None:
            self.refresh_token = m.get('RefreshToken')
        if m.get('RefreshTokenExpiredTime') is not None:
            self.refresh_token_expired_time = m.get('RefreshTokenExpiredTime')
        return self


class GetOfficeEditURLResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetOfficeEditURLResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetOfficeEditURLResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOfficePreviewURLRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        src_uri: str = None,
        src_type: str = None,
        watermark_type: int = None,
        watermark_value: str = None,
        watermark_fill_style: str = None,
        watermark_font: str = None,
        watermark_rotate: float = None,
        watermark_horizontal: int = None,
        watermark_vertical: int = None,
    ):
        self.project = project
        self.src_uri = src_uri
        self.src_type = src_type
        self.watermark_type = watermark_type
        self.watermark_value = watermark_value
        self.watermark_fill_style = watermark_fill_style
        self.watermark_font = watermark_font
        self.watermark_rotate = watermark_rotate
        self.watermark_horizontal = watermark_horizontal
        self.watermark_vertical = watermark_vertical

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.src_uri is not None:
            result['SrcUri'] = self.src_uri
        if self.src_type is not None:
            result['SrcType'] = self.src_type
        if self.watermark_type is not None:
            result['WatermarkType'] = self.watermark_type
        if self.watermark_value is not None:
            result['WatermarkValue'] = self.watermark_value
        if self.watermark_fill_style is not None:
            result['WatermarkFillStyle'] = self.watermark_fill_style
        if self.watermark_font is not None:
            result['WatermarkFont'] = self.watermark_font
        if self.watermark_rotate is not None:
            result['WatermarkRotate'] = self.watermark_rotate
        if self.watermark_horizontal is not None:
            result['WatermarkHorizontal'] = self.watermark_horizontal
        if self.watermark_vertical is not None:
            result['WatermarkVertical'] = self.watermark_vertical
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SrcUri') is not None:
            self.src_uri = m.get('SrcUri')
        if m.get('SrcType') is not None:
            self.src_type = m.get('SrcType')
        if m.get('WatermarkType') is not None:
            self.watermark_type = m.get('WatermarkType')
        if m.get('WatermarkValue') is not None:
            self.watermark_value = m.get('WatermarkValue')
        if m.get('WatermarkFillStyle') is not None:
            self.watermark_fill_style = m.get('WatermarkFillStyle')
        if m.get('WatermarkFont') is not None:
            self.watermark_font = m.get('WatermarkFont')
        if m.get('WatermarkRotate') is not None:
            self.watermark_rotate = m.get('WatermarkRotate')
        if m.get('WatermarkHorizontal') is not None:
            self.watermark_horizontal = m.get('WatermarkHorizontal')
        if m.get('WatermarkVertical') is not None:
            self.watermark_vertical = m.get('WatermarkVertical')
        return self


class GetOfficePreviewURLResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        preview_url: str = None,
        access_token_expired_time: str = None,
        access_token: str = None,
        refresh_token: str = None,
        refresh_token_expired_time: str = None,
    ):
        self.request_id = request_id
        self.preview_url = preview_url
        self.access_token_expired_time = access_token_expired_time
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.refresh_token_expired_time = refresh_token_expired_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.preview_url is not None:
            result['PreviewURL'] = self.preview_url
        if self.access_token_expired_time is not None:
            result['AccessTokenExpiredTime'] = self.access_token_expired_time
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.refresh_token is not None:
            result['RefreshToken'] = self.refresh_token
        if self.refresh_token_expired_time is not None:
            result['RefreshTokenExpiredTime'] = self.refresh_token_expired_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PreviewURL') is not None:
            self.preview_url = m.get('PreviewURL')
        if m.get('AccessTokenExpiredTime') is not None:
            self.access_token_expired_time = m.get('AccessTokenExpiredTime')
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('RefreshToken') is not None:
            self.refresh_token = m.get('RefreshToken')
        if m.get('RefreshTokenExpiredTime') is not None:
            self.refresh_token_expired_time = m.get('RefreshTokenExpiredTime')
        return self


class GetOfficePreviewURLResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetOfficePreviewURLResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetOfficePreviewURLResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProjectRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
    ):
        self.project = project

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        return self


class GetProjectResponseBody(TeaModel):
    def __init__(
        self,
        type: str = None,
        request_id: str = None,
        cu: int = None,
        create_time: str = None,
        endpoint: str = None,
        service_role: str = None,
        project: str = None,
        region_id: str = None,
        billing_type: str = None,
        modify_time: str = None,
    ):
        self.type = type
        self.request_id = request_id
        self.cu = cu
        self.create_time = create_time
        self.endpoint = endpoint
        self.service_role = service_role
        self.project = project
        self.region_id = region_id
        self.billing_type = billing_type
        self.modify_time = modify_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.cu is not None:
            result['CU'] = self.cu
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.service_role is not None:
            result['ServiceRole'] = self.service_role
        if self.project is not None:
            result['Project'] = self.project
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.billing_type is not None:
            result['BillingType'] = self.billing_type
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CU') is not None:
            self.cu = m.get('CU')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('ServiceRole') is not None:
            self.service_role = m.get('ServiceRole')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('BillingType') is not None:
            self.billing_type = m.get('BillingType')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        return self


class GetProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetProjectResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSetRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        set_id: str = None,
    ):
        self.project = project
        self.set_id = set_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.set_id is not None:
            result['SetId'] = self.set_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        return self


class GetSetResponseBody(TeaModel):
    def __init__(
        self,
        video_count: int = None,
        request_id: str = None,
        create_time: str = None,
        video_length: int = None,
        set_id: str = None,
        image_count: int = None,
        face_count: int = None,
        set_name: str = None,
        modify_time: str = None,
    ):
        self.video_count = video_count
        self.request_id = request_id
        self.create_time = create_time
        self.video_length = video_length
        self.set_id = set_id
        self.image_count = image_count
        self.face_count = face_count
        self.set_name = set_name
        self.modify_time = modify_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_count is not None:
            result['VideoCount'] = self.video_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.video_length is not None:
            result['VideoLength'] = self.video_length
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.image_count is not None:
            result['ImageCount'] = self.image_count
        if self.face_count is not None:
            result['FaceCount'] = self.face_count
        if self.set_name is not None:
            result['SetName'] = self.set_name
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoCount') is not None:
            self.video_count = m.get('VideoCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('VideoLength') is not None:
            self.video_length = m.get('VideoLength')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('ImageCount') is not None:
            self.image_count = m.get('ImageCount')
        if m.get('FaceCount') is not None:
            self.face_count = m.get('FaceCount')
        if m.get('SetName') is not None:
            self.set_name = m.get('SetName')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        return self


class GetSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSetResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVideoRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        set_id: str = None,
        video_uri: str = None,
    ):
        self.project = project
        self.set_id = set_id
        self.video_uri = video_uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.video_uri is not None:
            result['VideoUri'] = self.video_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('VideoUri') is not None:
            self.video_uri = m.get('VideoUri')
        return self


class GetVideoResponseBodyVideoTags(TeaModel):
    def __init__(
        self,
        tag_name: str = None,
        tag_confidence: float = None,
        tag_level: int = None,
        parent_tag_name: str = None,
    ):
        self.tag_name = tag_name
        self.tag_confidence = tag_confidence
        self.tag_level = tag_level
        self.parent_tag_name = parent_tag_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        if self.tag_confidence is not None:
            result['TagConfidence'] = self.tag_confidence
        if self.tag_level is not None:
            result['TagLevel'] = self.tag_level
        if self.parent_tag_name is not None:
            result['ParentTagName'] = self.parent_tag_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        if m.get('TagConfidence') is not None:
            self.tag_confidence = m.get('TagConfidence')
        if m.get('TagLevel') is not None:
            self.tag_level = m.get('TagLevel')
        if m.get('ParentTagName') is not None:
            self.parent_tag_name = m.get('ParentTagName')
        return self


class GetVideoResponseBody(TeaModel):
    def __init__(
        self,
        modify_time: str = None,
        process_status: str = None,
        video_width: int = None,
        source_type: str = None,
        source_uri: str = None,
        video_info: str = None,
        video_frame_tags_modify_time: str = None,
        remarks_a: str = None,
        video_faces_fail_reason: str = None,
        remarks_b: str = None,
        video_faces_status: str = None,
        remarks_c: str = None,
        video_ocrmodify_time: str = None,
        remarks_d: str = None,
        video_height: int = None,
        source_position: str = None,
        video_ocrfail_reason: str = None,
        video_frame_tags_status: str = None,
        video_tags_fail_reason: str = None,
        video_tags_modify_time: str = None,
        video_ocrstatus: str = None,
        video_frames: int = None,
        request_id: str = None,
        process_modify_time: str = None,
        video_sttmodify_time: str = None,
        process_fail_reason: str = None,
        create_time: str = None,
        external_id: str = None,
        video_sttfail_reason: str = None,
        video_uri: str = None,
        video_frame_tags_fail_reason: str = None,
        video_format: str = None,
        video_sttstatus: str = None,
        video_faces_modify_time: str = None,
        video_tags: List[GetVideoResponseBodyVideoTags] = None,
        video_duration: float = None,
        set_id: str = None,
        video_tags_status: str = None,
        file_size: int = None,
    ):
        self.modify_time = modify_time
        self.process_status = process_status
        self.video_width = video_width
        self.source_type = source_type
        self.source_uri = source_uri
        self.video_info = video_info
        self.video_frame_tags_modify_time = video_frame_tags_modify_time
        self.remarks_a = remarks_a
        self.video_faces_fail_reason = video_faces_fail_reason
        self.remarks_b = remarks_b
        self.video_faces_status = video_faces_status
        self.remarks_c = remarks_c
        self.video_ocrmodify_time = video_ocrmodify_time
        self.remarks_d = remarks_d
        self.video_height = video_height
        self.source_position = source_position
        self.video_ocrfail_reason = video_ocrfail_reason
        self.video_frame_tags_status = video_frame_tags_status
        self.video_tags_fail_reason = video_tags_fail_reason
        self.video_tags_modify_time = video_tags_modify_time
        self.video_ocrstatus = video_ocrstatus
        self.video_frames = video_frames
        self.request_id = request_id
        self.process_modify_time = process_modify_time
        self.video_sttmodify_time = video_sttmodify_time
        self.process_fail_reason = process_fail_reason
        self.create_time = create_time
        self.external_id = external_id
        self.video_sttfail_reason = video_sttfail_reason
        self.video_uri = video_uri
        self.video_frame_tags_fail_reason = video_frame_tags_fail_reason
        self.video_format = video_format
        self.video_sttstatus = video_sttstatus
        self.video_faces_modify_time = video_faces_modify_time
        self.video_tags = video_tags
        self.video_duration = video_duration
        self.set_id = set_id
        self.video_tags_status = video_tags_status
        self.file_size = file_size

    def validate(self):
        if self.video_tags:
            for k in self.video_tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.process_status is not None:
            result['ProcessStatus'] = self.process_status
        if self.video_width is not None:
            result['VideoWidth'] = self.video_width
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.source_uri is not None:
            result['SourceUri'] = self.source_uri
        if self.video_info is not None:
            result['VideoInfo'] = self.video_info
        if self.video_frame_tags_modify_time is not None:
            result['VideoFrameTagsModifyTime'] = self.video_frame_tags_modify_time
        if self.remarks_a is not None:
            result['RemarksA'] = self.remarks_a
        if self.video_faces_fail_reason is not None:
            result['VideoFacesFailReason'] = self.video_faces_fail_reason
        if self.remarks_b is not None:
            result['RemarksB'] = self.remarks_b
        if self.video_faces_status is not None:
            result['VideoFacesStatus'] = self.video_faces_status
        if self.remarks_c is not None:
            result['RemarksC'] = self.remarks_c
        if self.video_ocrmodify_time is not None:
            result['VideoOCRModifyTime'] = self.video_ocrmodify_time
        if self.remarks_d is not None:
            result['RemarksD'] = self.remarks_d
        if self.video_height is not None:
            result['VideoHeight'] = self.video_height
        if self.source_position is not None:
            result['SourcePosition'] = self.source_position
        if self.video_ocrfail_reason is not None:
            result['VideoOCRFailReason'] = self.video_ocrfail_reason
        if self.video_frame_tags_status is not None:
            result['VideoFrameTagsStatus'] = self.video_frame_tags_status
        if self.video_tags_fail_reason is not None:
            result['VideoTagsFailReason'] = self.video_tags_fail_reason
        if self.video_tags_modify_time is not None:
            result['VideoTagsModifyTime'] = self.video_tags_modify_time
        if self.video_ocrstatus is not None:
            result['VideoOCRStatus'] = self.video_ocrstatus
        if self.video_frames is not None:
            result['VideoFrames'] = self.video_frames
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.process_modify_time is not None:
            result['ProcessModifyTime'] = self.process_modify_time
        if self.video_sttmodify_time is not None:
            result['VideoSTTModifyTime'] = self.video_sttmodify_time
        if self.process_fail_reason is not None:
            result['ProcessFailReason'] = self.process_fail_reason
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.external_id is not None:
            result['ExternalId'] = self.external_id
        if self.video_sttfail_reason is not None:
            result['VideoSTTFailReason'] = self.video_sttfail_reason
        if self.video_uri is not None:
            result['VideoUri'] = self.video_uri
        if self.video_frame_tags_fail_reason is not None:
            result['VideoFrameTagsFailReason'] = self.video_frame_tags_fail_reason
        if self.video_format is not None:
            result['VideoFormat'] = self.video_format
        if self.video_sttstatus is not None:
            result['VideoSTTStatus'] = self.video_sttstatus
        if self.video_faces_modify_time is not None:
            result['VideoFacesModifyTime'] = self.video_faces_modify_time
        result['VideoTags'] = []
        if self.video_tags is not None:
            for k in self.video_tags:
                result['VideoTags'].append(k.to_map() if k else None)
        if self.video_duration is not None:
            result['VideoDuration'] = self.video_duration
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.video_tags_status is not None:
            result['VideoTagsStatus'] = self.video_tags_status
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ProcessStatus') is not None:
            self.process_status = m.get('ProcessStatus')
        if m.get('VideoWidth') is not None:
            self.video_width = m.get('VideoWidth')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('SourceUri') is not None:
            self.source_uri = m.get('SourceUri')
        if m.get('VideoInfo') is not None:
            self.video_info = m.get('VideoInfo')
        if m.get('VideoFrameTagsModifyTime') is not None:
            self.video_frame_tags_modify_time = m.get('VideoFrameTagsModifyTime')
        if m.get('RemarksA') is not None:
            self.remarks_a = m.get('RemarksA')
        if m.get('VideoFacesFailReason') is not None:
            self.video_faces_fail_reason = m.get('VideoFacesFailReason')
        if m.get('RemarksB') is not None:
            self.remarks_b = m.get('RemarksB')
        if m.get('VideoFacesStatus') is not None:
            self.video_faces_status = m.get('VideoFacesStatus')
        if m.get('RemarksC') is not None:
            self.remarks_c = m.get('RemarksC')
        if m.get('VideoOCRModifyTime') is not None:
            self.video_ocrmodify_time = m.get('VideoOCRModifyTime')
        if m.get('RemarksD') is not None:
            self.remarks_d = m.get('RemarksD')
        if m.get('VideoHeight') is not None:
            self.video_height = m.get('VideoHeight')
        if m.get('SourcePosition') is not None:
            self.source_position = m.get('SourcePosition')
        if m.get('VideoOCRFailReason') is not None:
            self.video_ocrfail_reason = m.get('VideoOCRFailReason')
        if m.get('VideoFrameTagsStatus') is not None:
            self.video_frame_tags_status = m.get('VideoFrameTagsStatus')
        if m.get('VideoTagsFailReason') is not None:
            self.video_tags_fail_reason = m.get('VideoTagsFailReason')
        if m.get('VideoTagsModifyTime') is not None:
            self.video_tags_modify_time = m.get('VideoTagsModifyTime')
        if m.get('VideoOCRStatus') is not None:
            self.video_ocrstatus = m.get('VideoOCRStatus')
        if m.get('VideoFrames') is not None:
            self.video_frames = m.get('VideoFrames')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ProcessModifyTime') is not None:
            self.process_modify_time = m.get('ProcessModifyTime')
        if m.get('VideoSTTModifyTime') is not None:
            self.video_sttmodify_time = m.get('VideoSTTModifyTime')
        if m.get('ProcessFailReason') is not None:
            self.process_fail_reason = m.get('ProcessFailReason')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExternalId') is not None:
            self.external_id = m.get('ExternalId')
        if m.get('VideoSTTFailReason') is not None:
            self.video_sttfail_reason = m.get('VideoSTTFailReason')
        if m.get('VideoUri') is not None:
            self.video_uri = m.get('VideoUri')
        if m.get('VideoFrameTagsFailReason') is not None:
            self.video_frame_tags_fail_reason = m.get('VideoFrameTagsFailReason')
        if m.get('VideoFormat') is not None:
            self.video_format = m.get('VideoFormat')
        if m.get('VideoSTTStatus') is not None:
            self.video_sttstatus = m.get('VideoSTTStatus')
        if m.get('VideoFacesModifyTime') is not None:
            self.video_faces_modify_time = m.get('VideoFacesModifyTime')
        self.video_tags = []
        if m.get('VideoTags') is not None:
            for k in m.get('VideoTags'):
                temp_model = GetVideoResponseBodyVideoTags()
                self.video_tags.append(temp_model.from_map(k))
        if m.get('VideoDuration') is not None:
            self.video_duration = m.get('VideoDuration')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('VideoTagsStatus') is not None:
            self.video_tags_status = m.get('VideoTagsStatus')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        return self


class GetVideoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetVideoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetVideoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVideoTaskRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        task_type: str = None,
        task_id: str = None,
    ):
        self.project = project
        self.task_type = task_type
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetVideoTaskResponseBody(TeaModel):
    def __init__(
        self,
        status: str = None,
        progress: int = None,
        notify_endpoint: str = None,
        parameters: str = None,
        task_id: str = None,
        end_time: str = None,
        request_id: str = None,
        task_type: str = None,
        start_time: str = None,
        notify_topic_name: str = None,
        error_message: str = None,
        result: str = None,
    ):
        self.status = status
        self.progress = progress
        self.notify_endpoint = notify_endpoint
        self.parameters = parameters
        self.task_id = task_id
        self.end_time = end_time
        self.request_id = request_id
        self.task_type = task_type
        self.start_time = start_time
        self.notify_topic_name = notify_topic_name
        self.error_message = error_message
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class GetVideoTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetVideoTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetVideoTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWebofficeURLRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        src_type: str = None,
        file_id: str = None,
        user: str = None,
        permission: str = None,
        file: str = None,
        notify_endpoint: str = None,
        notify_topic_name: str = None,
        watermark: str = None,
        hidecmb: bool = None,
    ):
        self.project = project
        self.src_type = src_type
        self.file_id = file_id
        self.user = user
        self.permission = permission
        self.file = file
        self.notify_endpoint = notify_endpoint
        self.notify_topic_name = notify_topic_name
        self.watermark = watermark
        self.hidecmb = hidecmb

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.src_type is not None:
            result['SrcType'] = self.src_type
        if self.file_id is not None:
            result['FileID'] = self.file_id
        if self.user is not None:
            result['User'] = self.user
        if self.permission is not None:
            result['Permission'] = self.permission
        if self.file is not None:
            result['File'] = self.file
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.watermark is not None:
            result['Watermark'] = self.watermark
        if self.hidecmb is not None:
            result['Hidecmb'] = self.hidecmb
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SrcType') is not None:
            self.src_type = m.get('SrcType')
        if m.get('FileID') is not None:
            self.file_id = m.get('FileID')
        if m.get('User') is not None:
            self.user = m.get('User')
        if m.get('Permission') is not None:
            self.permission = m.get('Permission')
        if m.get('File') is not None:
            self.file = m.get('File')
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('Watermark') is not None:
            self.watermark = m.get('Watermark')
        if m.get('Hidecmb') is not None:
            self.hidecmb = m.get('Hidecmb')
        return self


class GetWebofficeURLResponseBody(TeaModel):
    def __init__(
        self,
        refresh_token: str = None,
        request_id: str = None,
        access_token: str = None,
        refresh_token_expired_time: str = None,
        weboffice_url: str = None,
        access_token_expired_time: str = None,
    ):
        self.refresh_token = refresh_token
        self.request_id = request_id
        self.access_token = access_token
        self.refresh_token_expired_time = refresh_token_expired_time
        self.weboffice_url = weboffice_url
        self.access_token_expired_time = access_token_expired_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.refresh_token is not None:
            result['RefreshToken'] = self.refresh_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.refresh_token_expired_time is not None:
            result['RefreshTokenExpiredTime'] = self.refresh_token_expired_time
        if self.weboffice_url is not None:
            result['WebofficeURL'] = self.weboffice_url
        if self.access_token_expired_time is not None:
            result['AccessTokenExpiredTime'] = self.access_token_expired_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RefreshToken') is not None:
            self.refresh_token = m.get('RefreshToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('RefreshTokenExpiredTime') is not None:
            self.refresh_token_expired_time = m.get('RefreshTokenExpiredTime')
        if m.get('WebofficeURL') is not None:
            self.weboffice_url = m.get('WebofficeURL')
        if m.get('AccessTokenExpiredTime') is not None:
            self.access_token_expired_time = m.get('AccessTokenExpiredTime')
        return self


class GetWebofficeURLResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetWebofficeURLResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetWebofficeURLResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class IndexImageRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        set_id: str = None,
        image_uri: str = None,
        remarks_a: str = None,
        remarks_b: str = None,
        source_type: str = None,
        source_uri: str = None,
        source_position: str = None,
        remarks_c: str = None,
        remarks_d: str = None,
        external_id: str = None,
        notify_endpoint: str = None,
        notify_topic_name: str = None,
        remarks_array_a: str = None,
        remarks_array_b: str = None,
    ):
        self.project = project
        self.set_id = set_id
        self.image_uri = image_uri
        self.remarks_a = remarks_a
        self.remarks_b = remarks_b
        self.source_type = source_type
        self.source_uri = source_uri
        self.source_position = source_position
        self.remarks_c = remarks_c
        self.remarks_d = remarks_d
        self.external_id = external_id
        self.notify_endpoint = notify_endpoint
        self.notify_topic_name = notify_topic_name
        self.remarks_array_a = remarks_array_a
        self.remarks_array_b = remarks_array_b

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        if self.remarks_a is not None:
            result['RemarksA'] = self.remarks_a
        if self.remarks_b is not None:
            result['RemarksB'] = self.remarks_b
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.source_uri is not None:
            result['SourceUri'] = self.source_uri
        if self.source_position is not None:
            result['SourcePosition'] = self.source_position
        if self.remarks_c is not None:
            result['RemarksC'] = self.remarks_c
        if self.remarks_d is not None:
            result['RemarksD'] = self.remarks_d
        if self.external_id is not None:
            result['ExternalId'] = self.external_id
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.remarks_array_a is not None:
            result['RemarksArrayA'] = self.remarks_array_a
        if self.remarks_array_b is not None:
            result['RemarksArrayB'] = self.remarks_array_b
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        if m.get('RemarksA') is not None:
            self.remarks_a = m.get('RemarksA')
        if m.get('RemarksB') is not None:
            self.remarks_b = m.get('RemarksB')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('SourceUri') is not None:
            self.source_uri = m.get('SourceUri')
        if m.get('SourcePosition') is not None:
            self.source_position = m.get('SourcePosition')
        if m.get('RemarksC') is not None:
            self.remarks_c = m.get('RemarksC')
        if m.get('RemarksD') is not None:
            self.remarks_d = m.get('RemarksD')
        if m.get('ExternalId') is not None:
            self.external_id = m.get('ExternalId')
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('RemarksArrayA') is not None:
            self.remarks_array_a = m.get('RemarksArrayA')
        if m.get('RemarksArrayB') is not None:
            self.remarks_array_b = m.get('RemarksArrayB')
        return self


class IndexImageResponseBody(TeaModel):
    def __init__(
        self,
        remarks_array_b: str = None,
        modify_time: str = None,
        remarks_c: str = None,
        remarks_d: str = None,
        request_id: str = None,
        create_time: str = None,
        external_id: str = None,
        remarks_array_a: str = None,
        remarks_a: str = None,
        image_uri: str = None,
        set_id: str = None,
        remarks_b: str = None,
    ):
        self.remarks_array_b = remarks_array_b
        self.modify_time = modify_time
        self.remarks_c = remarks_c
        self.remarks_d = remarks_d
        self.request_id = request_id
        self.create_time = create_time
        self.external_id = external_id
        self.remarks_array_a = remarks_array_a
        self.remarks_a = remarks_a
        self.image_uri = image_uri
        self.set_id = set_id
        self.remarks_b = remarks_b

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.remarks_array_b is not None:
            result['RemarksArrayB'] = self.remarks_array_b
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.remarks_c is not None:
            result['RemarksC'] = self.remarks_c
        if self.remarks_d is not None:
            result['RemarksD'] = self.remarks_d
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.external_id is not None:
            result['ExternalId'] = self.external_id
        if self.remarks_array_a is not None:
            result['RemarksArrayA'] = self.remarks_array_a
        if self.remarks_a is not None:
            result['RemarksA'] = self.remarks_a
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.remarks_b is not None:
            result['RemarksB'] = self.remarks_b
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RemarksArrayB') is not None:
            self.remarks_array_b = m.get('RemarksArrayB')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('RemarksC') is not None:
            self.remarks_c = m.get('RemarksC')
        if m.get('RemarksD') is not None:
            self.remarks_d = m.get('RemarksD')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExternalId') is not None:
            self.external_id = m.get('ExternalId')
        if m.get('RemarksArrayA') is not None:
            self.remarks_array_a = m.get('RemarksArrayA')
        if m.get('RemarksA') is not None:
            self.remarks_a = m.get('RemarksA')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('RemarksB') is not None:
            self.remarks_b = m.get('RemarksB')
        return self


class IndexImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: IndexImageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = IndexImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class IndexVideoRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        set_id: str = None,
        video_uri: str = None,
        remarks_a: str = None,
        remarks_b: str = None,
        tgt_uri: str = None,
        remarks_c: str = None,
        remarks_d: str = None,
        external_id: str = None,
        notify_topic_name: str = None,
        notify_endpoint: str = None,
    ):
        self.project = project
        self.set_id = set_id
        self.video_uri = video_uri
        self.remarks_a = remarks_a
        self.remarks_b = remarks_b
        self.tgt_uri = tgt_uri
        self.remarks_c = remarks_c
        self.remarks_d = remarks_d
        self.external_id = external_id
        self.notify_topic_name = notify_topic_name
        self.notify_endpoint = notify_endpoint

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.video_uri is not None:
            result['VideoUri'] = self.video_uri
        if self.remarks_a is not None:
            result['RemarksA'] = self.remarks_a
        if self.remarks_b is not None:
            result['RemarksB'] = self.remarks_b
        if self.tgt_uri is not None:
            result['TgtUri'] = self.tgt_uri
        if self.remarks_c is not None:
            result['RemarksC'] = self.remarks_c
        if self.remarks_d is not None:
            result['RemarksD'] = self.remarks_d
        if self.external_id is not None:
            result['ExternalId'] = self.external_id
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('VideoUri') is not None:
            self.video_uri = m.get('VideoUri')
        if m.get('RemarksA') is not None:
            self.remarks_a = m.get('RemarksA')
        if m.get('RemarksB') is not None:
            self.remarks_b = m.get('RemarksB')
        if m.get('TgtUri') is not None:
            self.tgt_uri = m.get('TgtUri')
        if m.get('RemarksC') is not None:
            self.remarks_c = m.get('RemarksC')
        if m.get('RemarksD') is not None:
            self.remarks_d = m.get('RemarksD')
        if m.get('ExternalId') is not None:
            self.external_id = m.get('ExternalId')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        return self


class IndexVideoResponseBody(TeaModel):
    def __init__(
        self,
        modify_time: str = None,
        request_id: str = None,
        create_time: str = None,
        external_id: str = None,
        video_uri: str = None,
        remarks_a: str = None,
        remarks_b: str = None,
        remarks_c: str = None,
        remarks_d: str = None,
        set_id: str = None,
    ):
        self.modify_time = modify_time
        self.request_id = request_id
        self.create_time = create_time
        self.external_id = external_id
        self.video_uri = video_uri
        self.remarks_a = remarks_a
        self.remarks_b = remarks_b
        self.remarks_c = remarks_c
        self.remarks_d = remarks_d
        self.set_id = set_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.external_id is not None:
            result['ExternalId'] = self.external_id
        if self.video_uri is not None:
            result['VideoUri'] = self.video_uri
        if self.remarks_a is not None:
            result['RemarksA'] = self.remarks_a
        if self.remarks_b is not None:
            result['RemarksB'] = self.remarks_b
        if self.remarks_c is not None:
            result['RemarksC'] = self.remarks_c
        if self.remarks_d is not None:
            result['RemarksD'] = self.remarks_d
        if self.set_id is not None:
            result['SetId'] = self.set_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExternalId') is not None:
            self.external_id = m.get('ExternalId')
        if m.get('VideoUri') is not None:
            self.video_uri = m.get('VideoUri')
        if m.get('RemarksA') is not None:
            self.remarks_a = m.get('RemarksA')
        if m.get('RemarksB') is not None:
            self.remarks_b = m.get('RemarksB')
        if m.get('RemarksC') is not None:
            self.remarks_c = m.get('RemarksC')
        if m.get('RemarksD') is not None:
            self.remarks_d = m.get('RemarksD')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        return self


class IndexVideoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: IndexVideoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = IndexVideoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFaceGroupsRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        set_id: str = None,
        marker: str = None,
        limit: int = None,
        order: str = None,
        order_by: str = None,
        remarks_aquery: str = None,
        remarks_bquery: str = None,
        remarks_cquery: str = None,
        remarks_dquery: str = None,
        remarks_array_aquery: str = None,
        remarks_array_bquery: str = None,
        external_id: str = None,
    ):
        self.project = project
        self.set_id = set_id
        self.marker = marker
        self.limit = limit
        self.order = order
        self.order_by = order_by
        self.remarks_aquery = remarks_aquery
        self.remarks_bquery = remarks_bquery
        self.remarks_cquery = remarks_cquery
        self.remarks_dquery = remarks_dquery
        self.remarks_array_aquery = remarks_array_aquery
        self.remarks_array_bquery = remarks_array_bquery
        self.external_id = external_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.order is not None:
            result['Order'] = self.order
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.remarks_aquery is not None:
            result['RemarksAQuery'] = self.remarks_aquery
        if self.remarks_bquery is not None:
            result['RemarksBQuery'] = self.remarks_bquery
        if self.remarks_cquery is not None:
            result['RemarksCQuery'] = self.remarks_cquery
        if self.remarks_dquery is not None:
            result['RemarksDQuery'] = self.remarks_dquery
        if self.remarks_array_aquery is not None:
            result['RemarksArrayAQuery'] = self.remarks_array_aquery
        if self.remarks_array_bquery is not None:
            result['RemarksArrayBQuery'] = self.remarks_array_bquery
        if self.external_id is not None:
            result['ExternalId'] = self.external_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('RemarksAQuery') is not None:
            self.remarks_aquery = m.get('RemarksAQuery')
        if m.get('RemarksBQuery') is not None:
            self.remarks_bquery = m.get('RemarksBQuery')
        if m.get('RemarksCQuery') is not None:
            self.remarks_cquery = m.get('RemarksCQuery')
        if m.get('RemarksDQuery') is not None:
            self.remarks_dquery = m.get('RemarksDQuery')
        if m.get('RemarksArrayAQuery') is not None:
            self.remarks_array_aquery = m.get('RemarksArrayAQuery')
        if m.get('RemarksArrayBQuery') is not None:
            self.remarks_array_bquery = m.get('RemarksArrayBQuery')
        if m.get('ExternalId') is not None:
            self.external_id = m.get('ExternalId')
        return self


class ListFaceGroupsResponseBodyFaceGroupsGroupCoverFaceFaceBoundary(TeaModel):
    def __init__(
        self,
        top: int = None,
        width: int = None,
        height: int = None,
        left: int = None,
    ):
        self.top = top
        self.width = width
        self.height = height
        self.left = left

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        if self.left is not None:
            result['Left'] = self.left
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Left') is not None:
            self.left = m.get('Left')
        return self


class ListFaceGroupsResponseBodyFaceGroupsGroupCoverFace(TeaModel):
    def __init__(
        self,
        face_id: str = None,
        image_uri: str = None,
        face_boundary: ListFaceGroupsResponseBodyFaceGroupsGroupCoverFaceFaceBoundary = None,
        external_id: str = None,
        image_height: int = None,
        image_width: int = None,
    ):
        self.face_id = face_id
        self.image_uri = image_uri
        self.face_boundary = face_boundary
        self.external_id = external_id
        self.image_height = image_height
        self.image_width = image_width

    def validate(self):
        if self.face_boundary:
            self.face_boundary.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_id is not None:
            result['FaceId'] = self.face_id
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        if self.face_boundary is not None:
            result['FaceBoundary'] = self.face_boundary.to_map()
        if self.external_id is not None:
            result['ExternalId'] = self.external_id
        if self.image_height is not None:
            result['ImageHeight'] = self.image_height
        if self.image_width is not None:
            result['ImageWidth'] = self.image_width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceId') is not None:
            self.face_id = m.get('FaceId')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        if m.get('FaceBoundary') is not None:
            temp_model = ListFaceGroupsResponseBodyFaceGroupsGroupCoverFaceFaceBoundary()
            self.face_boundary = temp_model.from_map(m['FaceBoundary'])
        if m.get('ExternalId') is not None:
            self.external_id = m.get('ExternalId')
        if m.get('ImageHeight') is not None:
            self.image_height = m.get('ImageHeight')
        if m.get('ImageWidth') is not None:
            self.image_width = m.get('ImageWidth')
        return self


class ListFaceGroupsResponseBodyFaceGroups(TeaModel):
    def __init__(
        self,
        gender: str = None,
        create_time: str = None,
        remarks_c: str = None,
        group_cover_face: ListFaceGroupsResponseBodyFaceGroupsGroupCoverFace = None,
        face_count: int = None,
        remarks_array_b: str = None,
        remarks_d: str = None,
        max_age: float = None,
        group_id: str = None,
        group_name: str = None,
        remarks_a: str = None,
        average_age: float = None,
        remarks_array_a: str = None,
        min_age: float = None,
        image_count: int = None,
        external_id: str = None,
        remarks_b: str = None,
        modify_time: str = None,
    ):
        self.gender = gender
        self.create_time = create_time
        self.remarks_c = remarks_c
        self.group_cover_face = group_cover_face
        self.face_count = face_count
        self.remarks_array_b = remarks_array_b
        self.remarks_d = remarks_d
        self.max_age = max_age
        self.group_id = group_id
        self.group_name = group_name
        self.remarks_a = remarks_a
        self.average_age = average_age
        self.remarks_array_a = remarks_array_a
        self.min_age = min_age
        self.image_count = image_count
        self.external_id = external_id
        self.remarks_b = remarks_b
        self.modify_time = modify_time

    def validate(self):
        if self.group_cover_face:
            self.group_cover_face.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.remarks_c is not None:
            result['RemarksC'] = self.remarks_c
        if self.group_cover_face is not None:
            result['GroupCoverFace'] = self.group_cover_face.to_map()
        if self.face_count is not None:
            result['FaceCount'] = self.face_count
        if self.remarks_array_b is not None:
            result['RemarksArrayB'] = self.remarks_array_b
        if self.remarks_d is not None:
            result['RemarksD'] = self.remarks_d
        if self.max_age is not None:
            result['MaxAge'] = self.max_age
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.remarks_a is not None:
            result['RemarksA'] = self.remarks_a
        if self.average_age is not None:
            result['AverageAge'] = self.average_age
        if self.remarks_array_a is not None:
            result['RemarksArrayA'] = self.remarks_array_a
        if self.min_age is not None:
            result['MinAge'] = self.min_age
        if self.image_count is not None:
            result['ImageCount'] = self.image_count
        if self.external_id is not None:
            result['ExternalId'] = self.external_id
        if self.remarks_b is not None:
            result['RemarksB'] = self.remarks_b
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('RemarksC') is not None:
            self.remarks_c = m.get('RemarksC')
        if m.get('GroupCoverFace') is not None:
            temp_model = ListFaceGroupsResponseBodyFaceGroupsGroupCoverFace()
            self.group_cover_face = temp_model.from_map(m['GroupCoverFace'])
        if m.get('FaceCount') is not None:
            self.face_count = m.get('FaceCount')
        if m.get('RemarksArrayB') is not None:
            self.remarks_array_b = m.get('RemarksArrayB')
        if m.get('RemarksD') is not None:
            self.remarks_d = m.get('RemarksD')
        if m.get('MaxAge') is not None:
            self.max_age = m.get('MaxAge')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('RemarksA') is not None:
            self.remarks_a = m.get('RemarksA')
        if m.get('AverageAge') is not None:
            self.average_age = m.get('AverageAge')
        if m.get('RemarksArrayA') is not None:
            self.remarks_array_a = m.get('RemarksArrayA')
        if m.get('MinAge') is not None:
            self.min_age = m.get('MinAge')
        if m.get('ImageCount') is not None:
            self.image_count = m.get('ImageCount')
        if m.get('ExternalId') is not None:
            self.external_id = m.get('ExternalId')
        if m.get('RemarksB') is not None:
            self.remarks_b = m.get('RemarksB')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        return self


class ListFaceGroupsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        next_marker: str = None,
        face_groups: List[ListFaceGroupsResponseBodyFaceGroups] = None,
    ):
        self.request_id = request_id
        self.next_marker = next_marker
        self.face_groups = face_groups

    def validate(self):
        if self.face_groups:
            for k in self.face_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_marker is not None:
            result['NextMarker'] = self.next_marker
        result['FaceGroups'] = []
        if self.face_groups is not None:
            for k in self.face_groups:
                result['FaceGroups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NextMarker') is not None:
            self.next_marker = m.get('NextMarker')
        self.face_groups = []
        if m.get('FaceGroups') is not None:
            for k in m.get('FaceGroups'):
                temp_model = ListFaceGroupsResponseBodyFaceGroups()
                self.face_groups.append(temp_model.from_map(k))
        return self


class ListFaceGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListFaceGroupsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListFaceGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListImagesRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        set_id: str = None,
        create_time_start: str = None,
        marker: str = None,
        limit: int = None,
    ):
        self.project = project
        self.set_id = set_id
        self.create_time_start = create_time_start
        self.marker = marker
        self.limit = limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.create_time_start is not None:
            result['CreateTimeStart'] = self.create_time_start
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.limit is not None:
            result['Limit'] = self.limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('CreateTimeStart') is not None:
            self.create_time_start = m.get('CreateTimeStart')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        return self


class ListImagesResponseBodyImagesCroppingSuggestionCroppingBoundary(TeaModel):
    def __init__(
        self,
        left: int = None,
        top: int = None,
        width: int = None,
        height: int = None,
    ):
        self.left = left
        self.top = top
        self.width = width
        self.height = height

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class ListImagesResponseBodyImagesCroppingSuggestion(TeaModel):
    def __init__(
        self,
        score: float = None,
        aspect_ratio: str = None,
        cropping_boundary: ListImagesResponseBodyImagesCroppingSuggestionCroppingBoundary = None,
    ):
        self.score = score
        self.aspect_ratio = aspect_ratio
        self.cropping_boundary = cropping_boundary

    def validate(self):
        if self.cropping_boundary:
            self.cropping_boundary.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.score is not None:
            result['Score'] = self.score
        if self.aspect_ratio is not None:
            result['AspectRatio'] = self.aspect_ratio
        if self.cropping_boundary is not None:
            result['CroppingBoundary'] = self.cropping_boundary.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('AspectRatio') is not None:
            self.aspect_ratio = m.get('AspectRatio')
        if m.get('CroppingBoundary') is not None:
            temp_model = ListImagesResponseBodyImagesCroppingSuggestionCroppingBoundary()
            self.cropping_boundary = temp_model.from_map(m['CroppingBoundary'])
        return self


class ListImagesResponseBodyImagesFacesEmotionDetails(TeaModel):
    def __init__(
        self,
        happy: float = None,
        surprised: float = None,
        calm: float = None,
        disgusted: float = None,
        angry: float = None,
        sad: float = None,
        scared: float = None,
    ):
        self.happy = happy
        self.surprised = surprised
        self.calm = calm
        self.disgusted = disgusted
        self.angry = angry
        self.sad = sad
        self.scared = scared

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.happy is not None:
            result['HAPPY'] = self.happy
        if self.surprised is not None:
            result['SURPRISED'] = self.surprised
        if self.calm is not None:
            result['CALM'] = self.calm
        if self.disgusted is not None:
            result['DISGUSTED'] = self.disgusted
        if self.angry is not None:
            result['ANGRY'] = self.angry
        if self.sad is not None:
            result['SAD'] = self.sad
        if self.scared is not None:
            result['SCARED'] = self.scared
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HAPPY') is not None:
            self.happy = m.get('HAPPY')
        if m.get('SURPRISED') is not None:
            self.surprised = m.get('SURPRISED')
        if m.get('CALM') is not None:
            self.calm = m.get('CALM')
        if m.get('DISGUSTED') is not None:
            self.disgusted = m.get('DISGUSTED')
        if m.get('ANGRY') is not None:
            self.angry = m.get('ANGRY')
        if m.get('SAD') is not None:
            self.sad = m.get('SAD')
        if m.get('SCARED') is not None:
            self.scared = m.get('SCARED')
        return self


class ListImagesResponseBodyImagesFacesFaceAttributesFaceBoundary(TeaModel):
    def __init__(
        self,
        left: int = None,
        top: int = None,
        width: int = None,
        height: int = None,
    ):
        self.left = left
        self.top = top
        self.width = width
        self.height = height

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class ListImagesResponseBodyImagesFacesFaceAttributesHeadPose(TeaModel):
    def __init__(
        self,
        pitch: float = None,
        roll: float = None,
        yaw: float = None,
    ):
        self.pitch = pitch
        self.roll = roll
        self.yaw = yaw

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pitch is not None:
            result['Pitch'] = self.pitch
        if self.roll is not None:
            result['Roll'] = self.roll
        if self.yaw is not None:
            result['Yaw'] = self.yaw
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pitch') is not None:
            self.pitch = m.get('Pitch')
        if m.get('Roll') is not None:
            self.roll = m.get('Roll')
        if m.get('Yaw') is not None:
            self.yaw = m.get('Yaw')
        return self


class ListImagesResponseBodyImagesFacesFaceAttributes(TeaModel):
    def __init__(
        self,
        glasses_confidence: float = None,
        glasses: str = None,
        mask: str = None,
        beard_confidence: float = None,
        mask_confidence: float = None,
        beard: str = None,
        face_boundary: ListImagesResponseBodyImagesFacesFaceAttributesFaceBoundary = None,
        head_pose: ListImagesResponseBodyImagesFacesFaceAttributesHeadPose = None,
    ):
        self.glasses_confidence = glasses_confidence
        self.glasses = glasses
        self.mask = mask
        self.beard_confidence = beard_confidence
        self.mask_confidence = mask_confidence
        self.beard = beard
        self.face_boundary = face_boundary
        self.head_pose = head_pose

    def validate(self):
        if self.face_boundary:
            self.face_boundary.validate()
        if self.head_pose:
            self.head_pose.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.glasses_confidence is not None:
            result['GlassesConfidence'] = self.glasses_confidence
        if self.glasses is not None:
            result['Glasses'] = self.glasses
        if self.mask is not None:
            result['Mask'] = self.mask
        if self.beard_confidence is not None:
            result['BeardConfidence'] = self.beard_confidence
        if self.mask_confidence is not None:
            result['MaskConfidence'] = self.mask_confidence
        if self.beard is not None:
            result['Beard'] = self.beard
        if self.face_boundary is not None:
            result['FaceBoundary'] = self.face_boundary.to_map()
        if self.head_pose is not None:
            result['HeadPose'] = self.head_pose.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GlassesConfidence') is not None:
            self.glasses_confidence = m.get('GlassesConfidence')
        if m.get('Glasses') is not None:
            self.glasses = m.get('Glasses')
        if m.get('Mask') is not None:
            self.mask = m.get('Mask')
        if m.get('BeardConfidence') is not None:
            self.beard_confidence = m.get('BeardConfidence')
        if m.get('MaskConfidence') is not None:
            self.mask_confidence = m.get('MaskConfidence')
        if m.get('Beard') is not None:
            self.beard = m.get('Beard')
        if m.get('FaceBoundary') is not None:
            temp_model = ListImagesResponseBodyImagesFacesFaceAttributesFaceBoundary()
            self.face_boundary = temp_model.from_map(m['FaceBoundary'])
        if m.get('HeadPose') is not None:
            temp_model = ListImagesResponseBodyImagesFacesFaceAttributesHeadPose()
            self.head_pose = temp_model.from_map(m['HeadPose'])
        return self


class ListImagesResponseBodyImagesFaces(TeaModel):
    def __init__(
        self,
        emotion_confidence: float = None,
        attractive: float = None,
        group_id: str = None,
        gender: str = None,
        face_id: str = None,
        gender_confidence: float = None,
        face_quality: float = None,
        emotion: str = None,
        age: int = None,
        face_confidence: float = None,
        emotion_details: ListImagesResponseBodyImagesFacesEmotionDetails = None,
        face_attributes: ListImagesResponseBodyImagesFacesFaceAttributes = None,
    ):
        self.emotion_confidence = emotion_confidence
        self.attractive = attractive
        self.group_id = group_id
        self.gender = gender
        self.face_id = face_id
        self.gender_confidence = gender_confidence
        self.face_quality = face_quality
        self.emotion = emotion
        self.age = age
        self.face_confidence = face_confidence
        self.emotion_details = emotion_details
        self.face_attributes = face_attributes

    def validate(self):
        if self.emotion_details:
            self.emotion_details.validate()
        if self.face_attributes:
            self.face_attributes.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.emotion_confidence is not None:
            result['EmotionConfidence'] = self.emotion_confidence
        if self.attractive is not None:
            result['Attractive'] = self.attractive
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.face_id is not None:
            result['FaceId'] = self.face_id
        if self.gender_confidence is not None:
            result['GenderConfidence'] = self.gender_confidence
        if self.face_quality is not None:
            result['FaceQuality'] = self.face_quality
        if self.emotion is not None:
            result['Emotion'] = self.emotion
        if self.age is not None:
            result['Age'] = self.age
        if self.face_confidence is not None:
            result['FaceConfidence'] = self.face_confidence
        if self.emotion_details is not None:
            result['EmotionDetails'] = self.emotion_details.to_map()
        if self.face_attributes is not None:
            result['FaceAttributes'] = self.face_attributes.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EmotionConfidence') is not None:
            self.emotion_confidence = m.get('EmotionConfidence')
        if m.get('Attractive') is not None:
            self.attractive = m.get('Attractive')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('FaceId') is not None:
            self.face_id = m.get('FaceId')
        if m.get('GenderConfidence') is not None:
            self.gender_confidence = m.get('GenderConfidence')
        if m.get('FaceQuality') is not None:
            self.face_quality = m.get('FaceQuality')
        if m.get('Emotion') is not None:
            self.emotion = m.get('Emotion')
        if m.get('Age') is not None:
            self.age = m.get('Age')
        if m.get('FaceConfidence') is not None:
            self.face_confidence = m.get('FaceConfidence')
        if m.get('EmotionDetails') is not None:
            temp_model = ListImagesResponseBodyImagesFacesEmotionDetails()
            self.emotion_details = temp_model.from_map(m['EmotionDetails'])
        if m.get('FaceAttributes') is not None:
            temp_model = ListImagesResponseBodyImagesFacesFaceAttributes()
            self.face_attributes = temp_model.from_map(m['FaceAttributes'])
        return self


class ListImagesResponseBodyImagesTags(TeaModel):
    def __init__(
        self,
        tag_level: int = None,
        parent_tag_name: str = None,
        tag_confidence: float = None,
        tag_name: str = None,
    ):
        self.tag_level = tag_level
        self.parent_tag_name = parent_tag_name
        self.tag_confidence = tag_confidence
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_level is not None:
            result['TagLevel'] = self.tag_level
        if self.parent_tag_name is not None:
            result['ParentTagName'] = self.parent_tag_name
        if self.tag_confidence is not None:
            result['TagConfidence'] = self.tag_confidence
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagLevel') is not None:
            self.tag_level = m.get('TagLevel')
        if m.get('ParentTagName') is not None:
            self.parent_tag_name = m.get('ParentTagName')
        if m.get('TagConfidence') is not None:
            self.tag_confidence = m.get('TagConfidence')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class ListImagesResponseBodyImagesOCROCRBoundary(TeaModel):
    def __init__(
        self,
        left: int = None,
        top: int = None,
        width: int = None,
        height: int = None,
    ):
        self.left = left
        self.top = top
        self.width = width
        self.height = height

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class ListImagesResponseBodyImagesOCR(TeaModel):
    def __init__(
        self,
        ocrconfidence: float = None,
        ocrcontents: str = None,
        ocrboundary: ListImagesResponseBodyImagesOCROCRBoundary = None,
    ):
        self.ocrconfidence = ocrconfidence
        self.ocrcontents = ocrcontents
        self.ocrboundary = ocrboundary

    def validate(self):
        if self.ocrboundary:
            self.ocrboundary.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ocrconfidence is not None:
            result['OCRConfidence'] = self.ocrconfidence
        if self.ocrcontents is not None:
            result['OCRContents'] = self.ocrcontents
        if self.ocrboundary is not None:
            result['OCRBoundary'] = self.ocrboundary.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OCRConfidence') is not None:
            self.ocrconfidence = m.get('OCRConfidence')
        if m.get('OCRContents') is not None:
            self.ocrcontents = m.get('OCRContents')
        if m.get('OCRBoundary') is not None:
            temp_model = ListImagesResponseBodyImagesOCROCRBoundary()
            self.ocrboundary = temp_model.from_map(m['OCRBoundary'])
        return self


class ListImagesResponseBodyImagesImageQuality(TeaModel):
    def __init__(
        self,
        overall_score: float = None,
        color: float = None,
        color_score: float = None,
        contrast_score: float = None,
        contrast: float = None,
        exposure_score: float = None,
        clarity_score: float = None,
        clarity: float = None,
        exposure: float = None,
        composition_score: float = None,
    ):
        self.overall_score = overall_score
        self.color = color
        self.color_score = color_score
        self.contrast_score = contrast_score
        self.contrast = contrast
        self.exposure_score = exposure_score
        self.clarity_score = clarity_score
        self.clarity = clarity
        self.exposure = exposure
        self.composition_score = composition_score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.overall_score is not None:
            result['OverallScore'] = self.overall_score
        if self.color is not None:
            result['Color'] = self.color
        if self.color_score is not None:
            result['ColorScore'] = self.color_score
        if self.contrast_score is not None:
            result['ContrastScore'] = self.contrast_score
        if self.contrast is not None:
            result['Contrast'] = self.contrast
        if self.exposure_score is not None:
            result['ExposureScore'] = self.exposure_score
        if self.clarity_score is not None:
            result['ClarityScore'] = self.clarity_score
        if self.clarity is not None:
            result['Clarity'] = self.clarity
        if self.exposure is not None:
            result['Exposure'] = self.exposure
        if self.composition_score is not None:
            result['CompositionScore'] = self.composition_score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OverallScore') is not None:
            self.overall_score = m.get('OverallScore')
        if m.get('Color') is not None:
            self.color = m.get('Color')
        if m.get('ColorScore') is not None:
            self.color_score = m.get('ColorScore')
        if m.get('ContrastScore') is not None:
            self.contrast_score = m.get('ContrastScore')
        if m.get('Contrast') is not None:
            self.contrast = m.get('Contrast')
        if m.get('ExposureScore') is not None:
            self.exposure_score = m.get('ExposureScore')
        if m.get('ClarityScore') is not None:
            self.clarity_score = m.get('ClarityScore')
        if m.get('Clarity') is not None:
            self.clarity = m.get('Clarity')
        if m.get('Exposure') is not None:
            self.exposure = m.get('Exposure')
        if m.get('CompositionScore') is not None:
            self.composition_score = m.get('CompositionScore')
        return self


class ListImagesResponseBodyImagesAddress(TeaModel):
    def __init__(
        self,
        township: str = None,
        district: str = None,
        address_line: str = None,
        country: str = None,
        city: str = None,
        province: str = None,
    ):
        self.township = township
        self.district = district
        self.address_line = address_line
        self.country = country
        self.city = city
        self.province = province

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.township is not None:
            result['Township'] = self.township
        if self.district is not None:
            result['District'] = self.district
        if self.address_line is not None:
            result['AddressLine'] = self.address_line
        if self.country is not None:
            result['Country'] = self.country
        if self.city is not None:
            result['City'] = self.city
        if self.province is not None:
            result['Province'] = self.province
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Township') is not None:
            self.township = m.get('Township')
        if m.get('District') is not None:
            self.district = m.get('District')
        if m.get('AddressLine') is not None:
            self.address_line = m.get('AddressLine')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        return self


class ListImagesResponseBodyImages(TeaModel):
    def __init__(
        self,
        cropping_suggestion_status: str = None,
        image_quality_modify_time: str = None,
        tags_fail_reason: str = None,
        remarks_c: str = None,
        create_time: str = None,
        source_type: str = None,
        faces_fail_reason: str = None,
        faces_modify_time: str = None,
        image_time: str = None,
        ocrmodify_time: str = None,
        address_modify_time: str = None,
        image_quality_fail_reason: str = None,
        faces_status: str = None,
        remarks_array_a: str = None,
        image_height: int = None,
        external_id: str = None,
        source_uri: str = None,
        file_size: int = None,
        modify_time: str = None,
        source_position: str = None,
        image_quality_status: str = None,
        ocrfail_reason: str = None,
        address_fail_reason: str = None,
        cropping_suggestion_modify_time: str = None,
        image_format: str = None,
        image_width: int = None,
        remarks_array_b: str = None,
        orientation: str = None,
        remarks_d: str = None,
        tags_status: str = None,
        cropping_suggestion_fail_reason: str = None,
        remarks_a: str = None,
        image_uri: str = None,
        tags_modify_time: str = None,
        ocrstatus: str = None,
        address_status: str = None,
        exif: str = None,
        location: str = None,
        remarks_b: str = None,
        cropping_suggestion: List[ListImagesResponseBodyImagesCroppingSuggestion] = None,
        faces: List[ListImagesResponseBodyImagesFaces] = None,
        tags: List[ListImagesResponseBodyImagesTags] = None,
        ocr: List[ListImagesResponseBodyImagesOCR] = None,
        image_quality: ListImagesResponseBodyImagesImageQuality = None,
        address: ListImagesResponseBodyImagesAddress = None,
    ):
        self.cropping_suggestion_status = cropping_suggestion_status
        self.image_quality_modify_time = image_quality_modify_time
        self.tags_fail_reason = tags_fail_reason
        self.remarks_c = remarks_c
        self.create_time = create_time
        self.source_type = source_type
        self.faces_fail_reason = faces_fail_reason
        self.faces_modify_time = faces_modify_time
        self.image_time = image_time
        self.ocrmodify_time = ocrmodify_time
        self.address_modify_time = address_modify_time
        self.image_quality_fail_reason = image_quality_fail_reason
        self.faces_status = faces_status
        self.remarks_array_a = remarks_array_a
        self.image_height = image_height
        self.external_id = external_id
        self.source_uri = source_uri
        self.file_size = file_size
        self.modify_time = modify_time
        self.source_position = source_position
        self.image_quality_status = image_quality_status
        self.ocrfail_reason = ocrfail_reason
        self.address_fail_reason = address_fail_reason
        self.cropping_suggestion_modify_time = cropping_suggestion_modify_time
        self.image_format = image_format
        self.image_width = image_width
        self.remarks_array_b = remarks_array_b
        self.orientation = orientation
        self.remarks_d = remarks_d
        self.tags_status = tags_status
        self.cropping_suggestion_fail_reason = cropping_suggestion_fail_reason
        self.remarks_a = remarks_a
        self.image_uri = image_uri
        self.tags_modify_time = tags_modify_time
        self.ocrstatus = ocrstatus
        self.address_status = address_status
        self.exif = exif
        self.location = location
        self.remarks_b = remarks_b
        self.cropping_suggestion = cropping_suggestion
        self.faces = faces
        self.tags = tags
        self.ocr = ocr
        self.image_quality = image_quality
        self.address = address

    def validate(self):
        if self.cropping_suggestion:
            for k in self.cropping_suggestion:
                if k:
                    k.validate()
        if self.faces:
            for k in self.faces:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.ocr:
            for k in self.ocr:
                if k:
                    k.validate()
        if self.image_quality:
            self.image_quality.validate()
        if self.address:
            self.address.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cropping_suggestion_status is not None:
            result['CroppingSuggestionStatus'] = self.cropping_suggestion_status
        if self.image_quality_modify_time is not None:
            result['ImageQualityModifyTime'] = self.image_quality_modify_time
        if self.tags_fail_reason is not None:
            result['TagsFailReason'] = self.tags_fail_reason
        if self.remarks_c is not None:
            result['RemarksC'] = self.remarks_c
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.faces_fail_reason is not None:
            result['FacesFailReason'] = self.faces_fail_reason
        if self.faces_modify_time is not None:
            result['FacesModifyTime'] = self.faces_modify_time
        if self.image_time is not None:
            result['ImageTime'] = self.image_time
        if self.ocrmodify_time is not None:
            result['OCRModifyTime'] = self.ocrmodify_time
        if self.address_modify_time is not None:
            result['AddressModifyTime'] = self.address_modify_time
        if self.image_quality_fail_reason is not None:
            result['ImageQualityFailReason'] = self.image_quality_fail_reason
        if self.faces_status is not None:
            result['FacesStatus'] = self.faces_status
        if self.remarks_array_a is not None:
            result['RemarksArrayA'] = self.remarks_array_a
        if self.image_height is not None:
            result['ImageHeight'] = self.image_height
        if self.external_id is not None:
            result['ExternalId'] = self.external_id
        if self.source_uri is not None:
            result['SourceUri'] = self.source_uri
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.source_position is not None:
            result['SourcePosition'] = self.source_position
        if self.image_quality_status is not None:
            result['ImageQualityStatus'] = self.image_quality_status
        if self.ocrfail_reason is not None:
            result['OCRFailReason'] = self.ocrfail_reason
        if self.address_fail_reason is not None:
            result['AddressFailReason'] = self.address_fail_reason
        if self.cropping_suggestion_modify_time is not None:
            result['CroppingSuggestionModifyTime'] = self.cropping_suggestion_modify_time
        if self.image_format is not None:
            result['ImageFormat'] = self.image_format
        if self.image_width is not None:
            result['ImageWidth'] = self.image_width
        if self.remarks_array_b is not None:
            result['RemarksArrayB'] = self.remarks_array_b
        if self.orientation is not None:
            result['Orientation'] = self.orientation
        if self.remarks_d is not None:
            result['RemarksD'] = self.remarks_d
        if self.tags_status is not None:
            result['TagsStatus'] = self.tags_status
        if self.cropping_suggestion_fail_reason is not None:
            result['CroppingSuggestionFailReason'] = self.cropping_suggestion_fail_reason
        if self.remarks_a is not None:
            result['RemarksA'] = self.remarks_a
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        if self.tags_modify_time is not None:
            result['TagsModifyTime'] = self.tags_modify_time
        if self.ocrstatus is not None:
            result['OCRStatus'] = self.ocrstatus
        if self.address_status is not None:
            result['AddressStatus'] = self.address_status
        if self.exif is not None:
            result['Exif'] = self.exif
        if self.location is not None:
            result['Location'] = self.location
        if self.remarks_b is not None:
            result['RemarksB'] = self.remarks_b
        result['CroppingSuggestion'] = []
        if self.cropping_suggestion is not None:
            for k in self.cropping_suggestion:
                result['CroppingSuggestion'].append(k.to_map() if k else None)
        result['Faces'] = []
        if self.faces is not None:
            for k in self.faces:
                result['Faces'].append(k.to_map() if k else None)
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        result['OCR'] = []
        if self.ocr is not None:
            for k in self.ocr:
                result['OCR'].append(k.to_map() if k else None)
        if self.image_quality is not None:
            result['ImageQuality'] = self.image_quality.to_map()
        if self.address is not None:
            result['Address'] = self.address.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CroppingSuggestionStatus') is not None:
            self.cropping_suggestion_status = m.get('CroppingSuggestionStatus')
        if m.get('ImageQualityModifyTime') is not None:
            self.image_quality_modify_time = m.get('ImageQualityModifyTime')
        if m.get('TagsFailReason') is not None:
            self.tags_fail_reason = m.get('TagsFailReason')
        if m.get('RemarksC') is not None:
            self.remarks_c = m.get('RemarksC')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('FacesFailReason') is not None:
            self.faces_fail_reason = m.get('FacesFailReason')
        if m.get('FacesModifyTime') is not None:
            self.faces_modify_time = m.get('FacesModifyTime')
        if m.get('ImageTime') is not None:
            self.image_time = m.get('ImageTime')
        if m.get('OCRModifyTime') is not None:
            self.ocrmodify_time = m.get('OCRModifyTime')
        if m.get('AddressModifyTime') is not None:
            self.address_modify_time = m.get('AddressModifyTime')
        if m.get('ImageQualityFailReason') is not None:
            self.image_quality_fail_reason = m.get('ImageQualityFailReason')
        if m.get('FacesStatus') is not None:
            self.faces_status = m.get('FacesStatus')
        if m.get('RemarksArrayA') is not None:
            self.remarks_array_a = m.get('RemarksArrayA')
        if m.get('ImageHeight') is not None:
            self.image_height = m.get('ImageHeight')
        if m.get('ExternalId') is not None:
            self.external_id = m.get('ExternalId')
        if m.get('SourceUri') is not None:
            self.source_uri = m.get('SourceUri')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('SourcePosition') is not None:
            self.source_position = m.get('SourcePosition')
        if m.get('ImageQualityStatus') is not None:
            self.image_quality_status = m.get('ImageQualityStatus')
        if m.get('OCRFailReason') is not None:
            self.ocrfail_reason = m.get('OCRFailReason')
        if m.get('AddressFailReason') is not None:
            self.address_fail_reason = m.get('AddressFailReason')
        if m.get('CroppingSuggestionModifyTime') is not None:
            self.cropping_suggestion_modify_time = m.get('CroppingSuggestionModifyTime')
        if m.get('ImageFormat') is not None:
            self.image_format = m.get('ImageFormat')
        if m.get('ImageWidth') is not None:
            self.image_width = m.get('ImageWidth')
        if m.get('RemarksArrayB') is not None:
            self.remarks_array_b = m.get('RemarksArrayB')
        if m.get('Orientation') is not None:
            self.orientation = m.get('Orientation')
        if m.get('RemarksD') is not None:
            self.remarks_d = m.get('RemarksD')
        if m.get('TagsStatus') is not None:
            self.tags_status = m.get('TagsStatus')
        if m.get('CroppingSuggestionFailReason') is not None:
            self.cropping_suggestion_fail_reason = m.get('CroppingSuggestionFailReason')
        if m.get('RemarksA') is not None:
            self.remarks_a = m.get('RemarksA')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        if m.get('TagsModifyTime') is not None:
            self.tags_modify_time = m.get('TagsModifyTime')
        if m.get('OCRStatus') is not None:
            self.ocrstatus = m.get('OCRStatus')
        if m.get('AddressStatus') is not None:
            self.address_status = m.get('AddressStatus')
        if m.get('Exif') is not None:
            self.exif = m.get('Exif')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('RemarksB') is not None:
            self.remarks_b = m.get('RemarksB')
        self.cropping_suggestion = []
        if m.get('CroppingSuggestion') is not None:
            for k in m.get('CroppingSuggestion'):
                temp_model = ListImagesResponseBodyImagesCroppingSuggestion()
                self.cropping_suggestion.append(temp_model.from_map(k))
        self.faces = []
        if m.get('Faces') is not None:
            for k in m.get('Faces'):
                temp_model = ListImagesResponseBodyImagesFaces()
                self.faces.append(temp_model.from_map(k))
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListImagesResponseBodyImagesTags()
                self.tags.append(temp_model.from_map(k))
        self.ocr = []
        if m.get('OCR') is not None:
            for k in m.get('OCR'):
                temp_model = ListImagesResponseBodyImagesOCR()
                self.ocr.append(temp_model.from_map(k))
        if m.get('ImageQuality') is not None:
            temp_model = ListImagesResponseBodyImagesImageQuality()
            self.image_quality = temp_model.from_map(m['ImageQuality'])
        if m.get('Address') is not None:
            temp_model = ListImagesResponseBodyImagesAddress()
            self.address = temp_model.from_map(m['Address'])
        return self


class ListImagesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        next_marker: str = None,
        set_id: str = None,
        images: List[ListImagesResponseBodyImages] = None,
    ):
        self.request_id = request_id
        self.next_marker = next_marker
        self.set_id = set_id
        self.images = images

    def validate(self):
        if self.images:
            for k in self.images:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_marker is not None:
            result['NextMarker'] = self.next_marker
        if self.set_id is not None:
            result['SetId'] = self.set_id
        result['Images'] = []
        if self.images is not None:
            for k in self.images:
                result['Images'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NextMarker') is not None:
            self.next_marker = m.get('NextMarker')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        self.images = []
        if m.get('Images') is not None:
            for k in m.get('Images'):
                temp_model = ListImagesResponseBodyImages()
                self.images.append(temp_model.from_map(k))
        return self


class ListImagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListImagesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListImagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOfficeConversionTaskRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        marker: str = None,
        max_keys: int = None,
    ):
        self.project = project
        self.marker = marker
        self.max_keys = max_keys

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.max_keys is not None:
            result['MaxKeys'] = self.max_keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('MaxKeys') is not None:
            self.max_keys = m.get('MaxKeys')
        return self


class ListOfficeConversionTaskResponseBodyTasks(TeaModel):
    def __init__(
        self,
        status: str = None,
        percent: int = None,
        finish_time: str = None,
        create_time: str = None,
        page_count: int = None,
        notify_topic_name: str = None,
        notify_endpoint: str = None,
        src_uri: str = None,
        tgt_type: str = None,
        tgt_uri: str = None,
        image_spec: str = None,
        external_id: str = None,
        task_id: str = None,
    ):
        self.status = status
        self.percent = percent
        self.finish_time = finish_time
        self.create_time = create_time
        self.page_count = page_count
        self.notify_topic_name = notify_topic_name
        self.notify_endpoint = notify_endpoint
        self.src_uri = src_uri
        self.tgt_type = tgt_type
        self.tgt_uri = tgt_uri
        self.image_spec = image_spec
        self.external_id = external_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.percent is not None:
            result['Percent'] = self.percent
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        if self.src_uri is not None:
            result['SrcUri'] = self.src_uri
        if self.tgt_type is not None:
            result['TgtType'] = self.tgt_type
        if self.tgt_uri is not None:
            result['TgtUri'] = self.tgt_uri
        if self.image_spec is not None:
            result['ImageSpec'] = self.image_spec
        if self.external_id is not None:
            result['ExternalID'] = self.external_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Percent') is not None:
            self.percent = m.get('Percent')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        if m.get('SrcUri') is not None:
            self.src_uri = m.get('SrcUri')
        if m.get('TgtType') is not None:
            self.tgt_type = m.get('TgtType')
        if m.get('TgtUri') is not None:
            self.tgt_uri = m.get('TgtUri')
        if m.get('ImageSpec') is not None:
            self.image_spec = m.get('ImageSpec')
        if m.get('ExternalID') is not None:
            self.external_id = m.get('ExternalID')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ListOfficeConversionTaskResponseBody(TeaModel):
    def __init__(
        self,
        next_marker: str = None,
        request_id: str = None,
        tasks: List[ListOfficeConversionTaskResponseBodyTasks] = None,
    ):
        self.next_marker = next_marker
        self.request_id = request_id
        self.tasks = tasks

    def validate(self):
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_marker is not None:
            result['NextMarker'] = self.next_marker
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextMarker') is not None:
            self.next_marker = m.get('NextMarker')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = ListOfficeConversionTaskResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k))
        return self


class ListOfficeConversionTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListOfficeConversionTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListOfficeConversionTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProjectAPIsRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
    ):
        self.project = project

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        return self


class ListProjectAPIsResponseBody(TeaModel):
    def __init__(
        self,
        project: str = None,
        request_id: str = None,
        apis: List[str] = None,
    ):
        self.project = project
        self.request_id = request_id
        self.apis = apis

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.apis is not None:
            result['APIs'] = self.apis
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('APIs') is not None:
            self.apis = m.get('APIs')
        return self


class ListProjectAPIsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListProjectAPIsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListProjectAPIsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProjectsRequest(TeaModel):
    def __init__(
        self,
        marker: str = None,
        max_keys: int = None,
    ):
        self.marker = marker
        self.max_keys = max_keys

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.max_keys is not None:
            result['MaxKeys'] = self.max_keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('MaxKeys') is not None:
            self.max_keys = m.get('MaxKeys')
        return self


class ListProjectsResponseBodyProjects(TeaModel):
    def __init__(
        self,
        type: str = None,
        cu: int = None,
        create_time: str = None,
        service_role: str = None,
        endpoint: str = None,
        project: str = None,
        region_id: str = None,
        billing_type: str = None,
        modify_time: str = None,
    ):
        self.type = type
        self.cu = cu
        self.create_time = create_time
        self.service_role = service_role
        self.endpoint = endpoint
        self.project = project
        self.region_id = region_id
        self.billing_type = billing_type
        self.modify_time = modify_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.cu is not None:
            result['CU'] = self.cu
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.service_role is not None:
            result['ServiceRole'] = self.service_role
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.project is not None:
            result['Project'] = self.project
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.billing_type is not None:
            result['BillingType'] = self.billing_type
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('CU') is not None:
            self.cu = m.get('CU')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ServiceRole') is not None:
            self.service_role = m.get('ServiceRole')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('BillingType') is not None:
            self.billing_type = m.get('BillingType')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        return self


class ListProjectsResponseBody(TeaModel):
    def __init__(
        self,
        next_marker: str = None,
        request_id: str = None,
        projects: List[ListProjectsResponseBodyProjects] = None,
    ):
        self.next_marker = next_marker
        self.request_id = request_id
        self.projects = projects

    def validate(self):
        if self.projects:
            for k in self.projects:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_marker is not None:
            result['NextMarker'] = self.next_marker
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Projects'] = []
        if self.projects is not None:
            for k in self.projects:
                result['Projects'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextMarker') is not None:
            self.next_marker = m.get('NextMarker')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.projects = []
        if m.get('Projects') is not None:
            for k in m.get('Projects'):
                temp_model = ListProjectsResponseBodyProjects()
                self.projects.append(temp_model.from_map(k))
        return self


class ListProjectsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListProjectsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListProjectsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSetsRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        marker: str = None,
    ):
        self.project = project
        self.marker = marker

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.marker is not None:
            result['Marker'] = self.marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        return self


class ListSetsResponseBodySets(TeaModel):
    def __init__(
        self,
        video_count: int = None,
        create_time: str = None,
        video_length: int = None,
        set_id: str = None,
        image_count: int = None,
        face_count: int = None,
        set_name: str = None,
        modify_time: str = None,
    ):
        self.video_count = video_count
        self.create_time = create_time
        self.video_length = video_length
        self.set_id = set_id
        self.image_count = image_count
        self.face_count = face_count
        self.set_name = set_name
        self.modify_time = modify_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_count is not None:
            result['VideoCount'] = self.video_count
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.video_length is not None:
            result['VideoLength'] = self.video_length
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.image_count is not None:
            result['ImageCount'] = self.image_count
        if self.face_count is not None:
            result['FaceCount'] = self.face_count
        if self.set_name is not None:
            result['SetName'] = self.set_name
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoCount') is not None:
            self.video_count = m.get('VideoCount')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('VideoLength') is not None:
            self.video_length = m.get('VideoLength')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('ImageCount') is not None:
            self.image_count = m.get('ImageCount')
        if m.get('FaceCount') is not None:
            self.face_count = m.get('FaceCount')
        if m.get('SetName') is not None:
            self.set_name = m.get('SetName')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        return self


class ListSetsResponseBody(TeaModel):
    def __init__(
        self,
        next_marker: str = None,
        request_id: str = None,
        sets: List[ListSetsResponseBodySets] = None,
    ):
        self.next_marker = next_marker
        self.request_id = request_id
        self.sets = sets

    def validate(self):
        if self.sets:
            for k in self.sets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_marker is not None:
            result['NextMarker'] = self.next_marker
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Sets'] = []
        if self.sets is not None:
            for k in self.sets:
                result['Sets'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextMarker') is not None:
            self.next_marker = m.get('NextMarker')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.sets = []
        if m.get('Sets') is not None:
            for k in m.get('Sets'):
                temp_model = ListSetsResponseBodySets()
                self.sets.append(temp_model.from_map(k))
        return self


class ListSetsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSetsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListSetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSetTagsRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        set_id: str = None,
    ):
        self.project = project
        self.set_id = set_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.set_id is not None:
            result['SetId'] = self.set_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        return self


class ListSetTagsResponseBodyTags(TeaModel):
    def __init__(
        self,
        tag_level: int = None,
        tag_name: str = None,
        tag_count: int = None,
    ):
        self.tag_level = tag_level
        self.tag_name = tag_name
        self.tag_count = tag_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_level is not None:
            result['TagLevel'] = self.tag_level
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        if self.tag_count is not None:
            result['TagCount'] = self.tag_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagLevel') is not None:
            self.tag_level = m.get('TagLevel')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        if m.get('TagCount') is not None:
            self.tag_count = m.get('TagCount')
        return self


class ListSetTagsResponseBody(TeaModel):
    def __init__(
        self,
        set_id: str = None,
        request_id: str = None,
        tags: List[ListSetTagsResponseBodyTags] = None,
    ):
        self.set_id = set_id
        self.request_id = request_id
        self.tags = tags

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListSetTagsResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListSetTagsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSetTagsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListSetTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVideoAudiosRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        set_id: str = None,
        video_uri: str = None,
        marker: str = None,
    ):
        self.project = project
        self.set_id = set_id
        self.video_uri = video_uri
        self.marker = marker

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.video_uri is not None:
            result['VideoUri'] = self.video_uri
        if self.marker is not None:
            result['Marker'] = self.marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('VideoUri') is not None:
            self.video_uri = m.get('VideoUri')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        return self


class ListVideoAudiosResponseBodyAudiosAudioTexts(TeaModel):
    def __init__(
        self,
        end_time: float = None,
        library: str = None,
        confidence: float = None,
        begin_time: float = None,
        channel_id: int = None,
        emotion_value: float = None,
        speech_rate: int = None,
        text: str = None,
        person: str = None,
        silence_duration: float = None,
    ):
        self.end_time = end_time
        self.library = library
        self.confidence = confidence
        self.begin_time = begin_time
        self.channel_id = channel_id
        self.emotion_value = emotion_value
        self.speech_rate = speech_rate
        self.text = text
        self.person = person
        self.silence_duration = silence_duration

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.library is not None:
            result['Library'] = self.library
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.emotion_value is not None:
            result['EmotionValue'] = self.emotion_value
        if self.speech_rate is not None:
            result['SpeechRate'] = self.speech_rate
        if self.text is not None:
            result['Text'] = self.text
        if self.person is not None:
            result['Person'] = self.person
        if self.silence_duration is not None:
            result['SilenceDuration'] = self.silence_duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Library') is not None:
            self.library = m.get('Library')
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('EmotionValue') is not None:
            self.emotion_value = m.get('EmotionValue')
        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Person') is not None:
            self.person = m.get('Person')
        if m.get('SilenceDuration') is not None:
            self.silence_duration = m.get('SilenceDuration')
        return self


class ListVideoAudiosResponseBodyAudios(TeaModel):
    def __init__(
        self,
        source_position: str = None,
        remarks_c: str = None,
        create_time: str = None,
        source_type: str = None,
        audio_duration: float = None,
        audio_texts_status: str = None,
        audio_format: str = None,
        remarks_d: str = None,
        process_fail_reason: str = None,
        process_modify_time: str = None,
        audio_rate: int = None,
        audio_uri: str = None,
        audio_texts_modify_time: str = None,
        remarks_a: str = None,
        external_id: str = None,
        source_uri: str = None,
        process_status: str = None,
        audio_texts_fail_reason: str = None,
        remarks_b: str = None,
        file_size: int = None,
        modify_time: str = None,
        audio_texts: List[ListVideoAudiosResponseBodyAudiosAudioTexts] = None,
    ):
        self.source_position = source_position
        self.remarks_c = remarks_c
        self.create_time = create_time
        self.source_type = source_type
        self.audio_duration = audio_duration
        self.audio_texts_status = audio_texts_status
        self.audio_format = audio_format
        self.remarks_d = remarks_d
        self.process_fail_reason = process_fail_reason
        self.process_modify_time = process_modify_time
        self.audio_rate = audio_rate
        self.audio_uri = audio_uri
        self.audio_texts_modify_time = audio_texts_modify_time
        self.remarks_a = remarks_a
        self.external_id = external_id
        self.source_uri = source_uri
        self.process_status = process_status
        self.audio_texts_fail_reason = audio_texts_fail_reason
        self.remarks_b = remarks_b
        self.file_size = file_size
        self.modify_time = modify_time
        self.audio_texts = audio_texts

    def validate(self):
        if self.audio_texts:
            for k in self.audio_texts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_position is not None:
            result['SourcePosition'] = self.source_position
        if self.remarks_c is not None:
            result['RemarksC'] = self.remarks_c
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.audio_duration is not None:
            result['AudioDuration'] = self.audio_duration
        if self.audio_texts_status is not None:
            result['AudioTextsStatus'] = self.audio_texts_status
        if self.audio_format is not None:
            result['AudioFormat'] = self.audio_format
        if self.remarks_d is not None:
            result['RemarksD'] = self.remarks_d
        if self.process_fail_reason is not None:
            result['ProcessFailReason'] = self.process_fail_reason
        if self.process_modify_time is not None:
            result['ProcessModifyTime'] = self.process_modify_time
        if self.audio_rate is not None:
            result['AudioRate'] = self.audio_rate
        if self.audio_uri is not None:
            result['AudioUri'] = self.audio_uri
        if self.audio_texts_modify_time is not None:
            result['AudioTextsModifyTime'] = self.audio_texts_modify_time
        if self.remarks_a is not None:
            result['RemarksA'] = self.remarks_a
        if self.external_id is not None:
            result['ExternalId'] = self.external_id
        if self.source_uri is not None:
            result['SourceUri'] = self.source_uri
        if self.process_status is not None:
            result['ProcessStatus'] = self.process_status
        if self.audio_texts_fail_reason is not None:
            result['AudioTextsFailReason'] = self.audio_texts_fail_reason
        if self.remarks_b is not None:
            result['RemarksB'] = self.remarks_b
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        result['AudioTexts'] = []
        if self.audio_texts is not None:
            for k in self.audio_texts:
                result['AudioTexts'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourcePosition') is not None:
            self.source_position = m.get('SourcePosition')
        if m.get('RemarksC') is not None:
            self.remarks_c = m.get('RemarksC')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('AudioDuration') is not None:
            self.audio_duration = m.get('AudioDuration')
        if m.get('AudioTextsStatus') is not None:
            self.audio_texts_status = m.get('AudioTextsStatus')
        if m.get('AudioFormat') is not None:
            self.audio_format = m.get('AudioFormat')
        if m.get('RemarksD') is not None:
            self.remarks_d = m.get('RemarksD')
        if m.get('ProcessFailReason') is not None:
            self.process_fail_reason = m.get('ProcessFailReason')
        if m.get('ProcessModifyTime') is not None:
            self.process_modify_time = m.get('ProcessModifyTime')
        if m.get('AudioRate') is not None:
            self.audio_rate = m.get('AudioRate')
        if m.get('AudioUri') is not None:
            self.audio_uri = m.get('AudioUri')
        if m.get('AudioTextsModifyTime') is not None:
            self.audio_texts_modify_time = m.get('AudioTextsModifyTime')
        if m.get('RemarksA') is not None:
            self.remarks_a = m.get('RemarksA')
        if m.get('ExternalId') is not None:
            self.external_id = m.get('ExternalId')
        if m.get('SourceUri') is not None:
            self.source_uri = m.get('SourceUri')
        if m.get('ProcessStatus') is not None:
            self.process_status = m.get('ProcessStatus')
        if m.get('AudioTextsFailReason') is not None:
            self.audio_texts_fail_reason = m.get('AudioTextsFailReason')
        if m.get('RemarksB') is not None:
            self.remarks_b = m.get('RemarksB')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        self.audio_texts = []
        if m.get('AudioTexts') is not None:
            for k in m.get('AudioTexts'):
                temp_model = ListVideoAudiosResponseBodyAudiosAudioTexts()
                self.audio_texts.append(temp_model.from_map(k))
        return self


class ListVideoAudiosResponseBody(TeaModel):
    def __init__(
        self,
        video_uri: str = None,
        request_id: str = None,
        next_marker: str = None,
        set_id: str = None,
        audios: List[ListVideoAudiosResponseBodyAudios] = None,
    ):
        self.video_uri = video_uri
        self.request_id = request_id
        self.next_marker = next_marker
        self.set_id = set_id
        self.audios = audios

    def validate(self):
        if self.audios:
            for k in self.audios:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_uri is not None:
            result['VideoUri'] = self.video_uri
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_marker is not None:
            result['NextMarker'] = self.next_marker
        if self.set_id is not None:
            result['SetId'] = self.set_id
        result['Audios'] = []
        if self.audios is not None:
            for k in self.audios:
                result['Audios'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoUri') is not None:
            self.video_uri = m.get('VideoUri')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NextMarker') is not None:
            self.next_marker = m.get('NextMarker')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        self.audios = []
        if m.get('Audios') is not None:
            for k in m.get('Audios'):
                temp_model = ListVideoAudiosResponseBodyAudios()
                self.audios.append(temp_model.from_map(k))
        return self


class ListVideoAudiosResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListVideoAudiosResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListVideoAudiosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVideoFramesRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        set_id: str = None,
        video_uri: str = None,
        marker: str = None,
    ):
        self.project = project
        self.set_id = set_id
        self.video_uri = video_uri
        self.marker = marker

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.video_uri is not None:
            result['VideoUri'] = self.video_uri
        if self.marker is not None:
            result['Marker'] = self.marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('VideoUri') is not None:
            self.video_uri = m.get('VideoUri')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        return self


class ListVideoFramesResponseBodyFramesFacesEmotionDetails(TeaModel):
    def __init__(
        self,
        happy: float = None,
        surprised: float = None,
        calm: float = None,
        disgusted: float = None,
        angry: float = None,
        sad: float = None,
        scared: float = None,
    ):
        self.happy = happy
        self.surprised = surprised
        self.calm = calm
        self.disgusted = disgusted
        self.angry = angry
        self.sad = sad
        self.scared = scared

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.happy is not None:
            result['HAPPY'] = self.happy
        if self.surprised is not None:
            result['SURPRISED'] = self.surprised
        if self.calm is not None:
            result['CALM'] = self.calm
        if self.disgusted is not None:
            result['DISGUSTED'] = self.disgusted
        if self.angry is not None:
            result['ANGRY'] = self.angry
        if self.sad is not None:
            result['SAD'] = self.sad
        if self.scared is not None:
            result['SCARED'] = self.scared
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HAPPY') is not None:
            self.happy = m.get('HAPPY')
        if m.get('SURPRISED') is not None:
            self.surprised = m.get('SURPRISED')
        if m.get('CALM') is not None:
            self.calm = m.get('CALM')
        if m.get('DISGUSTED') is not None:
            self.disgusted = m.get('DISGUSTED')
        if m.get('ANGRY') is not None:
            self.angry = m.get('ANGRY')
        if m.get('SAD') is not None:
            self.sad = m.get('SAD')
        if m.get('SCARED') is not None:
            self.scared = m.get('SCARED')
        return self


class ListVideoFramesResponseBodyFramesFacesFaceAttributesFaceBoundary(TeaModel):
    def __init__(
        self,
        left: int = None,
        top: int = None,
        width: int = None,
        height: int = None,
    ):
        self.left = left
        self.top = top
        self.width = width
        self.height = height

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class ListVideoFramesResponseBodyFramesFacesFaceAttributesHeadPose(TeaModel):
    def __init__(
        self,
        pitch: float = None,
        roll: float = None,
        yaw: float = None,
    ):
        self.pitch = pitch
        self.roll = roll
        self.yaw = yaw

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pitch is not None:
            result['Pitch'] = self.pitch
        if self.roll is not None:
            result['Roll'] = self.roll
        if self.yaw is not None:
            result['Yaw'] = self.yaw
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pitch') is not None:
            self.pitch = m.get('Pitch')
        if m.get('Roll') is not None:
            self.roll = m.get('Roll')
        if m.get('Yaw') is not None:
            self.yaw = m.get('Yaw')
        return self


class ListVideoFramesResponseBodyFramesFacesFaceAttributes(TeaModel):
    def __init__(
        self,
        glasses_confidence: float = None,
        glasses: str = None,
        mask: str = None,
        beard_confidence: float = None,
        mask_confidence: float = None,
        beard: str = None,
        face_boundary: ListVideoFramesResponseBodyFramesFacesFaceAttributesFaceBoundary = None,
        head_pose: ListVideoFramesResponseBodyFramesFacesFaceAttributesHeadPose = None,
    ):
        self.glasses_confidence = glasses_confidence
        self.glasses = glasses
        self.mask = mask
        self.beard_confidence = beard_confidence
        self.mask_confidence = mask_confidence
        self.beard = beard
        self.face_boundary = face_boundary
        self.head_pose = head_pose

    def validate(self):
        if self.face_boundary:
            self.face_boundary.validate()
        if self.head_pose:
            self.head_pose.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.glasses_confidence is not None:
            result['GlassesConfidence'] = self.glasses_confidence
        if self.glasses is not None:
            result['Glasses'] = self.glasses
        if self.mask is not None:
            result['Mask'] = self.mask
        if self.beard_confidence is not None:
            result['BeardConfidence'] = self.beard_confidence
        if self.mask_confidence is not None:
            result['MaskConfidence'] = self.mask_confidence
        if self.beard is not None:
            result['Beard'] = self.beard
        if self.face_boundary is not None:
            result['FaceBoundary'] = self.face_boundary.to_map()
        if self.head_pose is not None:
            result['HeadPose'] = self.head_pose.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GlassesConfidence') is not None:
            self.glasses_confidence = m.get('GlassesConfidence')
        if m.get('Glasses') is not None:
            self.glasses = m.get('Glasses')
        if m.get('Mask') is not None:
            self.mask = m.get('Mask')
        if m.get('BeardConfidence') is not None:
            self.beard_confidence = m.get('BeardConfidence')
        if m.get('MaskConfidence') is not None:
            self.mask_confidence = m.get('MaskConfidence')
        if m.get('Beard') is not None:
            self.beard = m.get('Beard')
        if m.get('FaceBoundary') is not None:
            temp_model = ListVideoFramesResponseBodyFramesFacesFaceAttributesFaceBoundary()
            self.face_boundary = temp_model.from_map(m['FaceBoundary'])
        if m.get('HeadPose') is not None:
            temp_model = ListVideoFramesResponseBodyFramesFacesFaceAttributesHeadPose()
            self.head_pose = temp_model.from_map(m['HeadPose'])
        return self


class ListVideoFramesResponseBodyFramesFaces(TeaModel):
    def __init__(
        self,
        emotion_confidence: float = None,
        attractive: float = None,
        group_id: str = None,
        gender: str = None,
        face_id: str = None,
        gender_confidence: float = None,
        face_quality: float = None,
        emotion: str = None,
        age: int = None,
        face_confidence: float = None,
        emotion_details: ListVideoFramesResponseBodyFramesFacesEmotionDetails = None,
        face_attributes: ListVideoFramesResponseBodyFramesFacesFaceAttributes = None,
    ):
        self.emotion_confidence = emotion_confidence
        self.attractive = attractive
        self.group_id = group_id
        self.gender = gender
        self.face_id = face_id
        self.gender_confidence = gender_confidence
        self.face_quality = face_quality
        self.emotion = emotion
        self.age = age
        self.face_confidence = face_confidence
        self.emotion_details = emotion_details
        self.face_attributes = face_attributes

    def validate(self):
        if self.emotion_details:
            self.emotion_details.validate()
        if self.face_attributes:
            self.face_attributes.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.emotion_confidence is not None:
            result['EmotionConfidence'] = self.emotion_confidence
        if self.attractive is not None:
            result['Attractive'] = self.attractive
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.face_id is not None:
            result['FaceId'] = self.face_id
        if self.gender_confidence is not None:
            result['GenderConfidence'] = self.gender_confidence
        if self.face_quality is not None:
            result['FaceQuality'] = self.face_quality
        if self.emotion is not None:
            result['Emotion'] = self.emotion
        if self.age is not None:
            result['Age'] = self.age
        if self.face_confidence is not None:
            result['FaceConfidence'] = self.face_confidence
        if self.emotion_details is not None:
            result['EmotionDetails'] = self.emotion_details.to_map()
        if self.face_attributes is not None:
            result['FaceAttributes'] = self.face_attributes.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EmotionConfidence') is not None:
            self.emotion_confidence = m.get('EmotionConfidence')
        if m.get('Attractive') is not None:
            self.attractive = m.get('Attractive')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('FaceId') is not None:
            self.face_id = m.get('FaceId')
        if m.get('GenderConfidence') is not None:
            self.gender_confidence = m.get('GenderConfidence')
        if m.get('FaceQuality') is not None:
            self.face_quality = m.get('FaceQuality')
        if m.get('Emotion') is not None:
            self.emotion = m.get('Emotion')
        if m.get('Age') is not None:
            self.age = m.get('Age')
        if m.get('FaceConfidence') is not None:
            self.face_confidence = m.get('FaceConfidence')
        if m.get('EmotionDetails') is not None:
            temp_model = ListVideoFramesResponseBodyFramesFacesEmotionDetails()
            self.emotion_details = temp_model.from_map(m['EmotionDetails'])
        if m.get('FaceAttributes') is not None:
            temp_model = ListVideoFramesResponseBodyFramesFacesFaceAttributes()
            self.face_attributes = temp_model.from_map(m['FaceAttributes'])
        return self


class ListVideoFramesResponseBodyFramesTags(TeaModel):
    def __init__(
        self,
        tag_level: int = None,
        parent_tag_name: str = None,
        tag_confidence: float = None,
        tag_name: str = None,
    ):
        self.tag_level = tag_level
        self.parent_tag_name = parent_tag_name
        self.tag_confidence = tag_confidence
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_level is not None:
            result['TagLevel'] = self.tag_level
        if self.parent_tag_name is not None:
            result['ParentTagName'] = self.parent_tag_name
        if self.tag_confidence is not None:
            result['TagConfidence'] = self.tag_confidence
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagLevel') is not None:
            self.tag_level = m.get('TagLevel')
        if m.get('ParentTagName') is not None:
            self.parent_tag_name = m.get('ParentTagName')
        if m.get('TagConfidence') is not None:
            self.tag_confidence = m.get('TagConfidence')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class ListVideoFramesResponseBodyFramesOCROCRBoundary(TeaModel):
    def __init__(
        self,
        left: int = None,
        top: int = None,
        width: int = None,
        height: int = None,
    ):
        self.left = left
        self.top = top
        self.width = width
        self.height = height

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        if self.height is not None:
            result['Height'] = self.height
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        return self


class ListVideoFramesResponseBodyFramesOCR(TeaModel):
    def __init__(
        self,
        ocrconfidence: float = None,
        ocrcontents: str = None,
        ocrboundary: ListVideoFramesResponseBodyFramesOCROCRBoundary = None,
    ):
        self.ocrconfidence = ocrconfidence
        self.ocrcontents = ocrcontents
        self.ocrboundary = ocrboundary

    def validate(self):
        if self.ocrboundary:
            self.ocrboundary.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ocrconfidence is not None:
            result['OCRConfidence'] = self.ocrconfidence
        if self.ocrcontents is not None:
            result['OCRContents'] = self.ocrcontents
        if self.ocrboundary is not None:
            result['OCRBoundary'] = self.ocrboundary.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OCRConfidence') is not None:
            self.ocrconfidence = m.get('OCRConfidence')
        if m.get('OCRContents') is not None:
            self.ocrcontents = m.get('OCRContents')
        if m.get('OCRBoundary') is not None:
            temp_model = ListVideoFramesResponseBodyFramesOCROCRBoundary()
            self.ocrboundary = temp_model.from_map(m['OCRBoundary'])
        return self


class ListVideoFramesResponseBodyFrames(TeaModel):
    def __init__(
        self,
        tags_fail_reason: str = None,
        remarks_c: str = None,
        create_time: str = None,
        source_type: str = None,
        faces_fail_reason: str = None,
        faces_modify_time: str = None,
        image_time: str = None,
        ocrmodify_time: str = None,
        faces_status: str = None,
        image_height: int = None,
        external_id: str = None,
        source_uri: str = None,
        modify_time: str = None,
        file_size: int = None,
        source_position: str = None,
        ocrfail_reason: str = None,
        image_format: str = None,
        image_width: int = None,
        orientation: str = None,
        remarks_d: str = None,
        tags_status: str = None,
        remarks_a: str = None,
        image_uri: str = None,
        tags_modify_time: str = None,
        ocrstatus: str = None,
        exif: str = None,
        location: str = None,
        remarks_b: str = None,
        faces: List[ListVideoFramesResponseBodyFramesFaces] = None,
        tags: List[ListVideoFramesResponseBodyFramesTags] = None,
        ocr: List[ListVideoFramesResponseBodyFramesOCR] = None,
    ):
        self.tags_fail_reason = tags_fail_reason
        self.remarks_c = remarks_c
        self.create_time = create_time
        self.source_type = source_type
        self.faces_fail_reason = faces_fail_reason
        self.faces_modify_time = faces_modify_time
        self.image_time = image_time
        self.ocrmodify_time = ocrmodify_time
        self.faces_status = faces_status
        self.image_height = image_height
        self.external_id = external_id
        self.source_uri = source_uri
        self.modify_time = modify_time
        self.file_size = file_size
        self.source_position = source_position
        self.ocrfail_reason = ocrfail_reason
        self.image_format = image_format
        self.image_width = image_width
        self.orientation = orientation
        self.remarks_d = remarks_d
        self.tags_status = tags_status
        self.remarks_a = remarks_a
        self.image_uri = image_uri
        self.tags_modify_time = tags_modify_time
        self.ocrstatus = ocrstatus
        self.exif = exif
        self.location = location
        self.remarks_b = remarks_b
        self.faces = faces
        self.tags = tags
        self.ocr = ocr

    def validate(self):
        if self.faces:
            for k in self.faces:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.ocr:
            for k in self.ocr:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tags_fail_reason is not None:
            result['TagsFailReason'] = self.tags_fail_reason
        if self.remarks_c is not None:
            result['RemarksC'] = self.remarks_c
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.faces_fail_reason is not None:
            result['FacesFailReason'] = self.faces_fail_reason
        if self.faces_modify_time is not None:
            result['FacesModifyTime'] = self.faces_modify_time
        if self.image_time is not None:
            result['ImageTime'] = self.image_time
        if self.ocrmodify_time is not None:
            result['OCRModifyTime'] = self.ocrmodify_time
        if self.faces_status is not None:
            result['FacesStatus'] = self.faces_status
        if self.image_height is not None:
            result['ImageHeight'] = self.image_height
        if self.external_id is not None:
            result['ExternalId'] = self.external_id
        if self.source_uri is not None:
            result['SourceUri'] = self.source_uri
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.source_position is not None:
            result['SourcePosition'] = self.source_position
        if self.ocrfail_reason is not None:
            result['OCRFailReason'] = self.ocrfail_reason
        if self.image_format is not None:
            result['ImageFormat'] = self.image_format
        if self.image_width is not None:
            result['ImageWidth'] = self.image_width
        if self.orientation is not None:
            result['Orientation'] = self.orientation
        if self.remarks_d is not None:
            result['RemarksD'] = self.remarks_d
        if self.tags_status is not None:
            result['TagsStatus'] = self.tags_status
        if self.remarks_a is not None:
            result['RemarksA'] = self.remarks_a
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        if self.tags_modify_time is not None:
            result['TagsModifyTime'] = self.tags_modify_time
        if self.ocrstatus is not None:
            result['OCRStatus'] = self.ocrstatus
        if self.exif is not None:
            result['Exif'] = self.exif
        if self.location is not None:
            result['Location'] = self.location
        if self.remarks_b is not None:
            result['RemarksB'] = self.remarks_b
        result['Faces'] = []
        if self.faces is not None:
            for k in self.faces:
                result['Faces'].append(k.to_map() if k else None)
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        result['OCR'] = []
        if self.ocr is not None:
            for k in self.ocr:
                result['OCR'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagsFailReason') is not None:
            self.tags_fail_reason = m.get('TagsFailReason')
        if m.get('RemarksC') is not None:
            self.remarks_c = m.get('RemarksC')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('FacesFailReason') is not None:
            self.faces_fail_reason = m.get('FacesFailReason')
        if m.get('FacesModifyTime') is not None:
            self.faces_modify_time = m.get('FacesModifyTime')
        if m.get('ImageTime') is not None:
            self.image_time = m.get('ImageTime')
        if m.get('OCRModifyTime') is not None:
            self.ocrmodify_time = m.get('OCRModifyTime')
        if m.get('FacesStatus') is not None:
            self.faces_status = m.get('FacesStatus')
        if m.get('ImageHeight') is not None:
            self.image_height = m.get('ImageHeight')
        if m.get('ExternalId') is not None:
            self.external_id = m.get('ExternalId')
        if m.get('SourceUri') is not None:
            self.source_uri = m.get('SourceUri')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('SourcePosition') is not None:
            self.source_position = m.get('SourcePosition')
        if m.get('OCRFailReason') is not None:
            self.ocrfail_reason = m.get('OCRFailReason')
        if m.get('ImageFormat') is not None:
            self.image_format = m.get('ImageFormat')
        if m.get('ImageWidth') is not None:
            self.image_width = m.get('ImageWidth')
        if m.get('Orientation') is not None:
            self.orientation = m.get('Orientation')
        if m.get('RemarksD') is not None:
            self.remarks_d = m.get('RemarksD')
        if m.get('TagsStatus') is not None:
            self.tags_status = m.get('TagsStatus')
        if m.get('RemarksA') is not None:
            self.remarks_a = m.get('RemarksA')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        if m.get('TagsModifyTime') is not None:
            self.tags_modify_time = m.get('TagsModifyTime')
        if m.get('OCRStatus') is not None:
            self.ocrstatus = m.get('OCRStatus')
        if m.get('Exif') is not None:
            self.exif = m.get('Exif')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('RemarksB') is not None:
            self.remarks_b = m.get('RemarksB')
        self.faces = []
        if m.get('Faces') is not None:
            for k in m.get('Faces'):
                temp_model = ListVideoFramesResponseBodyFramesFaces()
                self.faces.append(temp_model.from_map(k))
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListVideoFramesResponseBodyFramesTags()
                self.tags.append(temp_model.from_map(k))
        self.ocr = []
        if m.get('OCR') is not None:
            for k in m.get('OCR'):
                temp_model = ListVideoFramesResponseBodyFramesOCR()
                self.ocr.append(temp_model.from_map(k))
        return self


class ListVideoFramesResponseBody(TeaModel):
    def __init__(
        self,
        video_uri: str = None,
        request_id: str = None,
        next_marker: str = None,
        set_id: str = None,
        frames: List[ListVideoFramesResponseBodyFrames] = None,
    ):
        self.video_uri = video_uri
        self.request_id = request_id
        self.next_marker = next_marker
        self.set_id = set_id
        self.frames = frames

    def validate(self):
        if self.frames:
            for k in self.frames:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_uri is not None:
            result['VideoUri'] = self.video_uri
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_marker is not None:
            result['NextMarker'] = self.next_marker
        if self.set_id is not None:
            result['SetId'] = self.set_id
        result['Frames'] = []
        if self.frames is not None:
            for k in self.frames:
                result['Frames'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VideoUri') is not None:
            self.video_uri = m.get('VideoUri')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NextMarker') is not None:
            self.next_marker = m.get('NextMarker')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        self.frames = []
        if m.get('Frames') is not None:
            for k in m.get('Frames'):
                temp_model = ListVideoFramesResponseBodyFrames()
                self.frames.append(temp_model.from_map(k))
        return self


class ListVideoFramesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListVideoFramesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListVideoFramesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVideosRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        set_id: str = None,
        create_time_start: str = None,
        marker: str = None,
    ):
        self.project = project
        self.set_id = set_id
        self.create_time_start = create_time_start
        self.marker = marker

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.create_time_start is not None:
            result['CreateTimeStart'] = self.create_time_start
        if self.marker is not None:
            result['Marker'] = self.marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('CreateTimeStart') is not None:
            self.create_time_start = m.get('CreateTimeStart')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        return self


class ListVideosResponseBodyVideosVideoTags(TeaModel):
    def __init__(
        self,
        tag_level: int = None,
        parent_tag_name: str = None,
        tag_name: str = None,
        tag_confidence: float = None,
    ):
        self.tag_level = tag_level
        self.parent_tag_name = parent_tag_name
        self.tag_name = tag_name
        self.tag_confidence = tag_confidence

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_level is not None:
            result['TagLevel'] = self.tag_level
        if self.parent_tag_name is not None:
            result['ParentTagName'] = self.parent_tag_name
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        if self.tag_confidence is not None:
            result['TagConfidence'] = self.tag_confidence
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagLevel') is not None:
            self.tag_level = m.get('TagLevel')
        if m.get('ParentTagName') is not None:
            self.parent_tag_name = m.get('ParentTagName')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        if m.get('TagConfidence') is not None:
            self.tag_confidence = m.get('TagConfidence')
        return self


class ListVideosResponseBodyVideos(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        remarks_c: str = None,
        video_tags_fail_reason: str = None,
        source_type: str = None,
        video_duration: float = None,
        process_modify_time: str = None,
        video_frames: int = None,
        video_tags_status: str = None,
        external_id: str = None,
        source_uri: str = None,
        modify_time: str = None,
        file_size: int = None,
        source_position: str = None,
        video_width: int = None,
        video_height: int = None,
        video_format: str = None,
        remarks_d: str = None,
        video_uri: str = None,
        video_tags_modify_time: str = None,
        process_fail_reason: str = None,
        remarks_a: str = None,
        process_status: str = None,
        remarks_b: str = None,
        video_tags: List[ListVideosResponseBodyVideosVideoTags] = None,
    ):
        self.create_time = create_time
        self.remarks_c = remarks_c
        self.video_tags_fail_reason = video_tags_fail_reason
        self.source_type = source_type
        self.video_duration = video_duration
        self.process_modify_time = process_modify_time
        self.video_frames = video_frames
        self.video_tags_status = video_tags_status
        self.external_id = external_id
        self.source_uri = source_uri
        self.modify_time = modify_time
        self.file_size = file_size
        self.source_position = source_position
        self.video_width = video_width
        self.video_height = video_height
        self.video_format = video_format
        self.remarks_d = remarks_d
        self.video_uri = video_uri
        self.video_tags_modify_time = video_tags_modify_time
        self.process_fail_reason = process_fail_reason
        self.remarks_a = remarks_a
        self.process_status = process_status
        self.remarks_b = remarks_b
        self.video_tags = video_tags

    def validate(self):
        if self.video_tags:
            for k in self.video_tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.remarks_c is not None:
            result['RemarksC'] = self.remarks_c
        if self.video_tags_fail_reason is not None:
            result['VideoTagsFailReason'] = self.video_tags_fail_reason
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.video_duration is not None:
            result['VideoDuration'] = self.video_duration
        if self.process_modify_time is not None:
            result['ProcessModifyTime'] = self.process_modify_time
        if self.video_frames is not None:
            result['VideoFrames'] = self.video_frames
        if self.video_tags_status is not None:
            result['VideoTagsStatus'] = self.video_tags_status
        if self.external_id is not None:
            result['ExternalId'] = self.external_id
        if self.source_uri is not None:
            result['SourceUri'] = self.source_uri
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.source_position is not None:
            result['SourcePosition'] = self.source_position
        if self.video_width is not None:
            result['VideoWidth'] = self.video_width
        if self.video_height is not None:
            result['VideoHeight'] = self.video_height
        if self.video_format is not None:
            result['VideoFormat'] = self.video_format
        if self.remarks_d is not None:
            result['RemarksD'] = self.remarks_d
        if self.video_uri is not None:
            result['VideoUri'] = self.video_uri
        if self.video_tags_modify_time is not None:
            result['VideoTagsModifyTime'] = self.video_tags_modify_time
        if self.process_fail_reason is not None:
            result['ProcessFailReason'] = self.process_fail_reason
        if self.remarks_a is not None:
            result['RemarksA'] = self.remarks_a
        if self.process_status is not None:
            result['ProcessStatus'] = self.process_status
        if self.remarks_b is not None:
            result['RemarksB'] = self.remarks_b
        result['VideoTags'] = []
        if self.video_tags is not None:
            for k in self.video_tags:
                result['VideoTags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('RemarksC') is not None:
            self.remarks_c = m.get('RemarksC')
        if m.get('VideoTagsFailReason') is not None:
            self.video_tags_fail_reason = m.get('VideoTagsFailReason')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('VideoDuration') is not None:
            self.video_duration = m.get('VideoDuration')
        if m.get('ProcessModifyTime') is not None:
            self.process_modify_time = m.get('ProcessModifyTime')
        if m.get('VideoFrames') is not None:
            self.video_frames = m.get('VideoFrames')
        if m.get('VideoTagsStatus') is not None:
            self.video_tags_status = m.get('VideoTagsStatus')
        if m.get('ExternalId') is not None:
            self.external_id = m.get('ExternalId')
        if m.get('SourceUri') is not None:
            self.source_uri = m.get('SourceUri')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('SourcePosition') is not None:
            self.source_position = m.get('SourcePosition')
        if m.get('VideoWidth') is not None:
            self.video_width = m.get('VideoWidth')
        if m.get('VideoHeight') is not None:
            self.video_height = m.get('VideoHeight')
        if m.get('VideoFormat') is not None:
            self.video_format = m.get('VideoFormat')
        if m.get('RemarksD') is not None:
            self.remarks_d = m.get('RemarksD')
        if m.get('VideoUri') is not None:
            self.video_uri = m.get('VideoUri')
        if m.get('VideoTagsModifyTime') is not None:
            self.video_tags_modify_time = m.get('VideoTagsModifyTime')
        if m.get('ProcessFailReason') is not None:
            self.process_fail_reason = m.get('ProcessFailReason')
        if m.get('RemarksA') is not None:
            self.remarks_a = m.get('RemarksA')
        if m.get('ProcessStatus') is not None:
            self.process_status = m.get('ProcessStatus')
        if m.get('RemarksB') is not None:
            self.remarks_b = m.get('RemarksB')
        self.video_tags = []
        if m.get('VideoTags') is not None:
            for k in m.get('VideoTags'):
                temp_model = ListVideosResponseBodyVideosVideoTags()
                self.video_tags.append(temp_model.from_map(k))
        return self


class ListVideosResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        next_marker: str = None,
        set_id: str = None,
        videos: List[ListVideosResponseBodyVideos] = None,
    ):
        self.request_id = request_id
        self.next_marker = next_marker
        self.set_id = set_id
        self.videos = videos

    def validate(self):
        if self.videos:
            for k in self.videos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_marker is not None:
            result['NextMarker'] = self.next_marker
        if self.set_id is not None:
            result['SetId'] = self.set_id
        result['Videos'] = []
        if self.videos is not None:
            for k in self.videos:
                result['Videos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NextMarker') is not None:
            self.next_marker = m.get('NextMarker')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        self.videos = []
        if m.get('Videos') is not None:
            for k in m.get('Videos'):
                temp_model = ListVideosResponseBodyVideos()
                self.videos.append(temp_model.from_map(k))
        return self


class ListVideosResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListVideosResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListVideosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVideoTasksRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        marker: str = None,
        max_keys: int = None,
        task_type: str = None,
    ):
        self.project = project
        self.marker = marker
        self.max_keys = max_keys
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.max_keys is not None:
            result['MaxKeys'] = self.max_keys
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('MaxKeys') is not None:
            self.max_keys = m.get('MaxKeys')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class ListVideoTasksResponseBodyTasks(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        status: str = None,
        start_time: str = None,
        task_type: str = None,
        progress: int = None,
        notify_endpoint: str = None,
        error_message: str = None,
        parameters: str = None,
        result: str = None,
        task_id: str = None,
        notify_topic_name: str = None,
    ):
        self.end_time = end_time
        self.status = status
        self.start_time = start_time
        self.task_type = task_type
        self.progress = progress
        self.notify_endpoint = notify_endpoint
        self.error_message = error_message
        self.parameters = parameters
        self.result = result
        self.task_id = task_id
        self.notify_topic_name = notify_topic_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.status is not None:
            result['Status'] = self.status
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.notify_endpoint is not None:
            result['NotifyEndpoint'] = self.notify_endpoint
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.result is not None:
            result['Result'] = self.result
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.notify_topic_name is not None:
            result['NotifyTopicName'] = self.notify_topic_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('NotifyEndpoint') is not None:
            self.notify_endpoint = m.get('NotifyEndpoint')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('NotifyTopicName') is not None:
            self.notify_topic_name = m.get('NotifyTopicName')
        return self


class ListVideoTasksResponseBody(TeaModel):
    def __init__(
        self,
        next_marker: str = None,
        request_id: str = None,
        tasks: List[ListVideoTasksResponseBodyTasks] = None,
    ):
        self.next_marker = next_marker
        self.request_id = request_id
        self.tasks = tasks

    def validate(self):
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_marker is not None:
            result['NextMarker'] = self.next_marker
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextMarker') is not None:
            self.next_marker = m.get('NextMarker')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = ListVideoTasksResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k))
        return self


class ListVideoTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListVideoTasksResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListVideoTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenImmServiceRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
    ):
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class OpenImmServiceResponseBody(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        request_id: str = None,
    ):
        self.order_id = order_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OpenImmServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OpenImmServiceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OpenImmServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutProjectRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        service_role: str = None,
    ):
        self.project = project
        self.service_role = service_role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.service_role is not None:
            result['ServiceRole'] = self.service_role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('ServiceRole') is not None:
            self.service_role = m.get('ServiceRole')
        return self


class PutProjectResponseBody(TeaModel):
    def __init__(
        self,
        project: str = None,
        modify_time: str = None,
        type: str = None,
        cu: int = None,
        service_role: str = None,
        request_id: str = None,
        endpoint: str = None,
        create_time: str = None,
        region_id: str = None,
        billing_type: str = None,
    ):
        self.project = project
        self.modify_time = modify_time
        self.type = type
        self.cu = cu
        self.service_role = service_role
        self.request_id = request_id
        self.endpoint = endpoint
        self.create_time = create_time
        self.region_id = region_id
        self.billing_type = billing_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.type is not None:
            result['Type'] = self.type
        if self.cu is not None:
            result['CU'] = self.cu
        if self.service_role is not None:
            result['ServiceRole'] = self.service_role
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.billing_type is not None:
            result['BillingType'] = self.billing_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('CU') is not None:
            self.cu = m.get('CU')
        if m.get('ServiceRole') is not None:
            self.service_role = m.get('ServiceRole')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('BillingType') is not None:
            self.billing_type = m.get('BillingType')
        return self


class PutProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PutProjectResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = PutProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefreshOfficeEditTokenRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        access_token: str = None,
        refresh_token: str = None,
    ):
        self.project = project
        self.access_token = access_token
        self.refresh_token = refresh_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.refresh_token is not None:
            result['RefreshToken'] = self.refresh_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('RefreshToken') is not None:
            self.refresh_token = m.get('RefreshToken')
        return self


class RefreshOfficeEditTokenResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        access_token_expired_time: str = None,
        refresh_token: str = None,
        access_token: str = None,
        refresh_token_expired_time: str = None,
    ):
        self.request_id = request_id
        self.access_token_expired_time = access_token_expired_time
        self.refresh_token = refresh_token
        self.access_token = access_token
        self.refresh_token_expired_time = refresh_token_expired_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.access_token_expired_time is not None:
            result['AccessTokenExpiredTime'] = self.access_token_expired_time
        if self.refresh_token is not None:
            result['RefreshToken'] = self.refresh_token
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.refresh_token_expired_time is not None:
            result['RefreshTokenExpiredTime'] = self.refresh_token_expired_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AccessTokenExpiredTime') is not None:
            self.access_token_expired_time = m.get('AccessTokenExpiredTime')
        if m.get('RefreshToken') is not None:
            self.refresh_token = m.get('RefreshToken')
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('RefreshTokenExpiredTime') is not None:
            self.refresh_token_expired_time = m.get('RefreshTokenExpiredTime')
        return self


class RefreshOfficeEditTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RefreshOfficeEditTokenResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RefreshOfficeEditTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefreshOfficePreviewTokenRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        access_token: str = None,
        refresh_token: str = None,
    ):
        self.project = project
        self.access_token = access_token
        self.refresh_token = refresh_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.refresh_token is not None:
            result['RefreshToken'] = self.refresh_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('RefreshToken') is not None:
            self.refresh_token = m.get('RefreshToken')
        return self


class RefreshOfficePreviewTokenResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        access_token_expired_time: str = None,
        refresh_token: str = None,
        access_token: str = None,
        refresh_token_expired_time: str = None,
    ):
        self.request_id = request_id
        self.access_token_expired_time = access_token_expired_time
        self.refresh_token = refresh_token
        self.access_token = access_token
        self.refresh_token_expired_time = refresh_token_expired_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.access_token_expired_time is not None:
            result['AccessTokenExpiredTime'] = self.access_token_expired_time
        if self.refresh_token is not None:
            result['RefreshToken'] = self.refresh_token
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.refresh_token_expired_time is not None:
            result['RefreshTokenExpiredTime'] = self.refresh_token_expired_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AccessTokenExpiredTime') is not None:
            self.access_token_expired_time = m.get('AccessTokenExpiredTime')
        if m.get('RefreshToken') is not None:
            self.refresh_token = m.get('RefreshToken')
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('RefreshTokenExpiredTime') is not None:
            self.refresh_token_expired_time = m.get('RefreshTokenExpiredTime')
        return self


class RefreshOfficePreviewTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RefreshOfficePreviewTokenResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RefreshOfficePreviewTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefreshWebofficeTokenRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        access_token: str = None,
        refresh_token: str = None,
    ):
        self.project = project
        self.access_token = access_token
        self.refresh_token = refresh_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.refresh_token is not None:
            result['RefreshToken'] = self.refresh_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('RefreshToken') is not None:
            self.refresh_token = m.get('RefreshToken')
        return self


class RefreshWebofficeTokenResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        access_token_expired_time: str = None,
        refresh_token: str = None,
        access_token: str = None,
        refresh_token_expired_time: str = None,
    ):
        self.request_id = request_id
        self.access_token_expired_time = access_token_expired_time
        self.refresh_token = refresh_token
        self.access_token = access_token
        self.refresh_token_expired_time = refresh_token_expired_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.access_token_expired_time is not None:
            result['AccessTokenExpiredTime'] = self.access_token_expired_time
        if self.refresh_token is not None:
            result['RefreshToken'] = self.refresh_token
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.refresh_token_expired_time is not None:
            result['RefreshTokenExpiredTime'] = self.refresh_token_expired_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AccessTokenExpiredTime') is not None:
            self.access_token_expired_time = m.get('AccessTokenExpiredTime')
        if m.get('RefreshToken') is not None:
            self.refresh_token = m.get('RefreshToken')
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('RefreshTokenExpiredTime') is not None:
            self.refresh_token_expired_time = m.get('RefreshTokenExpiredTime')
        return self


class RefreshWebofficeTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RefreshWebofficeTokenResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RefreshWebofficeTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFaceGroupRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        set_id: str = None,
        group_id: str = None,
        group_name: str = None,
        group_cover_face_id: str = None,
        remarks_a: str = None,
        remarks_b: str = None,
        remarks_c: str = None,
        remarks_d: str = None,
        remarks_array_a: str = None,
        remarks_array_b: str = None,
        external_id: str = None,
        reset_items: str = None,
    ):
        self.project = project
        self.set_id = set_id
        self.group_id = group_id
        self.group_name = group_name
        self.group_cover_face_id = group_cover_face_id
        self.remarks_a = remarks_a
        self.remarks_b = remarks_b
        self.remarks_c = remarks_c
        self.remarks_d = remarks_d
        self.remarks_array_a = remarks_array_a
        self.remarks_array_b = remarks_array_b
        self.external_id = external_id
        self.reset_items = reset_items

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_cover_face_id is not None:
            result['GroupCoverFaceId'] = self.group_cover_face_id
        if self.remarks_a is not None:
            result['RemarksA'] = self.remarks_a
        if self.remarks_b is not None:
            result['RemarksB'] = self.remarks_b
        if self.remarks_c is not None:
            result['RemarksC'] = self.remarks_c
        if self.remarks_d is not None:
            result['RemarksD'] = self.remarks_d
        if self.remarks_array_a is not None:
            result['RemarksArrayA'] = self.remarks_array_a
        if self.remarks_array_b is not None:
            result['RemarksArrayB'] = self.remarks_array_b
        if self.external_id is not None:
            result['ExternalId'] = self.external_id
        if self.reset_items is not None:
            result['ResetItems'] = self.reset_items
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('GroupCoverFaceId') is not None:
            self.group_cover_face_id = m.get('GroupCoverFaceId')
        if m.get('RemarksA') is not None:
            self.remarks_a = m.get('RemarksA')
        if m.get('RemarksB') is not None:
            self.remarks_b = m.get('RemarksB')
        if m.get('RemarksC') is not None:
            self.remarks_c = m.get('RemarksC')
        if m.get('RemarksD') is not None:
            self.remarks_d = m.get('RemarksD')
        if m.get('RemarksArrayA') is not None:
            self.remarks_array_a = m.get('RemarksArrayA')
        if m.get('RemarksArrayB') is not None:
            self.remarks_array_b = m.get('RemarksArrayB')
        if m.get('ExternalId') is not None:
            self.external_id = m.get('ExternalId')
        if m.get('ResetItems') is not None:
            self.reset_items = m.get('ResetItems')
        return self


class UpdateFaceGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        group_id: str = None,
        set_id: str = None,
    ):
        self.request_id = request_id
        self.group_id = group_id
        self.set_id = set_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.set_id is not None:
            result['SetId'] = self.set_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        return self


class UpdateFaceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateFaceGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateFaceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateImageRequestFaces(TeaModel):
    def __init__(
        self,
        face_id: str = None,
        group_id: str = None,
    ):
        self.face_id = face_id
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_id is not None:
            result['FaceId'] = self.face_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceId') is not None:
            self.face_id = m.get('FaceId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class UpdateImageRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        set_id: str = None,
        image_uri: str = None,
        remarks_a: str = None,
        remarks_b: str = None,
        source_type: str = None,
        source_uri: str = None,
        source_position: str = None,
        remarks_c: str = None,
        remarks_d: str = None,
        external_id: str = None,
        remarks_array_a: str = None,
        remarks_array_b: str = None,
        faces: List[UpdateImageRequestFaces] = None,
    ):
        self.project = project
        self.set_id = set_id
        self.image_uri = image_uri
        self.remarks_a = remarks_a
        self.remarks_b = remarks_b
        self.source_type = source_type
        self.source_uri = source_uri
        self.source_position = source_position
        self.remarks_c = remarks_c
        self.remarks_d = remarks_d
        self.external_id = external_id
        self.remarks_array_a = remarks_array_a
        self.remarks_array_b = remarks_array_b
        self.faces = faces

    def validate(self):
        if self.faces:
            for k in self.faces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        if self.remarks_a is not None:
            result['RemarksA'] = self.remarks_a
        if self.remarks_b is not None:
            result['RemarksB'] = self.remarks_b
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.source_uri is not None:
            result['SourceUri'] = self.source_uri
        if self.source_position is not None:
            result['SourcePosition'] = self.source_position
        if self.remarks_c is not None:
            result['RemarksC'] = self.remarks_c
        if self.remarks_d is not None:
            result['RemarksD'] = self.remarks_d
        if self.external_id is not None:
            result['ExternalId'] = self.external_id
        if self.remarks_array_a is not None:
            result['RemarksArrayA'] = self.remarks_array_a
        if self.remarks_array_b is not None:
            result['RemarksArrayB'] = self.remarks_array_b
        result['Faces'] = []
        if self.faces is not None:
            for k in self.faces:
                result['Faces'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        if m.get('RemarksA') is not None:
            self.remarks_a = m.get('RemarksA')
        if m.get('RemarksB') is not None:
            self.remarks_b = m.get('RemarksB')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('SourceUri') is not None:
            self.source_uri = m.get('SourceUri')
        if m.get('SourcePosition') is not None:
            self.source_position = m.get('SourcePosition')
        if m.get('RemarksC') is not None:
            self.remarks_c = m.get('RemarksC')
        if m.get('RemarksD') is not None:
            self.remarks_d = m.get('RemarksD')
        if m.get('ExternalId') is not None:
            self.external_id = m.get('ExternalId')
        if m.get('RemarksArrayA') is not None:
            self.remarks_array_a = m.get('RemarksArrayA')
        if m.get('RemarksArrayB') is not None:
            self.remarks_array_b = m.get('RemarksArrayB')
        self.faces = []
        if m.get('Faces') is not None:
            for k in m.get('Faces'):
                temp_model = UpdateImageRequestFaces()
                self.faces.append(temp_model.from_map(k))
        return self


class UpdateImageShrinkRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        set_id: str = None,
        image_uri: str = None,
        remarks_a: str = None,
        remarks_b: str = None,
        source_type: str = None,
        source_uri: str = None,
        source_position: str = None,
        remarks_c: str = None,
        remarks_d: str = None,
        external_id: str = None,
        remarks_array_a: str = None,
        remarks_array_b: str = None,
        faces_shrink: str = None,
    ):
        self.project = project
        self.set_id = set_id
        self.image_uri = image_uri
        self.remarks_a = remarks_a
        self.remarks_b = remarks_b
        self.source_type = source_type
        self.source_uri = source_uri
        self.source_position = source_position
        self.remarks_c = remarks_c
        self.remarks_d = remarks_d
        self.external_id = external_id
        self.remarks_array_a = remarks_array_a
        self.remarks_array_b = remarks_array_b
        self.faces_shrink = faces_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        if self.remarks_a is not None:
            result['RemarksA'] = self.remarks_a
        if self.remarks_b is not None:
            result['RemarksB'] = self.remarks_b
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.source_uri is not None:
            result['SourceUri'] = self.source_uri
        if self.source_position is not None:
            result['SourcePosition'] = self.source_position
        if self.remarks_c is not None:
            result['RemarksC'] = self.remarks_c
        if self.remarks_d is not None:
            result['RemarksD'] = self.remarks_d
        if self.external_id is not None:
            result['ExternalId'] = self.external_id
        if self.remarks_array_a is not None:
            result['RemarksArrayA'] = self.remarks_array_a
        if self.remarks_array_b is not None:
            result['RemarksArrayB'] = self.remarks_array_b
        if self.faces_shrink is not None:
            result['Faces'] = self.faces_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        if m.get('RemarksA') is not None:
            self.remarks_a = m.get('RemarksA')
        if m.get('RemarksB') is not None:
            self.remarks_b = m.get('RemarksB')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('SourceUri') is not None:
            self.source_uri = m.get('SourceUri')
        if m.get('SourcePosition') is not None:
            self.source_position = m.get('SourcePosition')
        if m.get('RemarksC') is not None:
            self.remarks_c = m.get('RemarksC')
        if m.get('RemarksD') is not None:
            self.remarks_d = m.get('RemarksD')
        if m.get('ExternalId') is not None:
            self.external_id = m.get('ExternalId')
        if m.get('RemarksArrayA') is not None:
            self.remarks_array_a = m.get('RemarksArrayA')
        if m.get('RemarksArrayB') is not None:
            self.remarks_array_b = m.get('RemarksArrayB')
        if m.get('Faces') is not None:
            self.faces_shrink = m.get('Faces')
        return self


class UpdateImageResponseBody(TeaModel):
    def __init__(
        self,
        remarks_array_b: str = None,
        modify_time: str = None,
        remarks_c: str = None,
        remarks_d: str = None,
        request_id: str = None,
        create_time: str = None,
        external_id: str = None,
        remarks_array_a: str = None,
        remarks_a: str = None,
        image_uri: str = None,
        set_id: str = None,
        remarks_b: str = None,
    ):
        self.remarks_array_b = remarks_array_b
        self.modify_time = modify_time
        self.remarks_c = remarks_c
        self.remarks_d = remarks_d
        self.request_id = request_id
        self.create_time = create_time
        self.external_id = external_id
        self.remarks_array_a = remarks_array_a
        self.remarks_a = remarks_a
        self.image_uri = image_uri
        self.set_id = set_id
        self.remarks_b = remarks_b

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.remarks_array_b is not None:
            result['RemarksArrayB'] = self.remarks_array_b
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.remarks_c is not None:
            result['RemarksC'] = self.remarks_c
        if self.remarks_d is not None:
            result['RemarksD'] = self.remarks_d
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.external_id is not None:
            result['ExternalId'] = self.external_id
        if self.remarks_array_a is not None:
            result['RemarksArrayA'] = self.remarks_array_a
        if self.remarks_a is not None:
            result['RemarksA'] = self.remarks_a
        if self.image_uri is not None:
            result['ImageUri'] = self.image_uri
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.remarks_b is not None:
            result['RemarksB'] = self.remarks_b
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RemarksArrayB') is not None:
            self.remarks_array_b = m.get('RemarksArrayB')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('RemarksC') is not None:
            self.remarks_c = m.get('RemarksC')
        if m.get('RemarksD') is not None:
            self.remarks_d = m.get('RemarksD')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExternalId') is not None:
            self.external_id = m.get('ExternalId')
        if m.get('RemarksArrayA') is not None:
            self.remarks_array_a = m.get('RemarksArrayA')
        if m.get('RemarksA') is not None:
            self.remarks_a = m.get('RemarksA')
        if m.get('ImageUri') is not None:
            self.image_uri = m.get('ImageUri')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('RemarksB') is not None:
            self.remarks_b = m.get('RemarksB')
        return self


class UpdateImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateImageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProjectRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        new_cu: int = None,
        new_service_role: str = None,
    ):
        self.project = project
        self.new_cu = new_cu
        self.new_service_role = new_service_role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.new_cu is not None:
            result['NewCU'] = self.new_cu
        if self.new_service_role is not None:
            result['NewServiceRole'] = self.new_service_role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('NewCU') is not None:
            self.new_cu = m.get('NewCU')
        if m.get('NewServiceRole') is not None:
            self.new_service_role = m.get('NewServiceRole')
        return self


class UpdateProjectResponseBody(TeaModel):
    def __init__(
        self,
        type: str = None,
        request_id: str = None,
        cu: int = None,
        create_time: str = None,
        service_role: str = None,
        project: str = None,
        region_id: str = None,
        modify_time: str = None,
    ):
        self.type = type
        self.request_id = request_id
        self.cu = cu
        self.create_time = create_time
        self.service_role = service_role
        self.project = project
        self.region_id = region_id
        self.modify_time = modify_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.cu is not None:
            result['CU'] = self.cu
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.service_role is not None:
            result['ServiceRole'] = self.service_role
        if self.project is not None:
            result['Project'] = self.project
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CU') is not None:
            self.cu = m.get('CU')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ServiceRole') is not None:
            self.service_role = m.get('ServiceRole')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        return self


class UpdateProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateProjectResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSetRequest(TeaModel):
    def __init__(
        self,
        project: str = None,
        set_id: str = None,
        set_name: str = None,
    ):
        self.project = project
        self.set_id = set_id
        self.set_name = set_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project
        if self.set_id is not None:
            result['SetId'] = self.set_id
        if self.set_name is not None:
            result['SetName'] = self.set_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            self.project = m.get('Project')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        if m.get('SetName') is not None:
            self.set_name = m.get('SetName')
        return self


class UpdateSetResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        create_time: str = None,
        set_name: str = None,
        modify_time: str = None,
        set_id: str = None,
    ):
        self.request_id = request_id
        self.create_time = create_time
        self.set_name = set_name
        self.modify_time = modify_time
        self.set_id = set_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.set_name is not None:
            result['SetName'] = self.set_name
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.set_id is not None:
            result['SetId'] = self.set_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('SetName') is not None:
            self.set_name = m.get('SetName')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('SetId') is not None:
            self.set_id = m.get('SetId')
        return self


class UpdateSetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateSetResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateSetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


