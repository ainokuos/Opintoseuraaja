from entities.course import Course
from config import COURSES_FILE_PATH
from repositories.csv_repository import CsvRepository

class CourseRepository:
    """ Luokka, joka vastaa suoritusten tallennuksesta.

        Attributes:
            file_path: osoite luokan käyttämään tiedostoon
    """
    def __init__(self, file_path):
        """ Luokan konstruktori, joka aloittaa uuden tallennuksen.

            Args:
                file_path: Merkkijono tiedoston osoitteesta
        """
        self._file_path = file_path
        self.csv_repository = CsvRepository(self._file_path)

    def _read(self):
        """ Lukee tiedostosta suoritukset

            Returns:
                courses: lista tiedostoon tallennetuista suorituksista
        """
        courses_list = self.csv_repository.read()
        courses = []
        for course in courses_list:
            parts = course.split(";")
            name = parts[0]
            cr = parts[1]
            grade = parts[2]
            username = parts[3]
            courses.append(Course(name,cr,grade, username))
        return courses

    def _write(self, courses):
        """ Tallentaa tiedostoon suoritukset

            Args:
                courses: lista tallennettavista suorituksista
        """
        self.csv_repository.ensure_file_exists()
        with open(self._file_path, "w") as file:
            for course in courses:
                row = f"{course.name};{course.cr};{course.grade};{course.username}"
                file.write(row+"\n")

    def create(self, course):
        """ Luo uuden suorituksen

            Args:
                course: Course-olio luotavasta suorituksesta
        """
        courses = self.find_all()
        courses.append(course)
        self._write(courses)

    def find_all(self):
        """ Hakee kaikki tallennetut suoritukset. """
        return self._read()

    def delete_all(self):
        """ Poistaa kaikki suoritukset. """
        self.csv_repository.delete_all()

    def delete_one(self, course):
        """ Poistaa yksittäisen suorituksen.

            Args:
                course: Course-olio poistettavasta suorituksesta
        """
        courses = self.find_all()
        for i in courses:
            if course.name == i.name and course.username == i.username:
                courses.remove(i)
                self._write(courses)
                break

course_repository = CourseRepository(COURSES_FILE_PATH)