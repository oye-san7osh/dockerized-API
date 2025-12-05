
# pagination by PageNumberPagination

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class StudentPagination(PageNumberPagination):
    
    page_size = 4       # items per page
    page_query_param = 'page'
    page_size_query_param = 'size'
    max_page_size = 5
    
    
    def get_page_size(self, request):
        
        if request.query_params.get('size'):
            
            return int(request.query_params.get('size'))
        
        return self.page_size
    
    
    def get_paginated_response(self, data):
        
        return Response(
            {
                "status": "success",
                "page_info":
                    {
                        "current_pages": self.page.number,
                        "page_size": self.get_page_size(self.request),
                        "total_items": self.page.paginator.count,
                        "total_pages": self.page.paginator.num_pages,
                    },
                "link":
                    {
                        "next_url": self.get_next_link(),
                        "previous_url": self.get_previous_link(),
                    },
                "results": data
            }
        )




"""
# pagination by LimitOffsetPagination

from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response


class StudentPagination(LimitOffsetPagination):
    
    default_limit = 4
    limit_query_param = "limit"
    offset_query_param = "offset"
    max_limit = 5
    
    
    def get_limit(self, request):
        
        if request.query_params.get("limit"):
            return int(request.query_params.get("limit"))
        return self.default_limit
    
    
    def get_offset(self, request):
        
        if request.query_params.get("offset"):
            return int(request.query_params.get("offset"))
        return 0
    
    
    def get_paginated_response(self, data):
        
        return Response(
            {
                "status": "success",
                "page_info":
                    {
                        "limit": self.limit,
                        "offset": self.offset,
                        "total_items": self.count,
                    },
                "links":
                    {
                        "next_url": self.get_next_link(),
                        "previous_url": self.get_previous_link(),
                    },
                "result": data
            }
        )
    """ 
    
"""    
# Pagination by CursorPagination


from rest_framework.pagination import CursorPagination
from rest_framework.response import Response


class StudentPagination(CursorPagination):
       
       page_size = 4
       cursor_query_param = 'cursor'
       ordering = "-admission_date"
       
       
       def get_paginated_response(self, data):
           
           return Response(
               {
                   "status": "success",
                   "pagination":
                       {
                           "page_size": self.page_size,
                           "ordering": self.ordering,
                       },
                    "links":
                        {
                            "next_url": self.get_next_link(),
                            "previous_url": self.get_previous_link(),
                        },
                    "results": data
               }
           )
"""
