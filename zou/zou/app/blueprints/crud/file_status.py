from zou.app.models.file_status import FileStatus
from zou.app.blueprints.crud.base import BaseModelResource, BaseModelsResource


class FileStatusesResource(BaseModelsResource):
    def __init__(self):
        BaseModelsResource.__init__(self, FileStatus)

    def check_read_permissions(self, options=None):
        return True


class FileStatusResource(BaseModelResource):
    def __init__(self):
        BaseModelResource.__init__(self, FileStatus)

    def check_read_permissions(self, instance):
        return True
