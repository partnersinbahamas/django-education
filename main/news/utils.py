class TitleControl(object):
    m_prop = 'string in Mix class'

    def get_prop_upper(self):
        return self.m_prop.upper()
    
    def get_upper(self, s, fieldName=None):
        if isinstance(s, str) and not fieldName:
            return s.upper()
        else:
            return getattr(s, fieldName).upper()