class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    email
    username
    first_name
    last_name
    hashed_password
    is_active
    todos = relationship('Todos', back_populates='owner')