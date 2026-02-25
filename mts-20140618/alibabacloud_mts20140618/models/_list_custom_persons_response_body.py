# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mts20140618 import models as main_models
from darabonba.model import DaraModel

class ListCustomPersonsResponseBody(DaraModel):
    def __init__(
        self,
        categories: main_models.ListCustomPersonsResponseBodyCategories = None,
        request_id: str = None,
    ):
        self.categories = categories
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.categories:
            self.categories.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.categories is not None:
            result['Categories'] = self.categories.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Categories') is not None:
            temp_model = main_models.ListCustomPersonsResponseBodyCategories()
            self.categories = temp_model.from_map(m.get('Categories'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListCustomPersonsResponseBodyCategories(DaraModel):
    def __init__(
        self,
        category: List[main_models.ListCustomPersonsResponseBodyCategoriesCategory] = None,
    ):
        self.category = category

    def validate(self):
        if self.category:
            for v1 in self.category:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Category'] = []
        if self.category is not None:
            for k1 in self.category:
                result['Category'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.category = []
        if m.get('Category') is not None:
            for k1 in m.get('Category'):
                temp_model = main_models.ListCustomPersonsResponseBodyCategoriesCategory()
                self.category.append(temp_model.from_map(k1))

        return self

class ListCustomPersonsResponseBodyCategoriesCategory(DaraModel):
    def __init__(
        self,
        category_description: str = None,
        category_id: str = None,
        category_name: str = None,
        persons: main_models.ListCustomPersonsResponseBodyCategoriesCategoryPersons = None,
    ):
        self.category_description = category_description
        self.category_id = category_id
        self.category_name = category_name
        self.persons = persons

    def validate(self):
        if self.persons:
            self.persons.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_description is not None:
            result['CategoryDescription'] = self.category_description

        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.category_name is not None:
            result['CategoryName'] = self.category_name

        if self.persons is not None:
            result['Persons'] = self.persons.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryDescription') is not None:
            self.category_description = m.get('CategoryDescription')

        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')

        if m.get('Persons') is not None:
            temp_model = main_models.ListCustomPersonsResponseBodyCategoriesCategoryPersons()
            self.persons = temp_model.from_map(m.get('Persons'))

        return self

class ListCustomPersonsResponseBodyCategoriesCategoryPersons(DaraModel):
    def __init__(
        self,
        person: List[main_models.ListCustomPersonsResponseBodyCategoriesCategoryPersonsPerson] = None,
    ):
        self.person = person

    def validate(self):
        if self.person:
            for v1 in self.person:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Person'] = []
        if self.person is not None:
            for k1 in self.person:
                result['Person'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.person = []
        if m.get('Person') is not None:
            for k1 in m.get('Person'):
                temp_model = main_models.ListCustomPersonsResponseBodyCategoriesCategoryPersonsPerson()
                self.person.append(temp_model.from_map(k1))

        return self

class ListCustomPersonsResponseBodyCategoriesCategoryPersonsPerson(DaraModel):
    def __init__(
        self,
        faces: main_models.ListCustomPersonsResponseBodyCategoriesCategoryPersonsPersonFaces = None,
        person_description: str = None,
        person_id: str = None,
        person_name: str = None,
    ):
        self.faces = faces
        self.person_description = person_description
        self.person_id = person_id
        self.person_name = person_name

    def validate(self):
        if self.faces:
            self.faces.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.faces is not None:
            result['Faces'] = self.faces.to_map()

        if self.person_description is not None:
            result['PersonDescription'] = self.person_description

        if self.person_id is not None:
            result['PersonId'] = self.person_id

        if self.person_name is not None:
            result['PersonName'] = self.person_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Faces') is not None:
            temp_model = main_models.ListCustomPersonsResponseBodyCategoriesCategoryPersonsPersonFaces()
            self.faces = temp_model.from_map(m.get('Faces'))

        if m.get('PersonDescription') is not None:
            self.person_description = m.get('PersonDescription')

        if m.get('PersonId') is not None:
            self.person_id = m.get('PersonId')

        if m.get('PersonName') is not None:
            self.person_name = m.get('PersonName')

        return self

class ListCustomPersonsResponseBodyCategoriesCategoryPersonsPersonFaces(DaraModel):
    def __init__(
        self,
        face: List[main_models.ListCustomPersonsResponseBodyCategoriesCategoryPersonsPersonFacesFace] = None,
    ):
        self.face = face

    def validate(self):
        if self.face:
            for v1 in self.face:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Face'] = []
        if self.face is not None:
            for k1 in self.face:
                result['Face'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.face = []
        if m.get('Face') is not None:
            for k1 in m.get('Face'):
                temp_model = main_models.ListCustomPersonsResponseBodyCategoriesCategoryPersonsPersonFacesFace()
                self.face.append(temp_model.from_map(k1))

        return self

class ListCustomPersonsResponseBodyCategoriesCategoryPersonsPersonFacesFace(DaraModel):
    def __init__(
        self,
        face_id: str = None,
        image_url: str = None,
    ):
        self.face_id = face_id
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.face_id is not None:
            result['FaceId'] = self.face_id

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceId') is not None:
            self.face_id = m.get('FaceId')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        return self

